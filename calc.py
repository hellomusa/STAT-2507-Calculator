# Calculator to use for (basic) statistics 
# Formulas to include:
# 1. Arithmetic Mean/Average
# 2. Median (and its rank)
# 3. Mode
# 4. Population Variance
# 5. Sample Variance
# 6. Population Standard Deviation
# 7. Sample Standard Deviation
# 8. Sample z-score
# 9. Percentiles
# 10. Interquartile Range
# 11. Minimum and maximum
# 12. Five-number summary (min, q1, median, q3, max)
# 13. Correlation Coefficient
# 14. The Regression Line (y = a + bx)
# 15. Probability? \\

import statistics
import math

### Read data from a file (each value seperated by a comma)
filein = open('data.txt', 'r')
data = filein.read().split(',')
data = [int(n.strip(' ')) for n in data]

print("Given data: " + str(data))
filein.close()

## Sum, size of data
data_sum = 0
size = 0
for n in data:
	data_sum += n
	size += 1


### Mean
def get_mean():
	mean = data_sum / size
	return mean


### Median
def get_median():
	data.sort()
	median_rank = (size + 1)/2
	median_val = statistics.median(data)
	median = [median_rank, median_val] #rank at m[0], val at m[1]
	return median


### Mode
def get_mode():
	mode = statistics.mode(data)
	return mode


## Max
def get_max():
	data_max = max(data)
	return data_max

## Min
def get_min():
	data_min = min(data)
	return data_min


### Population Variance:
def get_pop_variance():
	pop_variance = statistics.pvariance(data, get_mean())
	return pop_variance


## Sample Variance:
def get_sam_variance():
	sam_variance = statistics.variance(data, get_mean())
	return sam_variance


## Population Standard Deviation
def get_pop_sd():
	pop_sd = statistics.pstdev(data)
	return pop_sd


## Sample Standard Deviation
def get_sam_sd():
	sam_sd = statistics.stdev(data)
	return sam_sd


## Sample z-score
def get_zscore(x):
	z_score = ((x - get_mean()) / get_sam_sd())
	return z_score


## Percentiles
def get_percentile(p):
	percentile_pos = math.ceil(((p * size) / 100))
	percentile = data[percentile_pos - 1]
	return percentile


# ## Interquartile Range
def get_iqr():
	q3 = get_percentile(75)
	q1 = get_percentile(25)
	iqr = (q3 - q1)
	return iqr

def five_num_summary():
	d_min = get_min()
	q1 = get_percentile(25)
	median = get_median()
	q3 = get_percentile(75)
	d_max = get_max()

	summary_nums = [d_min, q1, median, q3, d_max]
	summary = "Minimum: " + str(d_min) + ", Q1: " + str(q1) + ", Median: " + str(median[1]) + ", Q3: " + str(q3) + ", Maximum: " + str(d_max)
	return summary


# # Dict of options
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
		'10': five_num_summary
		  }

names = ['Mean', 'Median', 'Mode', 'Population Variance', 'Sample Variance', 
		 'Population Standard Deviation', 'Sample Standard Deviation', 
		 'Sample z-score', 'Percentile', 'Interquartile Range', 'Five-number Summary']

def main():

	print('\n' + '*'*4 + " Welcome to the Statistics Calculator. " + '*'*4)
	# List options as a numbered list from 0 to 10
	for a, b in enumerate(names):
		print('{}:- "{}"'.format(a, b))

	while True: 

		try:
			user_choice = input("\nEnter option (Enter any non-integer to exit): ")
			# Ensures rank and value for median
			if user_choice == '1':
				print("---> The Median Rank is: " + str((options[user_choice]())[0]) + " and the Median Value is " + str((options[user_choice]())[1]))
			# Ensures argument for z-score and percentile calculations.
			elif user_choice == '7' or user_choice == '8':
				arg1 = float(input("Enter argument: "))
				if user_choice == '7':
					print("---> The " + str(names[int(user_choice)]) + " is: " + str(options[user_choice](arg1)))
				elif user_choice == '8':
					print("---> The " + str(int(arg1)) + "th " + str(names[int(user_choice)]) + " is: " + str(options[user_choice](arg1)))
			else:
				print("---> The " + str(names[int(user_choice)]) + " is: " + str(options[user_choice]()))

		except ValueError:
			break
		except IndexError:
			print("Error: Invalid option. Try again.")






if __name__ == "__main__":
	main()


# 1. Arithmetic Mean/Average
# 2. Median (and its rank)
# 3. Mode
# 4. Population Variance
# 5. Sample Variance
# 6. Population Standard Deviation
# 7. Sample Standard Deviation
# 8. Tchebycheff's Theorem (% between intervals, % before or after intervals, etc?)
# 9. Sample z-score
# 10. Sort
# 11. Percentiles
# 12. Interquartile Range
# 13. Minimum and maximum
# 14. Five-number summary (min, q1, median, q3, max)

# # Call functions in dict using input
# # Ex. if user inputs 0, call get_mean()
# print



