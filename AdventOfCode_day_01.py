# Day 01, 2020
# Report Repair

def read_input():
    data = open('Input_day_01.txt','r')
    #data = open('test_day_01.txt','r')
    report = [int(line.rstrip('\n')) for line in data]
    return report

def find_entries(report, desired_sum):
    answer = 0
    
    for entry in report:
        diff = desired_sum-entry

        if diff in report:
            print(str(entry)+' '+str(diff))
            print('\n\n')
            answer = entry*diff
            break
        
    return answer
    

def main():
    report = read_input()

    desired_sum = 2020

    answer = find_entries(report, desired_sum)
    print(answer)

    

    

if __name__ == "__main__":
    main()
