from preprocess.preprocess import Preprocess

preprocess= Preprocess()
preprocess.create_split_file_index('train')
preprocess.create_split_file_index('val')