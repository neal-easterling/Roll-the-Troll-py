import re

def color_shift(hex_color, shift_value):
	rrggbb=hex_color[1:]#remove # 
	#and convert to uppercase
	RRGGBB = rrggbb.upper()
	hex_values={
		'A' : 10,
		'B' : 11,
		'C' : 12,
		'D' : 13,
		'E' : 14, 
		'F' : 15,
		'10' : 'A',
		'11' : 'B',
		'12' : 'C',
		'13' : 'D',
		'14' : 'E',
		'15' : 'F'
	}
	conversions=[]
	for char in RRGGBB:
		if re.match('[0-9]', char):
			conversions.append(int(char))
		if re.match('[A-F]', char):
			v=hex_values[char]
			conversions.append(v)
	
	red = conversions[0] * 16 + conversions[1]
	green=conversions[2] * 16 + conversions[3]
	blue=conversions[4]*16 + conversions[5]
	
	red_ad = red + shift_value
	green_ad = green + shift_value
	blue_ad=blue + shift_value
	validates=[red_ad, green_ad, blue_ad]
	new_colors=[]
	for val in validates:
		if val < 0:
			new_color=0
		elif red_ad > 255:
			new_color= 255
		else:
			new_color=val
		new_colors.append(new_color)
	hexes=[]
	for color in new_colors:
		c1= color // 16
		c2=color%16
		hexes.append(c1)
		hexes.append(c2)
	new_hex='#'
	for hex in hexes:
			if hex <= 9:
				new_hex += str(hex)
			if hex > 9: 
				new_hex += hex_values[str(hex)]
	
	return new_hex
	
	