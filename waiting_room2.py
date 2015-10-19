def what_seats_are_taken(chairs_people_w):
    '''create dict with seats that are currently taken'''
    for chair, person in chairs_people_w.items():
        print chair


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
    what_seats_are_taken(chairs_people)
    return




last_chair(10)
last_chair(5)