# Day 01, 2020
# Report Repair

def read_input():
    data = open('Input_day_01.txt','r')
    #data = open('test_day_01.txt','r')
    report = [int(line.rstrip('\n')) for line in data]
    return report

def find_entries(report,desired_sum):
    for entry1 in report:
        for entry2 in report:
            diff = desired_sum-entry1-entry2
            if diff in report:
                print(str(entry1)+' '+str(entry2)+' '+str(diff))
                print('\n\n')
                answer = entry1*entry2*diff
                return answer
    return answer

def sort(report):
    report.sort()
    return report
    

def main():
    desired_sum = 2020
    report = read_input()
    report = sort(report)
    answer = find_entries(report, desired_sum)
    print('The answer in part 2 is: '+str(answer))
    

    

    

if __name__ == "__main__":
    main()
