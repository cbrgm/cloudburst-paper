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

t = [1611592699, 1611592700, 1611592701, 1611592702, 1611592703, 1611592704, 1611592705, 1611592706, 1611592707, 1611592708, 1611592709, 1611592710, 1611592711, 1611592712, 1611592713, 1611592714, 1611592715, 1611592716, 1611592717, 1611592718, 1611592719, 1611592720, 1611592721, 1611592722, 1611592723, 1611592724, 1611592725, 1611592726, 1611592727, 1611592728, 1611592729, 1611592730, 1611592731, 1611592732, 1611592733, 1611592734, 1611592735, 1611592736, 1611592737, 1611592738, 1611592739, 1611592740, 1611592741, 1611592742, 1611592743, 1611592744, 1611592745, 1611592746, 1611592747, 1611592748, 1611592749, 1611592750, 1611592751, 1611592752, 1611592753, 1611592754, 1611592755, 1611592756, 1611592757, 1611592758, 1611592759, 1611592760, 1611592761, 1611592762, 1611592763, 1611592764, 1611592765, 1611592766, 1611592767, 1611592768, 1611592769, 1611592770, 1611592771, 1611592772, 1611592773, 1611592774, 1611592775, 1611592776, 1611592777, 1611592778, 1611592779, 1611592780, 1611592781, 1611592782, 1611592783, 1611592784, 1611592785, 1611592786, 1611592787, 1611592788, 1611592789, 1611592790, 1611592791, 1611592792, 1611592793, 1611592794, 1611592795, 1611592796, 1611592797, 1611592798, 1611592799, 1611592800, 1611592801, 1611592802, 1611592803, 1611592804, 1611592805, 1611592806, 1611592807, 1611592808, 1611592809, 1611592810, 1611592811, 1611592812, 1611592813, 1611592814, 1611592815, 1611592816, 1611592817, 1611592818, 1611592819, 1611592820, 1611592821, 1611592822, 1611592823, 1611592824, 1611592825, 1611592826, 1611592827, 1611592828, 1611592829, 1611592830, 1611592831, 1611592832, 1611592833, 1611592834, 1611592835, 1611592836, 1611592837, 1611592838, 1611592839, 1611592840, 1611592841, 1611592842, 1611592843, 1611592844, 1611592845, 1611592846, 1611592847, 1611592848, 1611592849, 1611592850, 1611592851, 1611592852, 1611592853, 1611592854, 1611592855, 1611592856, 1611592857, 1611592858, 1611592859, 1611592860, 1611592861, 1611592862, 1611592863, 1611592864, 1611592865, 1611592866, 1611592867, 1611592868, 1611592869, 1611592870, 1611592871, 1611592872, 1611592873, 1611592874, 1611592875, 1611592876, 1611592877, 1611592878, 1611592879, 1611592880, 1611592881, 1611592882, 1611592883, 1611592884, 1611592885, 1611592886, 1611592887, 1611592888, 1611592889, 1611592890, 1611592891, 1611592892, 1611592893, 1611592894, 1611592895, 1611592896, 1611592897, 1611592898, 1611592899, 1611592900, 1611592901, 1611592902, 1611592903, 1611592904, 1611592905, 1611592906, 1611592907, 1611592908, 1611592909, 1611592910, 1611592911, 1611592912, 1611592913, 1611592914, 1611592915, 1611592916, 1611592917, 1611592918, 1611592919, 1611592920, 1611592921, 1611592922, 1611592923, 1611592924, 1611592925, 1611592926, 1611592927, 1611592928, 1611592929, 1611592930, 1611592931, 1611592932, 1611592933, 1611592934, 1611592935, 1611592936, 1611592937, 1611592938, 1611592939, 1611592940, 1611592941, 1611592942, 1611592943, 1611592944, 1611592945, 1611592946, 1611592947, 1611592948, 1611592949, 1611592950, 1611592951, 1611592952, 1611592953, 1611592954, 1611592955, 1611592956, 1611592957, 1611592958, 1611592959, 1611592960, 1611592961, 1611592962, 1611592963, 1611592964, 1611592965, 1611592966, 1611592967, 1611592968, 1611592969, 1611592970, 1611592971, 1611592972, 1611592973, 1611592974, 1611592975, 1611592976, 1611592977, 1611592978, 1611592979, 1611592980, 1611592981, 1611592982, 1611592983, 1611592984, 1611592985, 1611592986, 1611592987, 1611592988, 1611592989, 1611592990, 1611592991, 1611592992, 1611592993, 1611592994, 1611592995, 1611592996, 1611592997, 1611592998, 1611592999, 1611593000, 1611593001, 1611593002, 1611593003, 1611593004, 1611593005, 1611593006, 1611593007, 1611593008, 1611593009, 1611593010, 1611593011, 1611593012, 1611593013, 1611593014, 1611593015, 1611593016, 1611593017, 1611593018, 1611593019, 1611593020, 1611593021, 1611593022, 1611593023, 1611593024, 1611593025, 1611593026, 1611593027, 1611593028, 1611593029, 1611593030, 1611593031, 1611593032, 1611593033, 1611593034, 1611593035, 1611593036, 1611593037, 1611593038, 1611593039, 1611593040, 1611593041, 1611593042, 1611593043, 1611593044, 1611593045, 1611593046, 1611593047, 1611593048, 1611593049, 1611593050, 1611593051, 1611593052, 1611593053, 1611593054, 1611593055, 1611593056, 1611593057, 1611593058, 1611593059, 1611593060, 1611593061, 1611593062, 1611593063, 1611593064, 1611593065, 1611593066, 1611593067, 1611593068, 1611593069, 1611593070, 1611593071, 1611593072, 1611593073, 1611593074, 1611593075, 1611593076, 1611593077, 1611593078, 1611593079, 1611593080, 1611593081, 1611593082, 1611593083, 1611593084, 1611593085, 1611593086, 1611593087, 1611593088, 1611593089, 1611593090, 1611593091, 1611593092, 1611593093, 1611593094, 1611593095, 1611593096, 1611593097, 1611593098, 1611593099, 1611593100, 1611593101, 1611593102, 1611593103, 1611593104, 1611593105, 1611593106, 1611593107, 1611593108, 1611593109, 1611593110, 1611593111, 1611593112, 1611593113, 1611593114, 1611593115, 1611593116, 1611593117, 1611593118, 1611593119, 1611593120, 1611593121, 1611593122, 1611593123, 1611593124, 1611593125, 1611593126, 1611593127, 1611593128, 1611593129, 1611593130, 1611593131, 1611593132, 1611593133, 1611593134, 1611593135, 1611593136, 1611593137, 1611593138, 1611593139, 1611593140, 1611593141, 1611593142, 1611593143, 1611593144, 1611593145, 1611593146, 1611593147, 1611593148, 1611593149, 1611593150, 1611593151, 1611593152, 1611593153, 1611593154, 1611593155, 1611593156, 1611593157, 1611593158, 1611593159, 1611593160, 1611593161, 1611593162, 1611593163, 1611593164, 1611593165, 1611593166, 1611593167, 1611593168, 1611593169, 1611593170, 1611593171, 1611593172, 1611593173, 1611593174, 1611593175, 1611593176, 1611593177, 1611593178, 1611593179, 1611593180, 1611593181, 1611593182, 1611593183, 1611593184, 1611593185, 1611593186, 1611593187, 1611593188, 1611593189, 1611593190, 1611593191, 1611593192, 1611593193, 1611593194, 1611593195, 1611593196, 1611593197, 1611593198, 1611593199, 1611593200, 1611593201, 1611593202, 1611593203, 1611593204, 1611593205, 1611593206, 1611593207, 1611593208, 1611593209, 1611593210, 1611593211, 1611593212, 1611593213, 1611593214, 1611593215, 1611593216, 1611593217, 1611593218, 1611593219, 1611593220, 1611593221, 1611593222, 1611593223, 1611593224, 1611593225, 1611593226, 1611593227, 1611593228, 1611593229, 1611593230, 1611593231, 1611593232, 1611593233, 1611593234, 1611593235, 1611593236, 1611593237, 1611593238, 1611593239, 1611593240, 1611593241, 1611593242, 1611593243, 1611593244, 1611593245, 1611593246, 1611593247, 1611593248, 1611593249, 1611593250, 1611593251, 1611593252, 1611593253, 1611593254, 1611593255, 1611593256, 1611593257, 1611593258, 1611593259, 1611593260, 1611593261, 1611593262, 1611593263, 1611593264, 1611593265, 1611593266, 1611593267, 1611593268, 1611593269, 1611593270, 1611593271, 1611593272, 1611593273, 1611593274, 1611593275, 1611593276, 1611593277, 1611593278, 1611593279, 1611593280, 1611593281, 1611593282, 1611593283, 1611593284, 1611593285, 1611593286, 1611593287, 1611593288, 1611593289, 1611593290, 1611593291, 1611593292, 1611593293, 1611593294, 1611593295, 1611593296]
s0 = [0.018117777777777778, 0.02034, 0.022562222222222223, 0.024784444444444442, 0.02700666666666666, 0.029228888888888895, 0.03145111111111111, 0.03367333333333333, 0.035895555555555556, 0.03811777777777778, 0.03809511111111111, 0.04016918518518518, 0.04224325925925926, 0.04431733333333334, 0.046391407407407416, 0.049211888888888895, 0.051323, 0.05343411111111112, 0.05554522222222222, 0.05765633333333334, 0.06032639999999998, 0.062459733333333316, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.7466666666666667, 0.7466666666666667, 0.7466666666666667, 0.7466666666666667, 0.7466666666666667, 1.1237073777777777, 1.1624629333333332, 1.1626666666666665, 1.1626666666666665, 1.1626666666666665, 1.5014933333333333, 1.5548266666666668, 1.6, 1.6, 1.6, 1.9396464888888887, 2.0099576, 2.080268711111111, 2.1093333333333333, 2.1093333333333333, 2.3573333333333335, 2.3573333333333335, 2.3573333333333335, 2.3573333333333335, 2.3573333333333335, 2.474666666666667, 2.474666666666667, 2.474666666666667, 2.474666666666667, 2.474666666666667, 2.5813333333333333, 2.5813333333333333, 2.5813333333333333, 2.5813333333333333, 2.5813333333333333, 2.608, 2.608, 2.608, 2.608, 2.608, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.648, 2.648, 2.648, 2.648, 2.648, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.717333333333333, 2.717333333333333, 2.717333333333333, 2.717333333333333, 2.717333333333333, 2.7119999999999997, 2.7119999999999997, 2.7119999999999997, 2.7119999999999997, 2.7119999999999997, 2.722666666666667, 2.722666666666667, 2.722666666666667, 2.722666666666667, 2.722666666666667, 2.765333333333333, 2.765333333333333, 2.765333333333333, 2.765333333333333, 2.765333333333333, 2.752, 2.752, 2.752, 2.752, 2.752, 2.7893333333333334, 2.7893333333333334, 2.7893333333333334, 2.7893333333333334, 2.7893333333333334, 2.784, 2.784, 2.784, 2.784, 2.784, 2.7813333333333334, 2.7813333333333334, 2.7813333333333334, 2.7813333333333334, 2.7813333333333334, 2.7813333333333334, 2.7813333333333334, 2.7813333333333334, 2.7813333333333334, 2.7813333333333334, 2.752, 2.752, 2.752, 2.752, 2.752, 2.722666666666667, 2.722666666666667, 2.722666666666667, 2.722666666666667, 2.722666666666667, 2.5519999999999996, 2.5519999999999996, 2.5519999999999996, 2.5519999999999996, 2.5519999999999996, 2.026666666666667, 2.026666666666667, 2.026666666666667, 2.026666666666667, 2.026666666666667, 1.4613333333333334, 1.4613333333333334, 1.4613333333333334, 1.4613333333333334, 1.4613333333333334, 0.96, 0.96, 0.96, 0.96, 0.96, 0.44, 0.44, 0.44, 0.44, 0.44, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.14933333333333335, 0.14933333333333335, 0.14933333333333335, 0.14933333333333335, 0.14933333333333335, 0.6293333333333333, 0.6293333333333333, 0.6293333333333333, 0.6293333333333333, 0.6293333333333333, 1.1413333333333335, 1.1413333333333335, 1.1413333333333335, 1.1413333333333335, 1.1413333333333335, 1.656, 1.656, 1.656, 1.656, 1.656, 2.2453333333333334, 2.2453333333333334, 2.2453333333333334, 2.2453333333333334, 2.2453333333333334, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6986666666666665, 2.6986666666666665, 2.6986666666666665, 2.6986666666666665, 2.6986666666666665, 2.730666666666667, 2.730666666666667, 2.730666666666667, 2.730666666666667, 2.730666666666667, 2.7333333333333334, 2.7333333333333334, 2.7333333333333334, 2.7333333333333334, 2.7333333333333334, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.696, 2.696, 2.696, 2.696, 2.696, 2.6879999999999997, 2.6879999999999997, 2.6879999999999997, 2.6879999999999997, 2.6879999999999997, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.664, 2.664, 2.664, 2.664, 2.664, 2.664, 2.664, 2.664, 2.664, 2.664, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6533333333333333, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.661333333333333, 2.68, 2.68, 2.68, 2.68, 2.68, 2.6719999999999997, 2.6719999999999997, 2.6719999999999997, 2.6719999999999997, 2.6719999999999997, 2.6426666666666665, 2.6426666666666665, 2.6426666666666665, 2.6426666666666665, 2.6426666666666665, 2.5733333333333333, 2.5733333333333333, 2.5733333333333333, 2.5733333333333333, 2.5733333333333333, 2.0533333333333332, 2.0533333333333332, 2.0533333333333332, 2.0533333333333332, 2.0533333333333332, 1.528, 1.528, 1.528, 1.528, 1.528, 1.0053333333333334, 1.0053333333333334, 1.0053333333333334, 1.0053333333333334, 1.0053333333333334, 0.5119999999999999, 0.5119999999999999, 0.5119999999999999, 0.5119999999999999, 0.5119999999999999, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06399999999999999, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.06933333333333333, 0.08800000000000001, 0.08800000000000001, 0.08800000000000001, 0.08800000000000001, 0.08800000000000001, 0.5466666666666666, 0.5466666666666666, 0.5466666666666666, 0.5466666666666666, 0.5466666666666666, 1.0213333333333332, 1.0213333333333332, 1.0213333333333332, 1.0213333333333332, 1.0213333333333332, 1.5064256385644965, 1.5064256385644965, 1.5064256385644965, 1.5064256385644965, 1.5064256385644965, 2.008, 2.008, 2.008, 2.008, 2.008, 2.488, 2.488, 2.488, 2.488, 2.488, 2.5493333333333337, 2.5493333333333337, 2.5493333333333337, 2.5493333333333337, 2.5493333333333337, 2.5919999999999996, 2.5919999999999996, 2.5919999999999996, 2.5919999999999996, 2.5919999999999996, 2.635088280791593, 2.635088280791593, 2.635088280791593, 2.635088280791593, 2.635088280791593, 2.717333333333333, 2.717333333333333, 2.717333333333333, 2.717333333333333, 2.717333333333333, 2.832, 2.832, 2.832, 2.832, 2.832, 2.8426666666666667, 2.8426666666666667, 2.8426666666666667, 2.8426666666666667, 2.8426666666666667, 2.8533333333333335, 2.8533333333333335, 2.8533333333333335, 2.8533333333333335, 2.8533333333333335, 2.845333333333333, 2.845333333333333, 2.845333333333333, 2.845333333333333, 2.845333333333333, 2.7706666666666666, 2.7706666666666666, 2.7706666666666666, 2.7706666666666666, 2.7706666666666666, 2.685333333333333, 2.685333333333333, 2.685333333333333, 2.685333333333333, 2.685333333333333, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.6693333333333333, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6666666666666665, 2.6586666666666665, 2.6586666666666665, 2.6586666666666665, 2.6586666666666665, 2.6586666666666665, 2.6373333333333333, 2.6373333333333333, 2.6373333333333333, 2.6373333333333333, 2.6373333333333333, 2.605333333333333, 2.605333333333333, 2.605333333333333, 2.605333333333333, 2.605333333333333, 2.52, 2.52, 2.52, 2.52, 2.52, 2.477333333333333, 2.477333333333333, 2.477333333333333, 2.477333333333333, 2.477333333333333, 2.48, 2.48, 2.48, 2.48, 2.48, 2.469333333333333, 2.469333333333333, 2.469333333333333]
s1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
x_seconds = list(range(0,len(t)))

f=plot.figure(1)
plot.plot(x_seconds, s0, x_seconds, s1)

plot.legend(['desired', 'actual'], loc='upper left')
plot.xlabel('Experiment time (seconds)')
plot.ylabel('Computing demand (Instances)')

plot.grid(True)
plot.title('autoscaling behavior')

plot.savefig("workload-cold-to-spike-01.pdf",
    dpi=1000,
    bbox_inches='tight',
)
