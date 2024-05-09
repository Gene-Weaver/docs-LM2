====
Data
====

Primary options (data)
----------------------

Configure data output. Currently, LM2 saves data to CSV files. JSON files are not going to be helpful for most situations. 

To apply the conversion factor to all measurements, set ``do_apply_conversion_factor: True``

To include the DWC data in the output files, set ``include_darwin_core_data_from_combined_file: True``

.. code-block:: yaml
    
    leafmachine:
        data:
            save_json_rulers: False
            save_json_measurements: False
            save_individual_csv_files_rulers: False
            save_individual_csv_files_measurements: False
            include_darwin_core_data_from_combined_file: False
            do_apply_conversion_factor: True