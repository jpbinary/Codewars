'''def calc_distance_from_potential_chair_to_closest_occupied_chairs(seats_taken_calc, potential_chairs_and_distance_to_closest_occupied_chairs_calc):
    print seats_taken_calc
    print potential_chairs_and_distance_to_closest_occupied_chairs_calc
    pass
'''
def calc_distance_to_first_chair(first_chair_number):
    print first_chair_number
    pass

def calc_distance_to_second_chair(second_chair_number):
    print second_chair_number
    pass


def calc_potential_chairs(seats_taken_c):
    '''calculate what potential chairs the next person should sit in.
     based on distance to other occupied chairs.'''
    seats_taken_c_index_location = 0
    # need dictionary to hold potential chair as key, and a 2 item list with the
    # distance from the occupied chairs to the potential chair

    #potential_chairs_and_distance_to_closest_occupied_chairs = []
    potential_chairs_and_distance_to_closest_occupied_chairs = {}
    while seats_taken_c_index_location < len(seats_taken_c)-1:
        # take value of list item at index plus value of list item at index+1
        # and divide them by 2. This is the mid-way point between the two chairs.
        #potential_chairs_and_distance_to_closest_occupied_chairs.append((seats_taken_c[seats_taken_c_index_location] + \
                             #seats_taken_c[seats_taken_c_index_location + 1]) / 2)
        potential_chair = (seats_taken_c[seats_taken_c_index_location] + \
            seats_taken_c[seats_taken_c_index_location + 1]) / 2
        potential_chairs_and_distance_to_closest_occupied_chairs[potential_chair] = \
            [calc_distance_to_first_chair(seats_taken_c[seats_taken_c_index_location]),
             calc_distance_to_second_chair(seats_taken_c[seats_taken_c_index_location + 1])]

        #calc_distance_from_potential_chair_to_closest_occupied_chairs(
            #seats_taken_c, potential_chairs_and_distance_to_closest_occupied_chairs)

        seats_taken_c_index_location += 1
        # need to calc and save distance to other seats<<<
    return potential_chairs_and_distance_to_closest_occupied_chairs

def what_seats_are_taken(chairs_people_w):
    '''create dict with seats that are currently taken'''
    seats_taken_w = []
    for chair, person in chairs_people_w.items():
        ''' if person is in chair, save chair to seats_taken'''
        if person != 0:
            seats_taken_w.append(chair)
        print chair, person
    return seats_taken_w

def assign_first_and_second_person_chairs(chairs_people_a):
    ''' assign first person to first chair and second person to last chair'''
    chairs_people_a[1] = 1
    chairs_people_a[len(chairs_people_a)] = 2
    return chairs_people_a

def init_chairs_people(number_of_people):
    '''initialize a dictionary with 1 through the number of people as the keys,
    and set all the key values to 0.'''
    chairs_people_dict = {}
    for each_person in range(number_of_people):
        chairs_people_dict[each_person+1] = 0
    return chairs_people_dict


def last_chair(n):
    chairs_people = init_chairs_people(n)
    print chairs_people
    chairs_people = assign_first_and_second_person_chairs(chairs_people)
    print chairs_people
    seats_taken = what_seats_are_taken(chairs_people)
    print seats_taken
    potential_chairs = calc_potential_chairs(seats_taken)
    print potential_chairs

    return




last_chair(10)
last_chair(5)