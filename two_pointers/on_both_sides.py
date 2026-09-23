def two_sum(nums: list[int], target: int) -> list[int]:
    # Инициализация
    l = 0
    r = len(nums) - 1
    # рабочий цикл while
    while l < r:
        # Логика движения указателей
        curr_sum = nums[l] + nums[r]
        
        if curr_sum == target:
            return [l, r]
        elif curr_sum > target:
            r -= 1
        else:
            l += 1
    return [-1, -1]

print(two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

#  Время O(n)
#  Память O(1)