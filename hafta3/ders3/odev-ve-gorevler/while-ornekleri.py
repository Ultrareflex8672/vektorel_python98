i = 1
while i <= 10:
    print(i)
    i += 1

n = int(input("Bir sayı girin: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"{n} sayısının faktöriyeli: {factorial}")

total = 0
while True:
    number = input("Bir sayı girin (çıkmak için 'q' tuşlayın): ")
    if number.lower() == 'q':
        break
    total += int(number)
print(f"Girilen sayıların toplamı: {total}")

i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

n = int(input("Bir sayı girin: "))
i = 2
is_prime = True
while i < n:
    if n % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print(f"{n} sayısı asaldır.")
else:
    print(f"{n} sayısı asal değildir.")