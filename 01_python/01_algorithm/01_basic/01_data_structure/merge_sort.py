# 병합정렬 : 행렬을 먼저 더 이상 쪼개어지지 않을 때까지 나눈 후,
#           순서에 맞게 정렬한 후 다시 행렬을 합치는 정렬
# 시간복잡도 : O(nLog₂n)

data = [5, 4, 10, 6, 3, 1, 8, 9, 2, 7]


def merge(array_left, array_right):
    x, y = (0, 0)
    array = []

    while (x < len(array_left)) and (y < len(array_right)):
        if array_left[x] < array_right[y]:
            array.append(array_left[x])
            x += 1
        else:
            array.append(array_right[y])
            y += 1

    while x < len(array_left):
        array.append(array_left[x])
        x += 1

    while y < len(array_right):
        array.append(array_right[y])
        y += 1

    return array


def merge_sort(array):
    if len(array) <= 1:
        return array

    center = len(array) // 2
    array_left = array[:center]
    array_right = array[center:]

    array_left = merge_sort(array_left)
    array_right = merge_sort(array_right)

    return merge(array_left, array_right)


def run_merge_sort(array):
    print("data :", array)
    array = merge_sort(array)
    print("result :", array)


"""
< Divide >
[5, 4, 10, 6, 3, 1, 8, 9, 2, 7]

< Divide >
[5, 4, 10, 6, 3][1, 8, 9, 2, 7]

< Divide >
[5, 4][10, 6, 3][1, 8][9, 2, 7]

< Divide >
[5][4][10][6, 3][1][8][9][2, 7]

< Sort >
[5][4][10][6][3][1][8][9][2][7]

< Merge >
[4, 5][10][3, 6][1, 8][9][2, 7]

< Merge >
[4, 5][3, 6, 10][1, 8][2, 7, 9]

< Merge >
[3, 4, 5, 6, 10][1, 2, 7, 8, 9]

< Merge >
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
