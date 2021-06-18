
import mne

from mne.time_frequency import csd_fourier, csd_multitaper, csd_morlet, tfr_morlet

n_jobs = 5

frequencies = [16, 17, 18, 19, 20]

epochs = mne.read_epochs('data/segmented-merged-normal-epo.fif')

csd_fft = csd_fourier(epochs, fmin=15, fmax=20, n_jobs=n_jobs)

csd_mt = csd_multitaper(epochs, fmin=15, fmax=20, adaptive=True, n_jobs=n_jobs)

csd_wav = csd_morlet(epochs, frequencies, decim=10, n_jobs=n_jobs)

tfr_wav = tfr_morlet(epochs, frequencies, 3, return_itc=False)

csd_fft.plot()

csd_mt.plot()

csd_wav.plot()

tfr_wav.plot()

tfr_wav.save("spectrums/segmented-merged-normal-spectrums.fif")

csd_wav.save("spectrums/segmented-merged-normal-csd-spectrum.fif")