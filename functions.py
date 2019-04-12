def python_food():
    width = 80
    text = 'spam and eggs'
    left_margin = (width - len(text) // 2)
    print(" " * left_margin, text)


def center_text(text):
    text = str(text)
    left_margin = (80 - len(text) // 2)
    print(" " * left_margin, text)


python_food()
center_text("spam spam spam and spam")
center_text(12)
center_text("spam spam and eggs")

print("First","second","3","4",'spam')

