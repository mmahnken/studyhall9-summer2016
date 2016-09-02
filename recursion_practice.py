""" Some recursion practice.
	

"""

def recursive_sum(lst):
	""" Return the sum of all of the integers provided in the input list.

	>>> recursive_sum([3, 4])
	7

	>>> recursive_sum([100, 1, 6, 2])
	109
	"""

	if not lst:
		return 0

	if len(lst) == 1:
		return lst[0]
	else:
		return lst[0] + recursive_sum(lst[1:])


def return_sum(list1):
	if not list1:
		return 0
	last_el = list1.pop()
	return last_el + return_sum(list1)





def recursive_max(lst):
	""" Return the largest integer, given a list of integers.

	>>> recursive_max([3, 4, 7, 1])
	7

	>>> recursive_max([1])
	1
	"""

	if not lst:
		return None

	if len(lst) == 1:
		return lst[0]
	else:
		maximum = recursive_max(lst[1:])  # This is strange, but just assume this line works normally!
		if lst[0] > maximum:
			return lst[0]
		else:
			return maximum

def find(lst1, lst2):
	"""

	"""
	print lst1, '  ***   ', lst2

	if not lst1:
		return []
	else:
		# duplicates = find(lst1[1:], lst2[1:])
		# if lst1[0] in lst2:
		# 	duplicates.append(lst1[0])
		# if lst2[0] in lst1:
		# 	duplicates.append(lst2[0])
		# return duplicates
		duplicates = find(lst1[1:], lst2)
		if lst1[0] in lst2:
			duplicates.append(lst1[0])
		return duplicates

def find_common(lst1, lst2):
	"""
	>>> find([1,1,1], [1])
	[1,1,1]
	"""

	return find(lst1, lst2) , find(lst2, lst1)


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    new_nums = []
    for n in numbers:
    	new_nums.append(n/2.0)
    return new_nums

def half_rec(numbers):
	"""
	"""
	if not numbers:
		return []

	if len(numbers) == 1:
		return [ numbers[0] / 2.0 ]
	else:
		halves = half_rec(numbers[1:])
		this = [numbers[0] / 2.0 ]
		return this + halves






