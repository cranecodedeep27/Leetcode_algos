# Окно фиксированной длины
def k_elements_max_sum(nums: list[int], k: int) -> int:
    # Накопление
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
        
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        # формула перехода к следующему окну
        l = i - k
        window_sum = window_sum + nums[i] - nums[l]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

print(k_elements_max_sum([1, 5, 2, 4, 6, 9], 3))

#  Время: O(n)
#  Память: O(1)