# 이진탐색 : 순차적인 행렬에서 어떠한 값을 찾고자 할 때,
#              행렬을 둘로 나누고 찾고자 하는 값이 속한 부분을 더욱 잘게 나누어 찾는 방식
# 시간복잡도 : 실제는 무조건 1회 실행되므로 Log₂n+1이나, 상수는 삭제되므로 O(Log₂n)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def binary_search(array, search_data):
    array_len = len(array)

    if array_len == 0:
        return False

    if array_len == 1:
        if array[0] == search_data:
            return search_data
        else:
            return False

    center = array_len // 2

    if search_data == array[center]:
        return search_data
    if search_data > array[center]:
        return binary_search(array[center:], search_data)
    else:
        return binary_search(array[:center], search_data)

