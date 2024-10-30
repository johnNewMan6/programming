# Python program for the above approach

# Function to find length of
# longest substring containing '1'
def maxlength(s):
	n = len(s)
	ans = 0;
	for i in range(n):
		
		# Count the number of contiguous 1's
		if (s[i] == '1'):
			count = 1
			j = i + 1
			while(j <= n - 1 and s[j] == '1'):
				count += 1
				j += 1
			ans = max(ans, count)
	return ans

# Driver Code
s = "11101110";
print(maxlength(s))

# This code is contributed by Shivani
