#!/usr/bin/python3
#!/usr/bin/python3

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    print(sum_numbers([1, 2, 3, 4, 5]))
