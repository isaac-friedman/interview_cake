from random import randrange

def get_rand(ceiling):
    return randrange(0, ceiling+1)

def inplace_shuffle(input_list):
    for first_index in range(len(input_list)):
        second_index = get_rand(len(input_list))
        input_list[first_index], input_list[second_index] = input_list[second_index], input_list[first_index]
    print(input_list)
    return
