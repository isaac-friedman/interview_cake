def product_of_all_other_ints(input_list):
    products_before_each = [None] * len(input_list)
    products_after_each = [None] * len(input_list)
    products_besides_each = [None] * len(input_list)
    so_far = 1
    # Look at the product up to each index
    for i in range(len(input_list)):
        so_far *= input_list[i]
        products_before_each[i] = so_far

    # Reset our temp variable before going backwards
    so_far = 1
    for i in range(len(input_list) - 1, -1, -1):
        so_far *= input_list[i]
        products_after_each[i] = so_far
    print(products_before_each)
    print(products_after_each)

    for i in range(len(input_list)):
        products_besides_each[i] = products_before_each[i] * products_after_each[i]

    return products_besides_each


input_list = [1, 7, 3, 4]
print(product_of_all_other_ints(input_list))
