from CPU import CPU

# Specific CPU lists

# Platform and integrate VGA

# AMD
cpuAMD = []
apuAMD = []

# Intel
cpuIntel = []
apuIntel = []

# Socket
cpuAM4 = []  # AMD AM4 and AMD AM4G
cpuFM2 = []  # FM2+
cpuLGA1150 = []  # LGA1150
cpuLGA1151 = []  # LGA1151
cpuLGA1200 = []  # LGA1200
cpuLGA1700 = []  # LGA1700
cpuLGA2066 = []  # LGA2066

allData = CPU.c()


class FilterCPU:
    @staticmethod
    def cpu_Pichau():
        # Platform
        # AMD
        # FILTER == AMD APU integrate VGA
        for data in allData:
            if 'AMD' in data['Name']:
                if '0G' in data['Name'] or '0GE' in data['Name'] or 'FM2+' in data['Name']:
                    apuAMD.append(data)

        # FILTER == AMD CPU without VGA
                else:
                    cpuAMD.append(data)

        # Intel
        # FILTER == Intel CPU without VGA
        for data in allData:
            if 'Intel' in data['Name']:
                if '5F' in data['Name'] or '0KF' in data['Name'] or '0X' in data['Name'] or '0F' in data['Name']:
                    cpuIntel.append(data)

        # FILTER == Intel APU integrate VGA
                else:
                    apuIntel.append(data)

        # Socket

        # FILTER == AMD AM4 and AMD AM4G
        for data in allData:
            if 'AM4' in data['Name']:
                cpuAM4.append(data)

        # FILTER == FM2+
            if 'FM2+' in data['Name']:
                cpuFM2.append(data)

        # FILTER == LGA1150
            if 'LGA1150' in data['Name']:
                cpuLGA1150.append(data)

        # FILTER == LGA1151
            if 'LGA1151' in data['Name']:
                cpuLGA1151.append(data)

        # FILTER == LGA1200
            if 'LGA1200' in data['Name']:
                cpuLGA1200.append(data)

        # FILTER == LGA1700
            if 'LGA1700' in data['Name']:
                cpuLGA1700.append(data)

        # FILTER == LGA2066
            if 'LGA2066' in data['Name']:
                cpuLGA2066.append(data)

