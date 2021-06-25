# 병합정렬 : 해당 배열의 기준점(pivot)을 정한 후 기준점보다 작은 값은 왼쪽,
#           기준점보다 큰 값은 오른쪽으로 모으는 함수를 재귀용법을 통해 반복하며 정렬
# 시간복잡도 : O(nLog₂n), 최악의 경우 O(n²)

data = [5, 4, 10, 6, 3, 1, 8, 9, 2, 7]


def quick_sort(array):
    if len(array) <= 1:
        return array

    left, right = [], []
    pivot = array[0]

    for x in range(1, len(array)):
        if pivot > array[x]:
            left.append(array[x])
        else:
            right.append(array[x])

    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_use_generator(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = [component for component in array[1:] if component <= pivot]
    right = [component for component in array[1:] if component > pivot]
    return quick_sort_use_generator(left) + [pivot] + quick_sort_use_generator(right)


"""
right	< left : [] 		    pivot: [1] 		right : [2] >
left	< left : [1, 2] 	    pivot: [3] 		right : [] >
right	< left : [] 		    pivot: [1] 		right : [2] >
left	< left : [1, 2, 3] 	    pivot: [4] 		right : [] >
right	< left : [] 		    pivot: [1] 		right : [2] >
left	< left : [1, 2] 	    pivot: [3] 		right : [] >
right	< left : [] 		    pivot: [1] 		right : [2] >
array	< left : [7] 		    pivot: [8] 		right : [9] >
right	< left : [] 		    pivot: [6] 		right : [7, 8, 9] >
array	< left : [7] 		    pivot: [8] 		right : [9] >
left	< left : [6, 7, 8, 9] 	pivot: [10] 	right : [] >
array	< left : [7] 		    pivot: [8] 		right : [9] >
right	< left : [] 		    pivot: [6] 		right : [7, 8, 9] >
array	< left : [7] 		    pivot: [8] 		right : [9] >
array	< left : [1, 2, 3, 4] 	pivot: [5] 		right : [6, 7, 8, 9, 10] >
right	< left : [] 		    pivot: [1] 		right : [2] >
left	< left : [1, 2] 		pivot: [3] 		right : [] >
right	< left : [] 		    pivot: [1] 		right : [2] >
left	< left : [1, 2, 3] 		pivot: [4] 		right : [] >
right	< left : [] 		    pivot: [1] 		right : [2] >
left	< left : [1, 2] 		pivot: [3] 		right : [] >
right	< left : [] 		    pivot: [1] 		right : [2] >
array	< left : [7] 		    pivot: [8] 		right : [9] >
right	< left : [] 		    pivot: [6] 		right : [7, 8, 9] >
array	< left : [7] 		    pivot: [8] 		right : [9] >
left	< left : [6, 7, 8, 9] 	pivot: [10] 	right : [] >
array	< left : [7] 		    pivot: [8] 		right : [9] >
right	< left : [] 		    pivot: [6] 		right : [7, 8, 9] >
array	< left : [7] 		    pivot: [8] 		right : [9] >
"""
