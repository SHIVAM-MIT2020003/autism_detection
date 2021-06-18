Project Name: Autism Spectrum Disorder Diagnostic System Using HOS Bispectrum with EEG signals

Dependencies
1. MATLAB
2. EEGLAB
3. mne
4. matplotlib
5. pandas
6. numpy
7. random
8. csv	
9. sklearn
10. seaborn

Before Executing other files, Above libraries need to be installed.

Steps 1:
Use Matlab and eeglab for preprocessing of BCI2000.dat dataset file

Step 2:
Use "eeg_data_concatenation" file,to combine all the normal file into one file and all the autism file into one file.

Step 3:
use "segmentation_and_visualization" code file, to apply segmentation operation

Step 4:
Execute code which is in get_spectrum Folder to fetch the spectrum

NOTE: get_spectrum folder contains .py files. Therefore you need to execute those code files on some IDE. But before executing those files you need to install all the above dependencies on IDE first.

Step 5:
To extract important features, use ICA(independent component analysis) code

Step 6:
We have separate code file for calculating mean, variance, standard deviation, shannon entropy, and skewness. Execute them in any order to get the features.

Step 7:
Concatenate both normal and autism files into one single file

Step 8:
Use final concatenated csv file for classification



