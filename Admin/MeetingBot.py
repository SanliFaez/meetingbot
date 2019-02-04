"""
meeting bot creates the first draft of the meeting report from the personal progress files.

Version 0.1
Author: Sanli Faez, @sanli
Released under Mozilla Public License Version 2.0
"""

members = ['Maria', 'Captain', 'Liesl' , 'Louisa', 'Friedrich', 'Kurt', 'Brigitta', 'Marta', 'Greti']

thisweek = "2019_05"
root = ".."
mfile = f"group_meeting_{thisweek}.md"

import os.path
f = open(mfile, "w")
f.write(f"# group meeting {thisweek} \n")
f.write(f"### Announcements \n")
f.write(f"### Safety \n")
f.write(f"### Updates \n")
for m in members:
    fname = f"{root}/{m}/HiLoPlan/{m}_hilo_{thisweek}.md"
    if os.path.isfile(fname):
        f.write(f"__{m}__: \n")
        with open(fname, 'r') as fi: f.write(fi.read())
        f.write("  \n  \n")
        print(fname, "imported.")
    else:
        f.write(f"__{m}__ absent. <br/>\n")
        print(f"{m} is missing")

f.write(f"### Reports \n")
with open("report_schedule.md", "r") as fl:
    for line in fl:
        words = line.split()
        if thisweek in words:
            f.write(f"{line}  \n")
            next = fl.readline()


f.write(f"### Next week\n")
f.write(f"{next}  \n")

f.write(f"### Lab ordering/cleaning \n")
with open("cleaning_schedule.md", "r") as fl:
    for line in fl:
        words = line.split()
        if thisweek in words:
            f.write(f"{line}  \n")
            next = fl.readline()


f.close()

