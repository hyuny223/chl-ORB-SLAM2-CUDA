# chl_orbslam2_cuda

# 1. Goal of this project
Goal of this project is to minimize run time and RMSE of ORB_SLAM2.  

# 2. How to approach to achieve goal
My team focused on Frontend and Backend.  
## 1. Search Bottleneck
First, using easy-profiler, we searched bottleneck of ORB_SLAM2.  

Frontend : ORBextraction takes long time in Frontend  
![image](https://user-images.githubusercontent.com/58837749/184827344-c4a10d40-ffa9-4f52-8550-afcec9b60168.png)

Backend : LoopClosing takes long time in Backend
![image](https://user-images.githubusercontent.com/58837749/184828095-c63585c7-9b32-4e4a-9db2-dac567d7052a.png)  

Loopclosing in Backend
![image](https://user-images.githubusercontent.com/58837749/184828124-e2cf3c8b-edea-4f9c-bc39-e3e28e5a9482.png)

## 2. Adjust Parameter
Second, we decided to adjust parameter in Frontend and Backend.  
In Frontend, we can adjust such as the number of features for ORB detection.  
In Backend, we can adjust such as functions for non-linear optimization like Gauss-Newton, Levenberg, dogleg etc, Robust kernel like Huber, Cauchy etc, parameters of RANSAC etc.

## 3. Use CUDA
Third, we tried to apply cuda wherever it could be used.  
We uses this open source.  
[go to the github for ORB_SLAM2_CUDA](https://github.com/hoangthien94/ORB_SLAM2_CUDA.git)

# 3. Results
## 1. Frontend
![image](https://user-images.githubusercontent.com/58837749/184836382-db34521a-26f8-48ec-82fe-e70821e3e94b.png)


## 2. Backend
![image](https://user-images.githubusercontent.com/58837749/184835526-0483081c-72a6-4bf2-adee-42eb6cc76d23.png)

# 4. How To Run
Please refer to the sites below.  
ORB_SLAM2 : [here](https://github.com/raulmur/ORB_SLAM2.git)  
ORB_SLAM2_CUDA : [here](https://github.com/hoangthien94/ORB_SLAM2_CUDA.git)  
```bash
$ ./build.sh
$ python3 load.py
```
In "load.py" script, you can modify parameters needed in Backend.  
If you need to run CUDA, you should modify the command in "load.py" for CUDA.
