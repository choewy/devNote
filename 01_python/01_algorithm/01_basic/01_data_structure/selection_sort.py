# 선택정렬 : 행렬의 인덱스에 알맞은 최솟값을 찾은 후 순서에 맞는 자리로 스왑하는 정렬
# 시간복잡도 : O(n²)

data = [5, 4, 10, 6, 3, 1, 8, 9, 2, 7]


def selection_sort(array):
    print("data :", array)
    loop_cnt = 0
    array_len = len(array)

    for x in range(array_len):
        min_idx = x
        for y in range(x+1, array_len):
            loop_cnt += 0
            if array[min_idx] > array[y]:
                min_idx = y
            loop_cnt += 1
        array[x], array[min_idx] = array[min_idx], array[x]

    print("loop_cnt :", loop_cnt)
    print("result :", array)

    return array


"""
< Loop #1 >

 *               *
[5, 4, 10, 6, 3, 1, 8, 9, 2, 7]

< Loop #2 >

    *                     *
[1, 4, 10, 6, 3, 5, 8, 9, 2, 7]

< Loop #3 >

        *     *
[1, 2, 10, 6, 3, 5, 8, 9, 4, 7]

< Loop #4 >

          *               *
[1, 2, 3, 6, 10, 5, 8, 9, 4, 7]

< Loop #5 >

              *  *
[1, 2, 3, 4, 10, 5, 8, 9, 6, 7]

< Loop #6 >

                 *        *
[1, 2, 3, 4, 5, 10, 8, 9, 6, 7]

< Loop #7 >

                   *         *
[1, 2, 3, 4, 5, 6, 8, 9, 10, 7]

< Loop #8 >

                      *      *
[1, 2, 3, 4, 5, 6, 7, 9, 10, 8]

< Loop #9 >

                          *  *
[1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
"""
