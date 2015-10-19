NUMBER_OF_CHAIRS = 10

def find_chair_as_far_from_others():
    pass

def find_closest_empty_chair(empty_chairs_distance_dict):
    closest_empty_chair = -1
    for key in empty_chairs_distance_dict:
        print key, empty_chairs_distance_dict[key] #print key, value
        if closest_empty_chair == -1:
            closest_empty_chair = key
        elif closest_empty_chair > key:
            closest_empty_chair = key
    print closest_empty_chair, empty_chairs_distance_dict[closest_empty_chair]
    return closest_empty_chair

def choose_chair(choose_from_chair_patients_list):
    distance_to_exit_dict = {}
    print choose_from_chair_patients_list
    number_of_chairs = len(choose_from_chair_patients_list)
    print number_of_chairs

    for each_chair in choose_from_chair_patients_list:

        if each_chair[1] == 0:
            print str(each_chair[0]) + " empty chair"
            distance_to_exit = each_chair[0] - 1
            distance_to_exit_dict[each_chair[0]] = distance_to_exit
            print "distance_to_exit " + str(distance_to_exit)
            empty_chair_number = each_chair[0]

        else:
            print str(each_chair[0]) + " occupied chair"
            # for each occupied chair, find the furthest chair from this patient

    print distance_to_exit_dict
    find_closest_empty_chair(distance_to_exit_dict)

def last_chair(n_chairs):
    # make sure more than 2 chairs
    if n_chairs > 2:
        # initialize an N rows x 2 columns list
        chair_patients_list = []
        for each_number in range(n_chairs):
            column = []
            column.append(each_number+1) # + 1 so get 1 through N chairs entered first into list
            column.append(0) # set 2nd row to all zeroes initially. these are the patient numbers
            chair_patients_list.append(column)
        print chair_patients_list

        choose_chair(chair_patients_list)

        # print last column in the list
       # print chair_patients_list[9]
       # # print the last patients chair number
       # print chair_patients_list[9]
        return
    else:
        pass

last_chair(NUMBER_OF_CHAIRS)

