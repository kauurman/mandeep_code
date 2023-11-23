punc = '''!()-[]{}:;'"\,<>.%?@#$%^&*_~'''
string = input("enter anything here:")

empty_str = ""

for i in string: 
    if i not  in punc: 
        empty_str += 1
print (empty_str )        