#!/usr/bin/env python3
import os


class Mkdir(object):

    def __init__(self, zhu,z1,z2,z3):
        self.zhu = zhu
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.file = '__init__.py'

    def mkpath(self):
        pardir = os.getcwd()
        path_list = [self.z1,self.z2,self.z3]
        new_path = os.path.join(pardir,self.zhu)
        new_file = os.path.join(new_path,self.file)
        try:
            os.mkdir(new_path)
            self.tf(new_file)
        except:
            print('{} yi cun zai'.format(new_path))

        for i in path_list:
            new_path_son = os.path.join(new_path,i)
            new_file_son = os.path.join(new_path_son,self.file)
            try:
                os.mkdir(new_path_son)
                self.tf(new_file_son)
            except:
                print('{} yi cun zai'.format(new_path_son))

    def tf(self,filedir):
        os.system('touch {}'.format(filedir))
        print('ok')

def main():
    mkdi = Mkdir('syl','A','B','C')
    mkdi.mkpath()

if __name__ == '__main__':
    main()