import argparse
import os
import sys
import random


import torch
import models
#from torch.utils.tensorboard import SummaryWriter
from interact import *

SELF_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.join(SELF_DIR, os.pardir, os.pardir)
sys.path.append(ROOT_DIR)

MODEL_DIR = os.path.join(ROOT_DIR, os.pardir, "ImageNet_chips", "pretrained")
MODEL_PATHS = {
    '32bit': os.path.join(MODEL_DIR, "resnet18s_32bit.pth.tar"),
    'w1a8': os.path.join(MODEL_DIR, "resnet18s_w1a8.pth.tar")
}

    
#add codes for loading model

def load_model(model_name):

    manualSeed = random.randint(1, 10000)

    path = os.getcwd()

    if model_name == '32bit':
        save_dir = os.path.join(path ,'result/resnet18s/32bit')
    elif model_name == 'w1a8':
        save_dir = os.path.join(path ,'result/resnet18s/w1a8')
    else:
        print('MODEL NOT EXIST')

    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
        
    log = open(os.path.join(save_dir,
                            'log_seed_{}.txt'.format(manualSeed)), 'w')
    print_log('save path : {}'.format(save_dir), log)
    
    model_path = MODEL_PATHS[model_name]
    
    #model = torch.load(model_path, map_location=torch.device('cpu'))
    #print(model.keys())
    
    kwargs = {'load_dir': model_path,}
    
    model = models.resnetv2.resnet18s(pretrained = False, progress = True, **kwargs)
    
    print_log("=> network :\n {}".format(model), log)



if __name__ == "__main__":
    load_model('w1a8')
 

