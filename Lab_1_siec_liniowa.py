from random import randint


def activation_function(arg: float) -> int:
    if arg <= 0:
        return 0
    return 1


def point_evaluation(weights, point) -> float:
    return weights[0] * point[0] + weights[1] * point[1]


def main():
    training_points = [(-21, -64), (-62, 8), (-16, 76), (-5, -62), (95, -37), (18, -95), (-31, 48), (-3, 56), (1, 78),
                       (-10, -74), (58, -91), (-40, 39), (-72, 97), (-60, -28), (-80, 10), (24, 62), (71, 64),
                       (-17, -61),
                       (28, -1), (10, 65), (29, -48), (-57, 78), (-17, 76), (86, -93), (-65, -72), (-54, -49),
                       (-39, -32),
                       (-72, -87), (7, -50), (-22, -13), (44, 47), (80, -41), (14, -96), (-94, 70), (70, 29), (54, 59),
                       (36, -70), (29, 84), (21, 55), (91, -3), (-30, 23), (54, -29), (29, 16), (-93, 50), (15, -91),
                       (3, 85), (-72, 65), (-86, -100), (-89, 32), (-77, -67), (74, -17), (-79, -66), (67, -69),
                       (-95, -42),
                       (13, 13), (-78, 28), (87, 5), (73, 81), (-15, -26), (31, -25), (20, 80), (96, -6), (77, 71),
                       (-17, -88), (54, -11), (31, 86), (20, -90), (33, -93), (22, 69), (43, -51), (-67, -39),
                       (16, 100),
                       (-85, -85), (9, 0), (40, 84), (5, -56), (-82, -95), (-60, -49), (-95, 91), (49, 21), (97, 32),
                       (-92, -38), (-40, 77), (11, 54), (-32, 27), (21, 87), (14, 38), (-36, -41), (-12, -39),
                       (-41, -35),
                       (74, 47), (62, 66), (21, 27), (-8, -41), (-99, 58), (-98, 11), (-36, 54), (-9, 23), (-3, 19),
                       (-61, 24), (6, 47), (6, 39), (-92, 10), (-69, -43), (72, 66), (-67, 98), (23, 33), (69, -27),
                       (-69, -13), (-32, 46), (-74, -47), (-87, 3), (91, 38), (71, -1), (-1, -52), (47, -77), (31, 13),
                       (54, -31), (51, 61), (-45, 72), (71, -13), (-64, -49), (-71, -72), (23, -39), (-94, -21),
                       (-80, 4),
                       (-2, -60), (78, -57), (90, 26), (-96, -42), (10, -71), (-61, -24), (21, 63), (63, 49),
                       (-32, -71),
                       (-61, -31), (93, -79), (3, -69), (47, -84), (63, 33), (48, -11), (74, 25), (33, 36), (70, -80),
                       (-46, -9), (-10, 84), (67, -39), (-75, -90), (-88, 80), (-49, 47), (-70, -36), (-42, 78),
                       (-90, 88),
                       (73, -88), (93, -83), (17, -29), (9, 48), (97, 15), (-17, 45), (32, -29), (-4, 76), (57, 73),
                       (-99, 6), (7, 35), (78, -29), (-79, -87), (-48, 90), (-89, -97), (6, -18), (56, -14), (-37, -90),
                       (82, -26), (-37, 83), (-54, 68), (-69, 41), (-11, 46), (-6, -99), (-100, 81), (79, -44),
                       (7, -64),
                       (-46, 33), (26, 72), (93, 33), (43, 48), (19, -22), (49, 60), (-93, 2), (61, 3), (-43, -43),
                       (47, 15), (5, 34), (58, -90), (59, -69), (-70, -85), (-69, 16), (72, 14), (63, 44), (52, -68),
                       (4, -74), (-16, -55), (-93, 16), (91, -73), (82, -42), (87, -58), (-73, -69), (64, 58),
                       (-43, -92),
                       (-31, -64), (-27, -90), (-93, -83), (-10, 58), (-39, -5), (21, 7), (-73, -33), (-92, 12),
                       (-66, -89),
                       (22, -78), (-55, -43), (-18, -21), (-62, -19), (-76, 94), (-44, 75), (-42, 94), (-76, 83),
                       (49, -17),
                       (58, -84), (-22, -74), (69, -85), (73, 1), (-11, 59), (32, 63), (61, -99), (10, 32), (-1, 18),
                       (0, -15), (-10, 54), (68, -19), (-19, 13), (73, -77), (95, -57), (-26, -75), (83, 77), (-95, 26),
                       (-71, 19), (63, 19), (11, 92), (-62, 55), (-9, 4), (15, -97), (54, 40), (-12, -19), (9, -13),
                       (-76, -12), (-11, 59), (-67, 26), (72, 94), (-52, -44), (-96, -24), (-29, 20), (85, 85),
                       (-53, 21),
                       (-21, 80), (92, 4), (7, 33), (81, 49), (27, -9), (21, -73), (31, 85), (94, 46), (97, -54),
                       (0, -91),
                       (-63, 20), (-84, -16), (20, 70), (32, -94), (16, -75), (67, 56), (95, 63), (-78, 57), (-95, -86),
                       (-76, -50), (80, -97), (-77, -54), (-56, 71), (-98, 33), (33, 67), (-46, 92), (-91, -42),
                       (90, -44),
                       (70, 86), (59, 19), (16, -92), (-82, 63), (-20, -8), (99, 34), (-88, 11), (36, -99), (76, -53),
                       (-47, 83), (-96, 86), (-79, 87), (-71, 22), (10, 71), (-100, -92), (-30, 72), (37, 18),
                       (86, -15),
                       (-73, 99), (37, 46), (26, 18), (-75, -26), (-72, -16), (27, 74), (-3, 0), (100, 2), (12, 86),
                       (6, -98), (17, 42), (96, 56), (7, -70), (-32, 97), (9, 20), (-62, -49), (25, 39), (-79, -98),
                       (21, 27), (18, 6), (38, 25), (4, -1), (1, -68), (39, 32), (-15, 47), (-5, 88), (43, -28),
                       (-28, -15),
                       (67, 59), (31, 44), (30, 66), (-13, -40), (-78, -57), (-13, 96), (50, -83), (-23, -17),
                       (-73, -91),
                       (34, 88), (99, 84), (0, 69), (-16, 39), (-32, -28), (67, 55), (5, 96), (31, 77), (-74, 27),
                       (44, -61), (-39, -3), (45, 3), (8, 36), (-55, 12), (78, -6), (-82, -60), (-13, -19), (-73, -97),
                       (10, -23), (3, -19), (78, -87), (52, -76), (-95, 54), (-98, 13), (6, 10), (61, 4), (4, 63),
                       (-22, -30), (-3, 84), (58, -65), (70, 45), (-81, 17), (-97, 78), (45, 16), (-43, -78), (53, 66),
                       (-85, -54), (-64, -52), (75, -27), (50, -91), (19, 26), (-35, 6), (14, -81), (78, 9), (84, -82),
                       (48, 17), (-90, -6), (88, 52), (93, -56), (-98, 13), (13, -29), (13, 96), (14, 85), (34, 57),
                       (-56, 4), (56, 100), (-14, 0), (-51, -95), (63, 49), (38, 17), (85, -26), (78, -50), (29, -86),
                       (61, 32), (-31, 87), (73, -16), (-7, -64), (43, -51), (-46, -82), (-95, -1), (-89, -87),
                       (-51, 86),
                       (-7, 66), (-43, -45), (76, 18), (65, 88), (1, -45), (-47, -43), (-8, 49), (24, -41), (66, -18),
                       (-57, 51), (-83, 41), (-66, -28), (-68, 10), (-48, 87), (24, -97), (-98, -18), (-81, 57),
                       (-59, -64),
                       (-97, 44), (84, -55), (-74, -85), (-16, 55), (62, -31), (-71, -54), (-93, 80), (-74, -72),
                       (-73, 8),
                       (-67, 74), (33, 9), (44, 23), (43, 47), (28, -37), (-38, -23), (87, -9), (0, 6), (-15, -99),
                       (-66, 94), (-23, -35), (-45, 99), (43, 59), (75, -11), (-89, -5), (93, -71), (46, 50), (-60, 61),
                       (-32, -97), (-80, -30), (79, -27), (41, 74), (45, -20), (64, -51), (19, -62), (-62, 68),
                       (-38, -68),
                       (39, -2), (-85, -87), (-62, 69), (26, -1), (-94, 44), (69, -10), (-14, 7), (-16, -59), (-5, -47),
                       (-49, 76), (26, 71), (62, -97), (-98, -80), (-71, 14), (-36, -86), (-56, 91), (-82, -73),
                       (-31, -79),
                       (-28, -98), (82, 31), (-1, 62), (-32, 22), (-34, 37), (4, -37), (91, -85), (-27, -98), (19, 34),
                       (28, 14), (2, -29), (29, -18), (-51, -2), (-100, -65), (-15, -96), (56, 35), (-53, 87), (36, 52),
                       (-13, 12), (-23, 20), (27, -82), (64, 50), (-27, 7), (-48, 40), (-57, -98), (-23, -42),
                       (-45, -79),
                       (-34, 86), (21, 95), (1, -45), (91, -77), (-50, -83), (-99, 92), (64, -67), (-1, 97), (0, -44),
                       (43, -97), (61, 34), (27, 14), (90, 75), (-100, -32), (45, 12), (-91, -47), (11, 18), (-21, -2),
                       (-11, 7), (52, 69), (-64, 91), (-11, 90), (39, 59), (63, 56), (-73, 86), (18, 42), (-28, 55),
                       (-26, -10), (42, 7), (-71, -23), (-25, -6), (61, 36), (-5, 35), (79, -53), (-35, 77), (-47, 52),
                       (-34, -13), (-58, -33), (-84, -91), (17, 62), (37, -16), (-44, -95), (-21, -45), (-88, -65),
                       (-67, -47), (48, -45), (-55, 4), (-6, -11), (61, 8), (-64, -81), (-50, -42), (50, 58), (46, 11),
                       (72, -26), (29, -50), (-88, 10), (11, 39), (-5, 0), (-93, 82), (46, -71), (47, -91), (-76, -2),
                       (76, 77), (61, 52), (74, 66), (-58, -50), (59, -61), (-3, -49), (44, 100), (-3, -70), (5, 98),
                       (-89, -67), (23, -6), (50, -1), (-42, 9), (32, 49), (41, -96), (-71, 51), (-47, 70), (-64, -20),
                       (67, -19), (-35, 69), (-76, 46), (-20, -1), (100, -2), (49, -80), (-89, 24), (-30, 76), (6, -99),
                       (71, -82), (50, -65), (-60, -30), (-97, 68), (85, 60), (79, -74), (8, -97), (90, 18), (11, -84),
                       (41, 71), (-59, 12), (-87, -6), (49, 44), (17, -83), (27, -90), (95, 32), (-14, 53), (-85, 59),
                       (-87, 22), (-39, 26), (-99, -93), (75, 87), (50, 100), (29, 14), (-62, 47), (-99, -69), (15, 35),
                       (-31, -51), (-21, 100), (-34, 17), (-23, -85), (54, -41), (-80, 58), (52, -62), (-78, -81),
                       (-34, 3),
                       (16, 2), (-28, 87), (13, 8), (-100, -73), (33, 42), (-13, 11), (-91, 23), (73, 75), (26, -59),
                       (41, -48), (-97, 64), (50, 94), (90, -17), (-84, 96), (63, -16), (-98, 12), (-59, 68), (53, -50),
                       (-11, -41), (-46, 64), (62, -29), (71, -31), (-57, -98), (-66, -96), (86, -20), (54, 18),
                       (-14, 70),
                       (-46, 33), (-30, 6), (-93, 71), (68, -47), (-9, 17), (7, 50), (-96, -11), (-56, -14), (-37, 91),
                       (-50, 2), (69, -59), (-5, -11), (-18, 74), (19, -4), (93, -83), (-81, -78), (56, -39),
                       (-39, -17),
                       (74, -27), (-71, -58), (-10, -81), (-62, -30), (49, 40), (-46, -7), (-85, 7), (-99, -47),
                       (-4, -75),
                       (53, -55), (5, 25), (93, 73), (-34, 57), (82, 91), (-84, -84), (-91, -80), (43, 30), (-5, -91),
                       (-36, 89), (60, 93), (4, 94), (74, 69), (-77, -80), (-60, -9), (-94, -45), (5, 43), (3, 67),
                       (-38, 93), (-26, 28), (-51, -87), (69, 59), (15, 100), (32, -84), (91, -9), (-81, -65), (14, 51),
                       (13, -64), (57, 80), (-52, -4), (-40, -79), (30, -2), (-9, -70), (-51, 63), (44, -79),
                       (-51, -22),
                       (-12, 96), (-30, -2), (-50, 81), (42, 56), (-92, -31), (-71, -18), (54, -70), (-15, 93),
                       (6, -69),
                       (-100, 89), (30, 24), (-96, 60), (37, 24), (60, 100), (83, -60), (-99, 66), (81, 22), (-6, 62),
                       (50, 23), (100, -47), (83, 43), (-40, 41), (68, -79), (-87, -35), (32, -22), (-79, -40),
                       (76, 72),
                       (-54, 15), (73, 38), (23, 8), (-40, -24), (-2, 61), (93, -7), (-68, -4), (-10, -58), (97, 87),
                       (46, -14), (-17, -37), (-60, -23), (100, -3), (88, -81), (29, 38), (98, -90), (-30, 48),
                       (19, 56),
                       (0, -99), (-65, 74), (-19, 16), (75, -30), (-64, 81), (33, -20), (-29, -18), (24, 54), (-29, -1),
                       (-25, 55), (93, -3), (-20, -49), (49, -70), (-6, -13), (-66, -20), (-19, -48), (93, -47),
                       (91, 89),
                       (-82, 61), (-58, 20), (-12, 77), (-67, 43), (6, 68), (55, 32), (-30, 70), (-96, 1), (39, 10),
                       (-76, 42), (35, -83), (-54, -79), (-57, -23), (74, -73), (52, 58), (78, 35), (-83, 32), (87, 51),
                       (9, -2), (-48, -63), (-62, -41), (-69, -1), (-60, 6), (33, -18), (98, -6), (-84, 45), (-33, 14),
                       (80, -18), (91, -17), (-20, -35), (-68, 70), (54, 76), (8, 11), (-7, -43), (-34, 10), (-80, -61),
                       (-96, 84), (31, -15), (34, 75), (-68, 7), (-21, -5), (-87, -92), (-98, 65), (51, 96), (32, -73),
                       (-90, 47), (13, 13), (-2, 73), (35, -17), (50, 78), (-66, 91), (32, -35), (24, 75), (-15, -45),
                       (1, 63), (-61, -72), (62, 83), (7, -99), (77, -75), (-72, -84), (46, -41), (-92, 28), (-54, 100),
                       (1, 57), (-8, 11), (-83, -20), (-19, 69), (-58, 49), (-28, 20), (-70, 7), (-23, 40), (30, -80),
                       (-1, -100), (81, 10), (-31, 29), (15, 30), (-80, 28), (9, -56), (-24, -90), (-54, -96),
                       (97, -33),
                       (88, 82), (54, 65), (-50, -25), (26, -31), (-34, -40), (31, -4), (96, -81), (92, -17), (2, 87),
                       (-50, 22), (6, 2), (-38, -36), (6, -50), (-93, 84), (-88, 39), (-37, 73), (-79, 57), (85, -92),
                       (-61, -3), (74, -75), (26, 70), (33, 38), (-33, 66), (-82, 83), (-8, 89), (1, 52), (87, -56),
                       (25, 72), (-45, 70), (-100, -43), (-55, -81), (87, -49), (65, 74), (4, -2), (36, -11), (-9, -89),
                       (67, 27), (69, 94), (-46, -15), (52, -85), (-9, -55), (40, -77), (-11, 10), (-1, -23), (90, -89),
                       (24, 13), (18, -5), (53, -34), (-26, -18), (68, -9), (29, -31), (36, -21), (-79, -21), (80, -76),
                       (25, 76), (93, 49), (-47, 15), (5, -35), (-53, 76), (-79, -88), (82, -25), (-2, 71), (-4, -53),
                       (9, -26), (-82, -40), (-20, -100), (61, -35), (65, 61), (37, 10), (50, -8), (-2, -68),
                       (-61, -52),
                       (-12, -54), (21, 80), (-71, -33), (-78, -79), (-92, -88), (-79, 93), (-22, -91), (-55, -96),
                       (64, 90), (48, -1), (23, -1), (-67, 84), (-51, -33), (-42, -96), (73, -52), (-89, -52),
                       (-17, 14),
                       (16, 89), (-100, -52), (79, 92), (-83, -2), (81, -65), (34, -32), (-2, -83), (-24, 22), (51, 94),
                       (-18, 75), (-94, 3), (51, -70), (-71, 27), (45, -95), (71, 95), (-25, 77), (53, 62), (-58, 18),
                       (94, -71), (68, 27), (80, -30), (38, 4), (66, -89), (-76, 66), (10, 26), (-36, -73), (-81, -47),
                       (-21, -58), (-89, 63), (-72, -85), (13, -8), (-71, 100), (-83, 58), (-35, 69), (-4, -81),
                       (75, -11),
                       (-40, 78)]
    answers = [0] * 1000
    for i in range(1000):
        if training_points[i][0] + 2 > training_points[i][1]:
            answers[i] = 1
    eta = 0.2
    weights = [0.0, 0.0]
    index = 0
    for x, y in training_points:
        while activation_function(point_evaluation(weights, (x, y))) != answers[index]:
            weights[0] = weights[0] + (
                        answers[index] - activation_function(point_evaluation(weights, (x, y)))) * eta * x
            weights[1] = weights[1] + (
                        answers[index] - activation_function(point_evaluation(weights, (x, y)))) * eta * y
        index += 1
    print(weights)


def test:
    #TODO: napisac testy do modelu
if __name__ == "__main__":
    main()
