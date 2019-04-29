#!/usr/bin/env python

import re
pat_file_name='patterns.txt'

param_datab = dict()
regex_db = dict()

def print_trailer():
	print '#'*30

def parse_file(file_name):
	
	if file_name == None:
		file_name = 'logs.txt'

	file_handle = open(file_name, "r")
	if (file_handle == None):
		print ("No Log file found")

	#Read the lines
	file_buf = file_handle.readlines()
	
	#Get the length
	file_len = len(file_buf)

	#print file_len

	#Read and Match one by one
	i = 0
	while i < file_len:
		line = file_buf[i].strip()
		
		#Execute the regular exp one by one
		for k, v in regex_db.items():
			
			out = k.search(line)
			#print out
			
			if (out == None):
				continue
			else:
				#Print the variable name and value retrieved
				j = 0
				out_len = len(out.groups()) - 1
				while (j < out_len):
					print "{}: {}".format(v[j], out.group(j+2).strip())
					j=j+1
		i=i+1
			
def form_param_regex():
	for k,v in param_datab.items():
		#print k, v
		j = 0
		regex_string="("+k+")"
		param_len = len(v)
		
		#Create a list to hold all the parameter/variable names
		regex_param_name_list = list()

		while (j < param_len):
			param_name, param_format = v[j].split(',')
			#print param_name.strip()
			#print param_format.strip()
			regex_param_name_list.append(param_name.strip())
			if (param_format.strip() == "eol"):
				regex_string = regex_string + "(.*) "
			elif (param_format.strip() == "space"):
				regex_string = regex_string + "\s*(\w*)"
			elif ('#' in param_format.strip()):
				#print param_format.strip()
				param_hard_pattern = re.search(r'#(.*?)#', param_format.strip())
				#print param_hard_pattern
				if ('space' in param_format.strip()):
					regex_string = regex_string + "\s*"+param_hard_pattern.group(1)+"\s*(\w*)"
				elif ('eol' in param_format.strip()): 
					regex_string = regex_string + "\s*"+param_hard_pattern.group(1)+"(.*)"
				#print regex_string
			j=j+1
		regex_string = re.compile(regex_string.strip())
		#print regex_string.pattern
		#regex_list.append(regex_string)
		
		#Add the regex string and regex param list in a dict for later retrieval
		regex_db[regex_string]=regex_param_name_list
			
if __name__ == '__main__':
	
	#Read the patterns file and fetch the interesting patterns
	pat_file = open(pat_file_name, "r")
	if (pat_file == None):
		print ("No Pattern File Found")

	#Read the lines
	pat_file_buf = pat_file.readlines()

	#Get the length
	len_buf = len(pat_file_buf)

	i = 0
	while i < len_buf:
		line = pat_file_buf[i].strip()
		split_index =  line.find('$')
		pattern_string = ''
		pattern_params = ''
		if split_index <> -1:
			pattern_string = line[0:split_index]
			pattern_params = line[split_index+1:]

		#print pattern_string
		param_list = re.findall(r'\{(.*?)\}', pattern_params)
		#print param_list
		
		param_len = len(param_list)
		j = 0

		#Its a db of pattern strings containing the parameters to match
		if pattern_string not in param_datab:
			param_datab[pattern_string]=param_list
		'''
		while (j < param_len):
			param_name, param_format = param_list[j].split(',')
			j=j+1
			#print param_name.strip()
			#print param_format.strip()
		'''	
		i=i+1
	#print param_datab
	
	#Form Regular Expression Array
	form_param_regex()

	#Parse the log file
	parse_file("logs.txt")

	pat_file.close()
