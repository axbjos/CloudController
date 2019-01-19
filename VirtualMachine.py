###################
#
# Joe Axberg
# Dunwoody Cloud Project
#
#########################

#import VirtualNetwork

class VirtualMachine:

	def __init__(self, CPU=1, RAM=1, HDD=10, VMNET="NET"):

		self.CPU = CPU
		self.RAM = RAM
		self.HDD = HDD
		self.VMNET = VMNET

	def createVirtualMachine(self, CPU, RAM, HDD):
		self.CPU = CPU
		self.RAM = RAM
		self.HDD = HDD
		#self.VMNET = VirtualNetwork()

	def updateCPU(self, CPU):
		self.CPU = CPU
	
	def updateRAM(self, RAM):
		self.RAM = RAM

	def updateHDD(self, HDD):
		self.RAM = RAM

	def updateNET(self, VMNET):
		self.VMNET = VMNET

	def printVMDetails(self):
		print("VM Details")
		print(self.CPU, self.RAM, self.HDD, self.VMNET)

