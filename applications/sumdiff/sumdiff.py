"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 20))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

# q = (1, 3, 4, 7, 12)
# f(x) = x * 4 + 6
# f(q) = [10, 18, 22, 34, 54]
# ```
# f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
# f(1) + f(4) = f(12) - f(4)    10 + 22 = 54 - 22
# f(4) + f(1) = f(12) - f(4)    22 + 10 = 54 - 22
# f(1) + f(7) = f(12) - f(1)    10 + 34 = 54 - 10
# f(4) + f(4) = f(12) - f(1)    22 + 22 = 54 - 10
# f(7) + f(1) = f(12) - f(1)    34 + 10 = 54 - 10
# f(3) + f(3) = f(12) - f(3)    18 + 18 = 54 - 18

def sumdiff(nums):
    # init nums as list to for sets
    nums = list(nums)
    # init dict for f(a) + f(b)
    sums = {}
    # init dict for f(c) - f(d)
    diffs = {}

    # iterate through num list
    for i in range(len(nums)):
        for j in range(len(nums)):
            # calc all possible sums
            sums_result = f(nums[i]) + f(nums[j])
            sums_index = (nums[i], nums[j])
            sums[sums_index] = sums_result
            # print(sums_result)
            # print(sums)

            # calc all possile differences
            diffs_index = f(nums[i]) - f(nums[j])
            diffs_result = (nums[i], nums[j])
            # print(diffs_index)
            # print(diffs)

            # check if calculated diff is in diffs
            if diffs_index not in diffs:
                # insert key value into diffs
                diffs.setdefault(diffs_index, [diffs_result])
            else:
                # add value to diffs
                diffs[diffs_index].append(diffs_result)

    # match values in sums to values in diffs
    for (key, value) in sums.items():
        # print(sums.items())
        if value in diffs:
            for i in diffs[value]:
                print(f"f({key[0]}) + f({key[1]}) = f({i[0]}) - f({i[1]})\n     {f(key[0])} + {f(key[1])} = {f(i[0])} - {f(i[1])}")
   
    
sumdiff(q)
