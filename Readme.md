$$
# DICOM Decompressor

A simple CLI tool to recursively decompress compressed DICOM files into a mirrored `decompress/` folder alongside the input directory.

## VIDEO

[VIDEO INSTRUCTIONS](https://www.loom.com/share/6bfe6442047e4a42b75939abe67cc0a2)

## Features

- Recursively finds and decompresses all DICOM files with compressed transfer syntaxes.
- Mirrors the original directory structure under a new `decompress/` folder at the same level as your source directory.
- Leaves original files untouched.
- Reports progress and any errors encountered.

## Using the DICOM Decompressor

Follow these steps to decompress your DICOM files, even if you're new to the command line:

1. **Locate the executable**

   - After building or downloading, you’ll have an executable file named `dicom-decompress` (on macOS) inside the `dist/` folder.
   - Open Finder and navigate to your project’s `dist/` directory to see `dicom-decompress`.

2. **Open Terminal**

   - In Finder, go to **Applications > Utilities** and double-click **Terminal**, or press **Cmd + Space**, type “Terminal” and hit Enter.
   - A window with a prompt (e.g. `ryan@MacBook-Pro ~ %`) will appear.

3. **Drag & drop the executable**

   - In Finder, click and drag `dist/dicom-decompress` into the Terminal window.
   - This will paste the full path to the executable.

4. **Add the folder to process**

   - After the executable path in Terminal, type a space, then drag and drop the folder containing your DICOM files.
   - Example final command:

   ```bash
   /Users/ryan/Developer/UCLA/decompress-script/dist/dicom-decompress /Users/ryan/Downloads/nitro
   ```

5. **Run the command**

   - Press **Enter**.
   - The tool will print progress messages as it decompresses files into a new `decompress/` folder alongside your source directory.

6. **(Optional) Run anywhere**
   - To avoid dragging every time, you can move the executable into a folder in your PATH:
     ```bash
     sudo cp dist/dicom-decompress /usr/local/bin/
     ```
   - Then simply type:
     ```bash
     dicom-decompress /path/to/your/dicom_folder
     ```
   - and press **Enter**.

---

**Troubleshooting**

- **“Permission denied”**: Make the file executable:
  ```bash
  chmod +x dist/dicom-decompress
  ```
- **“command not found”**: Ensure you included a space before dragging the DICOM folder, and that the path is correct.

---

Now you’re ready to decompress DICOMs without memorizing any commands—just drag, drop, and go!
$$
