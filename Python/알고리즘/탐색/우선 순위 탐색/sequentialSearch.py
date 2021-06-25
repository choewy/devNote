# 순차탐색 : 데이터가 담긴 배열에서 원하는 데이터를 찾아내는 방법
# 시간복잡도 : O(n)

data = ["a", "b", "c", "d", "e", "f", "g"]


def sequential_search(array, search_data):
    for x in array:
        if search_data == x:
            return x
    return False
