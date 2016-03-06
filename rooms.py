def get_building(quadrangle, room_number):
    """Finds and returns the building that a room is in for a specific quadrangle, or None"""

    def in_ranges(ranges):
        """Determines if a room is in a list of ranges (each specified by tuples)"""
        for first, last in ranges:
            if first <= room_number <= last:
                return True
        return False

    if quadrangle == "porter":
        if in_ranges([(203, 208), (303, 311), (405, 417)]):
            return 1
        elif in_ranges([(209, 215), (312, 321), (418, 431)]):
            return 2
        elif in_ranges([(216, 219), (322, 326), (432, 440)]):
            return 3
        elif in_ranges([(551, 554), (641, 646), (741, 744), (841, 846), (941, 947), (1041, 1048)]):
            return 4
        elif in_ranges([(341, 346), (441, 447), (540, 550)]):
            return 5
        elif in_ranges([(361, 370), (461, 473), (561, 581)]):
            return 6
        elif in_ranges([(301, 302), (401, 404), (501, 506), (601, 604), (701, 706), (801, 807)]):
            return 7
    elif quadrangle == "red_jacket":
        if in_ranges([(201, 210), (301, 313), (401, 421)]):
            return 1
        elif in_ranges([(211, 219), (314, 325), (422, 439)]):
            return 2
        elif in_ranges([(326, 333), (440, 450), (540, 559)]):
            return 3
        elif in_ranges([(585, 588), (676, 681), (776, 779), (876, 881), (976, 982), (1076, 1083)]):
            return 4
        elif in_ranges([(361, 372), (461, 475), (561, 584)]):
            return 5
        elif in_ranges([(191, 192), (391, 394), (491, 496), (591, 594), (691, 696), (791, 797)]):
            return 6
    # elif quadrangle == "richmond":
    #     pass
    # elif quadrangle == "spaulding":
    #     pass
    # elif quadrangle == "wilkeson":
    #     pass
    return None
