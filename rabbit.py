##return the product of the numbers on the list
def rabbit(nums):
	if nums == []:
			return 1
	first = nums[0]
	rest = nums[1:]
	return first * rabbit(rest)
nums = [1,2,3]
def condonFactorial(n):
	return rabbit(range(1,n+1)
print rabbit(nums)
