from __future__ import print_function, division

import numpy as np
from matplotlib import pyplot as plt

from astroML.utils.decorators import pickle_results
from astroML.datasets import fetch_sdss_specgals
from astroML.correlation import bootstrap_two_point_angular

import pandas as pd

#Check for more details: https://www.astroml.org/user_guide/index.html

catalog_data = pd.read_csv('./NVSS_DEC_5_60_10mJy.csv', header=0)
filter_fluxmin=catalog_data['Flux_mJy']>20

catalog_data.where(filter_fluxmin   , inplace = True) 
filter_fluxmax=catalog_data['Flux_mJy']<=1000
catalog_data.where(filter_fluxmax   , inplace = True) 
filter_decmax= (catalog_data['DEJ2000']<20)
catalog_data.where(filter_decmax   , inplace = True)
filter_decmin=(catalog_data['DEJ2000']>5) 
catalog_data.where(filter_decmin   , inplace = True)
filter_ramax= (catalog_data['RAJ2000']<147)
catalog_data.where(filter_ramax   , inplace = True)
filter_ramin=(catalog_data['RAJ2000']>123) 
catalog_data.where(filter_ramin   , inplace = True)

rad=catalog_data['RAJ2000']
decd=catalog_data['DEJ2000']
rad=rad.dropna()
decd=decd.dropna()
print(rad)

bins=np.linspace(0.01,10,num=50)
bins=np.asarray(bins)
corr,corr_err, bootstraps = bootstrap_two_point_angular(rad,decd, bins,method='landy-szalay', Nbootstraps=10) #method = "standard" or "landy-szalay". default:standard

print('theta',bins)
print('w(theta)',corr)

bin_centers = 0.5 * (bins[1:] + bins[:-1])
#plt.plot(bin_centers, corr,'b.-')
plt.errorbar(bin_centers,corr,yerr=corr_err,fmt='rs')



#plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.show()



'''

If you need to apply some sort of masks for your surveys then it will be better to use TreeCorr

https://github.com/rmjarvis/TreeCorr/blob/main/tests/Tutorial.ipynb
https://rmjarvis.github.io/TreeCorr/_build/html/index.html


'''