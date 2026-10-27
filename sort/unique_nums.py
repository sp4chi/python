class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        steps = 0
        A.sort()
        prev = A[0]
        for i in range(1, len(A)):
            if A[i] <= prev:
                bump = prev + 1
                steps += bump - A[i]
                prev = bump
            else:
                prev = A[i]
        return steps
