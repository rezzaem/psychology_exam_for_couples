import os

# Get the current directory where the Python file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get a list of all files in the current directory
file_list = os.listdir('c:\\Users\\turbo\\Desktop\\Py\\Psychology project\\develope\\psychology_exam_for_couples\\v.2\\Psychology project\\scenarios\\amoozeshi\\a8')

# Iterate over each file in the directory
for file_name in filter(lambda f: f.endswith('.txt'), file_list):
    with open(file_name,'r+',encoding='utf-8') as file:
        # Read the contents of the file
        content = file.read()
        #=================================
        content = file.read()
        
        
        if "همکلاسی" in content:
            print(file_name)
        #=================================
        # for char in content:
        #     if char.isdigit():
        #         print(file_name)
        #     if char==':' or char==';':
                

        

# import os

# # Get the current directory where the Python file is located
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Get a list of all files in the current directory
# file_list = os.listdir(current_dir)

# # Iterate over each file in the directory
# for file_name in filter(lambda f: f.endswith('.txt'), file_list):
#     with open(file_name, 'r+',encoding='utf-8') as file:
#         # Read the contents of the file
#         content = file.read()

#         # Replace ':' and ';' with space ' '
#         content = content.replace(':', ' ').replace(';', ' ')

#         # Go to the beginning of the file
#         file.seek(0)

#         # Write the modified content back to the file
#         file.write(content)

#         # Truncate the remaining content if the new content is shorter
#         file.truncate()    