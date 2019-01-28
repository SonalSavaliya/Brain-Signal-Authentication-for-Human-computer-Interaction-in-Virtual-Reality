import mne
from mne.preprocessing import ICA
import pandas as pd
import numpy as np
import neo

#VR part
data = pd.read_csv("OpenBCI-RAW-Subject-4_Non-VR.txt", delimiter=",")
data = data.drop(['sample_index','extra1','extra2','extra3'], axis=1)

channel_data = data[['channel-1','channel-2','channel-3','channel-4','channel-5','channel-6','channel-7','channel-8']]


channel_data_array = channel_data.as_matrix()

channel_data_updated = channel_data_array.transpose()

ch_types = ['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg']
ch_names = ['CH 1','CH 2','CH 3', 'CH 4','CH 5','CH 6','CH 7','CH 8']
sfreq = 250

info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)

raw = mne.io.RawArray(channel_data_updated,info)

scalings = {'eeg':400,'eeg':400,'eeg':400,'eeg':400,'eeg':400,'eeg':400,'eeg':400,'eeg':400}
color = {'eeg':'blue'}

raw.plot(n_channels=8,scalings=scalings, color=color, title='Data from Channels', show=True, block=True)

#Rejecting the bad channels in the data
raw.info['bads'] = ['CH 5','CH 6']

raw.plot(n_channels=8,scalings=scalings, color=color, title='Data from Channels', show=True, block=True)


#Filtering the data using notch filter
picks = mne.pick_types(raw.info, meg=False, eeg=True, exclude='bads')

raw.notch_filter(60, picks=picks)
raw.plot(n_channels=8,scalings=scalings, color=color, title='Data from Channels', show=True, block=True)

#Sampling the data to 128Hz
raw.resample(128,npad="auto")
raw.plot_psd(area_mode='range', picks=picks, average=True, color='darkred')

#bandpass filtering in 4-45Hz
#To do the low-pass and high-pass filtering in one step we can do it so-called band-pass filter by running the following:

raw.filter(4,45.,fir_design='firwin')
raw.plot(n_channels=8,scalings=scalings, color=color, title='Data from Channels', show=True, block=True)

raw.plot_psd(average=True, color='darkred')

raw.save("Subject-16_VR.fif", picks=picks)

