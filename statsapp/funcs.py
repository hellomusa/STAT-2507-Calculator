import statistics
import math
import numpy as np

# Mean
def get_mean(data):
	data_sum = 0
	size = 0
	for n in data:
		data_sum += n
		size += 1
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
	pth = int(((p * (size + 1)) / 100)) - 1
	pos = pth % 1
	sorted_data = sorted(data)
	return sorted_data[int(pth)] + ((sorted_data[int(pth)+1] - sorted_data[int(pth)]))*pos

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