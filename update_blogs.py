#!/usr/local/bin/python3

'''
 ********************************************
 * Name        : update_blogs.py
 * Description : 
 * Date        : 2018-09-06
 * Author      : liuyy
 * E-mail      : 
 ********************************************
'''

import datetime
import re

def str_to_datetime(s):
    ints = [int(i) for i in re.split('[, :-]', s) if len(i) != 0]

    if len(ints) < 3:
        raise(TypeError("argument for datetime at least 3"))
    
    t = ""
    if len(ints) == 3:
        t = datetime.datetime(ints[0], ints[1], ints[2])
    elif len(ints) == 4:
        t = datetime.datetime(ints[0], ints[1], ints[2], ints[3])
    elif len(ints) == 5:
        t = datetime.datetime(ints[0], ints[1], ints[2], ints[3], ints[4])
    elif len(ints) == 6:
        t = datetime.datetime(ints[0], ints[1], ints[2], ints[3], ints[4], ints[5])

    return t

class entry:
    def __init__(self):
        self.properties = {}

    def __init__(self, filename):
        self.filename = filename
        self.realname = filename.split('/')[-1]
        self.create_time = str_to_datetime(self.realname.split('_')[0])
        self.last_time = ""
        self.only_brief = True
        self.brief = []

        with open(filename) as blog_fp:
            line = blog_fp.readline()

            while not line.startswith("###"): # get title
                line = blog_fp.readline()

            self.title = line.rstrip()
            line = blog_fp.readline().rstrip() # ---
            line = blog_fp.readline().rstrip() # last time
            self.last_time = str_to_datetime(line)

            line = blog_fp.readline().rstrip() # blank line
            line = blog_fp.readline()
            max_brief_count = 5
            while len(line) != 0 and max_brief_count > 0:
                self.brief.append(line.rstrip())
                line = blog_fp.readline()
                max_brief_count -= 1

            self.only_brief = max_brief_count > 0

    def __str__(self):
        return "create_time: {0}, last_time: {1}, filename: {2}, brief: {3}, only_brief: {4}".format(self.create_time,
                self.last_time, self.filename, self.brief, self.only_brief)

def parse_blogs():
    import os
    files = os.listdir("./_posts")

    return [entry("./_posts/" + i) for i in files]

def main():
    fp = open('index.md')
    nfp = open('index.md.new', 'w')

    line = fp.readline()
    last_time=""

    while len(line) != 0:
        line = line.rstrip()

        if line == "# Blogs":
            nfp.write(line + "\n")
            line = fp.readline().rstrip() #'---'
            nfp.write(line + "\n")
            line = fp.readline().rstrip() #'last time'
            last_time = str_to_datetime(line)

            # add new time
            #nfp.write(datetime.datetime.now().strftime("%Y, %m, %d, %H:%M:%S") + "\n")
            nfp.write("\n")
            line = fp.readline()

            while len(line) != 0 and not line.startswith("###"):
                nfp.write(line)
                line = fp.readline()
            break
        else:
            nfp.write(line + "\n")

        line = fp.readline()

    fp.close()

    blogs = parse_blogs()
    sorted_blogs = sorted(blogs, key = lambda i: i.create_time)

    for i in sorted_blogs:
        nfp.write(i.title + "\n")
        nfp.write("---\n\n")
        nfp.write('\n'.join(i.brief) + "\n")
        if not i.only_brief:
            nfp.write("[More ...]({0})\n".format(i.filename))
        nfp.write("\n")
    nfp.close()

if __name__ == '__main__':
    main()
    print("please mv index.md.new to index.md and update git")
