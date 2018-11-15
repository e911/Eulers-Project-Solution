from functools import reduce
# alpha_dict = {'A': 1,
#  'B': 2,
#  'C': 3,
#  'D': 4,
#  'E': 5,
#  'F': 6,
#  'G': 7,
#  'H': 8,
#  'I': 9,
#  'J': 10,
#  'K': 11,
#  'L': 12,
#  'M': 13,
#  'N': 14,
#  'O': 15,
#  'P': 16,
#  'Q': 17,
#  'R': 18,
#  'S': 19,
#  'T': 20,
#  'U': 21,
#  'V': 22,
#  'W': 23,
#  'X': 24,
#  'Y': 25,
#  'Z': 26
#  }
alpha_dict = dict(zip(list(range(1, 27)), list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))


def get_sorted_list_form_file(filename):
	file_object = open(filename, 'r')
	for each in file_object:
		#the line below is to parse the file to convert into list
		z=(each.replace('"','').split(','))
	return sorted(z)

def	sum_of_name_scores(sorted_list):
	sum_all = 0
	for each in range(len(sorted_list)):
		#the map function maps each letter of names into respective number
		#the reduce function is just to find the sum
		# each+1 as index has to start from 1 not 0 
		sum_all +=  (reduce(lambda x,y: x+y , map(lambda x: alpha_dict[x] ,list(sorted_list[each])))) * (each+1)
	return sum_all

if __name__ == "__main__":
	sorted_list = get_sorted_list_form_file("p022_names.txt")
	total = sum_of_name_scores(sorted_list)
	print("The sum of the namescores is", total)


