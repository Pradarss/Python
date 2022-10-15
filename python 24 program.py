def make_bold(fn):
    def wrapped():
        return "<b>"+fn()+"</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>"+fn()+"</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>"+fn()+"</u>"
    return wrapped

@make_bold
@make_italic
@make_underline

def hello():
    x=input("enter a word:")
    return x
#returns "<b><i><u>adarsh</u></i></b>"

print(hello())

#page no.-2.53
#ques no.-23
