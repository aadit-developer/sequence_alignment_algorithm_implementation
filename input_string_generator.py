def getInputString(file_path):

    with open(file_path,"r") as file:
        items = file.read().splitlines()

    str1 = items[0]
    str1_elements = []
    str2_elements = []
    elements = []

    for i in range(1,len(items)):
        if items[i].isdecimal():
            elements.append(int(items[i]))
        else:
            str1_elements = elements
            elements = []
            str2 = items[i]

    str2_elements = elements

    for i in str1_elements:
        beginning_substring = str1[:i+1]
        ending_substring = str1[i+1:]
        str1 = beginning_substring + str1 + ending_substring

    for i in str2_elements:
        beginning_substring = str2[:i+1]
        ending_substring = str2[i+1:]
        str2 = beginning_substring + str2 + ending_substring

    return[str1,str2]
