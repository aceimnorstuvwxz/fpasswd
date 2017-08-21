#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 ch3n.co


import json
import sys
import os


file_path = os.path.join(os.environ['HOME'], ".fpasswd")

def load_data():
    if os.path.exists(file_path):
        with open(file_path, 'r') as fp:
            data = json.load(fp)
            return data
    else:
        return []

def save_data(data):

    with open(file_path, 'w+') as fp:
        json.dump(data, fp)

def fadd(entry_fields):
    data = load_data()
    data.append(' '.join(entry_fields))
    save_data(data)
    print "added [%s]" % ' '.join(entry_fields)

def flist():
    data = load_data()
    for i, x in enumerate(data):
        print '[%d]'%i, x
    print '%d records' % len(data)


def fdelete(index):
    data = load_data()
    entry = data.pop(index)
    save_data(data)
    print '[%s] has deleted'%entry


def ffind(keyword):
    data = load_data()
    count = 0
    for i, x in enumerate(data):
        if keyword in x:
            print '[%d]' % i, x
            count += 1
    print '%d records' % count

def showusage():
    print '''
    USAGE,
    fpasswd add more entry data comes here... #add entry
    fpasswd list                              #list all
    fpasswd find keyword                      #find with keyword
    fpasswd delete ID                         #delete a certain entry
    '''

def main():
    if len(sys.argv) == 1:
        showusage()
        exit()

    cmd = sys.argv[1].lower()
    a = ""
    if cmd == "add":
        fadd(sys.argv[2:])
    elif cmd == "list":
        flist()
    elif len(sys.argv) > 2 and cmd == "delete":
        fdelete(int(sys.argv[2]))
    elif len(sys.argv) > 2 and cmd == "find":
        ffind(sys.argv[2])
    else:
        showusage()


if __name__ == "__main__":
    main()



