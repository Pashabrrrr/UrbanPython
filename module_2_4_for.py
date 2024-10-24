numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
primes.append(numbers[1])

for i in range(2, len(numbers)):
    # print(numbers[i])
    n = numbers[i]
    ost = 0
    for j in range((i - 1), 0, -1):
        # print(numbers[j])
        m = numbers[j]
        if n % m == 0:
            not_primes.append(n)
            ost = ost + 1
            break
    if ost == 0:
        primes.append(n)

print(primes)
print(not_primes)
