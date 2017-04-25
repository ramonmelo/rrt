#!/usr/bin/env python

import random, math
from math import sqrt,cos,sin,atan2

import numpy as np
from scipy.misc import comb

EPSILON = 7.0

def dist(p1,p2):
	return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def step_from_to(p1,p2):
	if dist(p1,p2) < EPSILON:
		return p2
	else:
		theta = atan2(p2[1]-p1[1],p2[0]-p1[0])
		return p1[0] + EPSILON*cos(theta), p1[1] + EPSILON*sin(theta)

def bernstein_poly(i, n, t):
    """
     The Bernstein polynomial of n, i as a function of t
    """

    return comb(n, i) * ( t**(n-i) ) * (1 - t)**i

def bezier_curve(points, nTimes=1000):
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       points should be a list of lists, or list of tuples
       such as [ [1,1],
                 [2,3],
                 [4,5], ..[Xn, Yn] ]
        nTimes is the number of time steps, defaults to 1000

        See http://processingjs.nihongoresources.com/bezierinfo/
    """

    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, nTimes)

    polynomial_array = np.array([ bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)   ])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return np.column_stack([xvals, yvals]).tolist()

def plan(map_size, init_point, end_point):
	print("planning")

	nodes = []
	nodes.append( init_point )
	reach = False;

	while not reach:
		best_node = None;
		base_node = nodes[-1]

		for i in range(25):
			rand_node = random.random() * float(map_size[0]) , random.random() * float(map_size[1])

			if best_node == None or (dist(rand_node, end_point) < dist(best_node, end_point)):
				best_node = rand_node

		newnode = step_from_to(base_node, best_node)
		nodes.append(newnode)

		if dist(newnode, end_point) < EPSILON:
			nodes.append(end_point)
			reach = True

	return nodes

def bezier_plan(map_size, init_point, end_point):
	return bezier_curve(plan(map_size, init_point, end_point))
