import random


def gen_random_series():
    list_of_random_elts = []
    list_of_numbers = []
    temp_list = [1]
    # dict = {}
    for i in range(51):
        list_of_numbers.append(i + 1)
        # key = i + 1
        # print(i)
        temp_list.append(i + 2)

        random_number = random.choice(temp_list)
        # print(temp_list)
        list_of_random_elts.append(random_number)

    print(list_of_random_elts)


gen_random_series()
