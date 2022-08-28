from RAM import RAM


# RAM Filter
# In this object there are two functions that
# scraping the all RAM memories of Pichau Store and
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


RAM_DDR, RAM_capacityDDR5, RAM_capacityDDR4, RAM_capacityDDR3, RAM_frequencyDDR5, RAM_frequencyDDR4, RAM_frequencyDDR3, allRAM = TerabyteRAM.RAM_FILTERS()