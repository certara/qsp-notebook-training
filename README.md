# QSP Notebook Training

Welcome to the **QSP Notebook Training** repository. This resource is designed to provide hands-on training and examples for using Certara's Quantitative Systems Pharmacology (QSP) Platform through a notebook-based interface.

The training materials in this project are used in the live demonstrations and workshops provided by Certara's support team. By working through the provided examples, you will gain practical experience with workflows and tools commonly used in QSP modeling, including parameter optimization, simulations, and uncertainty analysis.

## Getting Started

### Install Python Environment
You can open a terminal and type: `pixi install`, although if you use the Pixi Kernel from Jupyterlab, this will be handled automatically.

### Two ways to Learn
1. `Intro Workshop`
2. `Sample Workflows`

## Organization

### `Intro Workshop`
Introductory workshop materials for Python and QSP concepts.
- **`00_Python_Intro/`**: Python introduction with Jupyter Notebooks for basic scripting, plotting, and scripting.
- **`01_QSP_Notebook_Intro/`**: QSP-focused Jupyter Notebooks for simulations, optimizations, and parameter scans.
- **`02_DoseTable_Tutorial/`**: Tutorials on dose table creation and usage.
- **`Model_Files/`**: Example model files for QSP workflows.
- **`Tables/`**: Example tables for data simulations and analyses.
- Additional examples like `tornado_plot_live_example.ipynb`.

### `Advanced Topics`
Contains advanced tutorials and examples on specific topics.
- **`00_pre_simulation_processing/`**: Processing data and working with PRISM files.
- **`00a_basic_python_training/`**: Basic Python training resources (includes `README.md` for this subdirectory).
- **`01_reaction_model_functions/`**: Examples for modeling reactions and analyzing outputs.
- **`02_simulation_functions/`**: Examples of infusion/injection simulations.
- **`03a_post_simulation_processing/`**,
- **`03b_plots/`**,
- **`03c_post_simulation_statistics/`**

### `Sample Workflows`
Demonstrates complete workflows, including:
- **`model_files/`**: Model files used for .
- **`tables/`**: Data tables used in simulations and analyses.
- Various Jupyter Notebooks for optimizations, parameter scans, and simulations.

### Top-Level Files
- **`pixi.lock`** & **`pixi.toml`**: Configuration files for the training Python environment.
- **`_test_training_notebooks.py`**: A script to automate running all Jupyter Notebooks within the project used for testing purposes.


### `data/`
Supplementary data files for various examples and workflows.
