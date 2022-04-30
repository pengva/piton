import os
import re

def get_text_info(filepath):
    fileData = {}

    textData = get_word_from_string(read_file(filepath))
    for i in range(0, len(textData)):
        if textData[i] in fileData:
            fileData[textData[i]] += 1
        else:
            fileData[textData[i]] = 1

    result = ""
    for i in fileData.items():
        result += format_tuple(i)

    return result

def read_file(filepath):
    fileText = ""
    with open(filepath, 'r') as f:
        text = f.read()
        fileText += text
    return fileText

def format_tuple(i):
    return "{" + str(i[0]).lower() + "} - {" + str(i[1]) + "}\n"

def get_word_from_string(string):
    return re.findall(r'\w+', string)

def download_file(url):
    import urllib.request
    path = "andrii_vivcharenko/source_data/"
    fileName = "username.csv"
    create_dirs(path)
    create_file(path + fileName)
    urllib.request.urlretrieve(url, path + fileName)
    delete_last_file_row(path + fileName)
    print("Completed")

def create_dirs(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

def create_file(filepath):
    if not os.path.exists(filepath):
        file = open(filepath, 'w')
        file.close()

def remove_empty_strings(list):
    return [x for x in list if x != "" and x != " " and x != "\n"]

def delete_last_file_row(filepath):
    with open(filepath, 'r') as f:
        lines = remove_empty_strings(f.readlines())
        print(lines)
    with open(filepath, 'w') as f:
        for line in lines[:-1]:
            f.write(line)

if __name__ == "__main__":
    download_file("https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv")
    