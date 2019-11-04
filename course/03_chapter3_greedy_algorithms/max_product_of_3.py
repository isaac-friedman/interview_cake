def max_product_of_3(input_list):
    input_list = sorted(input_list)
    if abs(input_list[0]) > input_list[-1] and abs(input_list[1]) > input_list[-1]:
        output_list = [input_list[0], input_list[1], input_list[-1]]
    else:
        output_list = input_list[-3:]

    return output_list

input_list= [-10,-10,1,3,2]
print(max_product_of_3(input_list))
