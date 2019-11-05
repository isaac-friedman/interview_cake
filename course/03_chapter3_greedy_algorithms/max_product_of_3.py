def max_product_of_3(input_list):
    min_of_2 = input_list[0]*input_list[1]
    max_of_2 = input_list[0]*input_list[1]
    highest = max(input_list[0], input_list[1]
    lowest = min(input_list[0], input_list[1])
    max_of_3 = input_list[0] * input_list[1] * input_list[2]
    for i in range(2, len(input_list)):
        current = input_list[i]
        # check for new max of 2
        max_of_2 = max(max_of_2, current * highest, current * lowest)
        # check for new min of 2
        min_of_2 = min(min_of_2, current * highest, current * lowest)

        # Do we have a new highest?
        highest = max(highest, current)

        # Do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3

input_list= [-10,-10,1,3,2]
print(max_product_of_3(input_list))
