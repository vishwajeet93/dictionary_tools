import os
dirname = raw_input('Please enter book name name to ocr =>:')
for filename in os.listdir(dirname):

	image_file = os.path.join(dirname, filename)
	command = "tesseract "+ image_file +" "+image_file+".txt -l en+hi --psm=4"
	pid = subprocess.call(commmand)
print("This book is ocred")