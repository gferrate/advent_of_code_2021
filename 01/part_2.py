from input import nums

# Instead, consider sums of a three-measurement sliding window. Again considering the above example:
sum_3_nums = []
for i in range(len(nums)):
    try:
        sum_3_nums.append(nums[i] + nums[i+1] + nums[i+2])
    except IndexError:
        pass

assert len(sum_3_nums) == len(nums) - 2

count = 0
last_num = None
for n in sum_3_nums:
    if last_num is None:
        last_num = n
        continue
    elif n > last_num:
        count += 1
    last_num = n

print(count)