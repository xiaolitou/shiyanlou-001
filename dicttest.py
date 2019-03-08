
#!/usr/bin/env python3

import sys

def handle_data(arg):
    out_dict[arg.split(':')[0]] = arg.split(':')[1]
    #print(out_dict)

def print_data(key):
    print("ID:%s Name:%s"%(key,out_dict[key]))

out_dict = {}

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in sorted(out_dict):
        print_data(key)