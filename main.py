'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
nput: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def moveZeroes(nums): # 0 (n)
  #loop through the array nums
  
  placeHolder = [] # 0 (1)
  pointer = 0 # 0 (1)

  for e in range(len(nums)): # 0 (n)
    if nums[pointer] != 0: # 0 (1)
      temp = nums.pop(pointer) # 0 (1)
      placeHolder.append(temp) # 0 (1)
      
    else:
      pointer +=1 # 0 (1)
  
      
  nums=(placeHolder + nums) # 0 (n)
  return nums # 0 (1)

print(moveZeroes([0,0,1,34,234,2133,0,9,765]))