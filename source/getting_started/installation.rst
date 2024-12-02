============
Installation
============

.. attention:: To complete the steps below, you must have installed all of the prerequisites on your machine. If you haven't, please go to prerequisites and install them. 

Cloning the leafmachine2 repository
-----------------------------------

1. Open a terminal window and ``cd`` into a directory that you would like to install leafmachine2 in.
2. Clone the leafmachine2 repository from GitHub using ``git clone https://github.com/Gene-Weaver/LeafMachine2.git``. This will create a new directory called LeafMachine2.
3. Move into the newly created directory by using ``cd LeafMachine2``.

Setting up a python virtual environment (venv)
----------------------------------------------

A virtual environment is a tool to keep the dependencies required by different projects in separate places, by creating isolated python virtual environments for them. This avoids any conflicts between the packages that you have installed for different projects. It makes it easier to maintain different versions of packages for different projects.

The following instructions assume you are in the leafmachine2 directory. You may use ``pwd`` to see your current working directory to confirm this.

.. note:: You must name your virtual environment venv_LM2 if you want to use the desktop shortcut

.. tab-set::

    .. tab-item:: Ubuntu 20.04+
        :sync: key1

        1. Show that a venv is not currently active: ``which python``
        2. Create a virtual environment named venv_LM2: ``python -m venv venv_LM2``
        3. Activate the virtual environment: ``source ./venv_LM2/bin/activate``
        4. Confirm that the venv is active (output should differ from 1.): ``which python``

    .. tab-item:: Windows 10
        :sync: key2

        1. Show that a venv is not currently active: ``python --version``
        2. Create a virtual environment named venv_LM2: ``python -m venv venv_LM2``
        3. Activate the virtual environment: ``.\venv_LM2\Scripts\activate``
        4. Confirm that the venv is active (output should differ from 1.): ``python --version``

The instructions below assume that you have successfully created a virtual environment and have activated it.

Installing required packages with pip 
-------------------------------------

We include a ``requirements.txt`` file in the ``LeafMachine2/requirements/`` folder. If you experience version incompatibility following the instructions below, please refer to ``LeafMachine2/requirements/requirements_all.txt`` for an exhaustive list of packages and versions that are officially supported.

:bdg-info:`tip` You can click on :far:`clipboard` in the top right of the code block to copy the entire contents to your clipboard for easier pasting into your terminal.

.. tab-set::

    .. tab-item:: Ubuntu 20.04+ or macOS
        :sync: key1

        **Quick Installation**

        Install the python packages as outlined in the requirements

        .. code-block:: bash 

            pip install -r requirements.txt

        If your computer has a GPU use

        .. code-block:: bash 

            pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113

        If your computer *does not have* a GPU or you are using a Mac

        .. code-block:: bash

            pip3 install torch torchvision torchaudio
        
        **Detailed Installation**

        Install wheel

        1. .. code-block:: bash
            
            python -m pip install wheel

        Update pip and setuptools

        2. .. code-block:: bash 
        
            python -m pip install --upgrade pip setuptools

        Install the required dependencies to use LeafMachine2

        3. .. code-block:: bash 
        
            pip install -r requirements.txt

        Install pycococreator

        4. .. code-block:: bash
        
            pip install git+https://github.com/waspinator/pycococreator.git@fba8f4098f3c7aaa05fe119dc93bbe4063afdab8#egg=pycococreatortools


        Install COCO annotation tools and a special version of Open CV

        5. .. code-block:: bash
        
            pip install pycocotools>=2.0.5 opencv-contrib-python>=4.7.0.68

        LeafMachine2 algorithms require PyTorch version 1.11 for CUDA version 11.3+. If your computer does not have a GPU, then use the CPU version and the CUDA version is not applicable. PyTorch is large and will take a bit to install.

        If your computer has a GPU
 
        6. .. code-block:: bash
        
            pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113

        If your computer does not have a GPU or you are using a Mac

        6. .. code-block:: bash

            pip3 install torch torchvision torchaudio

        Install ViT for PyTorch. ViT is used for segmenting labels and rulers. The DocEnTr framework that we use for document image segmentation requires an older verison of ViT, the most recent version will cause an error.

        7. .. code-block:: bash
        
            pip install vit-pytorch==0.37.1

    .. tab-item:: Windows 10+
        :sync: key2

        **Quick Installation**
        
        1. .. code-block:: bash

            pip install -r requirements.txt

        2. .. code-block:: bash

            pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113

        3. .. code-block:: bash

            pip install pywin32

        **Detailed Installation**

        Install the required dependencies to use LeafMachine2

        1. .. code-block:: bash
        
            pip install -r requirements.txt

        Install pycococreator

        2. .. code-block:: bash
        
            pip install git+https://github.com/waspinator/pycococreator.git@fba8f4098f3c7aaa05fe119dc93bbe4063afdab8#egg=pycococreatortools

        Install COCO annotation tools, a special version of Open CV, and pywin32 for creating the desktop shortcut.

        3. .. code-block:: bash
        
            pip install pywin32 pycocotools>=2.0.5 opencv-contrib-python>=4.7.0.68
        
        Leafmachine2 algorithms require PyTorch version 1.11 for CUDA version 11.3+. If your computer does not have a GPU, then use the CPU version and the CUDA version is not applicable. PyTorch is large and will take a bit to install.

        4. .. code-block:: bash
        
            pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
        
        Install ViT for PyTorch. ViT is used for segmenting labels and rulers. The DocEnTr framework that we use for document image segmentation requires an older verison of ViT, the most recent version will cause an error.

        5. .. code-block:: bash
        
            pip install vit-pytorch==0.37.1

Troubleshooting CUDA
--------------------

- CUDA issues can be extremely frustrating. 
- Start by finding your current CUDA version or installing the most recent CUDA version that is compatible with your GPU. 
- Try installing the old version of PyTorch listed in these docs.
- If that works, great! If not, you can install the [latest pytorch release](https://pytorch.org/get-started/locally/) for your specific OS and CUDA version.
- If that fails, you might have a CUDA installation issue. 
- If you cannot get the GPU working, then you can install PyTorch with CPU only, avoiding the CUDA problem entirely, but that is not recommended given that LeafMachine2 is designed to use GPUs. The components that rely on ViT (binarization of labels) will *NOT* work without a GPU. The leaf segmentation may not work either, sometimes it does, sometimes not. 
- We have also validated CUDA 12.4 with PyTorch 2.X. If you have success with other versions of CUDA/pytorch, let us know and we will update our instructions. 