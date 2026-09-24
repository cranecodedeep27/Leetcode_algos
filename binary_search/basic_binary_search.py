# Базовый бинарный поиск
def search_last(nums: list[int], target: int) -> int:
    # Ищем последний хороший l = 0, r = len(nums), ответ в указателе l
    l, r = 0, len(nums)
    while r - l > 1:
        m = l + (r - l) // 2
        if nums[m] <= target: # ищем первый плохой l = -1, r = len(nums) -1
            l = m             # ответ в указателе r
        else:
            r = m
    
    return l if nums[l] == target else -1

print(search_last([1, 2, 2, 2, 5, 8], 2))

# Время: O(log(n))
# Память: O(1)  