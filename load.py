#!/usr/bin/env python3

import os,sys

kernel_list = ["Huber", "Cauchy"]

for d2 in range(1,11):
    for d3 in range(1,11):
        for iter in range(5,12,5):
            for minInliers in range(20,31):
                for maxIterations in range(300, 351):
                    for kernel in kernel_list:
                        try:
                            command = f"./Examples/Stereo/stereo_kitti Vocabulary/ORBvoc.txt Examples/Stereo/KITTI00-02.yaml ../kitti/sequences/00 \
                                {d2} {d3} {iter} {minInliers} {maxIterations} {kernel}"
                            os.system(command)
                        except:
                            print("exit")
                            sys.exit(0)

