#!/usr/bin/python

import sys
import re
import os.path

num_args = len(sys.argv)
if (num_args != 3 or os.path.isfile(sys.argv[1]) == False or sys.argv[2].isdigit() == False):
    print "Usage: %s <FILE> <NUM_PER_FILE>" % (sys.argv[0])
    sys.exit(1)

arg_file = sys.argv[1]
arg_num_per_file = sys.argv[2]

file = open(arg_file)
data = file.read()
file.close()
contacts = re.compile('BEGIN:VCARD(.*?)END:VCARD', re.DOTALL |  re.IGNORECASE).findall(data)
file_num = 0

def add_to_file(contacts):
    global file_num
    file = open('contacts_split_%d.vcf' % (file_num), 'w')
    [file.write("BEGIN:VCARD%sEND:VCARD\n" % (contact)) for contact in contacts]
    file.close()
    file_num += 1

def chunks(l, n):
    for i in xrange(0, len(l), int(n)):
        yield l[i:i+int(n)]

[add_to_file(l) for l in list(chunks(contacts, arg_num_per_file))]
