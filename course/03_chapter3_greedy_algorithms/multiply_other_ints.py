def product_of_all_other_ints(input_list):
    output_list = []
    master_multiple = 1
    for i in input_list:
        master_multiple *= i
    print(master_multiple)
    for i in input_list:
        output_list.append(master_multiple/i)
    return output_list



input_list = [1, 7, 3, 4]
print(product_of_all_other_ints(input_list))
