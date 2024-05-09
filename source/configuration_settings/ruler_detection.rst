===============
Ruler Detection
===============

Primary options (ruler_detection)
---------------------------------

⭐ Set these to save different versions of ruler QC images:

.. code-block:: yaml

    save_ruler_validation: False # the full QC image, includes the squarified image and intermediate steps
    save_ruler_validation_summary: True  # the recommended QC image
    save_ruler_processed: False # just the binary ruler

To limit conversion factor determination to highly confident rulers, set `minimum_confidence_threshold: 0.8`.
We find that `minimum_confidence_threshold: 0.4` is fine in general, though. 

Do not change the detecor names. LM2 v.2.1 only include networks from the publication. Additional networks will be available in future releases. 

.. code-block:: yaml

    leafmachine:
        ruler_detection:
            detect_ruler_type: True # only True right now
            ruler_detector: 'ruler_classifier_38classes_v-1.pt'  # MATCH THE SQUARIFY VERSIONS
            ruler_binary_detector: 'model_scripted_resnet_720_withCompression.pt'  # MATCH THE SQUARIFY VERSIONS
            minimum_confidence_threshold: 0.4
            save_ruler_validation: True # save_ruler_class_overlay: True
            save_ruler_validation_summary: True  # save_ruler_overlay: True 
            save_ruler_processed: False # this is the angle-corrected rgb ruler