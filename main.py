file_template = open('templates/SQLTemplate.txt', 'r')
template = file_template.read()
file_template.close()

with open('output/myfile.sql', 'w') as f:
    f.write(template.replace('##TABLENAME##', 'CUSTOMERS'))