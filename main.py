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
                new_file = file.name[0:4] + "_diff_" + str(num) + "_" + chr(ord('`')+counter) + "_uni" + file.suffix
                file.rename(path / new_file)
                counter += 1
            if file.suffix == ".ydd":
                new_file = file.name[0:4] + "_" + str(num) + "_u" + file.suffix
                file.rename(path / new_file)
    cmds()

def rename_complex():
    slot = input("Type (jbib, decl, task, accs, teef, feet, hand, lowr, uppr, hair, berd):\n")
    match slot:
        case "1":slot = "jbib"
        case "2":slot = "decl"
        case "3":slot = "task"
        case "4":slot = "accs"
        case "5":slot = "teef"
        case "6":slot = "feet"
        case "7":slot = "hand"
        case "8":slot = "lowr"
        case "9":slot = "uppr"
        case "10":slot = "hair"
        case "11":slot = "berd"
    numold = input("Old number:\n")
    numnew = input("New number:\n")
    if numold == "c" or numnew == "c" or slot == "c":
        exit()
    counter = 1
    for file in path.iterdir():
        if file.is_file() and file.name[0:4] == slot:
            if file.suffix == ".ytd" and file.name[10:13] == numold:
                new_file = file.name[0:4] + "_diff_" + str(numnew) + "_" + chr(ord('`')+counter) + "_uni" + file.suffix
                file.rename(path / new_file)
                counter += 1
            if file.suffix == ".ydd" and file.name[5:8] == numold:
                new_file = file.name[0:4] + "_" + str(numnew) + "_u" + file.suffix
                file.rename(path / new_file)
    cmds()
    
def rename_rearrange():
    current_slot = "accs"
    is_first = True
    counter = 1
    ydd_count = 0
    ytd_count = 0
    for file in path.iterdir():
        if file.is_file():
            if is_first:
                is_first = False
                current_slot = file.name[0:4]
            if not current_slot == file.name[0:4]:
                current_slot = file.name[0:4]
                ydd_count = 0
                ytd_count = -1
                print(current_slot)
            if file.suffix == ".ydd":
                new_file = file.name[0:4] + "_" + str(f"{ydd_count:03}") + "_u" + file.suffix
                file.rename(path / new_file)
                #print(file.name[0:4] + "_" + str(f"{ydd_count:03}") + "_u" + file.suffix)
                ydd_count += 1
            if file.suffix == ".ytd":
                if not chr(ord('`')+counter) == file.name[14:15]:
                    counter = 1
                    ytd_count += 1
                new_file = file.name[0:4] + "_diff_" + str(f"{ytd_count:03}") + "_" + chr(ord('`')+counter) + "_uni" + file.suffix
                file.rename(path / new_file)
                #print(file.name[0:4] + "_diff_" + str(f"{ytd_count:03}") + "_" + chr(ord('`')+counter) + "_uni" + file.suffix)
                counter += 1
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
    num = input("'1' for simple rename(rename all), '2' for complex rename(rename selected only), '3' for rearrange rename(rename all from lowest to highest)\n")
    match num:
        case "1":
            rename_simple()
        case "2":
            rename_complex()
        case "3":
            rename_rearrange()

if __name__ == "__main__":
    start()  