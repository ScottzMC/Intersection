import pytest 
import intersection as intersect

class TestIntersection:
	# Test the Intersection Method works
	
	intersectA = [[0,2]]
	intersectB = [[1,5]]
	expectedResultAB = [1, 2]

	intersectC = [[5,10]]
	intersectD = [[8,12]]
	expectedResultCD = [8, 10]

	intersectE = [[13,23]]
	intersectF = [[15,24]]
	expectedResultEF = [15, 23]

	intersectG = [[24,25]]
	intersectH = [[25,26]]
	expectedResultGH = [25, 25]

	intersectI = [[1,3], [5,9]]
	intersectJ = []
	expectedResultIJ = []

	intersectK = [[1,7]]
	intersectL = [[3,10]]
	expectedResultKL = [3,7]

	intersectM = [[0,2],[5,10],[13,23],[24,25]]
	intersectN = [[1,5],[8,12],[15,24],[25,26]]
	expectedResultMN = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

	try:
		def test_get_intersection_AB(self):
		    intersect.getIntersection(self.intersectA, self.intersectB) == self.expectedResultAB

		def test_get_intersection_CD(self):
		   	intersect.getIntersection(self.intersectC, self.intersectD) == self.expectedResultCD

		def test_get_intersection_EF(self):
		   	intersect.getIntersection(self.intersectE, self.intersectF) == self.expectedResultEF

		def test_get_intersection_GH(self):
		   	intersect.getIntersection(self.intersectG, self.intersectH) == self.expectedResultGH

		def test_get_intersection_IJ(self):
		   	intersect.getIntersection(self.intersectI, self.intersectJ) == self.expectedResultIJ

		def test_get_intersection_KL(self):
		   	intersect.getIntersection(self.intersectK, self.intersectL) == self.expectedResultKL

		def test_get_intersection_MN(self):
		   	intersect.getIntersection(self.intersectM, self.intersectN) == self.expectedResultMN

	except NameError:
		print("Error Found")
		exit()

if __name__ == '__main__':
    pytest.main()