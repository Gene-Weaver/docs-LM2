.. _configuration_settings:

=============
Configuration
=============

Now you can run LeafMachine2, but unless you setup the configuration file, nothing will happen! LeafMachine2 has many many configurable settings. Here we will outline settings that most folks will use. The LeafMachine2.yaml file is grouped by component, but not all settings within a component group need to be (or should be) modified.

Most settings dictate which output files LeafMachine2 will save. Some dictate how many leaves will be extracted or which ML networks will be used.

To change settings in the LeafMachine2.yaml file we recommend using a VS Code or another IDE because they will help reduce errors. But any plain text editor will work (e.g. Notepad on Windows)

Open the file and customize the options described below.


The most important settings are marked with a ⭐. Begin with these settings and then explore adjusting other settings (if needed).

.. toctree::
    :maxdepth: 2
    :numbered:

    project
    cropped_components
    data
    overlay
    plant_component_detector
    archival_component_detector
    landmark_detector
    ruler_detection
    leaf_segmentation
    download_from_gbif
