=============
Prerequisites
=============

In order to run leafmachine2, you will need to ensure that you have the following setup. 

Software
--------

python ``v3.8.10 <==> v3.11`` 
    If you don't yet have python installed, you may follow the instructions at https://python.org. You can test that you have python installed by running ``python --version``. On mac, you may need to run ``python3 --version`` as the operating system comes with python2 bundled.
pip
    pip is required to install many additional software components from the project. You can test that you have pip installed by running ``pip --version``. If you need to install pip, you can following the instructions at https://pip.pypa.io/en/stable/installation/
PyTorch ``v1.11``
    Can work with PyTorch 2.X if you are comfortable with other dependencies and CUDA. 
git
    This is required to clone the repository from github. If you don't have git installed, you may follow the instructions at https://git-scm.com to install it on your machine.
CUDA ``v11.3`` 
    If utilizing a GPU. See Troubleshooting CUDA for more information

Hardware
--------
- A GPU with at least 8 GB of VRAM is required
- LeafMachine2 v.2.1 is RAM limited. A batch size of 50 images could potentially utilize 48 GB+ of system memory. Setting batch sizes to 20 will only increase the number of summary and data files, but performance speed differences are minimal.
- The PCD confidence threshold dictates RAM usage. More leaves detected -> more RAM to store more leaves and derived measurements until they are saved to batch files and summary images. 
- The number of leaves per image dictates RAM usage. Taxa with hundred of leaves per image (e.g. *Diospyros buxifolia*) will require much more RAM than taxa with few leaves per image (e.g. *Quercus alba*)
- For most PCs, set the number of workers to 2 or 4. If you have a high performance PC with 128 GB+ of RAM and a powerful CPU, then 8 workers and batch sizes of 100+ are possible. 