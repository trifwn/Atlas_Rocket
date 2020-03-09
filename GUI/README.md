# :chart_with_upwards_trend:Telemetry GUI
We have implemented a graphical user interface (GUI) to monitor all of the measurements that we receive from the sensors.

## :file_folder:Structure
```
GUI/
├── data/ 
├── assets/
├── utils/
│   ├── __init__.py
│   └── dataloading.py
├── config.py
├── importing_modules.py
├── app.py
├── requirements.txt
└── README.md
```

## :nut_and_bolt:Setup

1.	[Install](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) conda
2.  In all three major desktop platforms (Linux, macOS, and Windows), [OpenGL](https://www.khronos.org/opengl/wiki/Getting_Started#Downloading_OpenGL) more or less comes with the system. However, you will need to ensure that you have downloaded and installed a recent driver for your graphics hardware.
3.  Use the terminal or an Anaconda Prompt for the following steps:
	
	To create and activate an environment:
	```
	conda create -n atlasGUI python=3
	source activate atlasGUI
	```
	Inside the GUI folder run the following command to install the necessary packages:
	```
	pip install -r requirements.txt
	```

##  :joystick:Usage
Use the terminal or Anaconda Prompt inside the GUI folder to start the deployment server using the following command:
```
python app.py
```
and click [here](http://127.0.0.1:8050/) to access it.