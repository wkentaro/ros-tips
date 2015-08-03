Video capture with C using OpenCV
=================================

Setup Environment
+++++++++++++++++
* Mac OS X
* Homebrew

Install opencv

.. code-block:: bash

  $ brew install opencv


How to use
++++++++++
Header files

.. code-block:: c

  #include <cv.h>
  #include <ctype.h>
  #include <highgui.h>

Compile & Execute

.. code-block:: bash

  # compile
  $ gcc -o video_capture video_capture.c `pkg-config opencv --cflags` `pkg-config opencv --libs`

  # execute
  $ ./video_capture


Example
+++++++
.. literalinclude:: video-capture-with-c-opencv_assets/video_capture.c
  :language: c

More information: https://github.com/wkentaro/c-opencv/tree/master/camera_capture