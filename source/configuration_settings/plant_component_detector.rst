========================
Plant Component Detector
========================

Primary options (plant_component_detector)
------------------------------------------

⭐ This is probably the most impactful setting in LM2: ``minimum_confidence_threshold: 0.5 ``
Higher values like ``0.9`` will detect fewer leaves, lower values like ``0.10`` will detect many leaves. 

Set ``do_save_prediction_overlay_images: True`` to save the YOLOv5 overlay images. These also show the bbox confidence and are useful for determining why some objects are not getting detected.

Set ``ignore_objects_for_overlay: ['leaf_partial]`` to hide predictions from the YOLOv5 overlay images. Can be useful for very cluttered images. Use the same names as in `Primary options (cropped_components) <cropped_components.html>`_.

Do not change the detecor names. LM2 v.2.1 only include networks from the publication. Additional networks will be available in future releases. 

.. code-block:: yaml

    leafmachine:
        plant_component_detector:
            # ./leafmachine2/component_detector/runs/train/detector_type/detector_version/detector_iteration/weights/detector_weights
            detector_type: 'Plant_Detector' 
            detector_version: 'PLANT_GroupAB_200'
            detector_iteration: 'PLANT_GroupAB_200'
            detector_weights: 'best.pt'
            minimum_confidence_threshold: 0.5 #0.2
            do_save_prediction_overlay_images: True
            ignore_objects_for_overlay: []