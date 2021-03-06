#!/usr/bin/python

"""

::

    This experiment is used to study inductive reactance XL


"""

from __future__ import print_function
from SEEL_Apps.utilitiesClass import utilitiesClass

from .templates import ui_template_xl as template_xl

import numpy as np
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'XLi.png',
'name':'Inductive\nReactance',
'hint':'''
	Calculate Inductive reactance(XL) by analysing input and output waveforms of an RC network.<br>
	Plot frequency vs XL, and verify its linear nature
	'''
}

class AppWindow(QtGui.QMainWindow, template_xl.Ui_MainWindow,utilitiesClass):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		
		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot1=self.add2DPlot(self.plot_area)
		labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
		self.plot1.setLabel('bottom','Time -->', units='S',**labelStyle)

		self.p2=self.enableRightAxis(self.plot1)

		self.plot1.getAxis('left').setLabel('Vl -->>', color='#ffffff')
		self.plot1.getAxis('right').setLabel('I -->>', units='A', color='#00ffff')

		self.I.set_gain('CH1',1)
		self.I.set_gain('CH2',1)
		self.plot1.setYRange(-8.5,8.5)

		self.p2.setYRange(-8.5/self.resistance.value(),8.5/self.resistance.value())


		from SEEL.analyticsClass import analyticsClass
		self.CC = analyticsClass()
		self.I.configure_trigger(0,'CH1',0)
		self.tg=20
		self.max_samples=2000
		self.samples = 2000
		self.prescaler = 0
		self.set_timebase(3)
		self.timer = self.newTimer()

		self.curveCH1 = self.addCurve(self.plot1,'VL(CH1-CH2)')
		self.curveCH2 = self.addCurve(self.p2,'Current',pen=[0,255,255])
		self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)

		self.fdial = self.addW1(self.I);
		self.WidgetLayout.addWidget(self.fdial)
		self.fdial.dial.setValue(100)

		self.WidgetLayout.addWidget(self.addTimebase(self.I,self.set_timebase))

		self.timer.singleShot(100,self.run)
		self.resultsTable.setRowCount(50)
		self.resultsTable.setColumnCount(4)
		self.resultsTable.setHorizontalHeaderLabels(['F','Vl','I (mA)','XL = Vl/I'])
		self.acquireParams = False
		self.running=True
		self.currentRow=0		
		self.plotAButton.setText('F vs XL')
		self.plotBButton.setParent(None)#Text('F vs 1/XL')
		self.splitter.setSizes([10,1000])


	def set_timebase(self,g):
		timebases = [1.5,2,4,8,16,32,128,256,512,1024]
		self.prescalerValue=[0,0,0,0,1,1,2,2,3,3,3][g]
		samplescaling=[1,1,1,1,1,0.5,0.4,0.3,0.2,0.2,0.1]
		self.tg=timebases[g]
		self.samples = int(self.max_samples*samplescaling[g])
		self.plot1.setXRange(0,self.samples*self.tg*1e-6)
		self.plot1.setLimits(yMax=8,yMin=-8,xMin=0,xMax=self.samples*self.tg*1e-6)
		self.p2.setLimits(yMax=8/self.resistance.value(),yMin=-8/self.resistance.value(),xMin=0,xMax=self.samples*self.tg*1e-6)
		return self.samples*self.tg*1e-6

	def fit(self):
		print ("Adding...")
		self.acquireParams = True
		
	def run(self):
		if not self.running:return
		if self.I.sine1freq < 150: self.prescaler = 3
		else: self.prescaler = 0
		self.I.configure_trigger(0,'CH1',0,resolution=10,prescaler=self.prescaler)
		self.I.capture_traces(2,self.samples,self.tg)
		if self.running:self.timer.singleShot(self.samples*self.I.timebase*1e-3+50,self.plotData)

	def plotData(self): 
		while(not self.I.oscilloscope_progress()[0]):
			time.sleep(0.1);n=0
			print (self.I.timebase,'correction required',n)
			n+=1
			if n>10:
				if self.running:self.timer.singleShot(100,self.run)
				return
		self.I.__fetch_channel__(1)
		self.I.__fetch_channel__(2)
		T = self.I.achans[0].get_xaxis()*1e-6
		VCH1 = self.I.achans[0].get_yaxis()
		VCH2 = self.I.achans[1].get_yaxis()
		I = VCH2/self.resistance.value()
		VC = VCH1-VCH2 - (I*self.resistanceInductor.value())
		self.curveCH1.setData(T,VC,connect='finite')
		self.curveCH2.setData(T,I,connect='finite')
		if self.acquireParams:
			pars1 = self.CC.sineFit(T,VC)
			pars2 = self.CC.sineFit(T,I)#,freq=self.frq)
			if pars1 and pars2:
				a1,f1,o1,p1 = pars1
				a2,f2,o2,p2 = pars2
				f1=f1*1e-6
				f2=f2*1e-6
				if (a2 and a1) and (abs(f2-self.I.sine1freq)<10) and (abs(f1-self.I.sine1freq)<10):
					#self.msg.setText("Set F:%.1f\tFitted F:%.1f"%(frq,f1))
					p2=(p2)
					p1=(p1)
					dp=(p2-p1)-360
					if dp<-360:dp+=360
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(self.I.sine1freq));self.resultsTable.setItem(self.currentRow, 0, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a1));self.resultsTable.setItem(self.currentRow, 1, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a2*1e3));self.resultsTable.setItem(self.currentRow, 2, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a1/a2));self.resultsTable.setItem(self.currentRow, 3, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
					self.currentRow+=1
					print ('F: %.2f,%.2f\tA: %.2f,%.2f\tP: %.1f,%.1f'%(f1,f2,a1,a2,p1,p2))
					print ('Xc*F %.3f'%(f2*a1/a2))
				else:
					self.displayDialog("Fit Failed. Please check parameters\nor change timescale")
			else:
				self.displayDialog("Fit Failed. Please check parameters\nor change timescale")
			self.acquireParams = False
		if self.running:self.timer.singleShot(100,self.run)
		#print (self.resultsTable.selectedRanges()[0].leftColumn(),self.resultsTable.selectedRanges()[0].rightColumn())


		
	def plotA(self):
		F,XC = self.fetchColumns(self.resultsTable,0,3)
		self.newPlot(F,XC,title = "F vs XL: ",xLabel = 'F',yLabel='XL')

	def plotB(self):
		pass
		#F,XC = self.fetchColumns(self.resultsTable,0,3)
		#self.newPlot(F,1./np.array(XC),title = "F vs 1/XL: ",xLabel = 'F',yLabel='1/XL')        

	def saveFile(self):
		self.saveToCSV(self.resultsTable)

	def savePlot(self):
		self.saveDataWindow([self.curveCH1,self.curveCH2],self.plot1)

	def setTimebase(self,T):
		self.tgs = [0.5,1,2,4,6,8,10,25,50,100]
		self.tg = self.tgs[T]
		self.tgLabel.setText(str(5000*self.tg*1e-3)+'mS')
		
	def closeEvent(self, event):
		self.running=False
		self.timer.stop()
		self.finished=True
		

	def __del__(self):
		self.timer.stop()
		print ('bye')

if __name__ == "__main__":
    from SEEL import interface
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=interface.connect())
    myapp.show()
    sys.exit(app.exec_())

