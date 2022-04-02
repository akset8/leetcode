# five LC everyday 
# maybe start with some python book also
# and an ML book 

class Solution:
	def twoSum(self, nums:List[int], target:int) -> List[int]:
		
		return self.twoSum_n2(nums, target)
		#return self.twoSum_nlgn(nums, target)
		#return self.twoSum_n(nums, target)

	
	def twoSum_n2(self, nums:List[int], target:int) -> List[int]:
		# two dependent loops 
		for num_i in range(len(nums)):
			for num_j in range(num_i+1, len(nums)):
				if nums[num_i] + nums[num_j] == target:
					return [num_i, num_j]

	def twoSum_nlgn(self, nums:List[int], target:int) -> List[int]:
		# two pointers 
		nums = nums.sort()
		i = 0, j = len(nums) - 1 
		
		while ( i < j):
			if ( nums[i] + nums[j]) == target:
				out =  [i,j]
				break
			elif ( nums[i] + nums[j]) < target:
				i = i + 1 
			else:
				j = j - 1
		
		return out 


	def twoSum_hash(self, nums:List[int], target:int) -> List[int]:
		# hashing
		# edge case bhi aayega what to do about the edge case
		
		nums_hash = {}
		for num_i in range(len(nums)):
			nums_hash[nums[num_i]] = num_i

		for num in nums:
			residual = target - num
			if residual in nums_hash:
				return []

		# some pretty wierd edge case here on overall 









