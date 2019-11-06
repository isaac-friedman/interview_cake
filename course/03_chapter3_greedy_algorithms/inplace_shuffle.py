from random import randrange

def get_rand(ceiling):
    return randrange(0, ceiling+1)

def inplace_shuffle(input_list):
    for i in range(len(input_list)-1):
        new_loc = get_rand(len(input_list))
        input_list[i], input_list[new_loc] = input_list[new_loc], input_list[i]
        print(input_list)
input_list = [11, 31, 21, 51, 41, 71, 61, 91, 81]
inplace_shuffle(input_list)
