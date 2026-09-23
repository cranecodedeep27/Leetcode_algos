# Пересекающиеся окна
def longest_ones_with_flips(nums: list[int], k: int) -> int:
    l = 0
    r = -1
    result = 0
    zeros_count = 0
    # Создаём состояние окна
    while l < len(nums):
        # Расширяем окно пока можем
        while r + 1 < len(nums) and (nums[r + 1] == 1 or zeros_count < k):
            if nums[r + 1] == 0:
                zeros_count += 1
            # Обновляем состояние окна
            r += 1
        # Обновляем результат
        result = max(result, r - l + 1)
        # Сужаем окно слева, обновляя состояние
        if nums[l] == 0:
            zeros_count -= 1
        l += 1
        
    return result

print(longest_ones_with_flips([1, 0, 1, 1, 0, 1, 0, 0, 1], 2))

# Время: O(n)
# Память: O(1)