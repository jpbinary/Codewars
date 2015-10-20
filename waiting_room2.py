'''
2nd attempt to solve Waiting room 7 kyu problem

Still incomplete: "Process was terminated. It took longer than 6000ms to complete"
Over 800 chairs and takes over 5 sec.
'''
import operator

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
    # need dictionary to hold potential chair as key, and a vlaue with the
    # distance from the occupied chairs to the potential chair
    potential_chairs_and_distance_to_closest_occupied_chairs = {}

    while seats_taken_c_index_location < len(seats_taken_c)-1:
        # take value of list item at index plus value of list item at index+1
        # and divide them by 2. This is the mid-way point between the two chairs.

        potential_chair = (seats_taken_c[seats_taken_c_index_location] + \
            seats_taken_c[seats_taken_c_index_location + 1]) / 2
        print "calc_potential_chairs potential_chair, ", potential_chair
        if potential_chair in seats_taken_c:
            print "potential chair is already taken: ", potential_chair
        # update the potential_chairs_and_distance_to_closest_occupied_chairs with a key value
        # equal to the potential chair, and a value equal to the distance to the 2
        # closest occupied chairs combined
        else:
            potential_chairs_and_distance_to_closest_occupied_chairs[potential_chair] = \
                calc_distance_to_occupied_chairs(potential_chair,
                                                 seats_taken_c[seats_taken_c_index_location],
                                                 seats_taken_c[seats_taken_c_index_location + 1])
        seats_taken_c_index_location += 1
    print "potential_chairs_and_distance_to_closest_occupied_chairs: ", potential_chairs_and_distance_to_closest_occupied_chairs
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
        # initialize chairs
        chairs_people = init_chairs_people(n)
        print chairs_people
        # 1st and 2nd person enter
        chairs_people = assign_first_and_second_person_chairs(chairs_people)
        print chairs_people
        seats_taken = what_seats_are_taken(chairs_people)
        print "seats taken: ", seats_taken

        # 3rd person enters
        count_person_who_enters = 3
        while count_person_who_enters <= n:
            #potential_chairs = {}
            print "seats taken: ", seats_taken
            potential_chairs = calc_potential_chairs(seats_taken)
            print 'potential chairs: ', potential_chairs

            # if there is only 1 potential chair, the person sits down in this chair
            if len(potential_chairs) == 1:
                for chair in potential_chairs:
                    # person takes their seat
                    chairs_people[chair] = count_person_who_enters
                print "chairs_people -- if ", chairs_people
                # seats taken is updated with latest change
                seats_taken = what_seats_are_taken(chairs_people)
                print "seats taken: ", seats_taken

            # if there are more than 1 potential chair, the person sits down in the chair
            # with the greatest distance to the other occupied chairs.
            # if the chairs are the same distance, then the person sits down in the
            # chair with the lowest number (closest to exit).
            else:
                total_chairs_to_check_count = 0
                total_chairs_to_check = len(potential_chairs)
                print 'potential chairs -- else: ', potential_chairs
                print "chairs_people -- else ", chairs_people
                selected_chair = -1
                selected_chair_distance = -1
                while total_chairs_to_check_count < len(potential_chairs):
                    for potential_chair, potential_chair_distance in potential_chairs.iteritems():
                        if selected_chair == -1:
                            selected_chair = potential_chair
                            selected_chair_distance = potential_chair_distance
                        elif potential_chair_distance > selected_chair_distance:
                            selected_chair = potential_chair
                            selected_chair_distance = potential_chair_distance
                        elif potential_chair_distance == selected_chair_distance:
                            if selected_chair < potential_chair:
                                selected_chair = selected_chair
                                selected_chair_distance = selected_chair_distance
                            else:
                                selected_chair = potential_chair
                                selected_chair_distance = potential_chair_distance

                    total_chairs_to_check_count += 1
                print "selected chair: ", selected_chair
                # person takes their seat
                chairs_people[selected_chair] = count_person_who_enters
                # seats taken is updated with latest change
                seats_taken = what_seats_are_taken(chairs_people)

            print "while loop chairs people ", chairs_people
            print "count ", count_person_who_enters
            count_person_who_enters += 1

        # determine the last patients chair number
        last_patient_chair_number = max(chairs_people.iteritems(), key=operator.itemgetter(1))[0]
        print "last patient chair number ", last_patient_chair_number
        return last_patient_chair_number



last_chair(5)
