# simpleWatch
An extremely simple file watcher, run a command when file is modified

##Usage
Usage is straight-forward and quick.

Tell simpleWatch to run a binary file whenever it is changed : 

    swatch "./theFile" theFile

Tell simpleWatch to restart your node server when app.js is changed (don't do this, nodemon is awesome) :

    swatch "node app.js" app.js

Tell simpleWatch to run make when a file is changed :

    swatch "make" someFile.cpp

##Installation
Installation is easy, just run the following code and simpleWatch will be installed on your system :

    pip install simpleWatch
