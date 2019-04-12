def python_food():
    width = 80
    text = 'spam and eggs'
    left_margin = (width - len(text) // 2)
    print(" " * left_margin, text)


'''* allows for multiple variables 
we also declare default parameters in python '''


def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text) // 2)
    print(" " * left_margin, text, end=end, file=file, flush=flush)

'''writes the current information to a file'''
with open("centered",mode='w') as center_file:
    python_food()
    center_text("spam spam spam and spam",file=center_file)
    center_text(12)
    center_text("spam spam and eggs",file=center_file)

    center_text("First", "second", "3", "4", 'spam', sep="-",file=center_file)
    print()
