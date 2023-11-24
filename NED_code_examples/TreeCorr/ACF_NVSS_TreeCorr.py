from __future__ import print_function
import treecorr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# File paths for NVSS and random NVSS catalogs
filename_NVSS = './NVSS_ra-125_175-dec-10_40_removed-bright_removed15mJy_sep-cuts_0.3.csv'
filename_NVSS_rand = './Random_NVSS_ra-125-175-deg-dec-10-40-borders_bright-removed-sep-cuts_0.3.csv'

# Read data from CSV files into Pandas DataFrames
dat_NVSS = pd.read_csv(filename_NVSS, header=0, delimiter=',')
dat_rand_NVSS = pd.read_csv(filename_NVSS_rand, header=0, delimiter=',')

# Number of patches
N = 4
# Number of bins, minimum and maximum separation for correlation function
nbins = 100
minsep = 0.01
maxsep = 4

# Create treecorr Catalog for NVSS and random NVSS data
cat_NVSS = treecorr.Catalog(ra=dat_NVSS['RAJ2000'].tolist(), dec=dat_NVSS['DEJ2000'].tolist(),
                            ra_units='degrees', dec_units='degrees', npatch=N)

cat_rand_NVSS = treecorr.Catalog(ra=dat_rand_NVSS['rand_ra'].tolist(), dec=dat_rand_NVSS['rand_dec'].tolist(),
                                 ra_units='degrees', dec_units='degrees', patch_centers=cat_NVSS.patch_centers)

# Initialize NNCorrelation objects for auto-correlation
rr_NVSS_auto = treecorr.NNCorrelation(nbins=nbins, min_sep=minsep, max_sep=maxsep, sep_units='degrees', var_method='bootstrap')
dd_NVSS_auto = treecorr.NNCorrelation(nbins=nbins, min_sep=minsep, max_sep=maxsep, sep_units='degrees', var_method='bootstrap')
dr_NVSS_auto = treecorr.NNCorrelation(nbins=nbins, min_sep=minsep, max_sep=maxsep, sep_units='degrees', var_method='bootstrap')

# Process the correlations
rr_NVSS_auto.process(cat_rand_NVSS, cat_rand_NVSS)
dd_NVSS_auto.process(cat_NVSS, cat_NVSS)
dr_NVSS_auto.process(cat_NVSS, cat_rand_NVSS)

# Calculate the correlation function
xi1, varxi1 = dd_NVSS_auto.calculateXi(rr_NVSS_auto, dr_NVSS_auto)

# Calculate radius and standard deviation
r1 = np.exp(dd_NVSS_auto.meanlogr)
sig1 = np.sqrt(varxi1)

# Save correlation function data to a CSV file
wtheta_file_ACF3 = np.empty((len(r1), 3))
wtheta_file_ACF3[:, 0] = r1
wtheta_file_ACF3[:, 1] = xi1
wtheta_file_ACF3[:, 2] = sig1
np.savetxt("./ACF_NVSS_NVSS-ra-125_175-dec-10_0.csv", list(wtheta_file_ACF3), delimiter=",", header="theta,wtheta,sd_wtheta")

# Plot the correlation function with error bars
plt.errorbar(r1, xi1, yerr=sig1, fmt='o', label='NVSS region ra between 125 & 175 and dec between 10 & 40 ACF using Landy-Szalay ')

# Set plot properties
plt.xscale('log')
plt.xlabel(r'$\theta$ (degrees)')
plt.legend()
plt.show()
