takeout = [1, 3, 5]
eatin = [2, 4, 6]
served = [1, 2, 3, 5, 4, 6]

def validate_order(takeout, eatin, served):
    takout_index 0
    eatin_index = 0

    for i in served:
        if i == takout[takout_index]:
            takout_index += 1
        elif i == eatin[eatin_index]:
            eatin_index += 1
        else:
            print("You are out of order!")
            return
    return "It VERKS!!!"
