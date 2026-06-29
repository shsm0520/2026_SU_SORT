
def sapart (number):
    listm = list(map(int, str(number)))
    listm.reverse()
    return listm


sort_list = [817,911, 423, 376, 811, 564]
print("\nList to be sorted:")
print(sort_list)

#corrent _temp list 0 to9 to store the count of each digit from 0 to 9 in the list
corrent = [0] * 10
#divide input list into reversed lists of digits
numbera = list(map(sapart, sort_list))

# for i in range(len(numbera)):
#     tlist = numbera[i]
# refactor for better readability
for tlist in numbera:

#only for first digit
    for j in range(1):
        t1list = tlist[j]
        corrent[t1list] +=1

#prefix sum calc
# for i in range(1, 9):
#     corrent[i] += corrent[i - 1]
# for better readability - range is same btw
for i in range(1, len(corrent)):
    corrent[i] += corrent[i - 1]


print("\nFirst digit csort")
print("------------------------------")
print("|0| 1| 2| 3| 4| 5| 6| 7| 8| 9|")
print(corrent)
print("------------------------------\n")

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

print("\nSorted list based on first digit:")
print(sorted_list)  
#if there are same first digit either first one of the list will be first in the sorted list. This is called stable sort.