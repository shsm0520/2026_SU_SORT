def sapart(number):
    listm = list(map(int, str(number)))
    listm.reverse()
    return listm


# for better performance get rid of value compareson (remove spart call)
#pairs = [(num, sapart(num)) for num in sort_list]

def counting_sort_by_digit(pairs, digit_index):
    corrent = [0] * 10

    #list will be returned each time ㅑteration
    #count the number of each digit from 0 to 9 in the list
    for num, tlist in pairs:
        #if shorter length digit just use 0 ex. 0000400 
        digit = tlist[digit_index] if digit_index < len(tlist) else 0
        corrent[digit] += 1

#prefix sum calc
    for i in range(1, len(corrent)):
        corrent[i] += corrent[i - 1]

    sorted_pairs = [0] * len(pairs)

    # csort and keep stable sort
    for i in range(len(pairs) - 1, -1, -1):
        num, tlist = pairs[i]
        digit = tlist[digit_index] if digit_index < len(tlist) else 0
        corrent[digit] -= 1
        #keep the pair to further iteration
        sorted_pairs[corrent[digit]] = (num, tlist)

    return sorted_pairs


def radix_sort(lists):
    if not lists:
        return []

    # make a parit and save for pairs
    pairs = [(num, sapart(num)) for num in lists]
    
    max_len = max(len(tlist) for num, tlist in pairs)

    # make digit csort
    for digit_index in range(max_len):
        pairs = counting_sort_by_digit(pairs, digit_index)

    # return only numbers list
    return [num for num, tlist in pairs]


sort_list = [817, 9112, 911, 423, 376, 811, 811, 564]
sorted_list = radix_sort(sort_list)

print(sorted_list)