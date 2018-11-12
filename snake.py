def snake(nums):
		if nums ==[]: return 0
		##total the numbers on a list
		first = nums[0]
		rest = nums[1:]
		return first + snake(rest)
nums = [1, 2, 3, 4]
print "snake([1,2,3,4]) = ", snake([1,2,3,4]), "expected: 10"
