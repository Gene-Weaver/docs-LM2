=======
Overlay
=======


Primary options (overlay)
-------------------------

Configure the overlay settings for most of the summary output. 

⭐ Set ``save_overlay_to_pdf: True`` to save each summary image to a PDF page. This is useful for keeping the number of total output files low.

⭐ Set ``save_overlay_to_jpgs: True``` to save each summary image at full resolution.

Since we place roated bounding boxes around leaves, you can set ``ignore_plant_detections_classes: ['leaf_whole', 'leaf_partial', 'specimen']`` to hide the bounding boxes the come directly from the PCD. Same for ``ignore_archival_detections_classes: []`` and ``ignore_landmark_classes: []``, but we recommend leaving them empty.

⭐ Depending on your image size, you can increase or decrease these settings to change the thickness of overlay lines:

.. code-block:: yaml

        line_width_archival: 2 # int # thick = 6, thin = 1
        line_width_plant: 6 # int # thick = 6, thin = 1
        line_width_seg: 12 # int # thick = 12, thin = 1
        line_width_efd: 6 # int # thick = 6, thin = 1


These settings are a good starting point:

.. code-block:: yaml
    
    leafmachine:
        overlay:
            save_overlay_to_pdf: True
            save_overlay_to_jpgs: True
            overlay_dpi: 300 # int |FROM| 100 to 300
            overlay_background_color: 'black' # str |FROM| 'white' or 'black'

            show_archival_detections: True
            ignore_archival_detections_classes: []
            show_plant_detections: True
            ignore_plant_detections_classes: ['leaf_whole', 'leaf_partial', 'specimen']
            show_segmentations: True
            show_landmarks: True
            ignore_landmark_classes: []

            line_width_archival: 2 # int
            line_width_plant: 6 # int
            line_width_seg: 12 # int # thick = 12
            line_width_efd: 6 # int # thick = 3
            alpha_transparency_archival: 0.3  # float between 0 and 1
            alpha_transparency_plant: 0
            alpha_transparency_seg_whole_leaf: 0.4
            alpha_transparency_seg_partial_leaf: 0.3