from standard import StandardBot
from aggressive import AggressiveBot

def print_numbered_list(l, title):
    print(title)
    for i, e in enumerate(l):
        print("(" + str(i + 1) + ") " + e)

def prompt_mode(modes):
    bot_mode_idx = input("Please select the number of your desired mode: ")

    if(type(bot_mode_idx) != int or bot_mode_idx <= 0 or bot_mode_idx > len(modes)):
        print("Invalid option.")
        exit(0)

    return modes[bot_mode_idx - 1]

def class_name(obj):
    return obj.__class__.__name__

if __name__ == '__main__':
    modes = [StandardBot(), AggressiveBot()]
    print_numbered_list(map(lambda x : class_name(x), modes), "==== Available Modes ====")

    mode = prompt_mode(modes)

    print("Selected " + class_name(mode) + ".")
