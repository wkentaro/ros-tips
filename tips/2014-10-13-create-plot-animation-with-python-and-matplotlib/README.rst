================================================
Create plot animation with python and matplotlib
================================================


Code
----

.. code:: python

    import numpy
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import mpl_toolkits.mplot3d.axes3d as p3

    def plot_3D_animation(X, Y, Z, n_frame=None,
                          xlim=None, ylim=None, zlim=None,
                          step=None, saveanime=None, show=True):
        """3D plotting animation"""
        fig = plt.figure()
        ax = p3.Axes3D(fig)

        if step is None:
            step = 1
        X = X[range(0, len(X), step)]
        Y = Y[range(0, len(Y), step)]
        Z = Z[range(0, len(Z), step)]

        data = [numpy.vstack((X, Y, Z))]

        lines = [ax.plot(dat[0, 0:1], dat[1, 0:1],
                         dat[2, 0:1])[0] for dat in data]

        # Setting the axes properties
        if xlim is None:
            ax.set_xlim3d([X.min(), X.max()])
        elif len(xlim) == 2:
            ax.set_xlim3d(xlim)
        ax.set_xlabel('X')
        if ylim is None:
            ax.set_ylim3d([Y.min(), Y.max()])
        elif len(ylim) == 2:
            ax.set_ylim3d(ylim)
        ax.set_ylabel('Y')
        if zlim is None:
            ax.set_zlim3d([Z.min(), Z.max()])
        elif len(zlim) == 2:
            ax.set_zlim3d(zlim)
        ax.set_zlabel('Z')
        ax.set_title('3D animation')
        ax.view_init(-10, 30)

        def update_lines(num, dataLines, lines):
            for line, data in zip(lines, dataLines):
                line.set_data(data[0:2, :num])
                line.set_3d_properties(data[2,:num])
            return lines

        if n_frame is None:
            n_frame = len(X)

        # Creating the Animation object
        anim = animation.FuncAnimation(fig,
                                       update_lines,
                                       n_frame,
                                       fargs=(data, lines),
                                       interval=1,
                                       blit=False)

        if type(saveanime) == str:
            writer = animation.FFMpegWriter()
            anim.save(saveanime, writer=writer)

        if show is True:
            plt.show()

        plt.clf()
        plt.close()


How to Use
----------

.. code:: bash

    >>> import numpy as np
    >>> X, Y, Z = np.array([1,2,3]), np.array([2,3,4]), np.array([4,5,6])
    >>> plot_3D_animation(X, Y, Z)


Example
-------

-  `Plot simulation with 3D printer <https://www.youtube.com/watch?v=ZJ2nRWYOFkk>`__
-  https://github.com/ut-3dprinter/ut-3dprinter/tree/master/Software