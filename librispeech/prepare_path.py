#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Prepare for making dataset (Librispeech corpus)."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os.path import join, basename, splitext, abspath
from glob import glob


class Prepare(object):
    """Prepare for making dataset.
    Args:
        data_path: path to librispeech corpus
        run_root_path: path to ./make.sh
        dataset_save_path: path to save dataset
    """

    def __init__(self, data_path, run_root_path):

        # Path to librispeech data
        self.train_clean100_path = join(data_path, 'train-clean-100')
        self.train_clean360_path = join(data_path, 'train-clean-360')
        self.train_other500_path = join(data_path, 'train-other-500')
        self.dev_clean_path = join(data_path, 'dev-clean')
        self.dev_other_path = join(data_path, 'dev-other')
        self.test_clean_path = join(data_path, 'test-clean')
        self.test_other_path = join(data_path, 'test-other')

        # Absolute path to this directory
        self.run_root_path = run_root_path

        self.__make()

    def __make(self):

        self.flac_train_clean100_paths, self.text_train_clean100_paths = [], []
        self.flac_train_clean360_paths, self.text_train_clean360_paths = [], []
        self.flac_train_other500_paths, self.text_train_other500_paths = [], []
        self.flac_dev_clean_paths, self.text_dev_clean_paths = [], []
        self.flac_dev_other_paths, self.text_dev_other_paths = [], []
        self.flac_test_clean_paths, self.text_test_clean_paths = [], []
        self.flac_test_other_paths, self.text_test_other_paths = [], []

        # train_clean_100
        for file_path in glob(join(self.train_clean100_path, '*/*/*')):
            if splitext(basename(file_path))[1] == '.flac':
                self.flac_train_clean100_paths.append(file_path)
            elif splitext(basename(file_path))[1] == '.txt':
                self.text_train_clean100_paths.append(file_path)

        # train_clean_360
        for file_path in glob(join(self.train_clean360_path, '*/*/*')):
            if splitext(basename(file_path))[1] == '.flac':
                self.flac_train_clean360_paths.append(file_path)
            elif splitext(basename(file_path))[1] == '.txt':
                self.text_train_clean360_paths.append(file_path)

        # train_other_500
        for file_path in glob(join(self.train_other500_path, '*/*/*')):
            if splitext(basename(file_path))[1] == '.flac':
                self.flac_train_other500_paths.append(file_path)
            elif splitext(basename(file_path))[1] == '.txt':
                self.text_train_other500_paths.append(file_path)

        # dev_clean
        for file_path in glob(join(self.dev_clean_path, '*/*/*')):
            if splitext(basename(file_path))[1] == '.flac':
                self.flac_dev_clean_paths.append(file_path)
            elif splitext(basename(file_path))[1] == '.txt':
                self.text_dev_clean_paths.append(file_path)

        # dev_other
        for file_path in glob(join(self.dev_other_path, '*/*/*')):
            if splitext(basename(file_path))[1] == '.flac':
                self.flac_dev_other_paths.append(file_path)
            elif splitext(basename(file_path))[1] == '.txt':
                self.text_dev_other_paths.append(file_path)

        # test_clean
        for file_path in glob(join(self.test_clean_path, '*/*/*')):
            if splitext(basename(file_path))[1] == '.flac':
                self.flac_test_clean_paths.append(file_path)
            elif splitext(basename(file_path))[1] == '.txt':
                self.text_test_clean_paths.append(file_path)

        # test_other
        for file_path in glob(join(self.test_other_path, '*/*/*')):
            if splitext(basename(file_path))[1] == '.flac':
                self.flac_test_other_paths.append(file_path)
            elif splitext(basename(file_path))[1] == '.txt':
                self.text_test_other_paths.append(file_path)

    def flac(self, data_type):
        """Get paths to flac files.
        Args:
            data_type: train_clean100 or train_clean360 or train_other500
                or dev_clean or dev_other or test_clean or test_clean
        Returns:
            paths to flac files
        """
        if data_type == 'train_clean100':
            return sorted(self.flac_train_clean100_paths)
        elif data_type == 'train_clean360':
            return sorted(self.flac_train_clean360_paths)
        elif data_type == 'train_other500':
            return sorted(self.flac_train_other500_paths)
        elif data_type == 'dev_clean':
            return sorted(self.flac_dev_clean_paths)
        elif data_type == 'dev_other':
            return sorted(self.flac_dev_other_paths)
        elif data_type == 'test_clean':
            return sorted(self.flac_test_clean_paths)
        elif data_type == 'test_other':
            return sorted(self.flac_test_other_paths)

    def text(self, data_type):
        """Get paths to transcription files.
        Args:
            data_type: train_clean100 or train_clean360 or train_other500
                or dev_clean or dev_other or test_clean or test_clean
        Returns:
            paths to transcription files
        """
        if data_type == 'train_clean100':
            return sorted(self.text_train_clean100_paths)
        elif data_type == 'train_clean360':
            return sorted(self.text_train_clean360_paths)
        elif data_type == 'train_other500':
            return sorted(self.text_train_other500_paths)
        elif data_type == 'dev_clean':
            return sorted(self.text_dev_clean_paths)
        elif data_type == 'dev_other':
            return sorted(self.text_dev_other_paths)
        elif data_type == 'test_clean':
            return sorted(self.text_test_clean_paths)
        elif data_type == 'test_other':
            return sorted(self.text_test_other_paths)


if __name__ == '__main__':

    data_path = '/n/sd8/inaguma/corpus/librispeech/data/'

    prep = Prepare(data_path, abspath('./'))

    print('===== train =====')
    print(len(prep.flac(data_type='train_clean100')))
    print(len(prep.text(data_type='train_clean100')))
    print(len(prep.flac(data_type='train_clean360')))
    print(len(prep.text(data_type='train_clean360')))
    print(len(prep.flac(data_type='train_other500')))
    print(len(prep.text(data_type='train_other500')))

    print('===== dev ======')
    print(len(prep.flac(data_type='dev_clean')))
    print(len(prep.text(data_type='dev_clean')))
    print(len(prep.flac(data_type='dev_other')))
    print(len(prep.text(data_type='dev_other')))

    print('===== test =====')
    print(len(prep.flac(data_type='test_clean')))
    print(len(prep.text(data_type='test_clean')))
    print(len(prep.flac(data_type='test_other')))
    print(len(prep.text(data_type='test_other')))
