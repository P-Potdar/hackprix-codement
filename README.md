# Deep fake detection Django Application

### Deepfake detector is a tool capable of detecting facially altered videos using ResNext and LSTM networks.
- The model is trained using over 700 videos and we achieved a prediction accuracy of 90%. 
- We also created a user-friendly web application using Django allowing users to upload videos for deepfake detection.

## Requirements:

- CUDA version >= 10.0 for GPU
- GPU Compute Capability > 3.0 


- Required modules are listed in the requirements.txt
```
Python >= v3.6
Django >= v3.0
```

# How to run the application on local machine

#### step 1: Download and Install Cuda version 12.1 (most compatible)

download link: https://developer.nvidia.com/cuda-12-1-0-download-archive

#### Step 2: Install requirements.txt 

#### Step 3: open folder Deep_fake_Django & start the server

`python manage.py runserver`

#### step 4: Go to localhost 127.0.0:8000 

#### step 5: Upload the video to be tested and select the bar to 40 frames. (Test videos are listed in folder - Test_Videos)