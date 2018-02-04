#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class A(object):
    bar = 1
    def func1(self):
        print('foo')
    
    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()

def main():
    A.func2()

if __name__ == '__main__':
    main()