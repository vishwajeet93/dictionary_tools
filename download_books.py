import requests 
import os

import sys

if len (sys.argv) != 3 :
    print "Usage: python download_books.py domain total_num_pages "
    sys.exit (1)
#book_name="Glossary_of_Information_Technology"
book_name = sys.argv[1]
if not os.path.exists(book_name):
    os.mkdir(book_name)

image_url = "http://www.csttpublication.mhrd.gov.in/ebook/"+book_name+"/content/pages/"

#total_pages= 420
total_pages = int(sys.argv[2])
for i in range(1,total_pages):
	page="page"+str(i)+".jpg"
	image_url_temp=image_url+page

	r = requests.get(image_url_temp) # create HTTP response object 
	 
	# send a HTTP request to the server and save 
	# the HTTP response in a response object called r 
	with open(book_name+"/"+page,'wb') as f: 
	  
	    # Saving received content as a png file in 
	    # binary format 
	  
	    # write the contents of the response (r.content) 
	    # to a new file in binary mode. 
	    f.write(r.content)