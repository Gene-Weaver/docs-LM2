.. _data_cleaning:

==============================
Data Cleaning Considerations
==============================


LeafMachine **WILL** automatically edit illegal characters out of file names and replace them with ``_`` or ``-``.

Illegal characters in file names include anything that is not a letter or number or ``_`` or ``-``.

Specifically, we use this function to clean names:

.. code-block:: python

    name_cleaned = re.sub(r"[^a-zA-Z0-9_-]","-",name)

Spaces will become ``_``.

Also, all images will be rotated to be vertical - downstream processes rely on this. This check will also **delete** any corrupt image files. We found that ~1/10,000 downloads from GBIF produce a corrupt file and this is how we chose to deal with it.

* Illegal character replacement and image rotation can be turned off, but doing so will likely cause bad things to happen. Change these config settings to ``False``:

.. code-block:: python

    leafmachine:
        do:
            check_for_illegal_filenames: False 
            check_for_corrupt_images_make_vertical: False

If these processing steps sound like they will significantly impact your raw images, then *please* make sure that you have back up copies of your original images. If you downloaded your images from GBIF, this should not be a worry. But if you are processing your own custom images, then please only run LeafMachine2 on copies of the original images. No one has a good day if a file is deleted! If you have concerns please reach out `LeafMachine.org <https://LeafMachine.org/>`.

If your taxa names (the actual file name) have special characters, LeafMachine2 will replace them with ``-``. Python code in general does not play nice with characters like:

* Viola lutea x tricolor x altaica  ➡  Viola_lutea_x_tricolor_x_altaica  
* Viola lutea x tricolor x altaica  ➡  Viola_lutea\_-`tricolor`-_altaica  (if the X is not the letter X)
* Dichondra sp. Inglewood (J.M.Dalby 86/93)  ➡  Dichondra_sp-_Inglewood_-J.M.Dalby_86-93-
* Sida sp. Musselbrook (M.B.Thomas+ MRS437)  ➡ Sida_sp-_Musselbrook_-M-B-Thomas-_MRS437-

These special characters should not be used in file names (in general, not just for LeafMachine2). 

Having spaces in names or directories can cause unexpected problems.

* ✔ ``./dir_names_with_underscores/file_name_with_underscores``
* ✔ ``./dir-names-with-dashes/file-name-with-dashes``
* ❌ ``./not great dir names/not great file names``

