import re
RE_INT = re.compile(r'^[-+]?([1-9]\d*|0)$')

print("Please make sure you have copied this code in the folder where the text file exists ")
file_name = raw_inpur("Please enter complete name of ocred dictionary file to convert to tab separated csv: ")

generated_dict = {}
csv_file = open(file_name+".csv",'w')
with open(file_name) as dict_file:
	for line in dict_file:
		line = line.strip()
		if RE_INT.match(line):
			continue
		print(line.strip())
		splitted = re.split("( [\u0900-ॾ])", line,1)
		english= splitted[0]
		hindi = str(splitted[1]+splitted[2])
		generated_dict[english] = hindi
		csv_file.write(english+'\t'+hindi)
		csv_file.write("\n")
		print(english+'	'+hindi)
csv_file.close()
print("I have processed your file and kept the file in same folder with a .csv extension")


