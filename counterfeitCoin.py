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
	
	
	The cool part is that it took less than or equal to 10 comparisons to find the fake coin!!!
'''

def findCounterF(coinArray):
    sliceFactor = int(len(coinArray)/2)
    firstIndex = 0
    secondIndex = sliceFactor-1
    #print('Slice Factor ', sliceFactor)
    #print('Second Index ', secondIndex )
    #print('First Index ', firstIndex )
    #print('--------------------------------')
    found = 0
    for i in range(int(len(coinArray)/(len(coinArray)/10))):
        #Base Case
        if arr[firstIndex] == 9:
            print('Found counterfeit at index: ', firstIndex)
            found = 1
            break;
        if arr[secondIndex] == 9:
            print('Found counterfeit at index: ', secondIndex)
            found = 1
            break;
        #Update Vars until fake coin is found
        if sum(arr[firstIndex:secondIndex])%10 == 0:
            firstIndex = firstIndex + sliceFactor
            sliceFactor = int(sliceFactor/2)+1
            secondIndex = secondIndex + sliceFactor
            #print('Slice Factor ', sliceFactor)
            #print('Second Index ', secondIndex )
            #print('First Index ', firstIndex )
            #print('i ', i )
            #print('--------------------------------')
        else:
            firstIndex = firstIndex
            secondIndex = firstIndex + int(sliceFactor/2)
            sliceFactor = int(sliceFactor/2)+1
            #print('Slice Factor ', sliceFactor)
            #print('Second Index ', secondIndex )
            #print('First Index ', firstIndex )
            #print('i ', i )
            #print('--------------------------------')

    if found == 0:
        print('NOT FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

#For loop to test if findCounterF() finds the fake
#coin no matter where it is located in the array.
'''
arr = 1000*[10]
for i in range(len(arr)):
    arr = len(arr)*[10]
    arr[i] = 9
    findCounterF(arr)
'''
