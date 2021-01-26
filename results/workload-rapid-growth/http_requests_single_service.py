import matplotlib.pyplot as plot
import matplotlib

W = 2.50 # inches
matplotlib.use("pgf")
matplotlib.rcParams.update({
    'figure.figsize': (W, W/(4/3)),
    'text.usetex' : True,
    'font.size' : 5,                   # Set font size to 11pt
    'axes.labelsize': 5,               # -> axis labels
    'legend.fontsize': 4,              # -> legends
    'font.family' : 'lmodern',
})

max_requests = 150
t = [1611594897, 1611594898, 1611594899, 1611594900, 1611594901, 1611594902, 1611594903, 1611594904, 1611594905, 1611594906, 1611594907, 1611594908, 1611594909, 1611594910, 1611594911, 1611594912, 1611594913, 1611594914, 1611594915, 1611594916, 1611594917, 1611594918, 1611594919, 1611594920, 1611594921, 1611594922, 1611594923, 1611594924, 1611594925, 1611594926, 1611594927, 1611594928, 1611594929, 1611594930, 1611594931, 1611594932, 1611594933, 1611594934, 1611594935, 1611594936, 1611594937, 1611594938, 1611594939, 1611594940, 1611594941, 1611594942, 1611594943, 1611594944, 1611594945, 1611594946, 1611594947, 1611594948, 1611594949, 1611594950, 1611594951, 1611594952, 1611594953, 1611594954, 1611594955, 1611594956, 1611594957, 1611594958, 1611594959, 1611594960, 1611594961, 1611594962, 1611594963, 1611594964, 1611594965, 1611594966, 1611594967, 1611594968, 1611594969, 1611594970, 1611594971, 1611594972, 1611594973, 1611594974, 1611594975, 1611594976, 1611594977, 1611594978, 1611594979, 1611594980, 1611594981, 1611594982, 1611594983, 1611594984, 1611594985, 1611594986, 1611594987, 1611594988, 1611594989, 1611594990, 1611594991, 1611594992, 1611594993, 1611594994, 1611594995, 1611594996, 1611594997, 1611594998, 1611594999, 1611595000, 1611595001, 1611595002, 1611595003, 1611595004, 1611595005, 1611595006, 1611595007, 1611595008, 1611595009, 1611595010, 1611595011, 1611595012, 1611595013, 1611595014, 1611595015, 1611595016, 1611595017, 1611595018, 1611595019, 1611595020, 1611595021, 1611595022, 1611595023, 1611595024, 1611595025, 1611595026, 1611595027, 1611595028, 1611595029, 1611595030, 1611595031, 1611595032, 1611595033, 1611595034, 1611595035, 1611595036, 1611595037, 1611595038, 1611595039, 1611595040, 1611595041, 1611595042, 1611595043, 1611595044, 1611595045, 1611595046, 1611595047, 1611595048, 1611595049, 1611595050, 1611595051, 1611595052, 1611595053, 1611595054, 1611595055, 1611595056, 1611595057, 1611595058, 1611595059, 1611595060, 1611595061, 1611595062, 1611595063, 1611595064, 1611595065, 1611595066, 1611595067, 1611595068, 1611595069, 1611595070, 1611595071, 1611595072, 1611595073, 1611595074, 1611595075, 1611595076, 1611595077, 1611595078, 1611595079, 1611595080, 1611595081, 1611595082, 1611595083, 1611595084, 1611595085, 1611595086, 1611595087, 1611595088, 1611595089, 1611595090, 1611595091, 1611595092, 1611595093, 1611595094, 1611595095, 1611595096, 1611595097, 1611595098, 1611595099, 1611595100, 1611595101, 1611595102, 1611595103, 1611595104, 1611595105, 1611595106, 1611595107, 1611595108, 1611595109, 1611595110, 1611595111, 1611595112, 1611595113, 1611595114, 1611595115, 1611595116, 1611595117, 1611595118, 1611595119, 1611595120, 1611595121, 1611595122, 1611595123, 1611595124, 1611595125, 1611595126, 1611595127, 1611595128, 1611595129, 1611595130, 1611595131, 1611595132, 1611595133, 1611595134, 1611595135, 1611595136, 1611595137, 1611595138, 1611595139, 1611595140, 1611595141, 1611595142, 1611595143, 1611595144, 1611595145, 1611595146, 1611595147, 1611595148, 1611595149, 1611595150, 1611595151, 1611595152, 1611595153, 1611595154, 1611595155, 1611595156, 1611595157, 1611595158, 1611595159, 1611595160, 1611595161, 1611595162, 1611595163, 1611595164, 1611595165, 1611595166, 1611595167, 1611595168, 1611595169, 1611595170, 1611595171, 1611595172, 1611595173, 1611595174, 1611595175, 1611595176, 1611595177, 1611595178, 1611595179, 1611595180, 1611595181, 1611595182, 1611595183, 1611595184, 1611595185, 1611595186, 1611595187, 1611595188, 1611595189, 1611595190, 1611595191, 1611595192, 1611595193, 1611595194, 1611595195, 1611595196, 1611595197, 1611595198, 1611595199, 1611595200, 1611595201, 1611595202, 1611595203, 1611595204, 1611595205, 1611595206, 1611595207, 1611595208, 1611595209, 1611595210, 1611595211, 1611595212, 1611595213, 1611595214, 1611595215, 1611595216, 1611595217, 1611595218, 1611595219, 1611595220, 1611595221, 1611595222, 1611595223, 1611595224, 1611595225, 1611595226, 1611595227, 1611595228, 1611595229, 1611595230, 1611595231, 1611595232, 1611595233, 1611595234, 1611595235, 1611595236, 1611595237, 1611595238, 1611595239, 1611595240, 1611595241, 1611595242, 1611595243, 1611595244, 1611595245, 1611595246, 1611595247, 1611595248, 1611595249, 1611595250, 1611595251, 1611595252, 1611595253, 1611595254, 1611595255, 1611595256, 1611595257, 1611595258, 1611595259, 1611595260, 1611595261, 1611595262, 1611595263, 1611595264, 1611595265, 1611595266, 1611595267, 1611595268, 1611595269, 1611595270, 1611595271, 1611595272, 1611595273, 1611595274, 1611595275, 1611595276, 1611595277, 1611595278, 1611595279, 1611595280, 1611595281, 1611595282, 1611595283, 1611595284, 1611595285, 1611595286, 1611595287, 1611595288, 1611595289, 1611595290, 1611595291, 1611595292, 1611595293, 1611595294, 1611595295, 1611595296, 1611595297, 1611595298, 1611595299, 1611595300, 1611595301, 1611595302, 1611595303, 1611595304, 1611595305, 1611595306, 1611595307, 1611595308, 1611595309, 1611595310, 1611595311, 1611595312, 1611595313, 1611595314, 1611595315, 1611595316, 1611595317, 1611595318, 1611595319, 1611595320, 1611595321, 1611595322, 1611595323, 1611595324, 1611595325, 1611595326, 1611595327, 1611595328, 1611595329, 1611595330, 1611595331, 1611595332, 1611595333, 1611595334, 1611595335, 1611595336, 1611595337, 1611595338, 1611595339, 1611595340, 1611595341, 1611595342, 1611595343, 1611595344, 1611595345, 1611595346, 1611595347, 1611595348, 1611595349, 1611595350, 1611595351, 1611595352, 1611595353, 1611595354, 1611595355, 1611595356, 1611595357, 1611595358, 1611595359, 1611595360, 1611595361, 1611595362, 1611595363, 1611595364, 1611595365, 1611595366, 1611595367, 1611595368, 1611595369, 1611595370, 1611595371, 1611595372, 1611595373, 1611595374, 1611595375, 1611595376, 1611595377, 1611595378, 1611595379, 1611595380, 1611595381, 1611595382, 1611595383, 1611595384, 1611595385, 1611595386, 1611595387, 1611595388, 1611595389, 1611595390, 1611595391, 1611595392, 1611595393, 1611595394, 1611595395, 1611595396, 1611595397, 1611595398, 1611595399, 1611595400, 1611595401, 1611595402, 1611595403, 1611595404, 1611595405, 1611595406, 1611595407, 1611595408, 1611595409, 1611595410, 1611595411, 1611595412, 1611595413, 1611595414, 1611595415, 1611595416, 1611595417, 1611595418, 1611595419, 1611595420, 1611595421, 1611595422, 1611595423, 1611595424, 1611595425, 1611595426, 1611595427, 1611595428, 1611595429, 1611595430, 1611595431, 1611595432, 1611595433, 1611595434, 1611595435, 1611595436, 1611595437, 1611595438, 1611595439, 1611595440, 1611595441, 1611595442, 1611595443, 1611595444, 1611595445, 1611595446, 1611595447, 1611595448, 1611595449, 1611595450, 1611595451, 1611595452, 1611595453, 1611595454, 1611595455, 1611595456, 1611595457, 1611595458, 1611595459, 1611595460, 1611595461, 1611595462, 1611595463, 1611595464, 1611595465, 1611595466, 1611595467, 1611595468, 1611595469, 1611595470, 1611595471, 1611595472, 1611595473, 1611595474, 1611595475, 1611595476, 1611595477, 1611595478, 1611595479, 1611595480, 1611595481, 1611595482, 1611595483, 1611595484, 1611595485, 1611595486, 1611595487, 1611595488, 1611595489, 1611595490, 1611595491, 1611595492, 1611595493, 1611595494, 1611595495, 1611595496, 1611595497]
s0 = [32, 32, 32, 32, 32, 42.39999999999999, 42.39999999999999, 42.39999999999999, 42.39999999999999, 42.39999999999999, 50, 50, 50, 50, 50, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 50, 50, 50, 50, 50, 50.4, 50.4, 50.4, 50.4, 50.4, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50.4, 50.4, 50.4, 50.4, 50.4, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 52.39999999999999, 52.39999999999999, 52.39999999999999, 52.39999999999999, 52.39999999999999, 51.599999999999994, 51.599999999999994, 51.599999999999994, 51.599999999999994, 51.599999999999994, 56, 56, 56, 56, 56, 65.6, 65.6, 65.6, 65.6, 65.6, 81.6, 81.6, 81.6, 81.6, 81.6, 92, 92, 92, 92, 92, 107.19999999999999, 107.19999999999999, 107.19999999999999, 107.19999999999999, 107.19999999999999, 118.79999999999998, 118.79999999999998, 118.79999999999998, 118.79999999999998, 118.79999999999998, 126.39999999999999, 126.39999999999999, 126.39999999999999, 126.39999999999999, 126.39999999999999, 134.4, 134.4, 134.4, 134.4, 134.4, 147.2, 149.2, 149.2, 153.2, 153.2, 152.8, 148.8, 146.8, 146.8, 146.8, 139.60000000000002, 139.60000000000002, 139.60000000000002, 139.60000000000002, 139.60000000000002, 134.79999999999998, 134.79999999999998, 134.79999999999998, 134.79999999999998, 134.79999999999998, 120.8, 120.8, 120.8, 120.8, 120.8, 112.4, 112.4, 112.4, 112.4, 112.4, 110.8, 110.8, 110.8, 110.8, 110.8, 116.8, 116.8, 116.8, 116.8, 116.8, 120.8, 120.8, 120.8, 120.8, 120.8, 128, 128, 128, 128, 128, 135.2, 135.2, 135.2, 135.2, 135.2, 137.6, 137.6, 137.6, 137.6, 137.6, 146, 146, 146, 146, 146, 152, 152, 152, 152, 152, 157.59999999999997, 157.59999999999997, 157.59999999999997, 157.59999999999997, 157.59999999999997, 161.6, 161.6, 161.6, 161.6, 161.6, 169.2, 169.2, 169.2, 169.2, 169.2, 158.4, 158.4, 158.4, 158.4, 158.4, 147.2, 147.2, 147.2, 147.2, 147.2, 138.79999999999998, 138.79999999999998, 138.79999999999998, 138.79999999999998, 138.79999999999998, 124, 124, 124, 124, 124, 116, 116, 116, 116, 116, 118.79999999999998, 118.79999999999998, 118.79999999999998, 118.79999999999998, 118.79999999999998, 127.6, 127.6, 127.6, 127.6, 127.6, 128.4, 128.4, 128.4, 128.4, 128.4, 126.39999999999999, 126.39999999999999, 126.39999999999999, 126.39999999999999, 126.39999999999999, 119.60000000000001, 119.60000000000001, 119.60000000000001, 119.60000000000001, 119.60000000000001, 118.79999999999998, 118.79999999999998, 118.79999999999998, 118.79999999999998, 118.79999999999998, 115.19999999999999, 115.19999999999999, 115.19999999999999, 115.19999999999999, 115.19999999999999, 117.19999999999999, 117.19999999999999, 117.19999999999999, 117.19999999999999, 117.19999999999999, 120.39999999999999, 120.39999999999999, 120.39999999999999, 120.39999999999999, 120.39999999999999, 125.19999999999999, 125.19999999999999, 125.19999999999999, 125.19999999999999, 125.19999999999999, 126, 126, 126, 126, 126, 122, 122, 122, 122, 122, 118.79999999999998, 118.79999999999998, 118.79999999999998, 118.79999999999998, 118.79999999999998, 119.60000000000001, 119.60000000000001, 119.60000000000001, 119.60000000000001, 119.60000000000001, 120.39999999999999, 120.39999999999999, 120.39999999999999, 120.39999999999999, 120.39999999999999, 118, 118, 118, 118, 118, 119.19999999999999, 119.19999999999999, 119.19999999999999, 119.19999999999999, 119.19999999999999, 123.19999999999999, 123.19999999999999, 123.19999999999999, 123.19999999999999, 123.19999999999999, 122.8, 122.8, 122.8, 122.8, 122.8, 120, 120, 120, 120, 120, 121.19999999999999, 121.19999999999999, 121.19999999999999, 121.19999999999999, 121.19999999999999, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 123.60000000000001, 128, 128, 128, 128, 128, 130, 130, 130, 130, 130, 129.60000000000002, 129.60000000000002, 129.60000000000002, 129.60000000000002, 129.60000000000002, 122.4, 122.4, 122.4, 122.4, 122.4, 122.4, 122.4, 122.4, 122.4, 122.4, 120.8, 120.8, 120.8, 120.8, 120.8, 119.19999999999999, 119.19999999999999, 119.19999999999999, 119.19999999999999, 119.19999999999999, 115.60000000000001, 115.60000000000001, 115.60000000000001, 115.60000000000001, 115.60000000000001, 109.60000000000001, 109.60000000000001, 109.60000000000001, 109.60000000000001, 109.60000000000001, 100.39999999999999, 100.39999999999999, 100.39999999999999, 100.39999999999999, 100.39999999999999, 87.19999999999999, 87.19999999999999, 87.19999999999999, 87.19999999999999, 87.19999999999999, 75.6, 75.6, 75.6, 75.6, 75.6, 66.80000000000001, 66.80000000000001, 66.80000000000001, 66.80000000000001, 66.80000000000001, 63.199999999999996, 63.199999999999996, 63.199999999999996, 63.199999999999996, 63.199999999999996, 63.599999999999994, 63.599999999999994, 63.599999999999994, 63.599999999999994, 63.599999999999994, 74.80000000000001, 74.80000000000001, 74.80000000000001, 74.80000000000001, 74.80000000000001, 84, 84, 84, 84, 84, 92, 92, 92, 92, 92, 100, 100, 100, 100, 100, 115.19999999999999, 115.19999999999999, 115.19999999999999, 115.19999999999999, 115.19999999999999, 132, 132, 132, 132, 132, 138, 142, 143, 145.3, 146.3, 147, 147, 147, 149.2, 150.2, 150, 150, 150, 150, 150, 150, 150, 150, 150, 148, 148, 148, 148, 148, 148, 148, 148, 148, 148, 148, 151.6, 151.6, 151.6, 151.6, 151.6, 132, 132, 132, 132, 132, 110.8, 110.8, 110.8, 110.8, 110.8, 104, 104, 104, 104, 104, 105.60000000000001, 105.60000000000001, 105.60000000000001, 105.60000000000001, 105.60000000000001, 101.6, 101.6, 101.6, 101.6, 101.6, 97.6, 97.6, 97.6, 97.6, 97.6, 98.79999999999998, 98.79999999999998, 98.79999999999998, 98.79999999999998, 98.79999999999998, 94, 94, 94, 94, 94, 77.2, 77.2, 77.2, 77.2, 77.2, 62, 62, 62, 62, 62, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 49.599999999999994, 34, 34, 34, 34, 34, 19.6, 19.6, 19.6, 19.6, 19.6, 19.199999999999996, 19.199999999999996, 19.199999999999996, 19.199999999999996, 19.199999999999996, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 20.8, 20.8, 20.8, 20.8, 20.8, 26.400000000000002, 26.400000000000002, 26.400000000000002, 26.400000000000002, 26.400000000000002, 29.6, 29.6, 29.6, 29.6, 29.6, 34, 34, 34, 34, 34, 37.599999999999994, 37.599999999999994, 37.599999999999994, 37.599999999999994, 37.599999999999994, 40.4, 40.4, 40.4, 40.4, 40.4, 39.6, 39.6, 39.6, 39.6, 39.6, 40]
x_seconds = list(range(0,len(t)))

f=plot.figure(1)
plot.plot(x_seconds, s0,)

plot.xlabel('Experiment time (seconds)')
plot.ylabel('http req/s')
plot.axhline(y=max_requests, xmin=0.0, xmax=1.0, color='r', linestyle=':', label="max")
plot.legend(['requests', 'threshold'], loc='upper left')

plot.grid(True)
plot.title('bubblesort service http req/s')

plot.savefig("workload-rapid-growth-02.pdf",
    dpi=1000,
    bbox_inches='tight',
)
