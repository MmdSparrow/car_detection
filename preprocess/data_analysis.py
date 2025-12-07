
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

from collections import Counter
from configs.VOC_dataset_configs import ANNOTATION_PATH
from configs.common_configs import DATA_ANALYSIS_RESULTS_PATH


def class_distribution():
    xml_files = [os.path.join(ANNOTATION_PATH, f) for f in os.listdir(ANNOTATION_PATH) if f.endswith('.xml')]
    print("Total number of files:", len(xml_files))
    
    class_counts = Counter()
        
    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for obj in root.findall('object'):
            difficult = obj.find('difficult')

            if difficult is None or difficult.text == '0':
                class_name = obj.find('name').text
                class_counts[class_name] += 1

    print(f"Total objects found (non-difficult): {sum(class_counts.values())}")
    print("\n Class distribution:")
    print(class_counts)

    class_df = pd.DataFrame(class_counts.most_common(), columns=["Class", "Count"])

    plt.figure(figsize=(12, 8))
    sns.barplot(x='Count', y='Class', data=class_df, palette='viridis')
    plt.title('Class Distribution in PASCAL VOC 2007', fontsize=16)
    plt.xlabel('Number of Objects', fontsize=12)
    plt.ylabel('Class Name', fontsize=12)
    plt.savefig(os.path.join(DATA_ANALYSIS_RESULTS_PATH, 'class_distribution_PASCAL_VOC_2007.png'))


def images_size():
    xml_files = [os.path.join(ANNOTATION_PATH, f) for f in os.listdir(ANNOTATION_PATH) if f.endswith('.xml')]
    images_data = []

    for file in xml_files:
        tree = ET.parse(file)
        root = tree.getroot()
        file_name = root.find('filename').text
        size_elem = root.find('size')

        width = int(size_elem.find('width').text)
        height = int(size_elem.find('height').text)
        area = width * height

        images_data.append({
                        'ID': file_name,
                        'width': width,
                        'height': height,
                        'area': area
                    })

    images_df = pd.DataFrame(images_data)
    print('Image sizes DataFrame (5 first rows)')
    print(images_df.head())
    print('\n Image sizes Data Statistics')
    print(images_df.describe())

def missing_value():
    xml_files = [os.path.join(ANNOTATION_PATH, f) for f in os.listdir(ANNOTATION_PATH) if f.endswith('.xml')]
    total_files = 0
    negative_image_files = []
    positive_image_files = 0

    for xml_file in xml_files:
        total_files += 1
        object_count = 0
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for obj in root.findall('object'):

            difficult =obj.find('difficult')
            if difficult is None or difficult.text == '0':
                object_count += 1

        if object_count == 0: 
            negative_image_files.append(xml_file)
        else:
            positive_image_files += 1

    print(f"Total files checked: {total_files}")
    print(f"Positive files (with objects): {positive_image_files}")
    print(f"Negative files (no objects): {len(negative_image_files)}")