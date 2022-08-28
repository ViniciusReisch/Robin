from RAM import RAM
from CPU import CPU


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


TerabyteCPU_Socket, TerabyteCPU_Platform, TerabyteAllCPU = TerabyteCPU.CPU_FILTERS()
# TerabyteRAM_DDR, TerabyteRAM_capacityDDR5, TerabyteRAM_capacityDDR4, TerabyteRAM_capacityDDR3, TerabyteRAM_frequencyDDR5, TerabyteRAM_frequencyDDR4, TerabyteRAM_frequencyDDR3, TerabyteAllRAM = TerabyteRAM.RAM_FILTERS()
