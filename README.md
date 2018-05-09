# Find-Counterfeit-Coin
Find Counterfeit Coin in an array with many elements using less than 10 comparisons
'''
About the program:
	Given X amount of coints, one of them being fake, findCounterF() is a function
	implemented to find the counterfeit coin using 10 or less comparisons. The assumption 
	is that the real coins have a weight of 10 g and the fake coin weights 9 g.

	The challenge of the problem stems from the fact that 100,000,000 could be given. 
	My program will still find the cointerfeit coin in 10 or less comparisons.

USAGE:
	First of all, an array has to be allocated with the desired number of coins.
	ex: arr = 1000*[10] 
	I declared an array, arr with 1000 real coins that weight 10 g.
	
	Next I will replace one of those coins with a fake coin that weights 9 g.
	ex: arr[87] = 9
	I replaced the 87th real coin with a cointerfeit.
	
	Finally, I run findCounterF(inputArray) where inputArray is the array I previously allocated
	ex: findCounterF(arr)
	The program will the output 'Found counterfeit at index: 87'.
	
	
	The cool part is that it takes less than or equal to 10 comparisons to find the fake coin!!!
'''
