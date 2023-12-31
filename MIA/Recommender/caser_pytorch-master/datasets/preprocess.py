# -*- coding: utf-8 -*-
import os

import numpy as np
import pandas as pd
import datetime


def preprocess(dataset, member, nonmember, member_train, member_test, nonmem_train):
    data = pd.read_csv(dataset, sep=',', header=None, skiprows=1)
    # data.columns = ['SessionID', 'ItemID', 'Rating', 'Time']
    data.columns = ['SessionID', 'ItemID', 'Rating']
    # split member and nonmember 5-5
    middle = round(data.SessionID.nunique()/2)
    member_data = pd.DataFrame()
    nonmember_data = pd.DataFrame()

    data = data.groupby('SessionID')
    for index, value in data:
        if index < middle:
            member_data = member_data.append(value)
        else:
            nonmember_data = nonmember_data.append(value)

    m_data = member_data.sort_values(by=['SessionID'], ascending=True)
    m_data.to_csv(member, sep=',', index=False, header=False)
    m_data = m_data.groupby('SessionID')
    m_train = pd.DataFrame()
    m_test = pd.DataFrame()
    for index, value in m_data:
        middle0 = round(len(value) * 0.7)
        middle = round(len(value) * 0.8)
        m_train = m_train.append(value.iloc[0:middle0, :])
        m_test = m_test.append(value.iloc[middle:, :])

    # Delete records in testing split where items are not in training split
    m_test = m_test[np.in1d(m_test.ItemID, m_train.ItemID)]
    m_train['Rating'] = 1
    m_train['SessionID'] = m_train['SessionID'] + 1
    m_test['Rating'] = 1
    m_test['SessionID'] = m_test['SessionID'] + 1
    # m_train = m_train.drop(columns=['Time'])
    # m_test = m_test.drop(columns=['Time'])
    m_train.to_csv(member_train, sep='\t', index=False, header=False)
    m_test.to_csv(member_test, sep='\t', index=False, header=False)

    n_data = nonmember_data.sort_values(by=['SessionID'], ascending=True)
    n_data.to_csv(nonmember, sep=',', index=False, header=False)
    n_data = n_data.groupby('SessionID')
    n_train = pd.DataFrame()
    for index, value in n_data:
        middle0 = round(len(value) * 0.7)
        n_train = n_train.append(value.iloc[0:middle0, :])

    n_train['Rating'] = 1
    n_train['SessionID'] = n_train['SessionID'] + 1
    n_train.to_csv(nonmem_train, sep=',', index=False, header=False)

    # Convert To CSV
    print('Member has', len(member_data), 'Events, ', member_data.SessionID.nunique(), 'Sequences, and',
          member_data.ItemID.nunique(), 'Items\n\n')
    # print('train has', len(m_train), 'Events, ', m_train.SessionID.nunique(), 'Sequences, and',
    #       m_train.ItemID.nunique(), 'Items\n\n')
    # print('test has', len(m_test), 'Events, ', m_test.SessionID.nunique(), 'Sequences, and',
    #       m_test.ItemID.nunique(), 'Items\n\n')
    print('Nonmember has', len(nonmember_data), 'Events, ', nonmember_data.SessionID.nunique(), 'Sequences, and',
          nonmember_data.ItemID.nunique(), 'Items\n\n')


if __name__ == '__main__':
  # BOOK
    dataBefore_root = "/content/drive/MyDrive/MIA/Dataset/data/processed_book"
    dataAfter_root = ""
    m_shadow_dataset = os.path.join(dataBefore_root, "book_shadow")
    m_shadow_member = os.path.join(dataAfter_root, "book_Smember")
    m_shadow_nonmember = os.path.join(dataAfter_root, "book_Snonmem")
    m_shadow_member_train = os.path.join(dataAfter_root, "book_Smember_train")
    m_shadow_member_test = os.path.join(dataAfter_root, "book_Smember_test")
    m_shadow_nonmem_train = os.path.join(dataAfter_root, "book_Snonmem_train")
    preprocess(m_shadow_dataset, m_shadow_member, m_shadow_nonmember,
               m_shadow_member_train, m_shadow_member_test, m_shadow_nonmem_train)
    m_target_dataset = os.path.join(dataBefore_root, "book_target")
    m_target_member = os.path.join(dataAfter_root, "book_Tmember")
    m_target_nonmember = os.path.join(dataAfter_root, "book_Tnonmemn")
    m_target_member_train = os.path.join(dataAfter_root, "book_Tmember_train")
    m_target_member_test = os.path.join(dataAfter_root, "book_Tmember_test")
    m_target_nonmem_train = os.path.join(dataAfter_root, "book_Tnonmem_train")
    preprocess(m_target_dataset, m_target_member, m_target_nonmember,
               m_target_member_train, m_target_member_test, m_target_nonmem_train)
    # m_target_dataset = os.path.join(dataBefore_root, "ml-1m_target")
    # m_target_member = os.path.join(dataAfter_root, "ml-1m_Tmember")
    # m_target_nonmember = os.path.join(dataAfter_root, "ml-1m_Tnonmemn")
    # m_target_member_train = os.path.join(dataAfter_root, "ml-1m_Tmember_train")
    # m_target_member_test = os.path.join(dataAfter_root, "ml-1m_Tmember_test")
    # m_target_nonmem_train = os.path.join(dataAfter_root, "ml-1m_Tnonmem_train")
    # preprocess(m_target_dataset, m_target_member, m_target_nonmember,
    #            m_target_member_train, m_target_member_test, m_target_nonmem_train)
    # # m: ml-1m a: Amazon
    # dataBefore_root = "/content/drive/MyDrive/DL-MIA-KDD-2022/DL-MIA-SR/Dataset/data/processed_movielens"
    # dataAfter_root = ""
    # m_shadow_dataset = os.path.join(dataBefore_root, "ml-1m_shadow")
    # m_shadow_member = os.path.join(dataAfter_root, "ml-1m_Smember")
    # m_shadow_nonmember = os.path.join(dataAfter_root, "ml-1m_Snonmem")
    # m_shadow_member_train = os.path.join(dataAfter_root, "ml-1m_Smember_train")
    # m_shadow_member_test = os.path.join(dataAfter_root, "ml-1m_Smember_test")
    # m_shadow_nonmem_train = os.path.join(dataAfter_root, "ml-1m_Snonmem_train")
    # preprocess(m_shadow_dataset, m_shadow_member, m_shadow_nonmember,
    #            m_shadow_member_train, m_shadow_member_test, m_shadow_nonmem_train)
    
    # m_target_dataset = os.path.join(dataBefore_root, "ml-1m_target")
    # m_target_member = os.path.join(dataAfter_root, "ml-1m_Tmember")
    # m_target_nonmember = os.path.join(dataAfter_root, "ml-1m_Tnonmemn")
    # m_target_member_train = os.path.join(dataAfter_root, "ml-1m_Tmember_train")
    # m_target_member_test = os.path.join(dataAfter_root, "ml-1m_Tmember_test")
    # m_target_nonmem_train = os.path.join(dataAfter_root, "ml-1m_Tnonmem_train")
    # preprocess(m_target_dataset, m_target_member, m_target_nonmember,
    #            m_target_member_train, m_target_member_test, m_target_nonmem_train)

    # m: ml-1m a: Amazon
    # dataBefore_root = "../../../Dataset/data/processed_amazon/"
    # dataAfter_root = ""
    # m_shadow_dataset = os.path.join(dataBefore_root, "beauty_shadow")
    # m_shadow_member = os.path.join(dataAfter_root, "beauty_Smember")
    # m_shadow_nonmember = os.path.join(dataAfter_root, "beauty_Snonmem")
    # m_shadow_member_train = os.path.join(dataAfter_root, "beauty_Smember_train")
    # m_shadow_member_test = os.path.join(dataAfter_root, "beauty_Smember_test")
    # m_shadow_nonmem_train = os.path.join(dataAfter_root, "beauty_Snonmem_train")
    # preprocess(m_shadow_dataset, m_shadow_member, m_shadow_nonmember,
    #            m_shadow_member_train, m_shadow_member_test, m_shadow_nonmem_train)

    # m_target_dataset = os.path.join(dataBefore_root, "beauty_target")
    # m_target_member = os.path.join(dataAfter_root, "beauty_Tmember")
    # m_target_nonmember = os.path.join(dataAfter_root, "beauty_Tnonmemn")
    # m_target_member_train = os.path.join(dataAfter_root, "beauty_Tmember_train")
    # m_target_member_test = os.path.join(dataAfter_root, "beauty_Tmember_test")
    # m_target_nonmem_train = os.path.join(dataAfter_root, "beauty_Tnonmem_train")
    # preprocess(m_target_dataset, m_target_member, m_target_nonmember,
    #            m_target_member_train, m_target_member_test, m_target_nonmem_train)
   