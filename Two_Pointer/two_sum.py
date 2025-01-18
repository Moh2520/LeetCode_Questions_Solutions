from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            other_pair = target - nums[i]
            if other_pair in seen:
                return [i,seen[other_pair]]
            else:
                seen[nums[i]] = i
        return []

# def main():
#     # Instantiate the Solution class
#     solution = Solution()
    
#     # Example inputs
#     nums = [2, 7, 11, 15]
#     target = 9
    
#     # Call the twoSum method
#     result = solution.twoSum(nums, target)
    
#     # Print the result
#     print(f"Indices of numbers that add up to {target} are: {result}")

# Run the main function
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()
    
    # Example inputs
    nums = [2, 7, 11, 15]
    target = 9
    
    # Call the twoSum method
    result = solution.twoSum(nums, target)
    
    # Print the result
    print(f"Indices of numbers that add up to {target} are: {result}")
    # nums = [2,7,11,12]
    # target = 9
    # res = Solution.twoSum(self, nums, target)
