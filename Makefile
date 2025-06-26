# Makefile for decompress-script

# Change this if you renamed your entry‐point script
LAUNCHER := dicom_decompressor/dicom_decompressor.py
# Name of the final executable
BIN_NAME := dicom-decompress

.PHONY: all clean build exec

all: build

# Clean out PyInstaller artifacts and old dist
clean:
	rm -rf build/ dist/ __pycache__ *.spec
	find dicom_decompressor -name '__pycache__' -exec rm -rf {} +

# Build the standalone executable
build: clean
	poetry run pyinstaller \
		--onefile \
		--name $(BIN_NAME) \
		--console \
		$(LAUNCHER)

# (Optional) Copy the executable somewhere, make it executable, etc.
exec: build
	chmod +x dist/$(BIN_NAME)
	@echo "Executable is at: dist/$(BIN_NAME)"