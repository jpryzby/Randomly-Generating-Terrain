# Randomly-Generating-Terrain

Made by: Jon Pryzby
Last Updated: 3/19/2021
Primary language: Python

###############################################################
###                                                         ###
###  Try this code at https://trinket.io/python/3b2f2a99b9  ###
###                                                         ###
###############################################################

A program that uses perlin noise to generate an infinite terrain.

At runtime, a 2d map is created using perlin noise to get an array of random values, where each value is similar to its neighbor. 

Once per game tick, a grid is drawn where each point is raised or lowered by its corresponding value in the perlin noise map. The grid moves one step towards the viewer each time.