

nums = [[val for val in range(num)]for num in range(3)]
for num in nums:
  print(nums)
  for val in num:
    if val < 2:
      print("*",end="")