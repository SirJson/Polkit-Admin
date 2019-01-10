Polkit Admin
---------------

**WIP! See admin branch**

Also sick of editing hundereds of XML Files?

Polkit Admin reads in a Polkit .policy file, parses its XML contents, and
presents the information it contains, on a more human-readable GUI window.
After selecting a policy File you can also modify the information shown. This makes setting up Polkit a lot easier.

Polkit policies define what the default permissions users are given to perform
certain tasks on their systems, for example, can a user eject a disk. These
permissions are granted or denied depending on if a user is logged in locally
(Active) , logged in remotely (Inactive), or just plain logged in.

This utility is intended to give you an insight into how your system is
configured by default and change the settings you don't like

Ported over to Python 3 and the QT5 library.

Requires
--------
    python3
    python3-qt5
    python3-lxml
    Qt libraries

Running
-------

To run, simply change into the PolkitAdmin directory and type ./polkitex.py

Menus
-----

Use File--->Open from the GUI to open the .policy file you wish to explore.

File--->Quit exits the application.

Help--->About brings up the About window.

Help--->Glossary brings up a window explaining the meanings of the information
        displayed.
        

This is being tested on Arch Linux and Ubuntu.

Files
-----

About.ui        : Qtdesigner file for the About window

Glossary.ui     : QtDesigner file for the Glossary window

PKEIconV001.png : The program's "logo"

polkitex.py     : The main Python program

polkitex.ui     : QtDesigner file for the main GUI

Ui_*.py         : Python code, compiled from the *.ui files using pyuic5

Any changes made to the .ui QtDesigner forms need to then be compiled via pyuic4.
Signal slots from the buttons to the main program are created inside QtDesigner.

Python will more than likely create some .pyc files after running this, it's
normal (compiled python files).

I hope this proves useful to someone.

