# Day 2 of Advent of code challenge
def valid_password():
    valid_passwords = 0
    passwords = []
    with open('day-2-input.txt', 'r') as reader:
        for line in reader:
            passwords.append(line.strip())
    print(passwords)
    for password in passwords:
        space_separated = password.split(' ')
        index = space_separated[0].split('-')
        letter = split(space_separated[1])
        user_pass = space_separated[2]
        test_1 = user_pass[int(index[0])-1] == letter[0]
        test_2 = user_pass[int(index[1])-1] == letter[0]
        if test_1 ^ test_2:
            valid_passwords += 1

    print(valid_passwords)


def split(word):
    return [char for char in word]


valid_password()
