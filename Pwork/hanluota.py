#!/usr/bin/env python3
#=.= coding:utf-8 =.=


def hello(greeting, *args):  
    if (len(args)==0):
        print('%s!' %greeting)
    else:
        print('%s, %s!'%(greeting,','.join(args)))

hello('Hi')
hello('Hi','Sarah')
hello('Hello','Michael','Bob','Adam')

names = ('Bart','Lisa')
hello('Hello',*names)

def print_scores(**kw):
    print('    Name  Score')
    print('----------------')
    for name, score in kw.items():
        print('%8s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee':99,
    'Lisa S':88,
    'F.Bart':77
    }

print_scores(**data)

def move(n, a, b, c):
    if n==1:
        print(a,'---->',c)
        return
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'a', 'b', 'c')
