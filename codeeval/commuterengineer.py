import math, itertools

if __name__ == "__main__":
	fileName = "data_COMMUTINGENGINEER.txt"
	dataFile = open(fileName, "r")
	pointIndex = 1
	points = {}
	for line in dataFile:
		dataLine = line.split()
		points.setdefault(int(dataLine[0]), [float(dataLine[-2][1:-2]), float(dataLine[-1][1:-2])])
	dist = {}
	d = 0.0
	for point1 in points:
		for point2 in points:
			if point1 != point2:
				d = math.pow((points[point1][0] - points[point2][0]), 2)
				d += math.pow((points[point1][1] - points[point2][1]), 2)
				d = math.sqrt(d)
				dist.setdefault(point1, {})
				dist[point1].setdefault(point2, d)
				d = 0
	
	pointSet = []
	for i in range(1, len(points) + 1):
		pointSet.append(i)
		
	path = [1]
	startPoint = 1
	endPoint = 0
	d = 10000
	best_dist = 10000
	for i in itertools.permutations(xrange(len(pointSet))):
		if i[0] != 0:
			break
		route = 0
		#print i
		for stop_num in xrange(len(i) - 1):
			#print stop_num, stop_num + 1
			#print i[stop_num], i[stop_num + 1]
			route += dist[i[stop_num] + 1][i[stop_num + 1] + 1]
		if route < best_dist:
			best_route = list(i)
			best_dist = route
	for i in xrange(len(best_route)):
		best_route[i] += 1
	path = best_route


	
	print path
	print dist[5][4], dist[5][6], dist[4][6]
	
	
				
	dataFile.close()
        
