def max_product_of_3(input_list):
    input_list = sorted(input_list)
    output_list = input_list[-3:]
    print(output_list)
    return "Naive solution"

input_list= [10,10,1,3,2]
max_product_of_3(input_list)
