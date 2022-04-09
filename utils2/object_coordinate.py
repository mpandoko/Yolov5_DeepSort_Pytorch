#tugas akhir by michael
import torch
import numpy as np

#Calculating Depth
def calcdepth(xywh, distance, depth_scale):
    dist_array = np.array([np.array([])])
    for  j in xywh: #loop for all bboxes
        xc = int(j[0].item())
        yc = int(j[1].item())
        dist = np.array([np.array([distance[yc, xc]])])
        dist_array = np.concatenate((dist_array, dist), axis=0) if dist_array.size else dist
    # Get data scale from the device and convert to meters
    z =  np.multiply(dist_array, depth_scale)
    # Same type with xywhs
    return torch.tensor(z).cuda()

    #https://github.com/IntelRealSense/librealsense/issues/6749 this potentially is more accurate, try later