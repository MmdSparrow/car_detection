import os

from configs.common_configs import DATA_PREPROCESS_OUTPUTS_PATH
from configs.VOC_dataset_configs import IMAGE_SETS_PATH, IMAGES_PATH

class Preprocess:
    def __init__(self):
        os.makedirs(DATA_PREPROCESS_OUTPUTS_PATH, exist_ok=True)
    
    def create_split_file_index(self, split_name):
        source_file_path = os.path.join(IMAGE_SETS_PATH, split_name + '.txt')
        output_file_path = os.path.join(DATA_PREPROCESS_OUTPUTS_PATH, split_name + '.txt')
        
        with open(output_file_path, 'w') as output_file:
            with open(source_file_path, 'r') as source_file:
                for basename in source_file:
                    image_name = basename.strip() + '.jpg'
                    full_image_path = os.path.join(IMAGES_PATH, image_name)
                    output_file.write(full_image_path + '\n')