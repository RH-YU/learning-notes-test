import argparse
import os
import sys
import random
#import shutil
#import time
#import warnings


import torch
#import torch.nn as nn
#import torch.nn.parallel
#import torch.backends.cudnn as cudnn
#import torch.distributed as dist
#import torch.optim
#import torch.multiprocessing as mp
#import torch.utils.data
#import torch.utils.data.distributed
#import torchvision.transforms as transforms
#import torchvision.datasets as datasets
import models
from torch.utils.tensorboard import SummaryWriter
from interact import *

SELF_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.join(SELF_DIR, os.pardir, os.pardir)
sys.path.append(ROOT_DIR)

MODEL_DIR = os.path.join(ROOT_DIR, os.pardir, "ImageNet_chips", "pretrained")
MODEL_PATHS = {
    '32bit': os.path.join(MODEL_DIR, "resnet18s_32bit.pth.tar"),
    'w1a8': os.path.join(MODEL_DIR, "resnet18s_w1a8.pth.tar")
}


model_names = sorted(name for name in models.__dict__
    if name.islower() and not name.startswith("__")
    and callable(models.__dict__[name]))

parser = argparse.ArgumentParser(description='PyTorch ImageNet Training')
parser.add_argument('data', metavar='DIR',
                    help='path to dataset')
parser.add_argument('-a', '--arch', metavar='ARCH', default='resnet18',
                    choices=model_names,
                    help='model architecture: ' +
                        ' | '.join(model_names) +
                        ' (default: resnet18)')
parser.add_argument('-j', '--workers', default=4, type=int, metavar='N',
                    help='number of data loading workers (default: 4)')
parser.add_argument('--epochs', default=90, type=int, metavar='N',
                    help='number of total epochs to run')
parser.add_argument('--start-epoch', default=0, type=int, metavar='N',
                    help='manual epoch number (useful on restarts)')
parser.add_argument('-b', '--batch-size', default=256, type=int,
                    metavar='N',
                    help='mini-batch size (default: 256), this is the total '
                         'batch size of all GPUs on the current node when '
                         'using Data Parallel or Distributed Data Parallel')
parser.add_argument('--lr', '--learning-rate', default=0.1, type=float,
                    metavar='LR', help='initial learning rate', dest='lr')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='momentum')
parser.add_argument('--wd', '--weight-decay', default=1e-4, type=float,
                    metavar='W', help='weight decay (default: 1e-4)',
                    dest='weight_decay')
parser.add_argument('-p', '--print-freq', default=10, type=int,
                    metavar='N', help='print frequency (default: 10)')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')
parser.add_argument('--pretrained', dest='pretrained', action='store_true',
                    help='use pre-trained model')
parser.add_argument('--world-size', default=-1, type=int,
                    help='number of nodes for distributed training')
parser.add_argument('--rank', default=-1, type=int,
                    help='node rank for distributed training')
parser.add_argument('--dist-url', default='tcp://224.66.41.62:23456', type=str,
                    help='url used to set up distributed training')
parser.add_argument('--dist-backend', default='nccl', type=str,
                    help='distributed backend')
parser.add_argument('--seed', default=None, type=int,
                    help='seed for initializing training. ')
parser.add_argument('--gpu', default=None, type=int,
                    help='GPU id to use.')
parser.add_argument('--multiprocessing-distributed', action='store_true',
                    help='Use multi-processing distributed training to launch '
                         'N processes per node, which has N GPUs. This is the '
                         'fastest way to use PyTorch for either single node or '
                         'multi node data parallel training')
parser.add_argument('--save-dir', dest='save_dir',
                    help='The directory used to save the trained models',
                    default='./save_temp/', type=str)
parser.add_argument('--load-dir', dest='load_dir',
                    help='The directory used to load the trained models',
                    default='./save_temp/', type=str)
parser.add_argument('--lr-type', default=1, type=int,
                    help='learning rate type for fine-tuning. ')
parser.add_argument('--classes', default=64, type=int,
                    help='classes of output. ')
parser.add_argument('--manualSeed', type=int, default=None, help='manual seed')
best_acc1 = 0



def load_model(model_name):
    model_path = MODEL_PATHS[model_name]
    model = torch.load(model_path, map_location=torch.device('cpu'))
    print(model.keys())
   
#add codes for loading model
    
def load_model_modified():
    
    args=parser.parse_args()

    if args.manualSeed is None:
        args.manualSeed = random.randint(1, 10000)
    if args.seed is not None:
        random.seed(args.seed)
        torch.manual_seed(args.seed)
        
    if not os.path.isdir(args.save_dir):
        os.makedirs(args.save_dir)

    log = open(os.path.join(args.save_dir,
                            'log_seed_{}.txt'.format(args.manualSeed)), 'w')
    print_log('save path : {}'.format(args.save_dir), log)
    state = {k: v for k, v in args._get_kwargs()}

    # print(state)
    print_log(state, log)

    # create model
    # kwargs = {'num_classes': 64, 'pin_memory': True}

    print_log("=> creating model '{}'".format(args.arch), log)
    kwargs = {'num_classes': args.classes,
              'load_dir': args.load_dir}
    if args.pretrained:
        print("=> using pre-trained model '{}'".format(args.arch))
        model = models.__dict__[args.arch](pretrained=True, progress = True, **kwargs)
    else:
        print("=> creating model '{}'".format(args.arch))
        # model = models.__dict__[args.arch]()
        model = models.__dict__[args.arch](pretrained = False, progress = True, **kwargs)
    print_log("=> network :\n {}".format(model), log)

#if __name__ == "__main__":
 #   load_model('32bit')
 
if __name__ == "__main__":
    load_model_modified()
