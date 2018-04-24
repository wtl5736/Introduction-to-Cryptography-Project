#!/usr/bin/python3

"""
Name: HW5 - Hash Function.py
Author: Wesley Lee
Assignment: HW5 #1
Date: 04-22-2018
"""

from time import *

def hash_function(binary_number):
	hash_list = []
	collision_list = []
	
	binary_number = int(binary_number, 2)
	
	hash_func = (((((8192 * binary_number) / 512) * binary_number))) % 15
	
	return hash_func
	
def main():
	startTime = time()
	
	hash_list = []
	collision_list = []
	for x in range(0, 256):
		bin_num = bin(x)[2:].zfill(16)
		hash_func = hash_function(bin_num)
		
		#print("#" + str(x) + "\t", hash_func, "\t->\t", bin(hash_func)[2:].zfill(16))
		#print(hash_func)
		if hash_func in hash_list:
				collision_list.append(hash_func)
		else:
			hash_list.append(hash_func)
	
	endTime = time()
	timeTaken = '%f' % (endTime - startTime)
	
	#print()
	#print(collision_list)
	print("\nNumber of Collisions:", len(collision_list), "out of 256 Tests")
	print("Ran Program in:", timeTaken, "seconds...")
	
main()