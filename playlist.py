import random

def playlist():
    nums1 = []
    for nums in range(10):
        # Get random list of 10 numbers
        my_nums = random.randint(10, 90)
        nums1.append(my_nums)
        print my_nums


    even = []
    odd = []
    for x in nums1:
      if x % 2 == 0:
          even.append(x)
          print(even)
      else:
          odd.append(x)
          print(odd)


playlist()
