#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  ipgenerator.py - Generates random IPs/networks for
	CCNA trainees to learn subnetting and binary conversion
	
	Copyright (C) Giorgio Vilardo - 2015
	
	This program is free software: you can redistribute it
	and/or modify it under the terms of the GNU General
	Public License as published by the Free Software
	Foundation, either version 3 of the License, or (at
	your option) any later version. 
	
	This program is distributed in the hope that it will
	be useful, but WITHOUT ANY WARRANTY; without even the
	implied warranty of MERCHANTABILITY or FITNESS FOR A
	PARTICULAR PURPOSE.  See the GNU General Public License
	for more details.
	
	You should have received a copy of the GNU General
	Public License along with this program.  If not, see
	http://www.gnu.org/licenses/	
"""
	
#Imports
from random import randint

#Main menu
def menu():
	print "\n|==== CCNA training IPgen v1.0 ====\n|"
	print "| 1: Decimal to binary conversion"
	print "| 2: Binary to decimal conversion"
	print "| 3: Network range generator"
	print "| Any other choice: quit program"
	print "|__________________________________"
	choice = raw_input("\nChoose the desired exercise [1/2/3]: ")
	if choice == "1":
		dec2bin()
	elif choice == "2":
		bin2dec()
	elif choice == "3":
		netgen()
	else:
		quit("\nQuitting the program.")

#Decimal to binary
def dec2bin():
	oct1 = randint(1, 255)
	oct2 = randint(0, 255)
	oct3 = randint(0, 255)
	oct4 = randint(0, 255)
	print "\nConvert this IP in binary: {}.{}.{}.{}\n".format(oct1, oct2, oct3, oct4)
	sol_dec2bin = raw_input("Press Enter for the solution, any other key for the menu: ")
	if bool(sol_dec2bin) == False:
		print "\n{}.{}.{}.{} in binary is:".format(oct1, oct2, oct3, oct4)
		print "{0:08b}.{0:08b}.{0:08b}.{0:08b}".format(oct1, oct2, oct3, oct4)
		menu()
	else:
		menu()

#Binary to decimal
def bin2dec():
	oct1 = randint(1, 255)
	oct2 = randint(0, 255)
	oct3 = randint(0, 255)
	oct4 = randint(0, 255)
	print "\nConvert this IP in decimal: {0:08b}.{0:08b}.{0:08b}.{0:08b}\n".format(oct1, oct2, oct3, oct4)
	sol_bin2dec = raw_input("Press Enter for the solution, any other key for the menu: ")
	if bool(sol_bin2dec) == False:
		print "{0:08b}.{0:08b}.{0:08b}.{0:08b}\n".format(oct1, oct2, oct3, oct4)
		print "{}.{}.{}.{}".format(oct1, oct2, oct3, oct4)
		menu()
	else:
		menu()

def netgen():
	oct1 = randint(1, 255)
	oct2 = randint(0, 255)
	oct3 = randint(0, 255)
	oct4 = randint(0, 255)
	bits = 0
	sm = randint(1, 30)
	print "Calculate network-address, broadcast-address and range of this subnet:"
	for i in xrange(32-sm,32):
		bits |= (1 << i)
	print "{}.{}.{}.{} {}.{}.{}.{}".format(oct1, oct2, oct3, oct4, (bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))
	solnetgen = raw_input("Press any key when finished: ")
	if bool(solnetgen) == False:
		menu()
	else:
		menu()

menu()
