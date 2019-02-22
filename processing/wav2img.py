# wave to spectrogram

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
import numpy as np

#classes = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
classes = os.listdir('./gender_voice')
modes = ['']
LEN = 16000
for label in classes:
    for mode in modes:
        path = os.path.join('./gender_voice', mode, label)
        waves = os.listdir(path)
        target_path = os.path.join('./gender_voice_img', mode, label)

        for wav_file in waves:
            if wav_file[-3:] == 'wav':
                rate, data = wavfile.read(os.path.join(path, wav_file))
                if len(data) > LEN:
                    data = data[:LEN]
                else:
                    data = np.pad(data, (0, max(0, LEN - len(data))), "constant")
                fig,ax = plt.subplots(1)
                fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
                ax.axis('off')
                pxx, freqs, bins, im = ax.specgram(x=data, Fs=rate, noverlap=384, NFFT=512)
                ax.axis('off')
                fig.savefig(os.path.join(target_path, wav_file)[:-4] + '.jpg', dpi=300, frameon='false')
                plt.close()
                print("Modification complete for ", os.path.join(target_path, wav_file)[:-4] + '.jpg')
