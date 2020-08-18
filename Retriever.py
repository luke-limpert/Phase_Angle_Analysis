# importing required modules
import PyPDF2
import os
import glob


dir_1 = 'V:/JATV_Plant2/ME & Maint/ME/Data Folder'
dir_data = 'J:/QA/CMM/RESULTS/PRISMOB2'

os.chdir(dir_data)

filenames = glob.glob("JGF02-000940**.pdf")
print(filenames)
os.chdir(dir_1)
with open("result.txt", "wt") as outfile:
    for f in filenames:
    	print('L')
    	os.chdir(dir_data)
    	with open(f, "rb") as pdfFileObj:
    		print('O')
    		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    		number_of_pages = pdfReader.getNumPages()
    		for i in range(0, number_of_pages):
    			pageObj = pdfReader.getPage(i)
    			os.chdir(dir_1)
    			print(pageObj.extractText())
    			outfile.write(pageObj.extractText())
    		pdfFileObj.close()
