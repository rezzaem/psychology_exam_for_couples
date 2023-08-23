from docx import Document

def remove_n(txt):
    txt=txt.replace('\n','')
    return txt




# Load the Word document
doc = Document('data.docx')

# Assume the table is the first table in the document
table = doc.tables[0]

# Initialize a list to store the extracted data
data = []

tmp=0
# Iterate through rows in the table
for row in table.rows:
    row_data = []
    for cell in row.cells:
        row_data.append(cell.text.strip())

    if tmp!=0:
        data.append(row_data)
        tmp+=1
    else:
        tmp+=1

txt_file=[]
# Print the extracted data
for row_num in range(0,len(data)):
    # print(row)
    row=data[row_num]
    print(row)
    if row_num%2==0 :
        
        for part in range(3):
            if part==0:
                plc_of_bn=row[part].find('\n')
                correct_place=plc_of_bn+2
                txt_file.append(row[part][correct_place:])
            elif part==1:
                counter_of_n=0
                plc_of_bn=0
                for i in range (4):
                    plc_of_bn=row[part][counter_of_n:].find('\n')
                    txt_file.append(row[part][counter_of_n:plc_of_bn])
                    counter_of_n=plc_of_bn+2
    print(txt_file)





