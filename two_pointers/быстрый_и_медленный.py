def move_zeros(nums: list[int]) -> list[int]:
    # Инициализация
    slow = 0
    fast = 0
    # Цикл движение двух указателей
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1
    # Возвращаем наш список с нулями в конце
    return nums

print(move_zeros([1, 0, 5, 6, 0, 0, 12, 1]))

# Время: O(n)
#  Память: O(1)