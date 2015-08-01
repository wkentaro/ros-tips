===================================
Makefile to compile C++ with OpenCV
===================================


Code
----

.. code:: mf

    # compiler
    CC :=g++
    # include files
    CFLAGS :=`pkg-config opencv --cflags` `pkg-config opencv --libs`
    LDFLAGS :=
    # compile all c++ files in dir
    SOURCES :=$(wildcard *.cpp)
    # C++ files .cpp removed file is executable
    EXECUTABLE :=$(SOURCES:.cpp=)

    all:$(EXECUTABLE)

    $(EXECUTABLE):$(SOURCES)
        $(CC) $< $(LDFLAGS) $(CFLAGS) -o $@

    clean:
        rm -rf $(EXECUTABLE)

How to Use
----------

.. code:: bash

    $ ls
    Makefile  mat.cpp
    $ make
    g++ mat.cpp  `pkg-config opencv --cflags` `pkg-config opencv --libs` -o mat
    $ ./mat