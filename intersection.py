# Intersection Module

def getIntersection(firstList, secondList):
	try:
		# First and Second Pointers for the Argument
	    firstPointer = 0
	    secondPointer = 0
	    
	    # Calculating the length of the List
	    firstLength = len(firstList)
	    secondLength = len(secondList)
	 	
	    # Looping through
	    while firstPointer < firstLength and secondPointer < secondLength:
	         
	        # Start bound for intersecting segment
	        start = max(firstList[firstPointer][0], secondList[secondPointer][0])
	         
	        # End bound for intersecting segment
	        end = min(firstList[firstPointer][1], secondList[secondPointer][1])
	         
	        # Return the Result
	        if start <= end:
	            print('[',start,',',end,']')
	        
	        # Removing the smallest endpoint
	        if firstList[firstPointer][1] < secondList[secondPointer][1]:
	            firstPointer += 1
	        else:
	            secondPointer += 1
	except TypeError:
		print("Error Found while Intersecting")
		exit()