def count_col_triang(points):
    total_points = len(points)
    

    def colours(points):
        colours = set()
        for i in points:
            colours.add(i[1])
        
        return len(colours), tuple(colours)
    

    total_colours = colours(points)[0]
    

    def colour_groups(points):
        colour_groups = {}
        for color_idx in range(colours(points)[0]):
            colour_group = []
            current_color_group = colours(points)[1][color_idx]
            for point in points:
                if point[1] == current_color_group:
                    colour_group.append(point[0])

            colour_groups[current_color_group] = colour_group
        
        return colour_groups


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
                        count_triang += len(others)
                        sub += 1
                        sub_idx = main_idx + sub
                        others = colour_group[sub_idx+1:]
                    main_idx += 1

            total_poss_triang += count_triang

        return total_poss_triang
            
    
    total_poss_triang_val = total_poss_triang(colour_groups(points))


    def max_group(colour_groups):
        max_col = {
            'colour': None,
            'count_points': 0,
            'points': []
        }
        for colour, colour_group in colour_groups.items():
            if max_col["count_points"] < len(colour_group):
                max_col["colour"] = colour
                max_col["count_points"] = len(colour_group)
                max_col["points"] = colour_group
        max_triang = total_poss_triang({max_col["colour"]: max_col["points"]})

        return [max_col["colour"], total_poss_triang({max_col["colour"]: max_col["points"]})]


    max_group = max_group(colour_groups(points))

    return [total_points, total_colours, total_poss_triang_val, max_group]


result = count_col_triang([[[3, -4], "blue"],  [[-7, -1], "red"], [[7, -6], "yellow"], [[2, 5], "yellow"],
 [[1, -5], "red"],   [[-1, 4], "red"],  [[1, 7], "red"],     [[-3, 5], "red"], 
 [[-3, -5], "blue"], [[4, 1], "blue"] ])

print(result)