# Day 02, 2020
# Password Philosophy

def read_input():
    data = open('Input_day_02.txt','r')
    #data = open('test_day_02.txt','r')
    password_list = [line.rstrip('\n').split(' ') for line in data]
    return password_list


def check_interval(entry):
    interval = entry.split('-')
    interval = [int(nr) for nr in interval]
    return interval


def check_letter(entry):
    letter = entry.rstrip(':')
    return letter


def count_occurence(letter, password):
    occurence = password.count(letter)
    return occurence


def check_validity(occurence, interval, nr_valid_passwords):
    if occurence >= interval[0] and occurence <= interval[1]:
        return nr_valid_passwords+1
    else:
        return nr_valid_passwords


def check_passwords(password_list):
    nr_valid_passwords = 0
    for entry in password_list:
        interval = check_interval(entry[0])
        letter = check_letter(entry[1])
        occurence = count_occurence(letter, entry[2])
        nr_valid_passwords = check_validity(occurence, interval, nr_valid_passwords)
    return nr_valid_passwords


def main():
    password_list = read_input()
    nr_valid_passwords = check_passwords(password_list)
    print('The number of valid passwords are: '+str(nr_valid_passwords))
    

if __name__ == "__main__":
    main()
