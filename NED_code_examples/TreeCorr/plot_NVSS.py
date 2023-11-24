import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename='./NVSS_ra-125_175-dec-10_40_removed-bright_removed15mJy_sep-cuts_0.3.csv'
catalog_data = pd.read_csv(filename, header=0,)
#print(catalog_data.head)
rad=catalog_data['RAJ2000']
decd=catalog_data['DEJ2000']

plt.figure(1)

#plt.plot(radr,decdr,'b.')
plt.plot(rad,decd,'r.')
plt.ylabel('DEC')
plt.xlabel('RA')
plt.gca().invert_xaxis()

plt.show()