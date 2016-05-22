mystr="&#238A"
chartoremove=['#','&']
newstr=''
for strval in mystr:
    if strval not in chartoremove:
        newstr+=strval

print newstr
