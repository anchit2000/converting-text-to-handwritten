from PIL import Image
import os

if not os.path.exists("./data"):
    os.mkdir("./data")
if not os.path.exists("./solutions"):
    os.mkdir("./solutions")

string_user = input("Enter a number:")

list_ = []

for i in string_user:
    try:
        list_.append(int(i))
    except:
        list_.append(str(i))

IMG = Image.new("RGB",(len(list_)*100,50),"white")

for i in range(len(list_)):
    try:
        img = Image.open(f"./data/{list_[i]}.jpeg")
        img = img.resize((40,40))
        IMG.paste(img,(i*90,0))
    except Exception as e:
        print(f"Add {list_[i]} to the data folder")
        IMG.paste(Image.new("RGB",(40,40),"white"),(i*90,0))

IMG.save(f"./solutions/{string_user}.jpeg")