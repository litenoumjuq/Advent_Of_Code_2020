# Day 02, 2020
# Password Philosophy

def read_input():
    data = open('Input_day_02.txt','r')
    #data = open('test_day_02.txt','r')
    password_list = [line.rstrip('\n').split(' ') for line in data]
    return password_list


def check_positions(entry):
    positions = entry.split('-')
    positions = [int(nr) for nr in positions]
    return positions


def check_letter(entry):
    letter = entry.rstrip(':')
    return letter


def check_validity(password, positions, letter, nr_valid_passwords):
    if password[positions[0]-1] == letter:
        if password[positions[1]-1] != letter:
            return nr_valid_passwords+1
        else:
            return nr_valid_passwords
    else:
        if password[positions[1]-1] == letter:
            return nr_valid_passwords+1
        else:
            return nr_valid_passwords


def check_passwords(password_list):
    nr_valid_passwords = 0
    for entry in password_list:
        positions = check_positions(entry[0])
        letter = check_letter(entry[1])
        password = entry[2]
        nr_valid_passwords = check_validity(password, positions, letter, nr_valid_passwords)
    return nr_valid_passwords


def main():
    password_list = read_input()
    nr_valid_passwords = check_passwords(password_list)
    print('The number of valid passwords are: '+str(nr_valid_passwords))
    

if __name__ == "__main__":
    main()
