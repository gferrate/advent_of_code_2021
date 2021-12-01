from input import nums

# count the number of times a depth measurement increases from the previous measurement.
count = 0
last_num = None
for n in nums:
    if last_num is None:
        last_num = n
        continue
    elif n > last_num:
        count += 1
    last_num = n

print(count)
