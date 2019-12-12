# Brain Signal Authentication for Human-Computer Interaction in Virtual Reality

The purpose of this research was to determine whether active portions of a person’s brain are influenced by their using Virtual Reality (VR) and whether those brain signals can be used for user authentication. 

The paper was presented at the IEEE CSE 2019 conference in August. The research paper can be accessed [here](https://ieeexplore.ieee.org/document/8919581).


### Data Collection:

My team and I collected VR (Virtual Reality) and non-VR Electroencephalography(EEG) data using Ultracortex EEG Mark IV headset with 8 channels. The headset has 8 electrodes to receive brain signals combined with an 8 channel biosensing board. Image 1 shows the locations of electrodes. OpenBCI GUI software was used to stream and store the data. Image 2 shows brain signal streaming. VeeR cardboard was used to collect VR data and computers were used to collect non-VR data. Three minutes of data was collected per subject without any muscle movement.  

<p align="center"><img src="https://github.com/SonalSavaliya/Brain-Signal-Authentication-for-Human-computer-Interaction-in-Virtual-Reality/blob/master/Images/8%20channel%20location.PNG" />
  <p align="center">Image 1: 8 Channel Location on Headset</p>
</p>

<p align="center"><img src="https://github.com/SonalSavaliya/Brain-Signal-Authentication-for-Human-computer-Interaction-in-Virtual-Reality/blob/master/Images/EEG%20Streaming.png"  height="500" />
  <p align="center">Image 2: 8 Channel EEG Streaming</p>
</p>
 
 

### Data Pre-processing and Analysis:

In data preprocessing, bad channels, eye blink and background noise were removed using MNE, Pandas, Numpy and Matplotlib python libraries. 

- For features Extraction, three methods were selected:
  1) Statistical Histogram (SH)
  2) Autoregressive (AR)
  3) Power Spectral Density (PSD)
  
  These methods were implemented with 5 seconds and 10 seconds time frames. A combination of two methods, for instance, Autoregressive with Statistical Histogram and  Statistical Histogram with Power Spectral Density were tried.
  
  For VR dataset, accuracy rate was 71.66% (SH), 70.92% (PSD+SH), and 75.62% (AR+SH), and for NonVR dataset, accuracy rate was 75.08% (SH), 70.92% (PSD+SH), and 75.70% (AR+SH).
  
  
- After that, Inter (Between person) and Intra (Within person) distance were calculated with set target value 1 for Inter and 0 for Intra
- Based on Inter and Intra distance, the Support Vector Machine (SVM) classifier was used for classification


### Conclusion:

In this research, the authentication of brain signals in virtual reality was performed with three different feature extraction methods. Autoregressive with Statistical Histogram works better compared to other methods. There was no significant difference in the accuracy rate between VR and Non-VR EEG data.




