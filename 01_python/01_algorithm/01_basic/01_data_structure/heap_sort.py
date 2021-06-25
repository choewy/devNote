# 병합정렬 : 해당 배열을 통해 힙 구조를 형성한 후,
#          힙을 반복적으로 탐색하면서 최댓값을 맨 뒤로 스왑하는 정렬
# 시간복잡도 : O(nLog₂n)

data = [5, 4, 10, 6, 3, 1, 8, 9, 2, 7]


def heapify(array, x, size):
    left = x + 1
    right = x + 2
    y = x
    if left < size and array[left] > array[y]:
        y = left
    if right < size and array[right] > array[y]:
        y = right
    if y != x:
        array[x], array[y] = array[y], array[x]
        heapify(array, y, size)


def heap_sort(array):
    size = len(array)

    for x in range(size // 2 - 1, -1, -1):
        heapify(array, x, size)

    for x in range(size-1, -1, -1):
        array[x], array[0] = array[0], array[x]
        heapify(array, 0, x)

    return array


"""
< Heapify #1 >
     5
  4     10
 6 8   1 9
7 2 3

< Heapify #2 >
     5
  4     10
 6 8   1 9
7 2 3

< Heapify #3 >
     5
  4     10
 6 8   1 9
7 2 3

< Heapify #4 >
     5
  4     10
 6 8   1 9
7 2 3

< Heapify #5 >
     5
  4     10
 8 9   1 7
6 2 3

< Heapify #6 >
     5
  4     10
 8 9   1 7
6 2 3

< Heapify #7 >
     5
  4     10
 8 9   1 7
6 2 3

< Heapify #8 >
     5
  4     10
 8 9   1 7
6 2 3

< Heapify #9 >
     5
  4     10
 8 9   1 7
6 2 3

< Heapify #10 >
     5
  10     9
 8 7   1 6
4 2 3

< Heapify #11 >
     5
  10     9
 8 7   1 6
4 2 3

< Heapify #12 >
     5
  10     9
 8 7   1 6
4 2 3

< Heapify #13 >
     5
  10     9
 8 7   1 6
4 2 3

< Heapify #14 >
     5
  10     9
 8 7   1 6
4 2 3

< Heapify #15 >
     10
  9     8
 7 6   1 5
4 2 3

< Heapify #16 >
     10
  9     8
 7 6   1 5
4 2 3

< Heapify #17 >
     10
  9     8
 7 6   1 5
4 2 3

< Heapify #18 >
     10
  9     8
 7 6   1 5
4 2 3

< Heapify #19 >
     10
  9     8
 7 6   1 5
4 2 3

< Heapify #20 >
     10
  9     8
 7 6   1 5
4 2 3

< Heapify #21 >
     9
  8     7
 6 5   1 4
3 2 10

< Heapify #22 >
     9
  8     7
 6 5   1 4
3 2 10

< Heapify #23 >
     9
  8     7
 6 5   1 4
3 2 10

< Heapify #24 >
     9
  8     7
 6 5   1 4
3 2 10

< Heapify #25 >
     9
  8     7
 6 5   1 4
3 2 10

< Heapify #26 >
     9
  8     7
 6 5   1 4
3 2 10

< Heapify #27 >
     9
  8     7
 6 5   1 4
3 2 10

< Heapify #28 >
     8
  7     6
 5 4   1 3
2 9 10

< Heapify #29 >
     8
  7     6
 5 4   1 3
2 9 10

< Heapify #30 >
     8
  7     6
 5 4   1 3
2 9 10

< Heapify #31 >
     8
  7     6
 5 4   1 3
2 9 10

< Heapify #32 >
     8
  7     6
 5 4   1 3
2 9 10

< Heapify #33 >
     8
  7     6
 5 4   1 3
2 9 10

< Heapify #34 >
     8
  7     6
 5 4   1 3
2 9 10

< Heapify #35 >
     7
  6     5
 4 3   1 2
8 9 10

< Heapify #36 >
     7
  6     5
 4 3   1 2
8 9 10

< Heapify #37 >
     7
  6     5
 4 3   1 2
8 9 10

< Heapify #38 >
     7
  6     5
 4 3   1 2
8 9 10

< Heapify #39 >
     7
  6     5
 4 3   1 2
8 9 10

< Heapify #40 >
     7
  6     5
 4 3   1 2
8 9 10

< Heapify #41 >
     6
  5     4
 3 2   1 7
8 9 10

< Heapify #42 >
     6
  5     4
 3 2   1 7
8 9 10

< Heapify #43 >
     6
  5     4
 3 2   1 7
8 9 10

< Heapify #44 >
     6
  5     4
 3 2   1 7
8 9 10

< Heapify #45 >
     6
  5     4
 3 2   1 7
8 9 10

< Heapify #46 >
     5
  4     3
 2 1   6 7
8 9 10

< Heapify #47 >
     5
  4     3
 2 1   6 7
8 9 10

< Heapify #48 >
     5
  4     3
 2 1   6 7
8 9 10

< Heapify #49 >
     5
  4     3
 2 1   6 7
8 9 10

< Heapify #50 >
     5
  4     3
 2 1   6 7
8 9 10

< Heapify #51 >
     4
  3     2
 1 5   6 7
8 9 10

< Heapify #52 >
     4
  3     2
 1 5   6 7
8 9 10

< Heapify #53 >
     4
  3     2
 1 5   6 7
8 9 10

< Heapify #54 >
     4
  3     2
 1 5   6 7
8 9 10

< Heapify #55 >
     3
  2     1
 4 5   6 7
8 9 10

< Heapify #56 >
     3
  2     1
 4 5   6 7
8 9 10

< Heapify #57 >
     3
  2     1
 4 5   6 7
8 9 10

< Heapify #58 >
     2
  1     3
 4 5   6 7
8 9 10

< Heapify #59 >
     2
  1     3
 4 5   6 7
8 9 10

< Heapify #60 >
     1
  2     3
 4 5   6 7
8 9 10

< Heapify #61 >
     1
  2     3
 4 5   6 7
8 9 10

"""
