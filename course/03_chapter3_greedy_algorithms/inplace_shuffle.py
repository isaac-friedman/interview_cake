from random import randrange

def get_rand(ceiling):
    return randrange(0, ceiling+1)

def inplace_shuffle(input_list):
    # Value in input_list is the key, new location is the value
    output_dict = {key:None for key in input_list}
    got_rand = 0
    for i in input_list:
        flag = False
        while flag == False:
            new_loc = get_rand(len(input_list))
            got_rand += 1
            if new_loc not in output_dict.values():
                flag = True
                output_dict[i] = new_loc
    print(f"This approach led to us calling get_rand {got_rand} times.")
    print(output_dict)
    return

input_list = [11, 31, 21, 51, 41, 71, 61, 91, 81]
inplace_shuffle(input_list)
