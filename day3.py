import day3list

def get_manahattan_distance(point_1, point_2):
    lr_distance = abs(point_1[0] - point_2[0])
    ud_distance = abs(point_1[1] - point_2[1])
    return lr_distance + ud_distance

def get_coordinate_points(instructions):
    coordinate_list = [[0,0]]
    # import pdb; pdb.set_trace()
    for instruction in instructions:
        previous_point = coordinate_list[-1][:]
        coordinate_list.append(previous_point)
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == "U":
            coordinate_list[-1][1] += distance
            for increment in range(distance + 1):
                coordinate_list.append([previous_point[0], previous])
        elif direction == "D":
            coordinate_list[-1][1] -= distance
        elif direction == "R":
            coordinate_list[-1][0] += distance
        elif direction == "L":
            coordinate_list[-1][0] -= distance
    
    previous_coordinate = coordinate_list[0]
    ennumerated_coordinate_list = [previous_coordinate]
    for coordinate in coordinate_list[1:]:
        x_differ
        
def get_intersections(first_wire, second_wire):
    first_wire_coordinates = get_coordinate_points(first_wire)
    second_wire_coordinates = get_coordinate_points(second_wire)
    intersections = []
    for coordinate in first_wire_coordinates:
        if coordinate in second_wire_coordinates:
            intersections.append(coordinate)
    return intersections 



