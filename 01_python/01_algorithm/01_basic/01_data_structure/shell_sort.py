# 셀정렬 : 행렬의 원소를 더 이상 나누어지지 않을 때까지 절반으로 나누고,
#         나누어진 각 행렬의 원소를 비교하여 순서에 맞게 스왑하는 정렬
# 시간복잡도 : O(n) 또는 O(n²), 평균 O(n^1.5)

data = [5, 4, 10, 6, 3, 1, 8, 9, 2, 7]


def shell_sort(array):
    print("data :", array)
    loop_cnt = 0
    array_len = len(array)
    half = array_len // 2

    while half > 0:
        for x in range(half, array_len):
            temp = array[x]
            y = x - half
            while y >= 0 and array[y] > temp:
                array[y + half] = array[y]
                y -= half
            array[y + half] = temp
        half //= 2

    print("loop_cnt :", loop_cnt)
    print("result :", array)

"""
< Loop #1 >

 *                 *
[1, 4, 10, 6, 3], [5, 8, 9, 2, 7]

    *                 *
[1, 4, 10, 6, 3], [5, 8, 9, 2, 7]

       *                *
[1, 4, 9, 6, 3], [5, 8, 10, 2, 7]

          *                 *
[1, 4, 9, 2, 3], [5, 8, 10, 6, 7]

             *                 *
[1, 4, 9, 2, 3], [5, 8, 10, 6, 7]

< Loop #2 >

 *       *
[1, 4], [9, 2], [3, 5], [8, 10], [6, 7]

    *       *
[1, 2], [9, 4], [3, 5], [8, 10], [6, 7]

         *       *
[1, 2], [3, 4], [9, 5], [8, 10], [6, 7]

            *       *
[1, 2], [3, 4], [9, 5], [8, 10], [6, 7]

                 *       *
[1, 2], [3, 4], [8, 5], [9, 10], [6, 7]

                    *       *
[1, 2], [3, 4], [8, 5], [9, 10], [6, 7]

                         *        *
[1, 2], [3, 4], [6, 5], [8, 10], [9, 7]

                            *       *
[1, 2], [3, 4], [6, 5], [8, 7], [9, 10]

< Loop #3 >

 *    *
[1], [2], [3], [4], [6], [5], [8], [7], [9], [10]

      *    *
[1], [2], [3], [4], [6], [5], [8], [7], [9], [10]

           *    *
[1], [2], [3], [4], [6], [5], [8], [7], [9], [10]

                *    *
[1], [2], [3], [4], [6], [5], [8], [7], [9], [10]

                     *    *
[1], [2], [3], [4], [5], [6], [8], [7], [9], [10]

                          *    *
[1], [2], [3], [4], [5], [6], [8], [7], [9], [10]

                               *    *
[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]

                                    *    *
[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]

                                         *    *
[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]
"""
