# DICOM Decompressor

A simple CLI tool to recursively decompress compressed DICOM files into a mirrored `decompress/` folder alongside the input directory.

## VIDEO

[VIDEO INSTRUCTIONS](https://www.loom.com/share/5e212c51b79542d89beb80251265b281)

## Features

- Recursively finds and decompresses all DICOM files with compressed transfer syntaxes.
- Mirrors the original directory structure under a new `decompress/` folder at the same level as your source directory.
- Leaves original files untouched.
- Reports progress and any errors encountered.

## Installation

### Part 1: One-Time Setup (Python 3.11 & Homebrew)

1. **Open Terminal**

   - Find Terminal in Applications > Utilities, or search for it via Spotlight (Cmd + Space).

2. **Install Homebrew** (if you don’t have it)

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Verify Homebrew Installation**

   ```bash
   brew --version
   ```

4. **Install Python 3.11**

   ```bash
   brew install python@3.11
   ```

5. **Add Python 3.11 to Your PATH**
   ```bash
   echo 'export PATH="/opt/homebrew/opt/python@3.11/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### Part 2: Set Up a Python Virtual Environment

> **Why?** Virtual environments keep your project’s Python tools and libraries organized and separate from your system Python.

1. **Navigate to your working directory** (e.g., Documents):

   ```bash
   cd ~/Documents
   ```

2. **Create the virtual environment**:

   ```bash
   python3.11 -m venv brainstorme-env
   ```

3. **Activate the virtual environment**:
   ```bash
   source brainstorme-env/bin/activate
   ```
   - Your prompt will show `(brainstorme-env)` when active.
   - To deactivate later:
     ```bash
     deactivate
     ```

### Part 3: Install & Run Brainstorme CLI

1. **Download the Brainstorme Tool**

   Use the file that ryan uploaded / proviedd to you or in the dist folder. Make sure it's accessible from your finder.

2. **Install the Tool**  
   With your virtual environment active:

   ```bash
   pip install /path/to/decompress_script-0.1.0.tar.gz
   ```

   > _Tip:_ Drag the file from Finder into Terminal to populate the full path.

3. **Test Your Installation**

   ```bash
   dicom-decompress --help
   ```

4. RUN
   ```bash
   poetry run dicom-decompress /path/to/your/dicom_directory
   ```

#### Quick Tips for CLI Beginners

- Commands are **case sensitive**.
- `~` is shorthand for your home folder (`/Users/yourname/`).
- Press **Tab** to auto-complete file and folder names.
- If you see “permission denied” or “command not found,” double-check spelling and your PATH setup.
