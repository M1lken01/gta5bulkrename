import pathlib

folder = "stuff"
path = pathlib.Path.cwd() / folder
                    
def rename_simple():
    num = input("New number:\n")
    if num == "c":
        exit()
    counter = 1
    for file in path.iterdir():
        if file.is_file():
            if file.suffix == ".ytd":
                new_file = str(file.name)[0:4] + "_diff_" + str(num) + "_" + chr(ord('`')+counter) + "_uni" + file.suffix
                file.rename(path / new_file)
                counter += 1
            if file.suffix == ".ydd":
                new_file = str(file.name)[0:4] + "_" + str(num) + "_u" + file.suffix
                file.rename(path / new_file)
    cmds()

def rename_complex():
    slot = input("Type (jbib, decl, task, accs, teef, feet, hand, lowr, uppr, hair, berd):\n")
    if slot == "1":slot = "jbib"
    if slot == "2":slot = "decl"
    if slot == "3":slot = "task"
    if slot == "4":slot = "accs"
    if slot == "5":slot = "teef"
    if slot == "6":slot = "feet"
    if slot == "7":slot = "hand"
    if slot == "8":slot = "lowr"
    if slot == "9":slot = "uppr"
    if slot == "10":slot = "hair"
    if slot == "11":slot = "berd"
    numold = input("Old number:\n")
    numnew = input("New number:\n")
    if numold == "c" or numnew == "c" or slot == "c":
        exit()
    counter = 1
    for file in path.iterdir():
        if file.is_file() and str(file.name)[0:4] == slot:
            if file.suffix == ".ytd" and file.name[10:13] == numold:
                new_file = str(file.name)[0:4] + "_diff_" + str(numnew) + "_" + chr(ord('`')+counter) + "_uni" + file.suffix
                file.rename(path / new_file)
                counter += 1
            if file.suffix == ".ydd" and file.name[5:8] == numold:
                new_file = str(file.name)[0:4] + "_" + str(numnew) + "_u" + file.suffix
                file.rename(path / new_file)
    cmds()
    
def start():
    if not path.exists():
        path.mkdir()
        print("First use.")
    print("""
░█▀▀░▀█▀░█▀█░█▀▀░░░█▀▄░█░█░█░░░█░█░░░░░█▀▄░█▀▀░█▀█░█▀█░█▄█░█▀▀
░█░█░░█░░█▀█░▀▀▄░░░█▀▄░█░█░█░░░█▀▄░░░░░█▀▄░█▀▀░█░█░█▀█░█░█░█▀▀
░▀▀▀░░▀░░▀░▀░▀▀░░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀
""")
    print("Instructions:\n  -Put the .ydd, .ytd files into the ./stuff folder")
    cmds()
        
def cmds():
    num = input("'1' for simple rename(rename all), '2' for complex rename(rename selected only)\n")
    if num == "1":rename_simple()
    if num == "2":rename_complex()

if __name__ == "__main__":
    start()  