FROM tensorflow/tensorflow:latest-gpu-py3

# Add all project files to container's root directory
ADD . /opt/

# Install all packages needed for program
RUN pip3 install -r /opt/requirements.txt

# Update!! 
RUN apt update -y

# These packages may be needed.
RUN apt install libsm6 libxext6 libxrender-dev -y -qq

# Install development tooling so I can work on-container.
# Comment this out for production
RUN apt install git vim -y -qq

# Decide what happens when you run the container.
# Make sure you run '-it'!
#ENTRYPOINT python3 /opt/mammclass.py /srv/datasets/BMvsMM_data_for_fine_tuning /opt/save/
ENTRYPOINT bash
