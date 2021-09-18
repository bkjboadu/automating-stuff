import random
coin = ['T','H']
streak = 0
num_of_streak = 0

for i in range(10000):
    flips = random.choices(coin, k=100)
    for i in range(94):
        for j in range(6):
            if flips[i + j] == flips[i]:
                streak += 1
            else:
                streak = 0

        if streak < 6:
            pass
        else:
            num_of_streak += 1


print(num_of_streak)
print('Chance of streak: %s' % (num_of_streak / 10000))




