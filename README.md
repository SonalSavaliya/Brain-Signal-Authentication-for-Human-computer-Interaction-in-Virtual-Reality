# Brain Signal Authentication for Human Computer Interaction using Virtual Reality 

### Data Collection and Pre-processing

The purpose of this study is to determine if a Virtual Reality (VR) system combined with brain signaling can produce biometric authentication in a usable form. My team and I collected VR (Virtual Reality) and non-VR data using Ultracortex EEG Mark IV headset. Data were preprocessed using MNE python library. 
 

### Data Analysis

- Extrected features of each subject using Statistical Histogram, Autoregressive and Power Spectral Density methods
- Calculated Inter (Between person) and Intra (Within person) distance and set target value 1 for Inter and 0 for Intra
- Base  on Inter and Intra distance, Support Vectore Machine (SVM) classifier was used for classification
- If data is within Intra data, then person belogs to the same group
