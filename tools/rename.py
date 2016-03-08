#! /usr/bin/env python
import re
import os
import sys

not_found = []
unknown_sex = []

male_names = set()
male_file = open("./male.data", "r")
for line in male_file:
	data = re.split(r'\s+', line)
	male_names.add(data[0])
male_file.close()

female_names = set()
female_file = open("./female.data", "r")
for line in female_file:
	data = re.split(r'\s+', line)
	female_names.add(data[0])
female_file.close()

for root, dirs, filenames in os.walk("."):
	for f in filenames:
		try:
			if f.endswith(".txt") and not f[0:2] in ["F-","M-","X-"]:
				filepath = os.path.join(root, f)
				book = open(filepath, "r")
				found = False
				line_num = 0
				for line in book:
					line_num += 1
					if line_num == 200:
						break
					data = re.split(r'\s+', line)
					if found:
						author = data[0:]
						break
					if data[0] == "Author:":
						author = data[1:]
						found = True
						if author:
							break
				book.close()

				if found:
					author_first_name = author[0].replace(',',"").replace('.',"")
					male = author_first_name.lower() in male_names or author_first_name.lower() in ["sir","lord","captain","duc"]
					female = author_first_name.lower() in female_names or author_first_name.lower() in ["mrs","miss","lady","madame", "mme"]

					if male and (not female):
						os.rename(f, "M-"+f)
						print ' '.join(author), "[MALE]"
					if (not male) and female:
						os.rename(f, "F-"+f)
						print ' '.join(author), "[FEMALE]"
					if (male and female) or ((not male) and (not female)):
						#os.rename(f, "X-"+f)
						#print ' '.join(author), "from ", f, " [?]"
						unknown_sex.append(' '.join(author) + 'from ' + f)

				else:
					os.rename(f, "X-"+f)
					#print f, "Author not found"
					not_found.append(f)

		except OSError:
			print f, "No file"

print
if len(not_found) > 0:
	print '============== AUTHOR NOT FOUND: ' + str(len(not_found)) + ' =============='
	for i in not_found:
		print i

print
if len(unknown_sex) > 0:
	print '============== UNKWNON SEX: ' + str(len(unknown_sex)) + ' =============='
	for i in unknown_sex:
		print i
