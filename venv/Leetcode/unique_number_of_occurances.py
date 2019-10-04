#https://leetcode.com/problems/unique-number-of-occurrences/
def uniqueOccurrences(self, arr: List[int]) -> bool:
    temp = []
    s = set(arr)
    for i in s:
        temp.append(arr.count(i))

    for x in range(len(temp) - 1):
        for c in range(x + 1, len(temp)):
            if temp[x] == temp[c]:
                return False

    return True








