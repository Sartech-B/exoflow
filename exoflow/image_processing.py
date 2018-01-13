def compare_pixel(p1, p2, tolerence):

	r1, g1, b1 = p1
	r2, g2, b2 = p2	

	if(abs(r1-r2)<=tolerence and abs(g1-g2)<=tolerence and abs(b1-b2)<=tolerence):
		return True
	else:
		return False

