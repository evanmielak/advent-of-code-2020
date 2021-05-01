# Day 1 of Advent of code challenge.
def expense_report():
    input_list = []
    with open('day-1-input.txt', 'r') as reader:
        for line in reader:
            input_list.append(line.strip())
    print(input_list)
    for input_1 in input_list:
        for input_2 in input_list:
            for input_3 in input_list:
                if int(input_1) + int(input_2) + int(input_3) == 2020:
                    return print(int(input_1) * int(input_2) * int(input_3))


expense_report()

# Part 1 answer

# def expense_report():
#     input_list = []
#     with open('day-1-input.txt', 'r') as reader:
#         for line in reader:
#             input_list.append(line.strip())
#     print(input_list)
#     for input_1 in input_list:
#         for input_2 in input_list:
#             if int(input_1) + int(input_2) == 2020:
#                 return print(int(input_1) * int(input_2))
#
#
# expense_report()

