# simpleWatch
An extremely simple file watcher, run a command when a file or directory is modified

##Usage
Usage is straight-forward and quick.

Execute a binary file whenever it is changed : 

    swatch "./theFile" theFile

Restart your node server when app.js is changed :

    swatch "node app.js" app.js

Run make when a file is changed :

    swatch "make" someFile.cpp

You can specify more than one file :

    swatch "echo something happened" file1.cpp file2.py file3.hs file4.js file5.c etc.etc

Or use glob patterns :

    swatch "clear; ./fizzBuzz 32" *.cpp

Or directories :

    swatch "echo current directory modified" .
    

##Installation
Installation is easy,  run the following command and simpleWatch will be installed on your system :

    pip install simpleWatch

Note : simpleWatch was written in Python3, will not work for 2.x
