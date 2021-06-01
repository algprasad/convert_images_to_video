import cv2
import numpy as np
import glob

img_array = []
#images_path = 'C:/New folder/Images/*.jpg'
images_path ='/home/alg/Downloads/output_images/'
#images_path ='/home/alg/misc_tools/consolidate_image_results/consolidated_images/'
total_images=750
for i in range(total_images):
    img_index = 500 + i
    filename =images_path + 'Frame' + str(img_index) + '.png'
    print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

#check if you need to change anything to convert this to mp4
out = cv2.VideoWriter('vsr_duf_lr_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
