a = "Make a lot of money"
b = "Buy now"
c = "Click this"
d = "Subscribe this"

comment = input("Enter your comment: ")

if(a in comment) or (b in comment) or (c in comment) or (d in comment):
    print("This is a spam comment")
else:
    print("This is not a spam comment")
    