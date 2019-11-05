def product_of_all_other_ints(input_list):
    print("This is horribly inefficient and is only for illustrative purposes.")
    output_list = []
    for i in range(len(input_list)):
        tmp = 1
        for j in range(len(input_list)):
            if j != i:
                tmp *= input_list[j]
            else:
                pass
        output_list.append(tmp)
    return output_list



input_list = [1, 7, 3, 4]
print(product_of_all_other_ints(input_list))
