# utils.py에 묶어둔 공통 파일 읽기 함수를 불러옵니다.
from utility import read_default_list

def merge_sort(arr=None):
        
    # 실제 머지소트 로직 (재귀 호출 시 원본 참조 및 파일 재읽기 방지를 위해 내부 함수로 분리)
    def _merge_sort_inner(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
            
        mid = len(sub_arr) // 2
        left_half = sub_arr[:mid]
        right_half = sub_arr[mid:]

        # 재귀 호출이 정렬해서 돌려준 값을 새롭게 받아옵니다.
        left_half = _merge_sort_inner(left_half)
        right_half = _merge_sort_inner(right_half)

        i = j = k = 0

        # 두 반쪽을 정렬하며 병합
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sub_arr[k] = left_half[i]
                i += 1
            else:
                sub_arr[k] = right_half[j]
                j += 1
            k += 1

        # 남은 원소들 처리
        while i < len(left_half):
            sub_arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            sub_arr[k] = right_half[j]
            j += 1
            k += 1
            
        return sub_arr

    return _merge_sort_inner(arr)


# 이 파일만 단독으로 실행하거나 테스트할 때 사용되는 블록
if __name__ == "__main__":
    listtbsort = read_default_list()
    print("list to be sorted:")
    print(listtbsort)
    sorted_file = merge_sort(listtbsort)
    print("sorted result:")
    print(sorted_file)
    