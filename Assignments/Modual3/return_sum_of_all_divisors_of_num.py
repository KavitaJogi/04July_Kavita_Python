sum = 0
num=int(input("Enter Number : "))

for i in range(1, num + 1):
    if num % i == 0:
        sum += i
print(f"Sum of divisors of {num}: {sum}")