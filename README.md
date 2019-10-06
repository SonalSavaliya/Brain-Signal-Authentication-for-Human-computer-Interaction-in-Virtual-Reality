# Brain Signal Authentication for Human-Computer Interaction using Virtual Reality 

The purpose of this study is to determine if a Virtual Reality (VR) system combined with brain signaling can produce biometric authentication in a usable form. 

### Data Collection:

My team and I collected VR (Virtual Reality) and non-VR data using Ultracortex EEG Mark IV headset with 8 channels. The headset has 8 electrodes to receive brain signals by combine with an 8 channel biosensing board. Image 1 shows the locations of electrodes. OpenBCI GUI software used to stream and store the data. Image 2 shows brain signal streaming. VeeR cardboard was used to collect VR data and Laptops were used to collect non-VR data. Three mins of data were collected per subject without muscle movement.  

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
  
  These methods were implemented with different time segments like 5 sec and 10 sec. We also tried a combination of two methods, for instance, Autoregressive with Statistical Histogram and  Statistical Histogram with Power Spectral Density.
  
- Then calculated Inter (Between person) and Intra (Within person) distance and set target value 1 for Inter and 0 for Intra
- Based on Inter and Intra distance, the Support Vector Machine (SVM) classifier was used for classification
- If data is within Intra data, then the person belongs to the same group


### Conclusion:

In this research, the authentication of brain signals in virtual reality was performed with three different feature extraction methods with different parameters. Autoregressive with Statistical Histogram works best compared to the other methods tested. Also, for classification, there was no significant difference between the accuracy rates for VR and Non-VR EEG data.




