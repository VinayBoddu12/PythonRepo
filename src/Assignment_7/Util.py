def print_formatted(number):
    for i in range(1,number+1):
        hex_value = "{0:x}".format(i)
        print(i," ",oct(i)[2:]," ", hex_value," ", bin(i)[2:])


# n = int(input())
#     print_formatted(n)