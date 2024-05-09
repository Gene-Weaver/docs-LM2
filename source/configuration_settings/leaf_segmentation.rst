=================
Leaf Segmentation
=================

Primary options (leaf_segmentation)
------------------------------------

⭐ Tell LM2 to segment ideal leaves by setting ``segment_whole_leaves: True`` and partial leaves by setting `segment_partial_leaves: False`. In general, there are *many* more partial leaves than ideal leaves. So segmenting partial leaves will *significantly* increase total processing time. Please refer to the publication for a more detailed overview of these settings. 

The LM2 leaf segmentation tool will try to segment all leaves that it sees, but we only want it to find one leaf, so we set ` keep_only_best_one_leaf_one_petiole: True` to tell LM2 to only keep the largest leaf and petiole. This is not perfect, but it gets the job done for now. 

⭐ To save all leaf mask overlays onto the full image as a PDF, set ``save_segmentation_overlay_images_to_pdf: True``

⭐ To save all leaf mask overlays onto the full image as individual images, set ``save_each_segmentation_overlay_image: True```

⭐ This saves each cropped leaf with its overlay to individual files ``save_individual_overlay_images: True`` and this sets the overlay line width ``overlay_line_width: 1``

⭐ LM2 can also save the masks to PNG files. To use the EFDs as the masks (these will be smooth compared to the raw mask) set ``use_efds_for_png_masks: False``

⭐ To save individual leaf masks, set ``save_masks_color: True``

⭐ To save full image leaf masks, set ``save_full_image_masks_color: True``

⭐ To save the RGB image, set ``save_rgb_cropped_images: True``

⭐ To measure length and width of leaves set ``find_minimum_bounding_box: True``

⭐ To calcualte EFDs set ``calculate_elliptic_fourier_descriptors: True`` and define the desired order with ``elliptic_fourier_descriptor_order: null``, the default is 40, which maintains detail.

We found no real need to change ``minimum_confidence_threshold: 0.7``, but you may find better results with adjustments. 

Do not change the ``segmentation_model``. LM2 v.2.1 only include networks from the publication. Additional networks will be available in future releases. 

.. code-block:: yaml

    leafmachine:
        leaf_segmentation:
            segment_whole_leaves: True
            segment_partial_leaves: False 

            keep_only_best_one_leaf_one_petiole: True

            save_segmentation_overlay_images_to_pdf: True
            save_each_segmentation_overlay_image: True
            save_individual_overlay_images: True
            overlay_line_width: 1 # int |DEFAULT| 1 
        
            use_efds_for_png_masks: False # requires that you calculate efds --> calculate_elliptic_fourier_descriptors: True
            save_masks_color: True
            save_full_image_masks_color: True
            save_rgb_cropped_images: True

            find_minimum_bounding_box: True

            calculate_elliptic_fourier_descriptors: True # bool |DEFAULT| True 
            elliptic_fourier_descriptor_order: null # int |DEFAULT| 40
            
            segmentation_model: 'GroupB_Dataset_100000_Iter_1176PTS_512Batch_smooth_l1_LR00025_BGR'
            minimum_confidence_threshold: 0.7 #0.7
            generate_overlay: False
            overlay_dpi: 300 # int |FROM| 100 to 300
            overlay_background_color: 'black' # str |FROM| 'white' or 'black'