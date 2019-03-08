#!/usr/bin/env python3

class UserData(object):
    def __init__(self,id,name):
        self.id = id
        self._name = name

class NewUser(UserData):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if len(value) > 3:
            self._name = value
        else:
            print('ERROR')
        self._name = value

    @classmethod
    def get_group(cls):
        return 'shiyanlou-louplus'
    
    @staticmethod
    def format_userdata(id,name):
        return "{0}'s id is {1}".format(name,id)
        
    def __call__(self):
        print('%s\'s id is %s'%(self.name,self.id))


if __name__ == '__main__':
    
    # user1 = NewUser(101,'Jack')
    # user1.name = 'Lou'
    # user1.name = 'Jackie'
    # user2 = NewUser(102,'Louplus')
    # print('ID:%s Name:%s'%(user1.num,user1.name))
    # print('ID:%s Name:%s'%(user2.num,user2.name))
    # print(user1.name)
    # print(user2.name)

    # print(NewUser.get_group())
    # print(NewUser.format_userdata(109,'Lucy'))

    user = NewUser(101,'Jack')
    user()