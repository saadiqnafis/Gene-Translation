"""
File: translate_dna.py
----------------
This program translates a strand of DNA to create its matching base pair.
A becomes T, T becomes A, G becomes C, and C becomes G.
"""


import os
import sys
# The line below imports TextGrid for use here
from TextGrid import TextGrid

def translate_DNA(filename):
	"""
	This function takes a DNA TextGrid and converts each nucleotide to its
	matching base pair.

	Input:
		filename (string): name of TextGrid to be read in

	Returns:
		TextGrid of DNA with all its base pairs changed
	"""

	dna = TextGrid(filename)
	width = dna.width
	height = dna.height
	
	# Your code here!
	for cell in dna:
			
			
		if cell.value == 'A':
			cell.value = 'T'
				
		elif cell.value == 'T':
			cell.value = 'A'
				
		elif cell.value == 'C':
			cell.value = 'G'
				
		elif cell.value == 'G':
			cell.value = 'C'
				

	return dna

#def complementary combination:
	#if cell.value == A

def main():
	"""
	This program tests your translate_DNA function by displaying
	the original DNA grid as well as the resulting DNA grid
	from your translate_DNA function.
	"""
	print('Original sequence:')
	original_dna = TextGrid('COVID19_firstsequence.txt')
	print(original_dna)
	print()
	print("Translated sequence:")
	translated_dna = translate_DNA('COVID19_firstsequence.txt')
	print(translated_dna)


if __name__ == '__main__':
	main()