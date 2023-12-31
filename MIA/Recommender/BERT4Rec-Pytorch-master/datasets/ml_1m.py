from .base import AbstractDataset

import pandas as pd

from datetime import date


class ML1MDataset(AbstractDataset):
    @classmethod
    def code(cls):
        return 'ml-1m'

    @classmethod
    def url(cls):
        return 'http://files.grouplens.org/datasets/movielens/ml-1m.zip'

    @classmethod
    def zip_file_content_is_folder(cls):
        return True

    @classmethod
    def all_raw_file_names(cls):
        return ['README',
                'movies.dat',
                'ratings.dat',
                'users.dat']

    def load_ratings_df(self):
        # folder_path = self._get_rawdata_folder_path()
        # file_path = folder_path.joinpath('ratings.dat')
        root_dir = '/content/drive/MyDrive/DL-MIA-KDD-2022/DL-MIA-SR/Recommender/BERT4Rec-Pytorch-master/mydata/processed/'
        # file_path = "../data/ml-1m_shadow"
        df = pd.read_csv(root_dir+'beauty_Tmember', sep=',', header=None, skiprows=1)
        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        return df


