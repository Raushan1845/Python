# Print Armstrong numbers from 1 to 1000

for num in range(1, 1001):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num)
