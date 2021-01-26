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

t = [1611594159, 1611594160, 1611594161, 1611594162, 1611594163, 1611594164, 1611594165, 1611594166, 1611594167, 1611594168, 1611594169, 1611594170, 1611594171, 1611594172, 1611594173, 1611594174, 1611594175, 1611594176, 1611594177, 1611594178, 1611594179, 1611594180, 1611594181, 1611594182, 1611594183, 1611594184, 1611594185, 1611594186, 1611594187, 1611594188, 1611594189, 1611594190, 1611594191, 1611594192, 1611594193, 1611594194, 1611594195, 1611594196, 1611594197, 1611594198, 1611594199, 1611594200, 1611594201, 1611594202, 1611594203, 1611594204, 1611594205, 1611594206, 1611594207, 1611594208, 1611594209, 1611594210, 1611594211, 1611594212, 1611594213, 1611594214, 1611594215, 1611594216, 1611594217, 1611594218, 1611594219, 1611594220, 1611594221, 1611594222, 1611594223, 1611594224, 1611594225, 1611594226, 1611594227, 1611594228, 1611594229, 1611594230, 1611594231, 1611594232, 1611594233, 1611594234, 1611594235, 1611594236, 1611594237, 1611594238, 1611594239, 1611594240, 1611594241, 1611594242, 1611594243, 1611594244, 1611594245, 1611594246, 1611594247, 1611594248, 1611594249, 1611594250, 1611594251, 1611594252, 1611594253, 1611594254, 1611594255, 1611594256, 1611594257, 1611594258, 1611594259, 1611594260, 1611594261, 1611594262, 1611594263, 1611594264, 1611594265, 1611594266, 1611594267, 1611594268, 1611594269, 1611594270, 1611594271, 1611594272, 1611594273, 1611594274, 1611594275, 1611594276, 1611594277, 1611594278, 1611594279, 1611594280, 1611594281, 1611594282, 1611594283, 1611594284, 1611594285, 1611594286, 1611594287, 1611594288, 1611594289, 1611594290, 1611594291, 1611594292, 1611594293, 1611594294, 1611594295, 1611594296, 1611594297, 1611594298, 1611594299, 1611594300, 1611594301, 1611594302, 1611594303, 1611594304, 1611594305, 1611594306, 1611594307, 1611594308, 1611594309, 1611594310, 1611594311, 1611594312, 1611594313, 1611594314, 1611594315, 1611594316, 1611594317, 1611594318, 1611594319, 1611594320, 1611594321, 1611594322, 1611594323, 1611594324, 1611594325, 1611594326, 1611594327, 1611594328, 1611594329, 1611594330, 1611594331, 1611594332, 1611594333, 1611594334, 1611594335, 1611594336, 1611594337, 1611594338, 1611594339, 1611594340, 1611594341, 1611594342, 1611594343, 1611594344, 1611594345, 1611594346, 1611594347, 1611594348, 1611594349, 1611594350, 1611594351, 1611594352, 1611594353, 1611594354, 1611594355, 1611594356, 1611594357, 1611594358, 1611594359, 1611594360, 1611594361, 1611594362, 1611594363, 1611594364, 1611594365, 1611594366, 1611594367, 1611594368, 1611594369, 1611594370, 1611594371, 1611594372, 1611594373, 1611594374, 1611594375, 1611594376, 1611594377, 1611594378, 1611594379, 1611594380, 1611594381, 1611594382, 1611594383, 1611594384, 1611594385, 1611594386, 1611594387, 1611594388, 1611594389, 1611594390, 1611594391, 1611594392, 1611594393, 1611594394, 1611594395, 1611594396, 1611594397, 1611594398, 1611594399, 1611594400, 1611594401, 1611594402, 1611594403, 1611594404, 1611594405, 1611594406, 1611594407, 1611594408, 1611594409, 1611594410, 1611594411, 1611594412, 1611594413, 1611594414, 1611594415, 1611594416, 1611594417, 1611594418, 1611594419, 1611594420, 1611594421, 1611594422, 1611594423, 1611594424, 1611594425, 1611594426, 1611594427, 1611594428, 1611594429, 1611594430, 1611594431, 1611594432, 1611594433, 1611594434, 1611594435, 1611594436, 1611594437, 1611594438, 1611594439, 1611594440, 1611594441, 1611594442, 1611594443, 1611594444, 1611594445, 1611594446, 1611594447, 1611594448, 1611594449, 1611594450, 1611594451, 1611594452, 1611594453, 1611594454, 1611594455, 1611594456, 1611594457, 1611594458, 1611594459, 1611594460, 1611594461, 1611594462, 1611594463, 1611594464, 1611594465, 1611594466, 1611594467, 1611594468, 1611594469, 1611594470, 1611594471, 1611594472, 1611594473, 1611594474, 1611594475, 1611594476, 1611594477, 1611594478, 1611594479, 1611594480, 1611594481, 1611594482, 1611594483, 1611594484, 1611594485, 1611594486, 1611594487, 1611594488, 1611594489, 1611594490, 1611594491, 1611594492, 1611594493, 1611594494, 1611594495, 1611594496, 1611594497, 1611594498, 1611594499, 1611594500, 1611594501, 1611594502, 1611594503, 1611594504, 1611594505, 1611594506, 1611594507, 1611594508, 1611594509, 1611594510, 1611594511, 1611594512, 1611594513, 1611594514, 1611594515, 1611594516, 1611594517, 1611594518, 1611594519, 1611594520, 1611594521, 1611594522, 1611594523, 1611594524, 1611594525, 1611594526, 1611594527, 1611594528, 1611594529, 1611594530, 1611594531, 1611594532, 1611594533, 1611594534, 1611594535, 1611594536, 1611594537, 1611594538, 1611594539, 1611594540, 1611594541, 1611594542, 1611594543, 1611594544, 1611594545, 1611594546, 1611594547, 1611594548, 1611594549, 1611594550, 1611594551, 1611594552, 1611594553, 1611594554, 1611594555, 1611594556, 1611594557, 1611594558, 1611594559, 1611594560, 1611594561, 1611594562, 1611594563, 1611594564, 1611594565, 1611594566, 1611594567, 1611594568, 1611594569, 1611594570, 1611594571, 1611594572, 1611594573, 1611594574, 1611594575, 1611594576, 1611594577, 1611594578, 1611594579, 1611594580, 1611594581, 1611594582, 1611594583, 1611594584, 1611594585, 1611594586, 1611594587, 1611594588, 1611594589, 1611594590, 1611594591, 1611594592, 1611594593, 1611594594, 1611594595, 1611594596, 1611594597, 1611594598, 1611594599, 1611594600, 1611594601, 1611594602, 1611594603, 1611594604, 1611594605, 1611594606, 1611594607, 1611594608, 1611594609, 1611594610, 1611594611, 1611594612, 1611594613, 1611594614, 1611594615, 1611594616, 1611594617, 1611594618, 1611594619, 1611594620, 1611594621, 1611594622, 1611594623, 1611594624, 1611594625, 1611594626, 1611594627, 1611594628, 1611594629, 1611594630, 1611594631, 1611594632, 1611594633, 1611594634, 1611594635, 1611594636, 1611594637, 1611594638, 1611594639, 1611594640, 1611594641, 1611594642, 1611594643, 1611594644, 1611594645, 1611594646, 1611594647, 1611594648, 1611594649, 1611594650, 1611594651, 1611594652, 1611594653, 1611594654, 1611594655, 1611594656, 1611594657, 1611594658, 1611594659, 1611594660, 1611594661, 1611594662, 1611594663, 1611594664, 1611594665, 1611594666, 1611594667, 1611594668, 1611594669, 1611594670, 1611594671, 1611594672, 1611594673, 1611594674, 1611594675, 1611594676, 1611594677, 1611594678, 1611594679, 1611594680, 1611594681, 1611594682, 1611594683, 1611594684, 1611594685, 1611594686, 1611594687, 1611594688, 1611594689, 1611594690, 1611594691, 1611594692, 1611594693, 1611594694, 1611594695, 1611594696, 1611594697, 1611594698, 1611594699, 1611594700, 1611594701, 1611594702, 1611594703, 1611594704, 1611594705, 1611594706, 1611594707, 1611594708, 1611594709, 1611594710, 1611594711, 1611594712, 1611594713, 1611594714, 1611594715, 1611594716, 1611594717, 1611594718, 1611594719, 1611594720, 1611594721, 1611594722, 1611594723, 1611594724, 1611594725, 1611594726, 1611594727, 1611594728, 1611594729, 1611594730, 1611594731, 1611594732, 1611594733, 1611594734, 1611594735, 1611594736, 1611594737, 1611594738, 1611594739, 1611594740, 1611594741, 1611594742, 1611594743, 1611594744, 1611594745, 1611594746, 1611594747, 1611594748, 1611594749, 1611594750, 1611594751, 1611594752, 1611594753, 1611594754, 1611594755, 1611594756, 1611594757, 1611594758, 1611594759]
s0 = [0.08266666666666665, 0.08266666666666665, 0.08266666666666665, 0.08266666666666665, 0.08266666666666665, 0.14933333333333335, 0.14933333333333335, 0.14933333333333335, 0.14933333333333335, 0.14933333333333335, 0.21600000000000003, 0.21600000000000003, 0.21600000000000003, 0.21600000000000003, 0.21600000000000003, 0.2826666666666666, 0.2826666666666666, 0.2826666666666666, 0.2826666666666666, 0.2826666666666666, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3306666666666666, 0.3306666666666666, 0.3306666666666666, 0.3306666666666666, 0.3306666666666666, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.3306666666666666, 0.3306666666666666, 0.3306666666666666, 0.3306666666666666, 0.3306666666666666, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.32266666666666666, 0.32266666666666666, 0.32266666666666666, 0.32266666666666666, 0.32266666666666666, 0.3173333333333333, 0.3173333333333333, 0.3173333333333333, 0.3173333333333333, 0.3173333333333333, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.33599999999999997, 0.376, 0.376, 0.376, 0.376, 0.376, 0.424, 0.424, 0.424, 0.424, 0.424, 0.504, 0.504, 0.504, 0.504, 0.504, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6906666666666668, 0.6906666666666668, 0.6906666666666668, 0.6906666666666668, 0.6906666666666668, 0.7786666666666666, 0.7786666666666666, 0.7786666666666666, 0.7786666666666666, 0.7786666666666666, 0.8426666666666666, 0.8426666666666666, 0.8426666666666666, 0.8426666666666666, 0.8426666666666666, 0.896, 0.896, 0.896, 0.896, 0.896, 0.9226666666666667, 0.9226666666666667, 0.9226666666666667, 0.9226666666666667, 0.9226666666666667, 0.9413333333333332, 0.9413333333333332, 0.9413333333333332, 0.9413333333333332, 0.9413333333333332, 0.9546666666666666, 0.9546666666666666, 0.9546666666666666, 0.9546666666666666, 0.9546666666666666, 1.0239999999999998, 1.0239999999999998, 1.0239999999999998, 1.0239999999999998, 1.0239999999999998, 1.1146666666666667, 1.1146666666666667, 1.1146666666666667, 1.1146666666666667, 1.1146666666666667, 1.2080000000000002, 1.2080000000000002, 1.2080000000000002, 1.2080000000000002, 1.2080000000000002, 1.3306666666666664, 1.3306666666666664, 1.3306666666666664, 1.3306666666666664, 1.3306666666666664, 1.4320000000000002, 1.4320000000000002, 1.4320000000000002, 1.4320000000000002, 1.4320000000000002, 1.5013333333333332, 1.5013333333333332, 1.5013333333333332, 1.5013333333333332, 1.5013333333333332, 1.5333333333333334, 1.5333333333333334, 1.5333333333333334, 1.5333333333333334, 1.5333333333333334, 1.597333333333333, 1.597333333333333, 1.597333333333333, 1.597333333333333, 1.597333333333333, 1.6320000000000001, 1.6320000000000001, 1.6320000000000001, 1.6320000000000001, 1.6320000000000001, 1.6346666666666665, 1.6346666666666665, 1.6346666666666665, 1.6346666666666665, 1.6346666666666665, 1.4746666666666668, 1.4746666666666668, 1.4746666666666668, 1.4746666666666668, 1.4746666666666668, 1.3253333333333333, 1.3253333333333333, 1.3253333333333333, 1.3253333333333333, 1.3253333333333333, 1.1413333333333335, 1.1413333333333335, 1.1413333333333335, 1.1413333333333335, 1.1413333333333335, 0.9519999999999998, 0.9519999999999998, 0.9519999999999998, 0.9519999999999998, 0.9519999999999998, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8079999999999999, 0.8079999999999999, 0.8079999999999999, 0.8079999999999999, 0.8079999999999999, 0.8293333333333333, 0.8293333333333333, 0.8293333333333333, 0.8293333333333333, 0.8293333333333333, 0.848, 0.848, 0.848, 0.848, 0.848, 0.92, 0.92, 0.92, 0.92, 0.92, 0.968, 0.968, 0.968, 0.968, 0.968, 1.0479999999999998, 1.0479999999999998, 1.0479999999999998, 1.0479999999999998, 1.0479999999999998, 1.1066666666666667, 1.1066666666666667, 1.1066666666666667, 1.1066666666666667, 1.1066666666666667, 1.1893333333333331, 1.1893333333333331, 1.1893333333333331, 1.1893333333333331, 1.1893333333333331, 1.1813333333333333, 1.1813333333333333, 1.1813333333333333, 1.1813333333333333, 1.1813333333333333, 1.2426666666666666, 1.2426666666666666, 1.2426666666666666, 1.2426666666666666, 1.2426666666666666, 1.2826666666666666, 1.2826666666666666, 1.2826666666666666, 1.2826666666666666, 1.2826666666666666, 1.3519999999999999, 1.3519999999999999, 1.3519999999999999, 1.3519999999999999, 1.3519999999999999, 1.3839999999999997, 1.3839999999999997, 1.3839999999999997, 1.3839999999999997, 1.3839999999999997, 1.488, 1.488, 1.488, 1.488, 1.488, 1.5413333333333334, 1.5413333333333334, 1.5413333333333334, 1.5413333333333334, 1.5413333333333334, 1.5866666666666667, 1.5866666666666667, 1.5866666666666667, 1.5866666666666667, 1.5866666666666667, 1.6506666666666665, 1.6506666666666665, 1.6506666666666665, 1.6506666666666665, 1.6506666666666665, 1.7173333333333332, 1.7173333333333332, 1.7173333333333332, 1.7173333333333332, 1.7173333333333332, 1.768, 1.768, 1.768, 1.768, 1.768, 1.837333333333333, 1.837333333333333, 1.837333333333333, 1.837333333333333, 1.837333333333333, 1.896, 1.896, 1.896, 1.896, 1.896, 1.9253333333333333, 1.9253333333333333, 1.9253333333333333, 1.9253333333333333, 1.9253333333333333, 1.9893333333333332, 1.9893333333333332, 1.9893333333333332, 1.9893333333333332, 1.9893333333333332, 2.0506666666666664, 2.0506666666666664, 2.0506666666666664, 2.0506666666666664, 2.0506666666666664, 2.037333333333333, 2.037333333333333, 2.037333333333333, 2.037333333333333, 2.037333333333333, 1.7786666666666668, 1.7786666666666668, 1.7786666666666668, 1.7786666666666668, 1.7786666666666668, 1.5066666666666666, 1.5066666666666666, 1.5066666666666666, 1.5066666666666666, 1.5066666666666666, 1.2186666666666666, 1.2186666666666666, 1.2186666666666666, 1.2186666666666666, 1.2186666666666666, 0.9093333333333332, 0.9093333333333332, 0.9093333333333332, 0.9093333333333332, 0.9093333333333332, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6693333333333332, 0.6693333333333332, 0.6693333333333332, 0.6693333333333332, 0.6693333333333332, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6693333333333332, 0.6693333333333332, 0.6693333333333332, 0.6693333333333332, 0.6693333333333332, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6613333333333332, 0.6613333333333332, 0.6613333333333332, 0.6613333333333332, 0.6613333333333332, 0.6906666666666668, 0.6906666666666668, 0.6906666666666668, 0.6906666666666668, 0.6906666666666668, 0.7279999999999999, 0.7279999999999999, 0.7279999999999999, 0.7279999999999999, 0.7279999999999999, 0.7786666666666666, 0.7786666666666666, 0.7786666666666666, 0.7786666666666666, 0.7786666666666666, 0.7893333333333333, 0.7893333333333333, 0.7893333333333333, 0.7893333333333333, 0.7893333333333333, 0.8879999999999999, 0.8879999999999999, 0.8879999999999999, 0.8879999999999999, 0.8879999999999999, 0.9066666666666666, 0.9066666666666666, 0.9066666666666666, 0.9066666666666666, 0.9066666666666666, 0.9706666666666667, 0.9706666666666667, 0.9706666666666667, 0.9706666666666667, 0.9706666666666667, 1.0213333333333332, 1.0213333333333332, 1.0213333333333332, 1.0213333333333332, 1.0213333333333332, 1.1146666666666667, 1.1146666666666667, 1.1146666666666667, 1.1146666666666667, 1.1146666666666667, 1.1626666666666665, 1.1626666666666665, 1.1626666666666665, 1.1626666666666665, 1.1626666666666665, 1.2639999999999998, 1.2639999999999998, 1.2639999999999998, 1.2639999999999998, 1.2639999999999998, 1.3413333333333335, 1.3413333333333335, 1.3413333333333335, 1.3413333333333335, 1.3413333333333335, 1.4639999999999997, 1.4639999999999997, 1.4639999999999997, 1.4639999999999997, 1.4639999999999997, 1.5786666666666667, 1.5786666666666667, 1.5786666666666667, 1.5786666666666667, 1.5786666666666667, 1.6693333333333331, 1.6693333333333331, 1.6693333333333331, 1.6693333333333331, 1.6693333333333331, 1.7786666666666668, 1.7786666666666668, 1.7786666666666668, 1.7786666666666668, 1.7786666666666668, 1.8506666666666665, 1.8506666666666665, 1.8506666666666665, 1.8506666666666665, 1.8506666666666665, 1.9173333333333331, 1.9173333333333331, 1.9173333333333331, 1.9173333333333331, 1.9173333333333331, 1.9813333333333336, 1.9813333333333336, 1.9813333333333336, 1.9813333333333336, 1.9813333333333336, 2.029333333333333, 2.029333333333333, 2.029333333333333, 2.029333333333333, 2.029333333333333, 2.0693333333333332, 2.0693333333333332, 2.0693333333333332, 2.0693333333333332, 2.0693333333333332, 2.1039999999999996, 2.1039999999999996, 2.1039999999999996, 2.1039999999999996, 2.1039999999999996, 2.0933333333333333, 2.0933333333333333, 2.0933333333333333, 2.0933333333333333, 2.0933333333333333, 2.112, 2.112, 2.112, 2.112, 2.112, 2.0826666666666664]
s1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
x_seconds = list(range(0,len(t)))

f=plot.figure(1)
plot.plot(x_seconds, s0, x_seconds, s1)

plot.legend(['desired', 'actual'], loc='upper left')
plot.xlabel('Experiment time (seconds)')
plot.ylabel('Computing demand (Instances)')

plot.grid(True)
plot.title('autoscaling behavior')

plot.savefig("workload-random-spikes-01.pdf",
    dpi=1000,
    bbox_inches='tight',
)
