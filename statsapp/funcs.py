import statistics
import math
import numpy as np

# Mean
def get_mean(data):
	map(int, data)
	mean = sum(data) / len(data)
	return mean


# Median
def get_median(data):
	data.sort()
	median_rank = (len(data) + 1)/2
	median_val = statistics.median(data)
	median = [median_rank, median_val] #rank at m[0], val at m[1]
	return median


# Mode
def get_mode(data):
	mode = statistics.mode(data)
	return mode


# Population Variance:
def get_pop_variance(data):
	pop_variance = statistics.pvariance(data, get_mean(data))
	return pop_variance


# Sample Variance:
def get_sam_variance(data):
	sam_variance = statistics.variance(data, get_mean(data))
	return sam_variance


# Population Standard Deviation
def get_pop_sd(data):
	pop_sd = statistics.pstdev(data)
	return pop_sd


# Sample Standard Deviation
def get_sam_sd(data):
	sam_sd = statistics.stdev(data)
	return sam_sd


# Sample z-score
def get_zscore(x, mean, sd):
	z_score = ((x - mean) / sd)
	return z_score


# Percentiles
def get_percentile(data, p):
	# pth = int(((p * (len(data) + 1)) / 100)) - 1
	# pos = pth % 1
	# sorted_data = sorted(data)
	# return sorted_data[int(pth)] + ((sorted_data[int(pth)+1] - sorted_data[int(pth)]))*pos
	return np.percentile(data, p)

# Interquartile Range
def get_iqr(data):
	q3 = get_percentile(data, 75)
	q1 = get_percentile(data, 25)
	iqr = (q3 - q1)
	return iqr

# Five Number Summary
def get_five_num_summary(data):
	d_min = min(data)
	q1 = get_percentile(data, 25)
	median = get_median(data)
	q3 = get_percentile(data, 75)
	d_max = max(data)
	summary_nums = [d_min, q1, median, q3, d_max]
	summary = str(d_min) + " " + str(q1) + " " + str(median[1]) + " " + str(q3) + " " + str(d_max)
	return summary


# Combinations
def get_combination(n, r):
	f = math.factorial
	return f(n) // f(r) //  f(n-r)


# Permutations
def get_permutation(n, r):
	f = math.factorial
	return f(n) // f(n-r)