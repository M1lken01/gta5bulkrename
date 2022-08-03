import pathlib
import string

'''def rename(num):
    path = pathlib.Path('.') / "stuff"    
    for folder in path.iterdir():
        if folder.is_dir():
            counter = 1
            for file in folder.iterdir():
                if file.is_file():
                    new_file = str(file.name)[0:4] + "_diff_" + str(num) + "_" + chr(ord('`')+counter) + "_uni" + file.suffix
                    file.rename(path / folder.name / new_file)
                    counter += 1'''
                    
def rename(num):
    path = pathlib.Path('.') / "stuff"    
    counter = 1
    for file in path.iterdir():
        if file.is_file():
            new_file = str(file.name)[0:4] + "_diff_" + str(num) + "_" + chr(ord('`')+counter) + "_uni" + file.suffix
            file.rename(path / new_file)
            counter += 1

def setnum():
    intro()
    num = input("New number:\n")
    if(num == "c"):
        exit()
    rename(num)
    
def intro():
    print("""
░█▀▀░▀█▀░█▀█░█▀▀░░░█▀▄░█░█░█░░░█░█░█▀▄░█▀▀░█▀█░█▀█░█▄█░█▀▀
░█░█░░█░░█▀█░▀▀▄░░░█▀▄░█░█░█░░░█▀▄░█▀▄░█▀▀░█░█░█▀█░█░█░█▀▀
░▀▀▀░░▀░░▀░▀░▀▀░░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀
""")
    print("Instructions:\n  -Put the files in ./stuff folder\n  -Enter the number to rename the files to")

setnum()    