# Work In Progress
# Calculator for STAT 2507

import statistics
import math
from funcs import *

print("Given data: " + str(data))
filein.close()

# Dict of options
options = { 
		'0' : get_mean,
		'1' : get_median,
		'2' : get_mode,
		'3' : get_pop_variance,
		'4' : get_sam_variance,
		'5' : get_pop_sd,
		'6' : get_sam_sd,
		'7' : get_zscore,
		'8' : get_percentile,
		'9' : get_iqr,
		'10': get_five_num_summary,
		'11': get_combination,
		'12': get_permutation	
		  }

names = ['Mean', 'Median', 'Mode', 'Population Variance', 'Sample Variance', 
		 'Population Standard Deviation', 'Sample Standard Deviation', 
		 'Sample z-score', 'Percentile', 'Interquartile Range', 'Five-number Summary', "Combination", "Permutation"]

def main():

	print('\n' + '*'*4 + " Welcome to the Statistics Calculator. " + '*'*4)

	for a, b in enumerate(names): # List options as a numbered list from 0 to 10
		print('{}:- "{}"'.format(a, b))

	while True: # Loop for input and output

		try:
			user_choice = input("\nEnter option (Enter any non-integer to exit): ") # Returns ValueError if non-int

			if user_choice == '1': # Median
				print("---> The Median Rank is: " + str((options[user_choice]())[0]) + " and the Median Value is " + str((options[user_choice]())[1]))
			
			elif user_choice == '11' or user_choice == '12': # Combinations and Permutations
				n = int(input("Enter n: "))
				r = int(input("Enter r: "))
				if user_choice == '11': # Combination
					print("---> The " + str(names[int(user_choice)]) + " of " + str(n) + " and " + str(r) + " is: " + str(options[user_choice](n, r)))
				elif user_choice == '12': # Permutation
					print("---> The " + str(names[int(user_choice)]) + " of " + str(n) + " and " + str(r) + " is: " + str(options[user_choice](n, r)))

			elif user_choice == '7' or user_choice == '8': # Z-score and Percentiles
				arg1 = float(input("Enter argument: "))

				if user_choice == '7': # Z-score
					print("---> The " + str(names[int(user_choice)]) + " is: " + str(options[user_choice](arg1)))
		
				elif user_choice == '8': # Percentile
					print("---> The " + str(int(arg1)) + "th " + str(names[int(user_choice)]) + " is: " + str(options[user_choice](arg1)))

			else: # All other operations
				print("---> The " + str(names[int(user_choice)]) + " is: " + str(options[user_choice]()))

		except ValueError: # Exits loop as per user's request to exit
			break

		except IndexError: # Retries
			print("Error: Invalid option. Try again.")


if __name__ == "__main__":
	main()


