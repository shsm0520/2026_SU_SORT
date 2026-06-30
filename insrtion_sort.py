from utility import read_default_list

def insertion_sort(arra=None):
    # Fallback to utility if no list is passed
    n = len(arra)
    
    # Start from the second element (index 1) as the first element is already sorted
    for i in range(1, n):
        key = arra[i]
        j = i - 1
        
        # Move elements of arra[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arra[j] > key:
            arra[j + 1] = arra[j]
            j -= 1
            
        # Insert the key into its correct sorted position
        arra[j + 1] = key
        
    return arra

if __name__ == "__main__":
    # Test case 1: Without arguments (reads from file via utility)
    
    listtbsort = read_default_list()
    print("list to be sorted:")
    print(listtbsort)
    sorted_file = insertion_sort(listtbsort)
    print("sorted result:")
    print(sorted_file)