================
Project Settings
================

Primary options (project)
-------------------------

⭐ Settings that tell LeafMachine2 where things are and where you want to save output files.

Strings must be inside '' or "". Forgetting them, or missing one, will cause errors.

Type ``null`` for the default value.

Pointing to directories. 

.. code-block:: yaml

    leafmachine:
        project:
            dir_output: '/full/path/to/output/directory' # LeafMachine2 will build the output dir structure here
            run_name: 'informative_run_name' # LeafMachine2 will build the output dir structure here
            dir_images_local: '/full/path/to/directory/containing/images' # This can also be a dir with subdirs

Set ``image_location`` to ``'local'`` if you already have images, or to ``'GBIF'`` if you will configure LM2 to download the images.

More information about downloading images `here <download_from_gbif.html>`_.

.. code-block:: yaml

    leafmachine:
        project:
            image_location: 'local' # str |FROM| 'local' or 'GBIF' # 
            GBIF_mode: 'all' 

⭐ Batch processing. Set based on PC hardware. We recommend 64 GB of RAM for ``batch_size: 50`` and ``num_workers: 4``. 

On your first run, set ``batch_size: 5 num_workers: 2`` just to make sure everything is working, then increase to taste. 

.. code-block:: yaml

    leafmachine:
        project:
            batch_size: 50 # default = 20
            num_workers: 2 # default = 2


Secondary (project)
-------------------

These are less common options. Do not change unless you need to. Set to ``null`` if not in use. 

These settings will find the GBIF images and occurrence CSV files, create a combined.csv file, and enable you to merge these data with the LM2 output data files. Requires images to already be downloaded and ``image_location: 'local'``. 

.. code-block:: yaml

    leafmachine:
        project:
            path_combined_csv_local: '/full/path/to/save/location/of/run_name_combined.csv' # do set the name of the combined file here
            path_occurrence_csv_local: '/full/path/to/occurrence_csv' # just the dir that containes the txt or csv file
            path_images_csv_local: '/full/path/to/images_csv' # just the dir that containes the txt or csv file


If you are reprocessing the same group of images multiple times, you can point LM2 to the *first* ACD and PCD detection files to save time. This assumes that you want to use the same ACD and PCD detections each time. Set to ``null`` to tell LM2 to run ACD and PCD each time. 

.. code-block:: yaml

    leafmachine:
        project:
            use_existing_plant_component_detections: '/full/path/to/output/directory/informative_run_name/Plant_Components/labels'
            use_existing_archival_component_detections: '/full/path/to/output/directory/informative_run_name/Archival_Components/labels'


This will allow you to select a random subset of a large image set. 

Setting ``n_images_per_species: 10`` will randomly pick 10 images from the species in 
``species_list: '/full/path/to/existing/species/names/10_images_per_species.csv'`` 
and save them to ``dir_images_subset: '/full/path/to/save/location/of/new/subset'``. 

Set ``process_subset_of_images: True`` to use, ``process_subset_of_images: False`` to skip.

The species list is a CSV file with this format:


    +----------------------------------+-------+
    | species                          | count |
    +----------------------------------+-------+
    | Ebenaceae_Diospyros_virginiana   | 3263  |
    +----------------------------------+-------+
    | Ebenaceae_Diospyros_ferrea       | 614   |
    +----------------------------------+-------+
    | Ebenaceae_Diospyros_iturensis    | 552   |
    +----------------------------------+-------+
    | Ebenaceae_Diospyros_mespiliformis| 478   |
    +----------------------------------+-------+
    | etc...                           |       |
    +----------------------------------+-------+


.. code-block:: yaml

    leafmachine:
        project:
            process_subset_of_images: True
            dir_images_subset: '/full/path/to/save/location/of/new/subset'
            n_images_per_species: 10
            species_list: '/full/path/to/existing/species/names/10_images_per_species.csv' 


