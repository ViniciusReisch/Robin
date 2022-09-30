from terabyte.FILTER import *
from pichau.FILTER import *
from kabum.FILTER import *


def get_All():
    # Kabum

    KabumAllCabinet = KabumCabinet.Cabinet_FILTERS()
    KabumAllFont = KabumFont.Font_FILTERS()
    KabumAllSSD = KabumSSD.SSD_FILTERS()
    KabumAllHD = KabumHD.HD_FILTERS()
    KabumAllMB = KabumMotherBoard.MB_FILTERS()
    KabumAllGPU = KabumGPU.GPU_FILTERS()
    KabumAllCPU = KabumCPU.CPU_FILTERS()
    KabumAllRAM = KabumRAM.RAM_FILTERS()

    # Pichau

    PichauAllCabinet = PichauCabinet.Cabinet_FILTERS()
    PichauAllFont = PichauFont.Font_FILTERS()
    PichauAllSSD = PichauSSD.SSD_FILTERS()
    PichauAllHD = PichauHD.HD_FILTERS()
    PichauAllMB = PichauMotherBoard.MB_FILTERS()
    PichauAllGPU = PichauGPU.GPU_FILTERS()
    PichauAllCPU = PichauCPU.CPU_FILTERS()
    PichauAllRAM = PichauRAM.RAM_FILTERS()

    # Terabyte

    TerabyteAllCabinet = TerabyteCabinet.Cabinet_FILTERS()
    TerabyteAllFont = TerabyteFont.Font_FILTERS()
    TerabyteAllSSD = TerabyteSSD.SSD_FILTERS()
    TerabyteAllHD = TerabyteHD.HD_FILTERS()
    TerabyteAllMB = TerabyteMotherBoard.MB_FILTERS()
    TerabyteAllGPU = TerabyteGPU.GPU_FILTERS()
    TerabyteAllCPU = TerabyteCPU.CPU_FILTERS()
    TerabyteAllRAM = TerabyteRAM.RAM_FILTERS()

    AllCabinet = [KabumAllCabinet, PichauAllCabinet, TerabyteAllCabinet]
    AllFont = [TerabyteAllFont, PichauAllFont, KabumAllFont]
    AllSSD = [KabumAllSSD, PichauAllSSD, TerabyteAllSSD]
    AllHD = [TerabyteAllHD, PichauAllHD, KabumAllHD]
    AllMB = [TerabyteAllMB, PichauAllMB, KabumAllMB]
    AllGPU = [TerabyteAllGPU, PichauAllGPU, KabumAllGPU]
    AllCPU = [TerabyteAllCPU, PichauAllCPU, KabumAllCPU]
    AllRAM = [TerabyteAllRAM, PichauAllRAM, KabumAllRAM]
    AllProducts = [AllRAM, AllMB, AllHD, AllCPU, AllGPU, AllSSD, AllFont, AllCabinet]
    Products = []

    for i in AllProducts:
        for k in i:
            for j in k:
                Products.append(j)

    return Products
