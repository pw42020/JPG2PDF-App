from plyer import filechooser

path = filechooser.open_file(title="Pick an image or document",path=r"C:\Users\Ninja\OneDrive\Desktop",multiple=True)

for i in range(len(path)):
    newstr=str(path[i])
    newstr=newstr.replace("[","")
    newstr=newstr.replace("]","")
    newstr=newstr.replace("'","")
    print(newstr)