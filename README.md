# CS-GO-Artitificial-Intelligence-Bot
AI project done in the summer of 2022 as a part of Institute Summer Technical Project organized by Institute Technical Council, Indian Institute of Technology, Bombay
Herein, We plan on the creating an AI bot which plays Counter Strike : Global Offensive completely by itself. We plan on to using YOLOv4 custom trained for CS:G0 for detecting enemy on the screen and then use deterministic algorithm along with RL to calculate the best course of action for shooting the enemy in frame. Other parts of bot include exploring the world and deciding actions regarding when it should move in what direction or when should it reload. We plan to implement deterministic algorithm for moving along the path not just keep moving towards a wall. 
So far we have integrated YOLOv4 model customized over CS:G0 dataset using transfer learning. Our next step would be filtering out the bounding boxes and write a Q-Learning algorithm for finding the correct keyboard mous input to provide to shoot the enemy. 
We would recommend using CUDA for high speed as the YOLOv4 takes quite a time to give bounding boxes. We got the YOLOv4 model customized over CS:GO dataset from this github repository - https://github.com/pythonlessons/YOLOv3-object-detection-tutorial/tree/master/YOLOv3-CSGO-detection. We changed some parts of this repository because the libraries used were outdated.

# Building Package (without CUDA)
1. Clone the repository using 'git clone git@github.com:namritaansh02/CS-GO-Artitificial-Intelligence-Bot.git'
2. Navigate to reach inside this repository. Run 'pip install -r requirements.txt'
3. In the logs folder extract all \*.7z together and you will get a single trained_weights_final.h5 file and place it in the same logs folder.
4. Run the window you want to capture on the top left corner of screen. You may adjust the size of windows you wish to capture by change the coordinates in screencapture.py file written in the ImageGrab command.
5. Run python screencapture.py in terminal. Wait for some time and ignore the warnings you get, they are mostly about not having CUDA setup and  the CNN having stride length values at some points such that kernel is going beyond image size.

# Building Package (with CUDA)
1. Clone the repository using 'git clone git@github.com:namritaansh02/CS-GO-Artitificial-Intelligence-Bot.git'
2. In the logs folder extract all \*.7z together and you will get a single trained_weights_final.h5 file and place it in the same logs folder.
3. Install CUDA 11.6 using the methods exactly as mentioned on this website. https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html 
4. Setup CuDNN following the methods exactly as mentioned on this website. https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html. Note that get the version of CuDNN matching with CUDA 11.X
5. Setup Anaconda from here https://www.anaconda.com/products/distribution 
6. Open Anaconda Navigator. Create a new environment with some random name. 
7. Open Anaconda Prompt. Run 'conda activate {new environment name}'
8. Run 'pip install --upgrade tensorflow-gpu'
9. Navigate to reach inside this repository. Run 'pip install -r requirements.txt'
10. Run the window you want to capture on the top left corner of screen. You may adjust the size of windows you wish to capture by change the coordinates in screencapture.py file written in the ImageGrab command.
11. Run python screencapture.py in the same anaconda prompt.
