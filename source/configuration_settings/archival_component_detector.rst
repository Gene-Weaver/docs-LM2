===========================
Archival Component Detector
===========================

Primary options (archival_component_detector)
---------------------------------------------

⭐ Archival components are detected exceptionally well. We have seen very few errors or problems with ``minimum_confidence_threshold: 0.5`` and recommend leaving this alone unless your images are substantially different from an average herbarium specimen. 

Set ``do_save_prediction_overlay_images: True`` to save the YOLOv5 overlay images. These also show the bbox confidence and are useful for determining why some objects are not getting detected.

Set ``ignore_objects_for_overlay: ['label]``` to hide predictions from the YOLOv5 overlay images. Can be useful for very cluttered images. Use the same names as in `Primary options (cropped_components) <cropped_components.html>`_.

Do not change the detector names. LM2 v.2.1 only include networks from the publication. Additional networks will be available in future releases. 

.. code-block:: yaml

    leafmachine:
        archival_component_detector:
            # ./leafmachine2/component_detector/runs/train/detector_type/detector_version/detector_iteration/weights/detector_weights
            detector_type: 'Archival_Detector' 
            detector_version: 'PREP_final'
            detector_iteration: 'PREP_final'
            detector_weights: 'best.pt'
            minimum_confidence_threshold: 0.5
            do_save_prediction_overlay_images: True
            ignore_objects_for_overlay: []