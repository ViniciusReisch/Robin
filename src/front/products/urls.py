from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ALL PATHS
    path('allproducts/', views.allProducts, name='allproducts'),
    path('allram/', views.ram, name='allram'),
    path('allmb/', views.motherboard, name='allmb'),
    path('allhd/', views.HD, name='allhd'),
    path('allssd/', views.SSD, name='allssd'),
    path('allgpu/', views.GPU, name='allgpu'),
    path('allcpu/', views.CPU, name='allcpu'),
    path('allfont/', views.font, name='allfont'),
    path('allcabinet/', views.cabinet, name='allcabinet'),


    # Motherboard DDR
    path('mbddr3/', views.motherboard_ddr3, name='motherboard_ddr3'),
    path('mbddr4/', views.motherboard_ddr4, name='motherboard_ddr4'),
    path('mbddr5/', views.motherboard_ddr5, name='motherboard_ddr5'),

    # Motherboard Socket
    path('mbAM4/', views.motherboard_socketAM4, name='motherboard_socketAM4'),
    path('mbLGA1700/', views.motherboard_socketLGA1700, name='motherboard_socketLGA1700'),
    path('mbLGA1200/', views.motherboard_socket1200, name='motherboard_socket1200'),
    path('mbLGA1150/', views.motherboard_socketLGA1150, name='motherboard_socketLGA1150'),
    path('mbLGA1151/', views.motherboard_socketLGA1151, name='motherboard_socketLGA1151'),
    path('mbLGA1155/', views.motherboard_socketLGA1155, name='motherboard_socketLGA1155'),
    path('mbFM2/', views.motherboard_socketFM2, name='motherboard_socketFM2'),

    # Motherboard Socket
    path('mbatx/', views.motherboard_ATX, name='motherboard_ATX'),
    path('mbeatx/', views.motherboard_EATX, name='motherboard_EATX'),
    path('mbmatx/', views.motherboard_MATX, name='motherboard_MATX'),
    path('mbminiitx/', views.motherboard_MiniITX, name='motherboard_MiniITX'),


    # CPU Format
    path('cpuintel/', views.Intel_CPU, name='intelcpu'),
    path('apuintel/', views.Intel_APU, name='apuintel'),
    path('cpuamd/', views.AMD_CPU, name='cpuamd'),
    path('apuamd/', views.AMD_APU, name='apuamd'),

    # CPU Socket
    path('socketam4/', views.socket_AM4, name='am4'),
    path('socketfm2/', views.socket_FM2, name='fm2'),
    path('socketlga1150/', views.socket_LGA1150, name='lga1150'),
    path('socketlga1151/', views.socket_LGA1151, name='lga1151'),
    path('socketlga1200/', views.socket_LGA1200, name='lga1200'),
    path('socketlga1700/', views.socket_LGA1700, name='lga1700'),
    path('socketlga2066/', views.socket_LGA2066, name='lga2066'),


    # RAM DDR

    path('ramddr3/', views.RAM_ddr3, name='RAM_ddr3'),
    path('ramddr4/', views.RAM_ddr4, name='RAM_ddr4'),
    path('ramddr5/', views.RAM_ddr5, name='RAM_ddr5'),

    # RAM Capacity

    path('ram4gb/', views.RAM_4gb, name='RAM_4gb'),
    path('ram8gb/', views.RAM_8gb, name='RAM_8gb'),
    path('ram16gb/', views.RAM_16gb, name='RAM_16gb'),
    path('ram32gb/', views.RAM_32gb, name='RAM_32gb'),
    path('ram64gb/', views.RAM_64gb, name='RAM_64gb'),

    # RAM Frequency

    path('ram1866mhz/', views.RAM_1866mhz, name='RAM_1866mhz'),
    path('ram3600mhz/', views.RAM_3600mhz, name='RAM_3600mhz'),
    path('ram3200mhz/', views.RAM_3200mhz, name='RAM_3200mhz'),
    path('ram3000mhz/', views.RAM_3000mhz, name='RAM_3000mhz'),
    path('ram2666mhz/', views.RAM_2666mhz, name='RAM_2666mhz'),
    path('ram1600mhz/', views.RAM_1600mhz, name='RAM_1600mhz'),
    path('ram2400mhz/', views.RAM_2400mhz, name='RAM_2400mhz'),
    path('ram6000mhz/', views.RAM_6000mhz, name='RAM_6000mhz'),
    path('ram5600mhz/', views.RAM_5600mhz, name='RAM_5600mhz'),
    path('ram4800mhz/', views.RAM_4800mhz, name='RAM_4800mhz'),

    # GPU Models

    path('gpugt1030/', views.GPU_GT1030, name='GPU_GT1030'),
    path('gpugt610/', views.GPU_GT610, name='GPU_GT610'),
    path('gpugt7101GB/', views.GPU_GT7101GB, name='GPU_GT7101GB'),
    path('gpugt7102GB/', views.GPU_GT7102GB, name='GPU_GT7102GB'),
    path('gpugt730/', views.GPU_GT730, name='GPU_GT730'),
    path('gpugt240/', views.GPU_GT240, name='GPU_GT240'),
    path('gpugtx10502GB/', views.GPU_GTX10502GB, name='GPU_GTX10502GB'),
    path('gpugtx10503GB/', views.GPU_GTX10503GB, name='GPU_GTX10503GB'),
    path('gpugtx1050TI/', views.GPU_GTX1050TI, name='GPU_GTX1050TI'),
    path('gpugtx1060/', views.GPU_GTX1060, name='GPU_GTX1060'),
    path('gpugtx1070/', views.GPU_GTX1070, name='GPU_GTX1070'),
    path('gpugtx1070TI/', views.GPU_GTX1070TI, name='GPU_GTX1070TI'),
    path('gpugtx1080/', views.GPU_GTX1080, name='GPU_GTX1080'),
    path('gpugtx1080TI/', views.GPU_GTX1080TI, name='GPU_GTX1080TI'),
    path('gpugtx1630/', views.GPU_GTX1630, name='GPU_GTX1630'),
    path('gpugtx1650/', views.GPU_GTX1650, name='GPU_GTX1650'),
    path('gpugtx1650SUPER/', views.GPU_GTX1650SUPER, name='GPU_GTX1650SUPER'),
    path('gpugtx1660/', views.GPU_GTX1660, name='GPU_GTX1660'),
    path('gpugtx1660SUPER/', views.GPU_GTX1660SUPER, name='GPU_GTX1660SUPER'),
    path('gpugtx1660TI/', views.GPU_GTX1660TI, name='GPU_GT1660TI'),
    path('gpugtx750TI/', views.GPU_GTX750TI, name='GPU_GTx750TI'),
    path('gpugtx980TI/', views.GPU_GTX980TI, name='GPU_GTX980TI'),
    path('gpunvs810/', views.GPU_NVS810, name='GPU_NVS810'),
    path('gpuprow6600/', views.GPU_PROW6600, name='GPU_PROW6600'),
    path('gpuquadrop1000/', views.GPU_QUADROP1000, name='GPU_QUADROP1000'),
    path('gpuquadrop2000/', views.GPU_QUADROP2000, name='GPU_QUADROP2000'),
    path('gpuquadrop400/', views.GPU_QUADROP400, name='GPU_QUADROP400'),
    path('gpuquadrop4000/', views.GPU_QUADROP4000, name='GPU_QUADROP4000'),
    path('gpuquadrop620/', views.GPU_QUADROP620, name='GPU_QUADROP620'),
    path('gpuquadrortx4000/', views.GPU_QUADRORTX4000, name='GPU_QUADRORTX4000'),
    path('gpuquadrortxa2000/', views.GPU_QUADRORTXA2000, name='GPU_QUADRORTXA2000'),
    path('gpuquadrortxa4000/', views.GPU_QUADRORTXA4000, name='GPU_QUADRORTXA4000'),
    path('gpuquadrortxa4500/', views.GPU_QUADRORTXA4500, name='GPU_QUADRORTXA4500'),
    path('gpuquadrortxa5000/', views.GPU_QUADRORTXA5000, name='GPU_QUADRORTXA5000'),
    path('gpuquadrot1000/', views.GPU_QUADROT1000, name='GPU_QUADROT1000'),
    path('gpuquadrot400/', views.GPU_QUADROT400, name='GPU_QUADROT400'),
    path('gpuquadrot600/', views.GPU_QUADROT600, name='GPU_QUADROT600'),
    path('gpur52202GB/', views.GPU_R52202GB, name='GPU_R52202GB'),
    path('gpur52301GB/', views.GPU_R52301GB, name='GPU_R52301GB'),
    path('gpur52302GB/', views.GPU_R52302GB, name='GPU_R52302GB'),
    path('gpur7240/', views.GPU_R7240, name='GPU_R7240'),
    path('gpurtx2060/', views.GPU_RTX2060, name='GPU_RTX2060'),
    path('gpurtx2060SUPER/', views.GPU_RTX2060SUPER, name='GPU_RTX2060SUPER'),
    path('gpurtx2070/', views.GPU_RTX2070, name='GPU_RTX2070'),
    path('gpurtx2070SUPER/', views.GPU_RTX2070SUPER, name='GPU_RTX2070SUPER'),
    path('gpurtx2080/', views.GPU_RTX2080, name='GPU_RTX2080'),
    path('gpurtx2080SUPER/', views.GPU_RTX2080SUPER, name='GPU_RTX2080SUPER'),
    path('gpurtx2080TI/', views.GPU_RTX2080TI, name='GPU_RTX2080TI'),
    path('gpurtx3050/', views.GPU_RTX3050, name='GPU_RTX3050'),
    path('gpurtx3060/', views.GPU_RTX3060, name='GPU_RTX3060'),
    path('gpurtx3060TI/', views.GPU_RTX3060TI, name='GPU_RTX3060TI'),
    path('gpurtx3070/', views.GPU_RTX3070, name='GPU_RTX3070'),
    path('gpurtx3070TI/', views.GPU_RTX3070TI, name='GPU_RTX3070TI'),
    path('gpurtx3080/', views.GPU_RTX3080, name='GPU_RTX3080'),
    path('gpurtx3080TI/', views.GPU_RTX3080TI, name='GPU_RTX3080TI'),
    path('gpurtx3090/', views.GPU_RTX3090, name='GPU_RTX3090'),
    path('gpurtx3090TI/', views.GPU_RTX3090TI, name='GPU_RTX3090TI'),
    path('gpurx460/', views.GPU_RX460, name='GPU_RX460'),
    path('gpurx550/', views.GPU_RX550, name='GPU_RX550'),
    path('gpurx5500/', views.GPU_RX550, name='GPU_RX5500'),
    path('gpurx5600XT/', views.GPU_RX5500XT, name='GPU_RX5600XT'),
    path('gpurx570/', views.GPU_RX570, name='GPU_RX570'),
    path('gpurx5700/', views.GPU_RX5700, name='GPU_RX5700'),
    path('gpurx580/', views.GPU_RX580, name='GPU_RX580'),
    path('gpurx590/', views.GPU_RX590, name='GPU_RX590'),
    path('gpurx6400/', views.GPU_RX6400, name='GPU_RX6400'),
    path('gpurx6500XT/', views.GPU_RX6500XT, name='GPU_RX6500XT'),
    path('gpurx6600/', views.GPU_RX6600, name='GPU_RX6600'),
    path('gpurx6600XT/', views.GPU_RX6600XT, name='GPU_RX6600XT'),
    path('gpurx6650XT/', views.GPU_RX6650XT, name='GPU_RX6650XT'),
    path('gpurx6700XT/', views.GPU_RX6700XT, name='GPU_RX6700XT'),
    path('gpurx6750XT/', views.GPU_RX6750XT, name='GPU_RX6750XT'),
    path('gpurx6800/', views.GPU_RX6800, name='GPU_RX6800'),
    path('gpurx6800XT/', views.GPU_RX6800XT, name='GPU_RX6800XT'),
    path('gpurx6900XT/', views.GPU_RX6900XT, name='GPU_RX6900XT'),
    path('gpurx6950XT/', views.GPU_RX6950XT, name='GPU_RX6950XT')


    # SSD Interface

    path('ssdnvme/', views.SSD_NVME, name='SSD_NVME'),
    path('ssdsata/', views.SSD_SATA, name='SSD_SATA'),

    # SSD Format

    path('ssd25/', views.SSD_25, name='SSD_25'),
    path('ssdm2/', views.SSD_M2, name='SSD_M2'),
    path('ssdpcie/', views.SSD_PCIe, name='SSD_PCIe'),

    # SSD Capacity

    path('ssd120gb/', views.SSD_120GB, name='SSD_120GB'),
    path('ssd128gb/', views.SSD_128GB, name='SSD_128GB'),
    path('ssd1tb/', views.SSD_1TB, name='SSD_1TB'),
    path('ssd2tb/', views.SSD_2TB, name='SSD_2TB'),
    path('ssd240gb/', views.SSD_240GB, name='SSD_240GB'),
    path('ssd250gb/', views.SSD_250GB, name='SSD_250GB'),
    path('ssd256gb/', views.SSD_256GB, name='SSD_256GB'),
    path('ssd480gb/', views.SSD_480GB, name='SSD_480GB'),
    path('ssd4tb/', views.SSD_4TB, name='SSD_4TB'),
    path('ssd500gb/', views.SSD_500GB, name='SSD_500GB'),
    path('ssd8tb/', views.SSD_8TB, name='SSD_8TB'),
    path('ssd980gb/', views.SSD_980GB, name='SSD_980GB'),


    # Cabinet Colors

    path('cabinetazul/', views.cabinet_Azul, name='cabinet_Azul'),
    path('cabinetbranco/', views.cabinet_Branco, name='cabinet_Branco'),
    path('cabinetpreto/', views.cabinet_Preto, name='cabinet_Preto'),
    path('cabinetcinza/', views.cabinet_Cinza, name='cabinet_Cinza'),
    path('cabinetrosa/', views.cabinet_Rosa, name='cabinet_Rosa'),
    path('cabinetverde/', views.cabinet_Verde, name='cabinet_Verde'),
    path('cabinetbrancopreto/', views.cabinet_BrancoPreto, name='cabinet_BrancoPreto'),
    path('cabinetpretolaranja/', views.cabinet_PretoLaranja, name='cabinet_PretoLaranja'),
    path('cabinetblackgray/', views.cabinet_BlackGray, name='cabinet_BlackGray'),
    path('cabinetred/', views.cabinet_Red, name='cabinet_Red'),


    # Cabinet Size

    path('cabinetfulltower/', views.cabinet_fulltower, name='cabinet_fulltower'),
    path('cabinetmidtower/', views.cabinet_midtower, name='cabinet_midtower'),
    path('cabinetminitower/', views.cabinet_minitower, name='cabinet_minitower'),

]