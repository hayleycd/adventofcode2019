import day3list

def get_manahattan_distance(point_1, point_2):
    lr_distance = abs(point_1[0] - point_2[0])
    ud_distance = abs(point_1[1] - point_2[1])
    return lr_distance + ud_distance

def get_coordinate_points(instructions):
    coordinate_list = [(0,0)]
    for instruction in instructions:
        previous_point = coordinate_list[-1][:]
        direction = instruction[0]
        distance = int(instruction[1:])
        for increment in range(1, distance + 1):
            if direction == "U":
                coordinate_list.append((previous_point[0], previous_point[1] + increment))
            elif direction == "D":
                coordinate_list.append((previous_point[0], previous_point[1] - increment))
            elif direction == "R":
                coordinate_list.append((previous_point[0] + increment, previous_point[1]))
            elif direction == "L":
                coordinate_list.append((previous_point[0] - increment , previous_point[1]))
    return coordinate_list
        
def get_intersections(first_wire, second_wire):
    first_wire_coordinates = get_coordinate_points(first_wire)
    second_wire_coordinates = get_coordinate_points(second_wire)
    return set(first_wire_coordinates) - (set(first_wire_coordinates) - set(second_wire_coordinates)) 

def determine_min_manhattan_distance(coordinate_list):
    distances = []
    for coordinate in coordinate_list:
        if coordinate != (0,0):
            distances.append(get_manahattan_distance(coordinate, [0,0]))
    return min(distances)

def determine_steps(coordinate_list, intersection):
    for index in range(len(coordinate_list) + 1):
        if coordinate_list[index] == intersection:
            return index

def get_total_steps_for_both_wires(coordinate_list_1, coordinate_list_2, intersection):
    wire_1_steps = determine_steps(coordinate_list_1, intersection)
    wire_2_steps = determine_steps(coordinate_list_2, intersection)
    return wire_1_steps + wire_2_steps

def determine_minimum_steps(coordinate_list_1, coordinate_list_2, intersections):
    steps = []
    for intersection in intersections:
        total_steps = get_total_steps_for_both_wires(coordinate_list_1, coordinate_list_2, intersection)
        if total_steps > 0:
            steps.append(total_steps)
    return steps

coordinate_list_1 = get_coordinate_points(day3list.first_wire.split(","))
coordinate_list_2 = get_coordinate_points(day3list.second_wire.split(","))
intersections = get_intersections(day3list.first_wire.split(","), day3list.second_wire.split(","))
minimum = determine_min_manhattan_distance(intersections)
minimum_steps = min(determine_minimum_steps(coordinate_list_1, coordinate_list_2, intersections))


