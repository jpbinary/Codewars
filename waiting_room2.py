
def calc_distance_to_occupied_chairs(potential_chair_cdc, first_chair_number, second_chair_number):
    print potential_chair_cdc
    print first_chair_number
    distance_to_first_chair = abs(potential_chair_cdc-first_chair_number)
    distance_to_second_chair = abs(potential_chair_cdc-second_chair_number)
    print distance_to_first_chair, distance_to_second_chair
    print distance_to_first_chair + distance_to_second_chair
    return distance_to_first_chair + distance_to_second_chair

def calc_potential_chairs(seats_taken_c):
    '''calculate what potential chairs the next person should sit in.
     based on distance to other occupied chairs.'''

    seats_taken_c_index_location = 0
    # need dictionary to hold potential chair as key, and a 2 item list with the
    # distance from the occupied chairs to the potential chair
    potential_chairs_and_distance_to_closest_occupied_chairs = {}

    while seats_taken_c_index_location < len(seats_taken_c)-1:
        # take value of list item at index plus value of list item at index+1
        # and divide them by 2. This is the mid-way point between the two chairs.
        potential_chair = (seats_taken_c[seats_taken_c_index_location] + \
            seats_taken_c[seats_taken_c_index_location + 1]) / 2
        # update the potential_chairs_and_distance_to_closest_occupied_chairs with a key value
        # equal to the potential chair, and a value equal to the distance to the 2
        # closest occupied chairs combined
        potential_chairs_and_distance_to_closest_occupied_chairs[potential_chair] = \
            calc_distance_to_occupied_chairs(potential_chair,
                                    seats_taken_c[seats_taken_c_index_location],
                                    seats_taken_c[seats_taken_c_index_location + 1])
        seats_taken_c_index_location += 1
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
    if n <= 2:
        print "please enter a value greater than 2"
    else:
        chairs_people = init_chairs_people(n)
        print chairs_people
        # 1st and 2nd person enter
        chairs_people = assign_first_and_second_person_chairs(chairs_people)
        print chairs_people
        seats_taken = what_seats_are_taken(chairs_people)
        print seats_taken

        # 3rd person enters
        potential_chairs = calc_potential_chairs(seats_taken)
        print 'potential chairs: ', potential_chairs


        for potential_chair, potential_chair_distance in potential_chairs.iteritems():
            print potential_chair, potential_chair_distance
        if len(potential_chairs) == 1:
            chairs_people.update(potential_chairs)
        print chairs_people


        return



last_chair(2)
#last_chair(10)
#last_chair(5)