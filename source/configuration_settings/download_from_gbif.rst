============================
Downloading Images from GBIF
============================

.. note:: An interactive Streamlit GUI is in the works, stay tuned!

.. code-block:: yaml

    leafmachine:
        project:
            # If location is GBIF, set the config in:
            # LeafMachine2/configs/config_download_from_GBIF_all_images_in_file OR
            # LeafMachine2/configs/config_download_from_GBIF_all_images_in_filter
            image_location: 'GBIF' # str |FROM| 'local' or 'GBIF'
            # all = config_download_from_GBIF_all_images_in_file.yml 
            # filter = config_download_from_GBIF_all_images_in_filter.yml
            GBIF_mode: 'all'  # str |FROM| 'all' or 'filter'. 