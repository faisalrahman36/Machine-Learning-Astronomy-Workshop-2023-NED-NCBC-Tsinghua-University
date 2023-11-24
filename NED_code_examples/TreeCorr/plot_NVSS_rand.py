import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename='./Random_NVSS_ra-125-175-deg-dec-10-40-borders_bright-removed-sep-cuts_0.3.csv'
catalog_data = pd.read_csv(filename, header=0,)
#print(catalog_data.head)
rad=catalog_data['rand_ra']
decd=catalog_data['rand_dec']

plt.figure(1)

#plt.plot(radr,decdr,'b.')
plt.plot(rad,decd,'r.')
plt.ylabel('DEC')
plt.xlabel('RA')
plt.gca().invert_xaxis()

plt.show()