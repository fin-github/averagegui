def average(nums:list):
    try: return sum(nums) / len(nums)
    except ZeroDivisionError: return 0