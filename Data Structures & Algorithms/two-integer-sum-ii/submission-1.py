class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while (i < j):
            n1, n2 = numbers[i], numbers[j]
            s = n1 + n2

            if s > target:
                j -= 1
            if s < target:
                i += 1
            if s == target:
                return [i + 1, j + 1]
        