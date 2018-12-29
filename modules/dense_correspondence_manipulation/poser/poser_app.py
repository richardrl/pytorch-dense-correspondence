#!/usr/bin/env directorPython

# system
import os
import argparse

# director
import director.vtkAll as vtk
import director.vtkNumpy as vnp
import director.objectmodel as om
import director.visualization as vis
from director import mainwindowapp
from director.timercallback import TimerCallback

# pdc
from dense_correspondence_manipulation.poser.poser_client import PoserClient
from dense_correspondence.dataset.scene_structure import SceneStructure


"""
Launches a poser client app
"""

VISUALIZE = False

if __name__ == "__main__":


    globalsDict = globals()

    if VISUALIZE:
        app = mainwindowapp.construct()
        app.gridObj.setProperty('Visible', True)
        app.viewOptions.setProperty('Orientation widget', True)
        app.viewOptions.setProperty('View angle', 30)
        app.sceneBrowserDock.setVisible(True)
        app.propertiesDock.setVisible(False)
        app.mainWindow.setWindowTitle('Depth Scanner')
        app.mainWindow.show()
        app.mainWindow.resize(920, 600)
        app.mainWindow.move(0, 0)

        view = app.view

        globalsDict['app'] = app
        globalsDict['view'] = view


    poser = PoserClient(use_director=VISUALIZE, visualize=VISUALIZE)

    def single_shot_function():
        poser.test_poser_on_example_data()


    if VISUALIZE:
        TimerCallback(callback=single_shot_function).singleShot(0)
        app.app.start(restoreWindow=True)
    else:
        poser.test_poser_on_example_data()


