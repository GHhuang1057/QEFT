# QEFT (Qualcomm Flashing Tool based on open-source edl project)

# Currently in development phase - may not be functional

## [ZH_CN](README.md)/EN

### Project Overview

#### QEFT is a GUI-based Qualcomm flashing tool built on the open-source edl project, designed to simplify the flashing process for Qualcomm devices. Written in Python with PyQt5 for the GUI framework, QEFT provides an intuitive interface for device flashing operations.

### Structure (Development Notes)
- `main.py`: Main program, launches the GUI interface
- `core/`: Core logic (to be implemented)
- `ui/`: GUI design files
- - `qeft_main_window.py`: Main window implementation
- - `qeft_start_window.py`: Startup window implementation
- `res/`: Resource files
- - `edl/`: Contains the edl project files

### Development Setup
Refer to the API documentation:  
[BK_EDLClient_API Documentation](BK_EDLClient_API_README.md)

~~~
Important: This project builds on the open-source edl project. The edl source code is not included - you must clone it into the res/edl folder before use:

cd res
git clone https://github.com/bkerler/edl.git
pip3 install -r requirements.txt
~~~

## Development Goals: Updated 2025/6/14
### Current Objectives
#### Improve device detection and loading logic (refer to edl repository README and API docs)
#### Enhance main interface (`ui/qeft_menu_window.py` / `menu.ui`)
### Target completion: July 5
---

### Usage Instructions
[BK_EDLClient_API Documentation](BK_EDLClient_API_README.md)

### Contributors
#### *630*
#### *kirin7098*
#### *huang1057*
---
### Welcome to Contribute Code
##### You can submit suggestions in issues or directly submit PRs
##### Code contributions must comply with the GPL-V3 open-source license
##### Code contributions require experience in Python and PyQt5 development