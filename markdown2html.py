#!/usr/bin/python3
""" markdown to html """

if __name__ == "__main__":

    import sys
    import os.path

    if len(sys.argv) < 2:
        sys.exit("Usage: ./markdown2html.py README.md README.html")
    elif (not os.path.isfile(sys.argv[1]) or not os.path.exists(sys.argv[1])):
        sys.exit("Missing {}".format(sys.argv[1]))
