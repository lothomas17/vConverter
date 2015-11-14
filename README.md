# vConverter
This is a small python app that can be used to simplify data entry by taking a string and checking inputs against that string to see if they exist. The primary application of this is in data entry, as it can take massive lists of data, and convert them into numerical vectors, which can then be input to Excel or SPSS.

##Example
Suppose we have a survey in which we ask people for their favorite colors, from a list of Red, Yellow, Blue, Green, and Pink. Each person can choose more than one option. We may get an data file that looks like:

    Red, Yellow
    Green
    Pink
    Mauve

vConverter will transform that file into the form

    11000
    00010
    00001
    00000

The second form is much easier to do statistical analyses on, which vConverter enables.

##Using vConverter
There are two ways to use vConverter. If you want to run it via command line, you will need the following dependencies:

Gooey:https://github.com/chriskiehl/Gooey

Once you have the dependencies installed, you can just call:

    >>python vConverter.py

If you want to generate a binary file that can be run then, you will also need to install pyinstaller, which can be found at http://www.pyinstaller.org/.

Once you have the dependencies installed for pyinstaller, just run

    >>pyinstaller build.spec
    
You will find the binary in the dist directory.

##References
https://github.com/chriskiehl/Gooey
