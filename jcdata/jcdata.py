import os
import pandas as pd
import csv

class DataImporter:

    def __init__(self, dir='.'):

        self.initFilePaths(dir)

        self.train = Dataset(self._training_path)
        self.test = Dataset(self._test_path)

    def initFilePaths(self, root_dir):

        self._training_path = os.path.join(root_dir, 'train')
        self._test_path = os.path.join(root_dir, 'test')


class Dataset:
    def __init__(self, dir):
        self._path = os.path.join(dir, 'data.csv')
        self.n_samples = self._countSamplesInCSV(self._path)
        self.batch_size = self.n_samples

    # Counts rows in a CSV file passed to it and stores it as the number of samples in that file
    def _countSamplesInCSV(self, filepath):
        file = csv.reader(filepath)
        return sum(1 for row in file)

    # Returns the batch of data at the index specified
    def getBatch(self, index):

        if(index * self.batch_size < self.n_samples):
            df = pd.read_csv(self._path, header=None, skiprows=index * self.batch_size, nrows=self.batch_size)
            labels = df.iloc[:, 0].values
            data = df.iloc[:, 1:].values
        else:
            print("No more batches available in dataset")
            data = None
            labels = None
        return data, labels

    @property
    def batch_size(self):
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value):
        self._batch_size = value

    @property
    def n_samples(self):
        return self._n_samples

    @n_samples.setter
    def n_samples(self, value):
        self._n_samples = value