#!/bin/bash

# Run this shell script after you have executed the command 
# git clone https://github.com/trifwn/Atlas_Rocket.git 'Atlas_Rocket'

DIR=$(pwd)
GUI=${DIR}/Atlas_Rocket/GUI

platform='unknown'
unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
   platform='linux'
elif [[ "$unamestr" == 'Darwin' ]]; then
   platform='OSX'
fi

# Install conda
if ! [ -x "$(command -v conda)" ]; then

    if [ $platform == 'linux' ];then 

        # Download the Miniconda3 Bash Script
        cd /tmp
        curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

        # Verify the Data Integrity of the Installer
        sha256sum Miniconda3-latest-Linux-x86_64.sh

        # Run the Miniconda Script
        bash Miniconda3-latest-Linux-x86_64.sh

        # Activate Installation
        source ~/.bashrc

    elif [ $platform == 'OSX' ];then 

        # Install homebrew
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

        # Install wget
        brew install wget

        # Download the Miniconda3 Bash Script
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

        # Verify the Data Integrity of the Installer
        shasum -a 256 Miniconda3-latest-MacOSX-x86_64.sh

        # Run the Miniconda Script
        bash Miniconda3-latest-Linux-x86_64.sh

        # Activate Installation
        source ~/.bashrc    
    else 
        echo "Unknown platform"
    fi

else:
    conda update conda
fi


# Create enviroment & activate it
conda create -n GUI python=3
source activate GUI

# Install dependencies
conda install pip
pip install -r requirements.txt

cd $GUI

# Run the server
python app.py