# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
"""

import random
import math
import Image
im = Image.new("RGB",(350,350))


def build_random_function(min_depth, max_depth):
	"""
	# choose one number between min_depth and max_depth randomly, make that depth of function conposed of product, sin_pi, cos_pi randomly.
	# input : min_depth(integer), max_depth(integer)
	# output : random function(nested list)
	"""
	function = [] # put random functions in here
	depth = random.randint(min_depth,max_depth)
	x = depth
	# functions are chosen in below two lists 
	building_block = [["prod",'a','b'],["cos_pi",'a'],["sin_pi",'a']] 
	simple_block = [['x'],['y']] 

	if x == 1:
		a = random.choice(simple_block) # depth = 1 so choose x or y
		function.append(a)
		x = x-1 # to return function when x=0
		return a
		
	if x > 1:
		a = random.choice(building_block) # choose prod or sin or cos
		function.append(a)
		if a == building_block[0]: # if a = "prod"
			a[1] = build_random_function(x-1,x-1) # use recursion
			a[2] = build_random_function(x-1,x-1) # length of prod list is 3 so need 2 argument
			return a
		else: # if a = "cos_pi" of "sin_pi"
			a[1] = build_random_function(x-1,x-1) # use recursion / need only 1 argument
			return a

	if x==0: # making random function finish so return function
		return function



def evaluate_random_function(f,x,y):
	"""
	# calcuate function f using argument x and y.
	# input : f (nested list), x(float), y(float)
	# output : calculated value (float)
	"""
	x1 = float(x)
	y1 = float(y)
	a = f 
	if len(a)==3: # if a[0]="prod"
		if len(a[1])>1: # if a[1] is nested list
			one = float(evaluate_random_function(a[1],x1,y1)) # use recursion
			two = float(evaluate_random_function(a[2],x1,y1))
			return one*two 
		if len(a[1])==1: # if a[1] is ['x'] or ['y']
			if a[1]==['x'] and a[2]==['x']:
				return x1*x1
			elif a[1]==['x'] and a[2]==['y']:
				return x1*y1
			elif a[1]==['y'] and a[2]==['x']:
				return x1*y1
			else:
				return y1*y1

	if len(a)==2: # if a[0] = "sin_pi" or "cos_pi"
		if len(a[1]) > 1: # if a[1] is nested list
			one = float(evaluate_random_function(a[1],x1,y1))
			if a[0]=='sin_pi':
				return float(math.sin(math.pi*one))
			else:
				return float(math.cos(math.pi*float(one)))
		if len(a[1])==1: # if a[1] is ['x'] or ['y']
			if a[0]=='sin_pi' and a[1]==['x']:
				return float(math.sin(math.pi*x1))
			elif a[0]=='sin_pi' and a[1]==['y']:
				return float(math.sin(math.pi*y1))
			elif a[0]=='cos_pi' and a[1]==['x']:
				return float(math.cos(math.pi*x1))
			else:
				return float(math.cos(math.pi*y1))
	if len(a)==1: # if a = ['x'] or ['y']
		if a[0]=='x':
			return x1
		else:
			return y1


def remap_interval(val,input_interval_start,input_interval_end,output_interval_start,output_interval_end):
	"""
	# maps the input value that is in the inverval [input_interval_start, input_interval_end] to the counterpart in output interval [output_interval_start, output_interval_end].
	# input : val(number), input_interval_start(number), input_interval_end(number), output_interval_start(number), output_interval_end(number)
	# output : corresponding value of input value
	"""
	a = float(val)
	b = float(input_interval_start)
	c= float(input_interval_end)
	d = float(output_interval_start)
	e = float(output_interval_end)
	# (output_interval_end - output_interval_start) * (value - input_interval_start) / (input_interval_end - input_interval_start) + output_interval_start
	# shape of y = ax + b
	f = float((e - d) * (val - b) / (c - b) + d)
	return f




def drawing(min_depth,max_depth,x,y):
	"""
	# make 3 random function for red, green and blue, put x axis value and y axis value in each rgb function, put the result to corresponding point in image
	# input : min_depth(integer), max_depth(integer), x(number), y(number)
	# output : image with random rgb value in every pixels
	"""
	R_function = build_random_function(min_depth,max_depth)
	G_function = build_random_function(min_depth,max_depth)
	B_function = build_random_function(min_depth,max_depth)
	im = Image.new("RGB",(x,y)) # make image with x*y size

	for i in range(x):
		for j in range(y): # for every point in the image
			a = remap_interval(i,0,x-1,-1,1) # if x=5 then interval is [0,4]
			b = remap_interval(j,0,y-1,-1,1)
			red_1 = evaluate_random_function(R_function,a,b) # value is between [-1,1]
			red_2 = int(remap_interval(red_1,-1,1,0,255)) # value is an integer between [0,255] which is for red in rgb
			green_1 = evaluate_random_function(G_function,a,b) # value is between [-1,1]
			green_2 = int(remap_interval(green_1,-1,1,0,255)) # value is an integer between [0,255] which is for green in rgb
			blue_1 = evaluate_random_function(B_function,a,b) # value is between [-1,1]
			blue_2 = int(remap_interval(blue_1,-1,1,0,255)) # value is an integer between [0,255] which is for blue in rgb
			
			im.putpixel((i,j),(red_2,green_2,blue_2)) # put rgb value in (i,j)
			
	im.save('soeun_pattern.png') # save image with name 'soeun_pattern'

drawing(4,15,350,350) # execuate function
