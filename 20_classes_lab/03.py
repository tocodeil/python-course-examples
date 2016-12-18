"""
Following code assumes a class named Widget that depends on
other widgets
Widget constructor takes a name, and function 
add_dependency(depends)
marks widget as depends on all widgets in "depends" list

When building a widget, you need to first build all the widgets it
depends on.

Implement widget so the following code works:

luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)

# print all widgets so each widget is printed before
# the ones it depends on
_all.build()
"""


class Widget(object):
    def __init__(self, name):
        self.name = name
        self.depends_on = []
        self.create = False

    def add_dependency(self, *depends):
        self.depends_on += depends

    def build(self):
        for actor in self.depends_on:
            if actor.create == True:
                continue
            actor.build()

        print self.name
        self.create = True



luke = Widget("Luke")
hansolo = Widget("Han Solo")
leia = Widget("Leia")
yoda = Widget("Yoda")
padme = Widget("Padme Amidala")
anakin = Widget("Anakin Skywalker")
obi = Widget("Obi-Wan")
darth = Widget("Darth Vader")
_all = Widget("All")

luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)
