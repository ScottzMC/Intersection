import intersection as intersect

def startProgram():
	try:
		intersectA = [[0,2],[5,10],[13,23],[24,25]]
		intersectB = [[1,5],[8,12],[15,24],[25,26]]
		result = intersect.getIntersection(intersectA, intersectB)

	except (ImportError, IndexError):
		if IndexError:
			print("Wrong Input Parameters")
		elif ImportError:
			print("Error Occurred where module is missing!")
		else:	
			print("Error Occurred")
		exit()

startProgram()