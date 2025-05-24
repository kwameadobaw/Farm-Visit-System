#!/bin/bash

# Make script executable
chmod +x build_files.sh

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python farmproject/manage.py collectstatic --noinput