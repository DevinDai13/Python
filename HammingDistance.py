# overall, the function finds all the possible binary numbers with the given hamming distance in a tree branch fashion
# where are only really two cases, you either change the digit or you don't
# if you change the digit, it's either from 0 to 1 or from 1 to 0

def hamming_distance(binary_num, distance):
    if distance == 0:           # Base Case:
        return binary_num       # if the distance is 0, then just return the original number

    else:
        binary_output = []      # the final set of numbers will be in a list
        for digit in range(len(binary_num)):    # traversing through the entire number
            if len(binary_num[digit:]) >= distance:  # only find the result if the distance is valid for the binary
                # if the digit in binary is '0' case
                if binary_num[digit] == '0':
                    rest_digit_list = hamming_distance(binary_num[digit + 1:], distance - 1)    # decrease distance
                    # distance is 1 :
                    # you can just concatenate the rest of the binary with the changed digit
                    # because that is the only change needed
                    if distance == 1:
                        binary_output.append(binary_num[:digit] + '1' + str(rest_digit_list))  # change the '0' to '1'
                    # distance other than 1:
                    # have to concatenate each digit in the rest of the binary individually
                    else:
                        for item in rest_digit_list:
                            binary_output.append(binary_num[:digit] + '1' + str(item))      # change the '0' to '1'
                # if the digit in binary is '1' case
                elif binary_num[digit] == '1':
                    rest_digit_list = hamming_distance(binary_num[digit + 1:], distance - 1)    # decrease distance
                    # distance is 1 :
                    # you can just concatenate the rest of the binary with the changed digit
                    # because that is the only change needed
                    if distance == 1:
                        binary_output.append(binary_num[:digit] + '0' + str(rest_digit_list))   # change the '1' to '0'
                    # distance other than 1 :
                    # have to concatenate each digit in the rest of the binary individually
                    else:
                        for item in rest_digit_list:
                            binary_output.append(binary_num[:digit] + '0' + str(item))      # change the '1' to '0'
        return binary_output    # return the list


prompt = input('Enter file name: ')        # asking the user for input file
with open(prompt)as input_f:   # get the input file from the user and read the file
    for line in input_f:
        new_line = line.strip().split(' ')  # read each line
        binary = new_line[0]        # first item in the list is always the number
        dist = new_line[1]             # second item in the list is always the distance
        result = hamming_distance(binary, int(dist))  # call the function to find all the possible output for the file
        if result == []:   # if return empty list, nothing found message
            print('No strings with distance ' + dist + ' from ' + binary)
        # if there are reults, then print all of them in the following form
        else:
            print('Strings with distance of ' + dist + ' from ' + binary)
            if int(dist) == 0:  # if distance is 0, just return the whole list as there is only 1 number in it
                print(result)
            else:
                for i in result:     # else print all the results one line at a time
                    print(i)
        print(' ')


