# Work In Progress
# Calculator for STAT 2507

import statistics
import math

# Read data from a file (each value seperated by a comma)
filein = open('data.txt', 'r')
data = filein.read().split(',')
data = [int(n.strip(' ')) for n in data]

print("Given data: " + str(data))
filein.close()

# Sum and size of data
data_sum = 0
size = 0
for n in data:
	data_sum += n
	size += 1


# Mean
def get_mean():
	mean = data_sum / size
	return mean


# Median
def get_median():
	data.sort()
	median_rank = (size + 1)/2
	median_val = statistics.median(data)
	median = [median_rank, median_val] #rank at m[0], val at m[1]
	return median


# Mode
def get_mode():
	mode = statistics.mode(data)
	return mode


# Max
def get_max():
	data_max = max(data)
	return data_max

# Min
def get_min():
	data_min = min(data)
	return data_min


# Population Variance:
def get_pop_variance():
	pop_variance = statistics.pvariance(data, get_mean())
	return pop_variance


# Sample Variance:
def get_sam_variance():
	sam_variance = statistics.variance(data, get_mean())
	return sam_variance


# Population Standard Deviation
def get_pop_sd():
	pop_sd = statistics.pstdev(data)
	return pop_sd


# Sample Standard Deviation
def get_sam_sd():
	sam_sd = statistics.stdev(data)
	return sam_sd


# Sample z-score
def get_zscore(x):
	z_score = ((x - get_mean()) / get_sam_sd())
	return z_score


# Percentiles
def get_percentile(p):
	percentile_pos = math.ceil(((p * size) / 100))
	percentile = data[percentile_pos - 1]
	return percentile


# Interquartile Range
def get_iqr():
	q3 = get_percentile(75)
	q1 = get_percentile(25)
	iqr = (q3 - q1)
	return iqr

# Five Number Summary
def get_five_num_summary():
	d_min = get_min()
	q1 = get_percentile(25)
	median = get_median()
	q3 = get_percentile(75)
	d_max = get_max()
	summary_nums = [d_min, q1, median, q3, d_max]
	summary = "Minimum: " + str(d_min) + ", Q1: " + str(q1) + ", Median: " + str(median[1]) + ", Q3: " + str(q3) + ", Maximum: " + str(d_max)
	return summary


# Combinations
def get_combination(n, r):
	f = math.factorial
	return f(n) // f(r) //  f(n-r)


# Permutations
def get_permutation(n, r):
	f = math.factorial
	return f(n) // f(n-r)


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


