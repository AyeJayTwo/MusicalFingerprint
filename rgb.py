def rgb_hsv(r, g, b):
	r2 = r/255.0
	g2 = g/255.0
	b2 = b/255.0
	c_max = max(r2, g2, b2)
	c_min = min(r2, g2, b2)
	delta = c_max - c_min

	v = c_max
	s = 0
	if c_max == 0:
		s = 0
	else:
		s = delta/c_max

	if c_max == r2:
		h = 60*((g2-b2)/delta%6)
	elif c_max == g2:
		h = 60*((b2-r2)/delta + 2)
	elif c_max == b2:
		h = 60*((r2-g2)/delta + 4)

	return h,s,v

def hsv_rgb(h,s,v):
	c = v * s
	h = h/60
	x = c * (1 - abs(h%2 - 1))
	m = v - c

	if h < 1:
		return (c+m,x+m,m)
	elif h < 2:
		return (x+m, c+m, m)
	elif h < 3:
		return (m, c+m, x+m)
	elif h < 4:
		return (m, x+m, c+m)
	elif h < 5:
		return (x+m, m, c+m)
	elif h < 6:
		return (c+m, m, x+m)

	#return r,g,b