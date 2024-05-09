=================
Landmark Detector
=================

Primary options (landmark_detector)
------------------------------------

⭐ To enable landmark detection set ``landmark_whole_leaves: True``. LM2 v.2.1 does not support landmark detection for partial leaves, so set ``landmark_whole_leaves: False``. 

⭐ Please refer to the publication for an explanation of why ``minimum_confidence_threshold: 0.1`` is set so low. We found this to be a happy spot, but tweaking the value up or down may improve results for some taxa. 

Set ``do_save_prediction_overlay_images: True`` to save the landmarking overlay images to a PDF file for review. *To show the landmark detections in the whole specimen summary images, this needs to be set to `True` too*. This applies to ``do_save_final_images: True`` as well.

Do not change the detecor names. LM2 v.2.1 only include networks from the publication. Additional networks will be available in future releases. 

.. code-block:: yaml

    leafmachine:
        landmark_detector:
            # ./leafmachine2/component_detector/runs/train/detector_type/detector_version/detector_iteration/weights/detector_weights
            landmark_whole_leaves: True
            landmark_partial_leaves: False
            
            detector_type: 'Landmark_Detector_YOLO' 
            detector_version: 'Landmarks'
            detector_iteration: 'Landmarks'
            detector_weights: 'last.pt'
            minimum_confidence_threshold: 0.1
            do_save_prediction_overlay_images: True 
            ignore_objects_for_overlay: [] # list[str] # list of objects that can be excluded from the overlay # all = null
            use_existing_landmark_detections: null

            do_show_QC_images: False
            do_save_QC_images: True

            do_show_final_images: False
            do_save_final_images: True