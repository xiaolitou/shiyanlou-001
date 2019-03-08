#!/usr/bin/env python3

import sys

def copy_file(src,dst):
    with open(src,'r') as src_file:
        with open(dst,'w') as dst_file:
            # dst_file.write(src_file.readlines())
            src_list = src_file.readlines()
            for i,element in enumerate(src_list):
                dst_file.write('{} {}'.format(i+1,element))
            print('copy is ok')

def main():
    if len(sys.argv) == 3:
        copy_file(sys.argv[1],sys.argv[2])
    else:
        print('Parameter Error')
        print(sys.argv[0],'srcfile,dstfile')
        sys.exit(-1)

if __name__ == '__main__':
    main()