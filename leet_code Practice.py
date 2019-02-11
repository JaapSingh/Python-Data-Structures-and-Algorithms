# given a contiguous sequence of numners in which each number repeats thrice, find the missing number
# 	e.g. 11122333: 2
def soln(my_string):
	blocks = map(''.join, zip(*[iter(my_string)]*3))
	if len(blocks)*3 != len(my_string): return my_string[-1]
	for block in blocks:
		if (block[1] != block[2]):
			return block[1]
	return "all match!"


print(soln("111222333444"))

# find the longest palindromic substring in s

# The centre of a palindrome must be 2n-1, where it is either in between or not. 
# In either case, you pick your centre, then move outwards

def center_expand(s, left, right, length):
	max_length = 0
	curr_length = 0
	return_string = ""
	while(left>=0 and right < length):
			if s[left] != s[right]:
				break
			curr_length += 1
			if curr_length > max_length:
				max_length = curr_length
				return_string = s[left:right+1]
			left-=1
			right+=1
	return return_string

# example: "babaaabaad"
def max_substring(s):
	length = len(s)
	return_string = ""
	for i in range(0, length):
		# check for even case
		return_string_even = center_expand(s, i, i, length)
		return_string_odd = center_expand(s, i, i+1, length)
		if len(return_string_even) > len(return_string_odd) and len(return_string_even) > len(return_string):
			return_string = return_string_even
		elif len(return_string_even) < len(return_string_odd) and len(return_string_odd) > len(return_string):
			return_string = return_string_odd
	return return_string

print(max_substring("asaaasb"))


# phone number to name:
#	iterate through your beginnings
#		recursively call letter_converter, on the rest of the string
num_to_letter = {'2': "abc", '3':"def", '4':"ghi", '5':"jki", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
def letter_converter(number):
	# if number == 0:
	# 	return ""
	# if number >=9 or number <=1:
	# 	raise ValueError("invalid input")

	return_array = [""]
	for digit in number:
		letters = num_to_letter[digit]
		new_result = []
		for char in letters:
			for string in return_array:
				new_result.append(string+char)
		return_array = new_result
	return return_array

print(letter_converter("238"))


# n sets of paranthesis, how many way to order it?
# generally will follow a few given patterns:
#	n = 4: 
#		(((()))), (())(()), ()()()(), ((()))(), (())()(), ()((())), ()()(())

# brute force:
#		generate all 2^2^n possibilities, and then check each if they are valid

# before making a new possibility, check if you have any open paranthesis left from global, 
#	and if you have a matching opening brace for each closing
ans = []
def backtrack(N, S, left, right):
	if len(S) == 2 * N:
		ans.append(S)
		return
	if left<N:
		backtrack(N, S+"(", left + 1, right)
	if right < left:
		backtrack(N, S+")", left, right + 1)

backtrack(3, '', 0, 0)
print(ans)


# return elements in a spiral pattern... interesting! I smell recursion!!
# basically, we iterate through the outer layer of the matrix, then recurse on the next layer
# let's start with our recursive function:

def outer_layer(matrix, start , end, spiral):
	# we will want to decrement end and increment start for the columns. 
	# rows will be decremented by recursive call on smaller matrix
	if matrix == []:
		return spiral
	#adds first row
	for column in range(start, end-1):
		spiral.append(matrix[0][column])
	#adds outer column
	for row in matrix:
		spiral.append(row[end-1])
	if len(matrix) == 1: return spiral
	#adds bottom row
	for column in reversed(range(start, end)[:-1]):
		spiral.append(matrix[-1][column])
	#adds inner column
	for row in reversed(matrix[1:-1]):
		spiral.append(row[start])

	outer_layer(matrix[1:-1], start+1, end-1, spiral)
	return spiral

def soln2(matrix):
	end = len(matrix[0])
	return outer_layer(matrix, 0, end, [])

my_matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

second_matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
#print(my_matrix[1:-1])
#print(soln(second_matrix))


class Solution(object):
	def spiralOrder(self, matrix):
		def outer_layer(matrix, start , end, spiral):
			# if the matrix is empty, or our start and end have overlapped
			if matrix == [] or start == end:
				return spiral

			#adds first row from start+1 to end-1
			for column in range(start, end-1):
				spiral.append(matrix[0][column])
			#adds outer column
			for row in matrix:
				spiral.append(row[end-1])

			# if our matrix has m=1, do not print remainder
			if len(matrix) == 1 or start == end-1: return spiral
			#adds bottom row from 
			for column in reversed(range(start+1, end-1)):
				spiral.append(matrix[-1][column])
			#adds inner column
			for row in reversed(matrix[1:]):
				spiral.append(row[start])

			outer_layer(matrix[1:-1], start+1, end-1, spiral)
			return spiral

		if matrix == []: 
			return []
		return outer_layer(matrix, 0, len(matrix[0]), [])

my_soln = Solution()
# print(my_soln.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
# print(my_soln.spiralOrder([[2,5],[8,4],[0,-1]]))

# next permutation
# lets see... lexicographical order required.
#	first, we have to find the next number that is larger than the previous. this will bubble forward
# if none exits, then we know to cycle back a reordering to iniial level, which is just reversed string
# [1, 4, 5, 9, 2, 3]


class Solution2(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        min_so_far = i
        while (i>=0 and nums[i + 1] <= nums[i]):
        	i-=1
        if (i>=0):
        	j = len(nums)-1
        	while (j>=0 and nums[j] <= nums[i]):
        		j-=1
        	nums[j], nums[i] = nums[i], nums[j]
        nums[i+1:] = nums[i+1:][::-1]

my_soln = Solution2()
my_array= [1, 3, 2]
my_soln.nextPermutation(my_array)
print(my_array)

class Solution3(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = False
        neg_dividend = False
        if divisor < 0:
        	negative = True
        	divisor = 0-divisor
        if dividend < 0:
        	dividend = 0-dividend
        	neg_dividend = True
        if divisor < 0:
        	negative = True
        	divisor = 0-divisor
        quotient= 0
        while (dividend >= divisor):
        	dividend -= divisor
        	quotient += 1
        if negative or neg_dividend:
        	quotient = 0 - quotient
        if negative and neg_dividend:
        	quotient = 0 - quotient
        return quotient
my_soln = Solution3()
print(my_soln.divide(-2147483648, -1))