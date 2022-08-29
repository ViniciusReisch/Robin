from terabyte.FILTER import *
from pichau.FILTER import *
from kabum.FILTER import *

# Terabyte

TerabyteCabinet_Types, TerabyteCabinet_Colors, TerabyteAllCabinet = TerabyteCabinet.Cabinet_FILTERS()
TerabyteFont_Potency, TerabyteAllFont = TerabyteFont.Font_FILTERS()
TerabyteSSD_Interface, TerabyteSSD_Format, TerabyteSSD_Capacity, TerabyteAllSSD = TerabyteSSD.SSD_FILTERS()
TerabyteHD_Capacity, TerabyteAllHD = TerabyteHD.HD_FILTERS()
TerabyteMB_DDR, TerabyteMB_Format, TerabyteMB_Socket, TerabyteAllMB = TerabyteMotherBoard.MB_FILTERS()
TerabyteGPU_Model, TerabyteAllGPU = TerabyteGPU.GPU_FILTERS()
TerabyteCPU_Socket, TerabyteCPU_Platform, TerabyteAllCPU = TerabyteCPU.CPU_FILTERS()
TerabyteRAM_DDR, TerabyteRAM_capacityDDR5, TerabyteRAM_capacityDDR4, TerabyteRAM_capacityDDR3, TerabyteRAM_frequencyDDR5, TerabyteRAM_frequencyDDR4, TerabyteRAM_frequencyDDR3, TerabyteAllRAM = TerabyteRAM.RAM_FILTERS()


# Pichau


PichauFont_Potency, PichauAllFont = PichauFont.Font_FILTERS()
PichauCabinet_Types, PichauCabinet_Colors, PichauAllCabinet = PichauCabinet.Cabinet_FILTERS()
PichauCapacity_HardDisk, PichauAllHD = PichauHD.HD_FILTERS()
PichauInterface_SSD, PichauFormat_SSD, PichauCapacity_SSD, PichauAllSSD = PichauSSD.SSD_FILTERS()
PichauRAM_DDR, PichauRAM_capacityDDR5, PichauRAM_capacityDDR4, PichauRAM_capacityDDR3, PichauRAM_frequencyDDR5, PichauRAM_frequencyDDR4, PichauRAM_frequencyDDR3, PichauAllRAM = PichauRAM.RAM_FILTERS()
motherBoard_DDR, motherBoard_Format, motherBoard_Socket, PichauAllMB = PichauMotherBoard.MB_FILTERS()
PichauCPU_Socket, PichauCPU_Platform, PichauAllCPU = PichauCPU.CPU_FILTERS()
PichauGPU_Model, PichauAllGPU = PichauGPU.GPU_FILTERS()


# All Stores

class AllStores:
    @staticmethod
    def allData():  
        allHardDisk = [PichauAllHD, TerabyteAllHD]
        allCabinet = [PichauAllCabinet, TerabyteAllCabinet]
        allFont = [PichauAllFont, TerabyteAllFont]       
        allCPU = [PichauAllCPU, TerabyteAllCPU]
        allRAM = [PichauAllRAM, TerabyteAllRAM]
        allSSD = [PichauAllSSD, TerabyteAllSSD]
        allGPU = [PichauAllGPU, TerabyteAllGPU]
        
    def RAM():
        allRAM_DDR = [Pi]   
        allRAM_capacityDDR5 = []   
        allRAM_capacityDDR4 = []   
        allRAM_capacityDDR3 = []   
        allRAM_frequencyDDR5 = []   
        allRAM_frequencyDDR4 = []   
        allRAM_frequencyDDR3 = []      

