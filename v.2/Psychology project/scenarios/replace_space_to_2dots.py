import os

# Get the current directory where the Python file is located

file_list = os.listdir('c:\\Users\\turbo\\Desktop\\Py\\Psychology project\\develope\\psychology_exam_for_couples\\v.2\\Psychology project\\scenarios\\amoozeshi\\a5')
for file_name in filter(lambda f: f.endswith('.txt'), file_list):
    with open(file_name, 'r+',encoding='utf-8') as file:
        # Read the contents of the file
        content = file.read()
        content = content.replace(' f', ':f').replace(' t', ':t')

        file.seek(0)

        file.write(content)

        file.truncate()   