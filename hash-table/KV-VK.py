# KV-VK = key value - value key
def frequency_sort(s: str) -> str:
    # Этап 1: KV
    count ={}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    # Этап 2: VK
    freq_list = [[] for _ in range(len(s) + 1)]
    for char, freq in count.items():
        freq_list[freq].append(char)
        
    # Этап 3: Собираем результат с конца
    result = []
    for freq in range(len(freq_list) - 1, 0, -1):
        for char in freq_list[freq]:
            result.append(char * freq)
            
    return "".join(result)

print(frequency_sort("abcdeqycxz"))

# Время: O(n)
# Память: O(n)