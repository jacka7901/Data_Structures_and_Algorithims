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


def uniqueOccurrences2(self, arr: List[int]) -> bool:
    temp = []
    s = set(arr)
    for i in s:
        temp.append(arr.count(i))

    new_set = set(temp)

    if len(new_set) != len(temp):
        return False

    return True








