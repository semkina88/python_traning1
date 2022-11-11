import getopt
import os.path
import random
import re
import string
import sys

import jsonpickle

from model.class_for_test import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    stroka = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    stroka = re.sub('\s+', ' ', stroka).strip()
    return stroka


def random_number(prefix):
    symbols = string.digits
    number = prefix + "".join([random.choice(symbols) for i in range(10)])
    return number


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
                    company="", address="", home_phone="", cell_phone="", work_phone="", fax="",
                    email="", email2="", email3="", address2="",
                    secondary_phone="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
                       nickname=random_string("nickname", 20), title=random_string("title", 20),
                       company=random_string("company", 20), address=random_string("address", 30),
                       home_phone=random_string("home_phone", 10), cell_phone=random_string("cell_phone", 10),
                       work_phone=random_string("work_phone", 10), fax=random_string("fax", 10),
                       email=random_string("email", 20), email2=random_string("email2", 20),
                       email3=random_string("email3", 20),
                       address2=random_string("address2", 30), secondary_phone=random_string("secondary_phone", 10),
                       notes=random_string("notes", 40))
               for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
