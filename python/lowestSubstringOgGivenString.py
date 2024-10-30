# Python implementation of the above approach
import math

def maxLength(lis, n):
	or_val = 0

	# Calculate OR of each element of string
	for i in range(n):
		or_val |= lis[i]

	count = [0 for i in range(32)]
	for i in range(n):
		for j in range(32):
			if (lis[i] & (1 << j)) != 0:
				count[j] += 1

	ans = 0
	l = 0
	temp_or = 0
	for r in range(n):
		temp_or |= lis[r]

		flag = True
		for i in range(32):
			if (lis[r] & (1 << i)) != 0:
				count[i] -= 1
				if count[i] == 0:
					flag = False

		# If flag = false
		if not flag:
			while l <= r:
				flag1 = True
				for i in range(32):
					if (lis[l] & (1 << i)) != 0:
						count[i] += 1
					if count[i] == 0:
						flag1 = False
				l += 1
				if flag1:
					break

		# If OR of leftover elements and substring elements is equal
		if temp_or == or_val:
			ans = max(ans, r - l + 1)

	# Print the result
	if ans != 0:
		print(ans)
	else:
		print(-1)

# Driver Code
S = "2347"
N = len(S)
A = [int(S[i]) for i in range(N)]

# Function Call
maxLength(A, N)

# This code is contributed by lokeshmvs21.
