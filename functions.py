def python_food():
    width = 80
    text = 'spam and eggs'
    left_margin = (width - len(text) // 2)
    print(" " * left_margin, text)


'''* allows for multiple variables 
we also declare default parameters in python '''


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text) // 2)
    return " " * left_margin + text

'''writes the current information to a file'''
# with open("centered",mode='w') as center_file:
python_food()
s1=(center_text("spam spam spam and spam"))
center_text(12)
s2=(center_text("spam spam and eggs"))
s3=(center_text("First", "second", "3", "4", 'spam'))
print(s1)
print(s2)
print(s3)

