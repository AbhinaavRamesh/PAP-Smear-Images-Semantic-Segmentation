# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:17:24 2019

@author: AbhinaavRamesh
"""

import os,time,cv2, sys, math
import tensorflow as tf
import argparse
import numpy as np

from utils import utils, helpers
from builders import model_builder

parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, default=r".\Images\\", required=False, help='The image you want to predict on. ')
parser.add_argument('--result', type=str, default=r".\Predictions\\", required=False, help='The image you want to predict on. ')
parser.add_argument('--checkpoint_path', type=str, default=r".\check\model.ckpt", required=False, help='The path to the latest checkpoint weights for your model.')
parser.add_argument('--crop_height', type=int, default=128, help='Height of cropped input image to network')
parser.add_argument('--crop_width', type=int, default=128, help='Width of cropped input image to network')
parser.add_argument('--model', type=str, default="FC-DenseNet56", required=False, help='The model you are using')
parser.add_argument('--dataset', type=str, default="PAP", required=False, help='The dataset you are using')
args = parser.parse_args(args=[])

class_names_list, label_values = helpers.get_label_info(os.path.join(args.dataset, "Class.csv"))

num_classes = len(label_values)

print("\n***** Begin prediction *****")
print("Dataset -->", args.dataset)
print("Model -->", args.model)
print("Crop Height -->", args.crop_height)
print("Crop Width -->", args.crop_width)
print("Num Classes -->", num_classes)
print("Image -->", args.image)

# Initializing network
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess=tf.Session(config=config)

net_input = tf.placeholder(tf.float32,shape=[None,None,None,3])
net_output = tf.placeholder(tf.float32,shape=[None,None,None,num_classes]) 

network, _ = model_builder.build_model(args.model, net_input=net_input,
                                        num_classes=num_classes,
                                        crop_width=args.crop_width,
                                        crop_height=args.crop_height,
                                        is_training=False)

sess.run(tf.global_variables_initializer())

print('Loading model checkpoint weights')
saver=tf.train.Saver(max_to_keep=1000)
saver.restore(sess, args.checkpoint_path)
file_ls=os.listdir(args.image)
count=0
for imgf in file_ls:
    img1=cv2.imread(args.image+imgf)
    img=cv2.cvtColor(np.uint8(img1), cv2.COLOR_BGR2RGB)
      
    width,length=img.shape[0:2]
    if width>length:
        ldiff=width-length
        img_padded=cv2.copyMakeBorder(img,0,0,int(ldiff/2),ldiff-int(ldiff/2),cv2.BORDER_CONSTANT,value=[0,0,0])
        
    elif length>width:
        ldiff=length-width
        img_padded=cv2.copyMakeBorder(img,int(ldiff/2),ldiff-int(ldiff/2),0,0,cv2.BORDER_CONSTANT,value=[0,0,0])
    img = cv2.resize(img_padded, (128,128) , interpolation = cv2.INTER_AREA) 
    #rows=img.shape[0]
    #cols=img.shape[1]
    #dim=img.shape[2]
    #pred_image=np.zeros(np.shape(img))#,dtype=uint8)
    print("Testing image " + imgf)
    #for r in range(0,img.shape[0],256):
    #   for c in range(0,img.shape[1],256):
    #      temp=img[r:r+256, c:c+256,:]
    input_image = np.expand_dims(np.float32(img),axis=0)/255.0
    st = time.time()
    output_image = sess.run(network,feed_dict={net_input:input_image})
    run_time = time.time()-st
    output_image = np.array(output_image[0,:,:,:])
    output_image = helpers.reverse_one_hot(output_image)
    out_vis_image = helpers.colour_code_segmentation(output_image, label_values)
    out=cv2.cvtColor(np.uint8(out_vis_image), cv2.COLOR_RGB2BGR)
    filename=imgf[:-4]+"_pred.png"
    cv2.imwrite(args.result+filename,out)
    #cv2.imwrite(args.result+str(count)+".png",cv2.cvtColor(np.uint8(out_vis_image), cv2.COLOR_RGB2BGR))
            #count+=1
    
    
    print("")
    print("Finished!")
    print("Wrote image " + filename)

