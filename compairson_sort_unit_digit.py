from utility import read_default_list

def sapart (number):
    listm = list(map(int, str(number)))
    listm.reverse()
    return listm

def get_corrent(sort_list):
    #corrent _temp list 0 to9 to store the count of each digit from 0 to 9 in the list
    corrent = [0] * 10
    #divide input list into reversed lists of digits
    numbera = list(map(sapart, sort_list))

    # refactor for better readability
    for tlist in numbera:
        #currently only happens in first digie
        corrent[tlist[0]] += 1

    # prefix sum calc
    # for better readability - range is same btw
    for i in range(1, len(corrent)):
        corrent[i] += corrent[i - 1]
        
    return corrent, numbera

def first_digit_counting_sort(sort_list=None):
    corrent, numbera = get_corrent(sort_list)

    #to create empty list for random position input
    sorted_list = [0] * len(sort_list)

    for i in range(len(sort_list) - 1, -1, -1):
        # for later on perpose to keep the stable sort.
        # make it fit with list number aka start from 0
        num = sort_list[i]
        digit = numbera[i][0]
        #only for first digit
        corrent[digit] -= 1
        sorted_list[corrent[digit]] = num

    return sorted_list

if __name__ == "__main__":

    listtbsort = read_default_list()
    print("list to be sorted:")
    print(listtbsort)
    
    main_corrent, _ = get_corrent(listtbsort)
    print("\nFirst digit csort")
    print("------------------------------")
    print("|0| 1| 2| 3| 4| 5| 6| 7| 8| 9|")
    print(main_corrent)
    print("------------------------------\n")

    sorted_file = first_digit_counting_sort(listtbsort)
    print("sorted result:")
    print(sorted_file)