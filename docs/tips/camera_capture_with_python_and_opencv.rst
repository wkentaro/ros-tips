=====================================
Camera Capture with Python and OpenCV
=====================================


Code
----

.. code:: python

    import cv2
    def capture_camera(mirror=True, size=None):
        """Capture video from camera"""
        # Capture camera
        cap = cv2.VideoCapture(0) # 0 is camera device number

        while True:
            # ret is getting image success flag
            ret, frame = cap.read()

            # mirror or not
            if mirror is True:
                frame = frame[:,::-1]

            # resize frame
            # example size is (800, 600)
            if size is not None and len(size) == 2:
                frame = cv2.resize(frame, size)

            # display frame
            cv2.imshow('camera capture', frame)

            k = cv2.waitKey(1) # wait 1msec
            if k == 27: # finish with esc
                break

        # release capture
        cap.release()
        cv2.destroyAllWindows()

How to Use
----------

.. code-block:: bash

    $ python
    >>> capture_camera()