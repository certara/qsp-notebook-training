# Runs all the Jupyter notebooks in this directory and subdirectories, checking for errors.
#
# How to use:
#
#     If running in JupyterLab:
#          1. Open this file in the text editor
#          2. Right-click inside the editor window and select "Create Console for Editor"
#          3. In the menu that pops up, choose "pixi" for the kernel and click the "Select" button
#          4. In the top menu bar, click Run -> Run All Code
#     If running in a terminal:
#          Run the following command: pixi run python _test_training_notebooks.py

import pytest, os, sys
import __main__ as main

# Get directory this file is in
if hasattr(main, "__file__"):
    # __file__ only exists if this is being run from a terminal
    dir_path = os.path.dirname(os.path.realpath(__file__))
else:
    # Use current working directory when running from JupyterLab
    dir_path = os.getcwd()

# Run all notebooks
# Force it to use the "python3" kernel. Note that this is the python3 kernel
# inside the pixi environment, not the one outside.
retval = pytest.main(["--nbmake", dir_path, "--nbmake-kernel", "python3"])
if retval != pytest.ExitCode.OK:
    sys.exit(1)
