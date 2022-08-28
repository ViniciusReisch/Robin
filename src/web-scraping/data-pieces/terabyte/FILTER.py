from RAM import RAM
from CPU import CPU
from GPU import GraphicsCard
from MB import MotherBoard
from HD import HardDisk


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

        # Double Data Rate
        DDR = {
            "memoryDDR5": [],
            "memoryDDR4": [],
            "memoryDDR3": []
        }

        # Capacity
        capacityDDR5 = {
            "8gb": [],
            "16gb": [],
            "32gb": []
        }
        capacityDDR4 = {
            "4gb": [],
            "8gb": [],
            "16gb": [],
            "32gb": []
        }
        capacityDDR3 = {
            "4gb": [],
            "8gb": [],
            "16gb": [],
            "32gb": []
        }

        # Frequency
        frequencyDDR5 = {
            # 16gb and DDR5
            "8gb_48000MHz": [],

            # 16gb and DDR5
            "16gb_4800MHz": [],

            # 32gb and DDR5
            "32gb_5600MHz": [],
            "32gb_6000MHz": []
        }
        frequencyDDR4 = {
            # 4gb and DDR4
            "4gb_2400MHz": [],
            "4gb_1600MHz": [],

            # 8gb and DDR4
            "8gb_3200Mhz": [],
            "8gb_3000Mhz": [],
            "8gb_2666Mhz": [],

            # 16gb and DDR4
            "16gb_3600Mhz": [],
            "16gb_3200Mhz": [],
            "16gb_3000Mhz": [],
            "16gb_2666Mhz": [],

            # 32gb and DDR4
            "32gb_3600Mhz": [],
            "32gb_3200Mhz": [],
            "32gb_3000Mhz": [],
            "32gb_2666Mhz": []
        }
        frequencyDDR3 = {
            # 4gb and DDR3
            "4gb_1600Mhz": [],
            "4gb_1333Mhz": [],

            # 8gb and DDR3
            "8gb_1600Mhz": [],
            "8gb_1866Mhz": [],

            # 16gb and DDR3
            "16gb_1600Mhz": [],
            "16gb_1866Mhz": [],

            # 32gb and DDR3
            "32gb_1600Mhz": []
        }
        # Filters

        # Double Data Rate
        allDDR = ['DDR5', 'DDR4', 'DDR3']
        key = list(DDR.values())
        for i in range(len(allDDR)):
            for data in allRAM:
                if allDDR[i] in data['Name']:
                    key = list(DDR.values())
                    key[i].append(data)

        # Capacity / DDR5
        allCapacity = ['8GB', '16GB', '32GB']
        key = list(capacityDDR5.values())
        for i in range(len(allCapacity)):
            for data in DDR['memoryDDR5']:
                if allCapacity[i] in data['Name']:
                    key = list(capacityDDR5.values())
                    key[i].append(data)

        # Capacity / DDR4
        allCapacity = ['4GB', '8GB', '16GB', '32GB']
        key = list(capacityDDR4.values())
        for i in range(len(allCapacity)):
            for data in DDR['memoryDDR4']:
                if allCapacity[i] in data['Name']:
                    key = list(capacityDDR4.values())
                    key[i].append(data)

        # Capacity / DDR3
        key = list(capacityDDR3.values())
        for i in range(len(allCapacity)):
            for data in DDR['memoryDDR3']:
                if allCapacity[i] in data['Name']:
                    key = list(capacityDDR3.values())
                    key[i].append(data)

        # Frequency / DDR5

        # FILTER == 8gb
        for data in capacityDDR5['8gb']:  # 4800Mhz 16gb DDR5
            if '4800MHz' in data['Name']:
                frequencyDDR5['8gb_48000MHz'].append(data)

        # FILTER == 16gb
        for data in capacityDDR5['16gb']:  # 4800Mhz 16gb DDR5
            if '4800MHz' in data['Name']:
                frequencyDDR5['16gb_4800MHz'].append(data)

        # FILTER == 32gb
        for data in capacityDDR5['32gb']:
            if '5600MHz' in data['Name']:  # 5600Mhz 32gb DDR5
                frequencyDDR5['32gb_5600MHz'].append(data)
            if '6000MHz' in data['Name']:  # 6000Mhz 32gb DDR5
                frequencyDDR5['32gb_6000MHz'].append(data)

        # # Frequency / DDR4

        # FILTER == 4gb
        for data in capacityDDR4['4gb']:
            if '2400MHz' in data['Name']:  # 2600Mhz 4gb DDR4
                frequencyDDR4['4gb_2400MHz'].append(data)
            if '1600MHz' in data['Name']:  # 1600MHz 4gb DDR4
                frequencyDDR4['4gb_1600MHz'].append(data)

        # FILTER == 8gb
        for data in capacityDDR4['8gb']:
            if '2666MHz' in data['Name']:  # 2666MHz 8gb DDR4
                frequencyDDR4['8gb_2666Mhz'].append(data)
            if '3000MHz' in data['Name']:  # 3000MHz 8gb DDR4
                frequencyDDR4['8gb_3000Mhz'].append(data)
            if '3200MHz' in data['Name']:  # 3200MHz 8gb DDR4
                frequencyDDR4['8gb_3200Mhz'].append(data)

        # FILTER == 16gb
        for data in capacityDDR4['16gb']:
            if '2666MHz' in data['Name']:  # 2666MHz 16gb DDR4
                frequencyDDR4['16gb_2666Mhz'].append(data)
            if '3600MHz' in data['Name']:  # 3600MHz 16gb DDR4
                frequencyDDR4['16gb_3600Mhz'].append(data)
            if '3000MHz' in data['Name']:  # 3000MHz 16gb DDR4
                frequencyDDR4['16gb_3200Mhz'].append(data)
            if '3200MHz' in data['Name']:  # 3200MHz 16gb DDR4
                frequencyDDR4['16gb_3200Mhz'].append(data)

        # FILTER == 32gb
        for data in capacityDDR4['32gb']:
            if '2666MHz' in data['Name']:  # 5600Mhz 32gb DDR4
                frequencyDDR4['32gb_2666Mhz'].append(data)
            if '3600MHz' in data['Name']:  # 5600Mhz 32gb DDR4
                frequencyDDR4['32gb_3600Mhz'].append(data)
            if '3000MHz' in data['Name']:  # 5600Mhz 32gb DDR4
                frequencyDDR4['32gb_3000Mhz'].append(data)
            if '3200MHz' in data['Name']:  # 5600Mhz 32gb DDR4
                frequencyDDR4['32gb_3200Mhz'].append(data)

        # Frequency / DDR3

        # FILTER == 4gb
        for data in capacityDDR3['4gb']:
            if '2400MHz' in data['Name']:  # 2400MHz 4gb DDR3
                frequencyDDR3['4gb_1333Mhz'].append(data)
            if '1600MHz' in data['Name']:  # 1600MHz 4gb DDR3
                frequencyDDR3['4gb_1600Mhz'].append(data)

        # FILTER == 8gb
        for data in capacityDDR3['8gb']:
            if '1600MHz' in data['Name']:  # 1600MHz 8gb DDR3
                frequencyDDR3['8gb_1600Mhz'].append(data)
            if '1866MHz' in data['Name']:  # 1866MHz 8gb DDR3
                frequencyDDR3['8gb_1866Mhz'].append(data)

        # FILTER == 16gb
        for data in capacityDDR3['16gb']:
            if '1600MHz' in data['Name']:  # 1600MHz 16gb DDR3
                frequencyDDR3['16gb_1600Mhz'].append(data)
            if '1866MHz' in data['Name']:  # 1866MHz 16gb DDR3
                frequencyDDR3['16gb_1866Mhz'].append(data)

        # FILTER == 32gb
        for data in capacityDDR3['32gb']:
            if '1600MHz' in data['Name']:  # 1600MHz 32gb DDR3
                frequencyDDR3['32gb_1600Mhz'].append(data)

        return DDR, capacityDDR5, capacityDDR4, capacityDDR3, frequencyDDR5, frequencyDDR4, frequencyDDR3, allRAM


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

        # Platform and integrate GPU
        Platform = {
            "AMD": {
                "cpuAMD": [],
                "apuAMD": []
            },
            "Intel": {
                "cpuIntel": [],
                "apuIntel": []
            }
        }
        Socket = {
            "cpuAM4": [],  # AMD AM4 and AMD AM4G
            "cpuFM2": [],  # FM2+
            "cpuLGA1150": [],  # LGA1150
            "cpuLGA1151": [],  # LGA1151
            "cpuLGA1200": [],  # LGA1200
            "cpuLGA1700": [],  # LGA1700
            "cpuLGA2066": [],  # LGA2066
        }

        # Platform

        # AMD
        # FILTER == AMD APU integrate GPU
        for data in allCPU:
            if 'AMD' in data['Name']:
                if '0G' in data['Name'] or '0GE' in data['Name'] or 'FM2+' in data['Name']:
                    Platform['AMD']['apuAMD'].append(data)

                # FILTER == AMD CPU without GPU
                else:
                    Platform['AMD']['cpuAMD'].append(data)

        # Intel
        # FILTER == Intel CPU without GPU
        for data in allCPU:
            if 'Intel' in data['Name']:
                if '5F' in data['Name'] or '0KF' in data['Name'] or '0X' in data['Name'] or '0F' in data['Name']:
                    Platform['Intel']['cpuIntel'].append(data)

                # FILTER == Intel APU integrate GPU
                else:
                    Platform['Intel']['apuIntel'].append(data)

        # Socket

        # FILTER == AMD AM4 and AMD AM4G
        allSocket = ['AM4', 'FM2+', 'LGA 1150', 'LGA 1151', 'LGA 1200', 'LGA 1700', 'LGA 2066']
        key = list(Socket.values())
        for i in range(len(allSocket)):
            for data in allCPU:
                if allSocket[i] in data['Name']:
                    key = list(Socket.values())
                    key[i].append(data)

        return Socket, Platform, allCPU


# GPU Filter
# In this object there are two functions that
# scraping the all GPU of Pichau Store and
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
        Model = {
            'GT 1030 2GB': [],
            'GT 610 2GB': [],
            'GT 710 1GB': [],
            'GT 710 2GB': [],
            'GT 730 2GB': [],
            'GT 730 4GB': [],
            'GT 240 1GB': [],
            'GTX 1050 2GB': [],
            'GTX 1050 3GB': [],
            'GTX 1050 TI 4GB': [],
            'GTX 1060 3GB': [],
            'GTX 1060 6GB': [],
            'GTX 1070 8GB': [],
            'GTX 1070 TI 8GB': [],
            'GTX 1080 8GB': [],
            'GTX 1080 TI 11GB': [],
            'GTX 1630 4GB': [],
            'GTX 1650 4GB': [],
            'GTX 1650 SUPER': [],
            'GTX 1660 6GB': [],
            'GTX 1660 SUPER': [],
            'GTX 1660 TI 6GB': [],
            'GTX 750 TI 2GB': [],
            'GTX 750 TI 4GB': [],
            'GTX 980 TI 6GB': [],
            'NVS 810 4GB': [],
            'PRO W6600 8GB': [],
            'QUADRO P1000 4GB': [],
            'QUADRO P2000 5GB': [],
            'QUADRO P400 2GB': [],
            'QUADRO P4000 8GB': [],
            'QUADRO P620 2GB': [],
            'QUADRO RTX 4000 8GB': [],
            'QUADRO RTX A2000 12GB': [],
            'QUADRO RTX A2000 6GB': [],
            'QUADRO RTX A4000 16GB': [],
            'QUADRO RTX A4500 20GB': [],
            'QUADRO RTX A5000 24GB': [],
            'QUADRO T1000 4GB': [],
            'QUADRO T1000 8GB': [],
            'QUADRO T400 2GB': [],
            'QUADRO T600 4GB': [],
            'R5 220 2GB': [],
            'R5 230 1GB': [],
            'R5 230 2GB': [],
            'R7 240': [],
            'RTX 2060 12GB': [],
            'RTX 2060 6GB': [],
            'RTX 2060 SUPER 8GB': [],
            'RTX 2070 8GB': [],
            'RTX 2070 SUPER 8GB': [],
            'RTX 2080 8GB': [],
            'RTX 2080 SUPER 8GB': [],
            'RTX 2080 TI 11GB': [],
            'RTX 3050 4GB': [],
            'RTX 3050 8GB': [],
            'RTX 3060 12GB': [],
            'RTX 3060 TI 8GB': [],
            'RTX 3070 8GB': [],
            'RTX 3070 TI 8GB': [],
            'RTX 3080 10GB': [],
            'RTX 3080 12GB': [],
            'RTX 3080 TI 12GB': [],
            'RTX 3090 24GB': [],
            'RTX 3090 TI 24 GB': [],
            'RX 460 2GB': [],
            'RX 550 2GB': [],
            'RX 550 4GB': [],
            'RX 5500 4GB': [],
            'RX 5600 XT 6GB': [],
            'RX 570 4GB': [],
            'RX 570 8GB': [],
            'RX 5700 8GB': [],
            'RX 5700 XT 8GB': [],
            'RX 580 4GB': [],
            'RX 580 8GB': [],
            'RX 590 8GB': [],
            'RX 6400 4GB': [],
            'RX 6500 XT 4GB': [],
            'RX 6600 8GB': [],
            'RX 6600 XT 8GB': [],
            'RX 6650 XT 8GB': [],
            'RX 6700 XT 12GB': [],
            'RX 6750 XT 12GB': [],
            'RX 6800 16GB': [],
            'RX 6800 XT 16GB': [],
            'RX 6900 XT 16GB': [],
            'RX 6950 XT 16GB': []
        }
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
        key = list(Model.values())
        for i in range(len(allModel)):
            for data in allGPU:
                if allModel[i] in data['Name']:
                    key = list(Model.values())
                    key[i].append(data)

        return Model, allGPU


# Mother Board Filter
# In this object there are two functions that
# scraping the all MotherBoards of Pichau Store and
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
        DDR = {
            "motherBoardDDR5": [],
            "motherBoardDDR4": [],
            "motherBoardDDR3": []
        }
        # MotherBoard Format
        Format = {
            "motherBoardATX": [],
            "motherBoardE_ATX": [],
            "motherBoardMicro_ATX": [],
            "motherBoardMini_ITX": []
        }
        # MotherBoard Socket
        Socket = {
            "motherBoardAM4": [],
            "motherBoardLGA1700": [],
            "motherBoardLGA1200": [],
            "motherBoardLGA1150": [],
            "motherBoardLGA1151": [],
            "motherBoardLGA1155": [],
            "motherBoardFM2": []
        }

        # Double Data Rate
        allDDR = ['DDR5', 'DDR4', 'DDR3']
        key = list(DDR.values())
        for i in range(len(allDDR)):
            for data in allMB:
                if allDDR[i] in data['Name']:
                    key = list(DDR.values())
                    key[i].append(data)

        # Format
        allFormat = ['ATX', 'E-ATX', 'MATX', 'Mini-ITX']
        key = list(Format.values())
        for i in range(len(allFormat)):
            for data in allMB:
                if allFormat[i] in data['Name']:
                    key = list(Format.values())
                    key[i].append(data)

        # Socket
        allSocket = ['AM4', 'LGA 1700', '1200', 'LGA 1150', 'LGA 1151', 'LGA 1155', 'FM2+']
        key = list(Socket.values())
        for i in range(len(allSocket)):
            for data in allMB:
                if allSocket[i] in data['Name']:
                    key = list(Socket.values())
                    key[i].append(data)

        return DDR, Format, Socket, allMB


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
        Capacity = {
            '10TB': [],
            '12TB': [],
            '14TB': [],
            '16TB': [],
            '1TB': [],
            '2TB': [],
            '3TB': [],
            '4TB': [],
            '6TB': [],
            '8TB': []
        }
        # Filters

        # HardDisk Capacity
        allCapacity = ['10TB', '12TB', '14TB', '16TB', '1TB', '2TB', '3TB', '4TB', '6TB', '8TB']
        key = list(Capacity.values())
        for i in range(len(allCapacity)):
            for data in allHD:
                if allCapacity[i] in data['Name']:
                    key = list(Capacity.values())
                    key[i].append(data)

        return Capacity, allHD


Terabyte_Capacity, TerabyteAllHD = TerabyteHD.HD_FILTERS()
TerabyteMB_DDR, TerabyteMB_Format, TerabyteMB_Socket, TerabyteAllMB = TerabyteMotherBoard.MB_FILTERS()
# TerabyteGPU_Model, TerabyteAllGPU = TerabyteGPU.GPU_FILTERS()
# TerabyteCPU_Socket, TerabyteCPU_Platform, TerabyteAllCPU = TerabyteCPU.CPU_FILTERS()
# TerabyteRAM_DDR, TerabyteRAM_capacityDDR5, TerabyteRAM_capacityDDR4, TerabyteRAM_capacityDDR3, TerabyteRAM_frequencyDDR5, TerabyteRAM_frequencyDDR4, TerabyteRAM_frequencyDDR3, TerabyteAllRAM = TerabyteRAM.RAM_FILTERS()
