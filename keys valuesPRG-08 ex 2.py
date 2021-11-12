import csv
import csv
fname = input('What is your first name:')
sname = input('What is your surname:')
jobtitle = input('What is your job title:')
company = input('what is your company name:')
dictionary = {"Name: ":fname, "surname: ":sname, "jobtitle: ":jobtitle,"company:":company}
veda_file = open('userinfo.csv','a')
writer = csv.writer(veda_file,delimiter='\t')
for i, dictionary[i] in dictionary.items():
     writer.writerow([i],dictionary[i])
veda_file.close()
     