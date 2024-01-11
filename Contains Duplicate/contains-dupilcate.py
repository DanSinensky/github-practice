def containsDuplicate(self, nums: list[int]) -> bool:
    result = []

    nums_set = set(nums)
    if len(nums) == len(nums_set):
        return False
    return True