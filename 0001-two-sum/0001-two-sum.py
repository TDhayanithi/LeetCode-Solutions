class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, current_number in enumerate(nums):
            needed_number = target - current_number

            if needed_number in seen:
                return [seen[needed_number], index]

            seen[current_number] = index
