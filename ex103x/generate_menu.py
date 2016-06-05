#!/usr/bin/env python2

import sys

import data

filename = "menu"

def main(args):
    with open(filename, "w+") as f:
        for item in data.menu.keys():
            name = data.menu[item]["name"]
            price = data.menu[item]["price"]
            category = data.menu[item]["category"]
            f.write("{}|{}|{}|{}\n".format(item, name, price, category))

if __name__ == "__main__":
    main(sys.argv[1:])
