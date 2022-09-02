from RAM import RAM
from CPU import CPU
from GPU import GraphicsCard
from MB import MotherBoard
from HD import HardDisk
from SSD import SSD
from FONT import Font
from CABINET import Cabinet


# RAM Filter
# In this object there are two functions that
# scraping the all RAM memories of Terabyte Store and
# return in several dictionaries for different filters
class TerabyteRAM:
    @staticmethod
    def RAM_get():
        allRAM = RAM.RAM_Crawl()
        return allRAM

    @staticmethod
    def RAM_FILTERS():
        allRAM = TerabyteRAM.RAM_get()
        # Specific memory lists

        # Filters

        # Double Data Rate
        allDDR = ['DDR5', 'DDR4', 'DDR3']
        for i in range(len(allDDR)):
            for data in allRAM:
                if allDDR[i] in data['Name']:
                    data.update({'DDR': allDDR[i]})

        # Capacity / DDR5
        allCapacity = ['8GB', '16GB', '32GB']
        for i in range(len(allCapacity)):
            for data in allRAM:
                if allCapacity[i] in data['Name'] and 'DDR5' in data['Name']:
                    data.update({'Capacity': allCapacity[i]})

        # Capacity / DDR4
        allCapacity = ['4GB', '8GB', '16GB', '32GB']
        for i in range(len(allCapacity)):
            for data in allRAM:
                if allCapacity[i] in data['Name'] and 'DDR4' in data['Name']:
                    data.update({'Capacity': allCapacity[i]})

        # Capacity / DDR3
        for i in range(len(allCapacity)):
            for data in allRAM:
                if allCapacity[i] in data['Name'] and 'DDR3' in data['Name']:
                    data.update({'Capacity': allCapacity[i]})

        # Frequency / DDR5

        # FILTER == 8gb
        for data in allRAM:
            if '4800MHz' in data['Name'] and 'DDR5' in data['Name'] and '8GB' in data['Name']:
                data.update({'Frequency': '4800MHz'})
                data.update({'Model': '4800MHz 8GB DDR5'})

        # FILTER == 16gb
            if '4800MHz' in data['Name'] and 'DDR5' in data['Name'] and '16GB' in data['Name']:
                data.update({'Frequency': '4800MHz'})
                data.update({'Model': '4800MHz 16GB DDR5'})

        # FILTER == 32gb
            if '5600MHz' in data['Name'] and 'DDR5' in data['Name'] and '32GB' in data['Name']:  # 5600Mhz 32gb DDR5
                data.update({'Frequency': '5600MHz'})
                data.update({'Model': '5600MHz 32GB DDR5'})

            if '6000MHz' in data['Name'] and 'DDR5' in data['Name'] and '32GB' in data['Name']:  # 6000Mhz 32gb DDR5
                data.update({'Frequency': '6000MHz'})
                data.update({'Model': '6000MHz 32GB DDR5'})

        # # Frequency / DDR4

        # FILTER == 4gb
            if '2400MHz' in data['Name'] and 'DDR4' in data['Name'] and '4GB' in data['Name']:  # 2400MHz 4GB DDR4
                data.update({'Frequency': '2400MHz'})
                data.update({'Model': '2400MHz 4GB DDR4'})

            if '1600MHz' in data['Name'] and 'DDR4' in data['Name'] and '4GB' in data['Name']:  # 1600MHz 4GB DDR4
                data.update({'Frequency': '1600MHz'})
                data.update({'Model': '1600MHz 4GB DDR4'})

        # FILTER == 8gb
            if '2666MHz' in data['Name'] and 'DDR4' in data['Name'] and '8GB' in data['Name']:  # 2666MHz 8GB DDR4
                data.update({'Frequency': '2666MHz'})
                data.update({'Model': '2666MHz 8GB DDR4'})

            if '3000MHz' in data['Name'] and 'DDR4' in data['Name'] and '8GB' in data['Name']:  # 3000MHz 8GB DDR4
                data.update({'Frequency': '3000MHz'})
                data.update({'Model': '3000MHz 8GB DDR4'})

            if '3200MHz' in data['Name'] and 'DDR4' in data['Name'] and '8GB' in data['Name']:  # 3200MHz 8GB DDR4
                data.update({'Frequency': '3200MHz'})
                data.update({'Model': '3200MHz 8GB DDR4'})

        # FILTER == 16gb
            if '2666MHz' in data['Name'] and 'DDR4' in data['Name'] and '16GB' in data['Name']:  # 2666MHz 16GB DDR4
                data.update({'Frequency': '2666MHz'})
                data.update({'Model': '2666MHz 16GB DDR4'})

            if '3000MHz' in data['Name'] and 'DDR4' in data['Name'] and '16GB' in data['Name']:  # 3000MHz 16GB DDR4
                data.update({'Frequency': '3000MHz'})
                data.update({'Model': '3000MHz 16GB DDR4'})

            if '3200MHz' in data['Name'] and 'DDR4' in data['Name'] and '16GB' in data['Name']:  # 3200MHz 16GB DDR4
                data.update({'Frequency': '3200MHz'})
                data.update({'Model': '3200MHz 16GB DDR4'})

            if '3600MHz' in data['Name'] and 'DDR4' in data['Name'] and '16GB' in data['Name']:  # 3600MHz 16GB DDR4
                data.update({'Frequency': '3600MHz'})
                data.update({'Model': '3600MHz 16GB DDR4'})

        # FILTER == 32gb
            if '2666MHz' in data['Name'] and 'DDR4' in data['Name'] and '32GB' in data['Name']:  # 2666MHz 32GB DDR4
                data.update({'Frequency': '2666MHz'})
                data.update({'Model': '2666MHz 32GB DDR4'})

            if '3000MHz' in data['Name'] and 'DDR4' in data['Name'] and '32GB' in data['Name']:  # 3000MHz 32GB DDR4
                data.update({'Frequency': '3000MHz'})
                data.update({'Model': '3000MHz 32GB DDR4'})

            if '3200MHz' in data['Name'] and 'DDR4' in data['Name'] and '32GB' in data['Name']:  # 3200MHz 32GB DDR4
                data.update({'Frequency': '3200MHz'})
                data.update({'Model': '3200MHz 32GB DDR4'})

            if '3600MHz' in data['Name'] and 'DDR4' in data['Name'] and '32GB' in data['Name']:  # 3600MHz 32GB DDR4
                data.update({'Frequency': '3600MHz'})
                data.update({'Model': '3600MHz 32GB DDR4'})

        # Frequency / DDR3

        # FILTER == 4gb
            if '2400MHz' in data['Name'] and 'DDR3' in data['Name'] and '4GB' in data['Name']:  # 2400MHz 4gb DDR3
                data.update({'Frequency': '2400MHz'})
                data.update({'Model': '2400MHz 4GB DDR3'})

            if '1600MHz' in data['Name'] and 'DDR3' in data['Name'] and '4GB' in data['Name']:  # 1600MHz 4gb DDR3
                data.update({'Frequency': '1600MHz'})
                data.update({'Model': '1600MHz 4GB DDR3'})

        # FILTER == 8gb
            if '1600MHz' in data['Name'] and 'DDR3' in data['Name'] and '8GB' in data['Name']:  # 1600MHz 8GB DDR3
                data.update({'Frequency': '1600MHz'})
                data.update({'Model': '1600MHz 8GB DDR3'})

            if '1866MHz' in data['Name'] and 'DDR3' in data['Name'] and '8GB' in data['Name']:  # 1866MHz 8GB DDR3
                data.update({'Frequency': '1866MHz'})
                data.update({'Model': '1866MHz 8GB DDR3'})

        # FILTER == 16gb
            if '1600MHz' in data['Name'] and 'DDR3' in data['Name'] and '16GB' in data['Name']:  # 1600MHz 16GB DDR3
                data.update({'Frequency': '1600MHz'})
                data.update({'Model': '1600MHz 16GB DDR3'})

            if '1866MHz' in data['Name'] and 'DDR3' in data['Name'] and '16GB' in data['Name']:  # 1866MHz 16GB DDR3
                data.update({'Frequency': '1866MHz'})
                data.update({'Model': '1866MHz 16GB DDR3'})

        # FILTER == 32gb
            if '1600MHz' in data['Name'] and 'DDR3' in data['Name'] and '32GB' in data['Name']:  # 1600MHz 32GB DDR3
                data.update({'Frequency': '1600MHz'})
                data.update({'Model': '1600MHz 32GB DDR3'})

        return allRAM


# CPU Filter
# In this object there are two functions that
# scraping the all CPU of Terabyte Store and
# return in several dictionaries for different filters
class TerabyteCPU:

    @staticmethod
    def CPU_get():
        allCPU = CPU.CPU_Crawl()
        return allCPU

    @staticmethod
    def CPU_FILTERS():
        allCPU = TerabyteCPU.CPU_get()
        # Specific CPU lists

        # Platform

        # AMD
        # FILTER == AMD APU integrate GPU
        for data in allCPU:
            if 'AMD' in data['Name']:
                if '0G' in data['Name'] or '0GE' in data['Name'] or 'FM2+' in data['Name']:
                    data.update({'Platform': 'AMD APU'})

                # FILTER == AMD CPU without GPU
                else:
                    data.update({'Platform': 'AMD CPU'})

        # Intel
        # FILTER == Intel CPU without GPU
        for data in allCPU:
            if 'Intel' in data['Name']:
                if '5F' in data['Name'] or '0KF' in data['Name'] or '0X' in data['Name'] or '0F' in data['Name']:
                    data.update({'Platform': 'Intel CPU'})

                # FILTER == Intel APU integrate GPU
                else:
                    data.update({'Platform': 'Intel APU'})

        # Socket

        # FILTER == AMD AM4 and AMD AM4G
        allModel = ['AM4', 'FM2+', 'LGA 1150', 'LGA 1151', 'LGA 1200', 'LGA 1700', 'LGA 2066']
        for i in range(len(allModel)):
            for data in allCPU:
                if allModel[i] in data['Name']:
                    data.update({'Model': allModel[i]})

        return allCPU


# GPU Filter
# In this object there are two functions that
# scraping the all GPU of Terabyte Store and
# return in several dictionaries for different filters
class TerabyteGPU:

    @staticmethod
    def GPU_get():
        allGPU = GraphicsCard.GPU_Crawl()
        return allGPU

    @staticmethod
    def GPU_FILTERS():
        allGPU = TerabyteGPU.GPU_get()

        # Specific GPU lists

        allModel = [
            'GT 1030', 'GT 610', 'GT 710 1GB', 'GT 710 2GB', 'GT 730', 'GT 730',
            'GT240', 'GTX 1050 2GB', 'GTX 1050 3GB', 'GTX 1050 TI', 'GTX 1060',
            'GTX 1060', 'GTX 1070', 'GTX 1070 TI', 'GTX 1080', 'GTX 1080 TI',
            'GTX 1630', 'GTX 1650', 'GTX 1650 Super', 'GTX 1660', 'GTX 1660 Super',
            'GTX 1660 TI', 'GTX 750 TI 2GB', 'GTX 750 TI 4GB', 'GTX 980 TI', 'NVS 810',
            'PRO W6600', 'QUADRO P1000', 'QUADRO P2000', 'QUADRO P400', 'QUADRO P4000',
            'QUADRO P620', 'QUADRO RTX 4000', 'QUADRO RTX A2000', 'QUADRO RTX A2000',
            'QUADRO RTX A4000', 'QUADRO RTX A4500', 'QUADRO RTX A5000', 'QUADRO T1000',
            'QUADRO T1000', 'QUADRO T400', 'QUADRO T600', 'R5 220 2GB', 'R5 230 1GB',
            'R5 230 2GB', 'R7 240', 'RTX 2060', 'RTX 2060', 'RTX 2060 Super', 'RTX 2070',
            'RTX 2070 Super', 'RTX 2080', 'RTX 2080 Super', 'RTX 2080 TI', 'RTX 3050',
            'RTX 3050', 'RTX 3060', 'RTX 3060 TI', 'RTX 3070', 'RTX 3070 TI', 'RTX 3080',
            'RTX 3080', 'RTX 3080 TI', 'RTX 3090', 'RTX 3090 TI', 'RX 460', 'RX 550',
            'RX 550', 'RX 5500', 'RX 5600 XT', 'RX 570', 'RX 570', 'RX 5700',
            'RX 5700 XT', 'RX 580', 'RX 580', 'RX 590', 'RX 6400', 'RX 6500 XT',
            'RX 6600', 'RX 6600 XT', 'RX 6650 XT', 'RX 6700 XT', 'RX 6750 XT',
            'RX 6800', 'RX 6800 XT', 'RX 6900 XT', 'RX 6950 XT'
        ]
        for i in range(len(allModel)):
            for data in allGPU:
                if allModel[i] in data['Name']:
                    data.update({'Model': allModel[i]})

        return allGPU


# Mother Board Filter
# In this object there are two functions that
# scraping the all MotherBoards of Terabyte Store and
# return in several dictionaries for different filters
class TerabyteMotherBoard:

    @staticmethod
    def MB_get():
        allMB = MotherBoard.MB_Crawl()
        return allMB

    @staticmethod
    def MB_FILTERS():
        allMB = TerabyteMotherBoard.MB_get()
        # Specific MotherBoard lists

        # Double Data Rate
        allDDR = ['DDR5', 'DDR4', 'DDR3']
        for i in range(len(allDDR)):
            for data in allMB:
                if allDDR[i] in data['Name']:
                    data.update({'DDR': allDDR[i]})

        # Format
        allFormat = ['ATX', 'E-ATX', 'MATX', 'Mini-ITX']
        for i in range(len(allFormat)):
            for data in allMB:
                if allFormat[i] in data['Name']:
                    data.update({'Format': allFormat[i]})

        # Socket
        allModel = ['AM4', 'LGA 1700', '1200', 'LGA 1150', 'LGA 1151', 'LGA 1155', 'FM2+']
        for i in range(len(allModel)):
            for data in allMB:
                if allModel[i] in data['Name']:
                    data.update({'Model': allModel[i]})
        return allMB


# Hard Disk Filter
# In this object there are two functions that
# scraping the all HD Data of Terabyte Store and
# return in several dictionaries for different filters
class TerabyteHD:
    @staticmethod
    def HD_get():
        allHD = HardDisk.HD_Crawl()
        return allHD

    @staticmethod
    def HD_FILTERS():
        allHD = TerabyteHD.HD_get()
        # Specific HardDisk lists

        # HardDisk Capacity

        # Filters

        # HardDisk Capacity
        allModel = ['10TB', '12TB', '14TB', '16TB', '1TB', '2TB', '3TB', '4TB', '6TB', '8TB']
        for i in range(len(allModel)):
            for data in allHD:
                if allModel[i] in data['Name']:
                    data.update({'Model': allModel[i]})

        return allHD


# SSD Filter
# In this object there are two functions that
# scraping the all SSD Data of Terabyte Store and
# return in several dictionaries for different filters
class TerabyteSSD:
    @staticmethod
    def SSD_get():
        allSSD = SSD.SSD_Crawl()
        return allSSD

    @staticmethod
    def SSD_FILTERS():
        allSSD = TerabyteSSD.SSD_get()
        # Specific SSD lists

        # Filters

        # SSD Interface
        allInterface = ['NVMe', 'SATA']
        for i in range(len(allInterface)):
            for data in allSSD:
                if allInterface[i] in data['Name']:
                    data.update({'Interface': allInterface[i]})

        # SSD Format
        allFormat = ['2.5', 'M.2', 'PCIe']
        for i in range(len(allFormat)):
            for data in allSSD:
                if allFormat[i] in data['Name']:
                    data.update({'Format': allFormat[i]})

        # SSD Capacity
        allModel = ['120', '128', '1TB', '240',
                    '250', '256', '2TB', '480',
                    '4TB', '500', '8TB', '980']
        for i in range(len(allModel)):
            for data in allSSD:
                if allModel[i] in data['Name']:
                    data.update({'Model': allModel[i]})

        return allSSD


# Font Filter
# In this object there are two functions that
# scraping the all Font of Pichau Store and
# return in several dictionaries for different filters
class TerabyteFont:
    @staticmethod
    def Font_get():
        allFont = Font.Font_Crawl()
        return allFont

    @staticmethod
    def Font_FILTERS():
        allFont = TerabyteFont.Font_get()
        # Specific Fonts lists

        # Font Potency

        allModel = ['200', '400', '450', '500', '550', '600', '650', '700', '750', '850', '1200']
        for i in range(len(allModel)):
            for data in allFont:
                if allModel[i] in data['Name']:
                    data.update({'Model': allModel[i] + 'W'})

        return allFont


# Cabinet Filter
# In this object there are two functions that
# scraping the all cases of Pichau Store and
# return in several dictionaries for different filters
class TerabyteCabinet:
    @staticmethod
    def Cabinet_get():
        allCabinet = Cabinet.Cabinet_Crawl()
        return allCabinet

    @staticmethod
    def Cabinet_FILTERS():
        allCabinet = TerabyteCabinet.Cabinet_get()
        # Specific Case lists

        # Filters

        # Case Colors
        allColors = ['Blue', 'White', 'White/Black', 'Gray', 'Silver', 'Black', 'Preto/Azul',
                     'Black/White', 'Preto/Laranja', 'Black/Gray', 'Red', 'Pink', 'Green']
        for i in range(len(allColors)):
            for data in allCabinet:
                if allColors[i] in data['Name']:
                    data.update({'Color': allColors[i]})

        # Case Model
        allModel = ['Full Tower', 'Mid Tower', 'Mini Tower']
        for i in range(len(allModel)):
            for data in allCabinet:
                if allModel[i] in data['Name']:
                    data.update({'Model': allModel[i]})

        return allCabinet


TerabyteAllCabinet = TerabyteCabinet.Cabinet_FILTERS()
TerabyteAllFont = TerabyteFont.Font_FILTERS()
TerabyteAllSSD = TerabyteSSD.SSD_FILTERS()
TerabyteAllHD = TerabyteHD.HD_FILTERS()
TerabyteAllMB = TerabyteMotherBoard.MB_FILTERS()
TerabyteAllGPU = TerabyteGPU.GPU_FILTERS()
TerabyteAllCPU = TerabyteCPU.CPU_FILTERS()
TerabyteAllRAM = TerabyteRAM.RAM_FILTERS()
