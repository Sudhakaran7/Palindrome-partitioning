class Solution(object):
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        n = len(s)

        is_palindrome = [[0 for j in range(n)] for i in range(n)]
        for i in reversed(range(0, n)):
            for j in range(i, n):
                is_palindrome[i][j] = s[i] == s[j] and ((j - i < 2 ) or is_palindrome[i + 1][j - 1])

        sub_partition = [[] for i in range(n)]
        for i in reversed(range(n)):
            for j in range(i, n):
                if is_palindrome[i][j]:
                    if j + 1 < n:
                        for p in sub_partition[j + 1]:
                            sub_partition[i].append([s[i:j + 1]] + p)
                    else:
                        sub_partition[i].append([s[i:j + 1]])

        return sub_partition[0]
val=Solution()
s=input()
print(*val.partition(s))
