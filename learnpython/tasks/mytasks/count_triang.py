def count_col_triang(points):
    """
    В эту функцию нужно передать массив точек вида
    [[[координаты], цвет], [[x, y], цвет], [[0, 3], 'red]]
    и эта функция вернет
    [колво_точек, колво_цветов, колво_треугольников, [цвет_с_наибольшим_колвом_треугольников, колво_треугольников_этого цвета]]
    """
    total_points = len(points)
    

    def get_colours(points):
        colours_with_dubl = [p[1] for p in points]
        colours = list(dict.fromkeys(colours_with_dubl))

        return len(colours), tuple(colours)
    
    colours = get_colours(points)
    total_colours = colours[0]
    

    def get_color_groups(points):
        color_groups = {}
        for color_idx in range(colours[0]):
            colour_group = []
            current_color_group = colours[1][color_idx]
            for point in points:
                if point[1] == current_color_group:
                    colour_group.append(point[0])

            color_groups[current_color_group] = colour_group
        
        return color_groups

    colour_groups = get_color_groups(points)

    def total_poss_triang(colour_groups):
        total_poss_triang = 0
        for colour, colour_group in colour_groups.items():
            if len(colour_group) < 3:
                continue
            elif len(colour_group) == 3:
                total_poss_triang += 1
                continue
            else:
                count_triang = 0
                main_idx = 0
                while main_idx != len(colour_group) - 2:
                    sub = 1
                    sub_idx = main_idx + sub
                    others = colour_group[sub_idx+1:]
                    while others != []:
                        count_line_points = 0
                        for other in others:
                            if colour_group[main_idx][0] == colour_group[sub_idx][0] == other[0]:
                                count_line_points += 1
                            elif colour_group[main_idx][1] == colour_group[sub_idx][1] == other[1]:
                                count_line_points += 1
                        count_triang += (len(others) - count_line_points)
                        sub += 1
                        sub_idx = main_idx + sub
                        others = colour_group[sub_idx+1:]
                    main_idx += 1

            total_poss_triang += count_triang

        return total_poss_triang
            
    
    total_poss_triang_val = total_poss_triang(colour_groups)


    def max_group(colour_groups):
        max_col = {
            'colours': [],
            'count_points': 0,
            'points': []
        }
        for colour, colour_group in colour_groups.items():
            if max_col["count_points"] < len(colour_group):
                max_col["colours"] = [colour]
                max_col["count_points"] = len(colour_group)
                max_col["points"] = colour_group
            
            if max_col["count_points"] == len(colour_group):
                max_col["colours"].append(colour)
                max_col["count_points"] = len(colour_group)
                max_col["points"] = colour_group
        
        colours = list(dict.fromkeys(max_col['colours']))
        max_col["colours"] = colours

        total_triang_max_col = total_poss_triang({max_col["colours"][0]: max_col["points"]})
        if  total_triang_max_col == 0:
            return []

        return [*max_col["colours"], total_triang_max_col]
 

    max_group = max_group(colour_groups)

    return [total_points, total_colours, total_poss_triang_val, max_group]


test1 =  [[[150, -176], 'purple'], [[-4, -125], 'sky_blue'], [[19, -61], 'purple'], [[-140, 198], 'silver'], [[-69, 13], 'blue'], [[146, 117], 'sky_blue'], [[13, 9], 'sky_blue'], [[109, 37], 'green'], [[143, -10], 'purple'], [[-24, 170], 'silver'], [[-96, 118], 'blue'], [[-66, -5], 'sky_blue'], [[-186, 180], 'purple'], [[106, 1], 'sky_blue'], [[-109, 162], 'purple'], [[-179, -70], 'blue'], [[-93, -179], 'green']]


print(count_col_triang(test1))