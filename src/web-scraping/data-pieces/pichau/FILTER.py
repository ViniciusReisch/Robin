from GPU import GraphicsCard
from CPU import CPU

class PichauGPU:

    @staticmethod
    def GPU_get():
        allGPU = GraphicsCard.GPU_Crawl()
        return allGPU

    @staticmethod
    def GPU_FILTERS():
        allGPU = PichauGPU.GPU_get()

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


class PichauCPU:

    @staticmethod
    def CPU_get():
        allGPU = GraphicsCard.GPU_Crawl()
        return allGPU

    @staticmethod
    def GPU_FILTERS():
        allGPU = PichauGPU.GPU_get()
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
        allSocket = ['AM4', 'FM2+', 'LGA1150', 'LGA1151', 'LGA1200', 'LGA1700', 'LGA2066']
        key = list(Socket.values())
        for i in range(len(allSocket)):
            for data in allCPU:
                if allSocket[i] in data['Name']:
                    key = list(Socket.values())
                    key[i].append(data)