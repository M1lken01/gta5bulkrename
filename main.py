import pathlib
import string
                    
def rename(num):
    path = pathlib.Path('.') / "stuff"    
    counter = 1
    for file in path.iterdir():
        if file.is_file():
            new_file = str(file.name)[0:4] + "_diff_" + str(num) + "_" + chr(ord('`')+counter) + "_uni" + file.suffix
            file.rename(path / new_file)
            counter += 1
    
def start():
    print("""
░█▀▀░▀█▀░█▀█░█▀▀░░░█▀▄░█░█░█░░░█░█░█▀▄░█▀▀░█▀█░█▀█░█▄█░█▀▀
░█░█░░█░░█▀█░▀▀▄░░░█▀▄░█░█░█░░░█▀▄░█▀▄░█▀▀░█░█░█▀█░█░█░█▀▀
░▀▀▀░░▀░░▀░▀░▀▀░░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀
""")
    print("Instructions:\n  -Put the files in ./stuff folder\n  -Enter the number to rename the files to")
    num = input("New number:\n")
    if(num == "c"):
        exit()
    rename(num)

start()    