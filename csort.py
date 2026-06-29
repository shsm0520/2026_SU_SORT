
def sapart(number):
    listm = list(map(int, str(number)))
    listm.reverse()
    return listm


def counting_sort_by_digit(values, digit_index):
    corrent = [0] * 10
    numbera = list(map(sapart, values))
   

    for tlist in numbera:
        # smaller number controll
        digit = tlist[digit_index] if digit_index < len(tlist) else 0
        corrent[digit] += 1

    for i in range(1, len(corrent)):
        corrent[i] += corrent[i - 1]

    sorted_list = [0] * len(values)

    for i in range(len(values) - 1, -1, -1):
        num = values[i]
        tlist = numbera[i]
        digit = tlist[digit_index] if digit_index < len(tlist) else 0
        corrent[digit] -= 1
        sorted_list[corrent[digit]] = num

    return sorted_list


def radix_sort(lists):
    if not lists:
        return []

    numbera = list(map(sapart, lists))
    #find the maximum length of the digit from original numbers
    max_len = max(len(tlist) for tlist in numbera)

    current_list = lists

    for digit_index in range(max_len):
        current_list = counting_sort_by_digit(current_list, digit_index)

    return current_list


sort_list = [817, 9112, 911, 423, 376, 811,811, 564]
sorted_list = radix_sort(sort_list)

print(sorted_list)