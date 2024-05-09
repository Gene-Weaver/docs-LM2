==================
Cropped Components
==================

Primary options (cropped_components)
------------------------------------

Saves cropped RGB images based on detections from the ACD and PCD. 

⭐ If you want to save none, set ``do_save_cropped_annotations: False``

If you want to save all cropped images (which is heaps and heaps of images...), set ``save_cropped_annotations: ['save_all']```

Use the template below to pick and choose classes to save. 

⭐ Set ``binarize_labels: True`` to use a ViT ML network to clean labels and rulers. 

.. note:: This will binarize all classes in ``save_cropped_annotations: ['label', 'ruler']``.

Set ``binarize_labels_skeletonize: True`` to skeletonize the binary image. Not useful for most situations. 

.. code-block:: yaml

    leafmachine:
        cropped_components:
            # add to list to save, lowercase, comma seperated, in 'quotes'
            # archival |FROM| 
            #           ruler, barcode, colorcard, label, map, envelope, photo, attached_item, weights
            # plant |FROM| 
            #           leaf_whole, leaf_partial, leaflet, seed_fruit_one, seed_fruit_many, flower_one, flower_many, bud, specimen, roots, wood
            do_save_cropped_annotations: True
            save_cropped_annotations: ['label', 'ruler'] # 'save_all' to save all classes
            save_per_annotation_class: True # saves crops into class-names folders
            binarize_labels: True
            binarize_labels_skeletonize: False