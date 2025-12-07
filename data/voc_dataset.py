import os
import cv2
import torch
import random
import numpy as np
import xml.etree.ElementTree as ET
import torchvision.transforms as transforms

from torch.utils.data import Dataset


class VOCDataset(Dataset):

    def __init__(self, is_train, image_dir, label_txt, image_size=448, grid_size=7, num_bboxes=2, num_classes=20):
        tree = ET.parse('data/000005.xml')
        all_objects = tree.getroot().findall('object')

        print(f"All objects tag: {all_objects[0].find('name').text}")
        print(f"All objects tag: {all_objects[0].find('difficult').text}")
        print(f"All objects tag: {all_objects[0].find('bndbox').find('xmin').text}")
        print(f"All objects tag: {all_objects[0].find('bndbox').find('ymin').text}")
        print(f"All objects tag: {all_objects[0].find('bndbox').find('xmax').text}")
        print(f"All objects tag: {all_objects[0].find('bndbox').find('ymax').text}")