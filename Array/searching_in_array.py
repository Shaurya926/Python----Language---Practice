array = [23, 45, 12, 67, 34, 89, 10]
key = 34
for i in range(len(array)):
    if array[i] == key:
        print(f"Element {key} found at index {i}")
        break