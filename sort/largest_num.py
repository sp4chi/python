from functools import cmp_to_key


class Solution:
    # @param A : list of integers
    # @return a strings
    def largestNumber(self, A):
        # 12 , 121 - 12121 , 12112

        def comparator(X, Y):
            xy = str(X) + str(Y)
            yx = str(Y) + str(X)

            if xy > yx:
                return -1
            elif yx < xy:
                return 1
            else:
                return 0

        A.sort(key=cmp_to_key(comparator))
        return str(int("".join(map(str, A))))
