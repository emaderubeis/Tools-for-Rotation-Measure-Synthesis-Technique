import numpy as np
import matplotlib.pyplot as plt

x_axis = np.array([13,20,25,30,35,40,45,50])

### RESULTS FOR 5sigma REGIONS, 1 FOR THE NORTH RELIC, 1 FOR THE SOUTH RELIC

## TOTAL INTENSITY RESULTS

imsmooth_I_north = np.array([5.953e-3, 5.254e-3, 4.767e-3, 4.317e-3, 3.916e-3, 3.564e-3, 3.263e-3, 3.008e-3])
imsmooth_I_north_rms = np.array([2.88e-4, 5.82e-4, 8.13e-4, 1.050e-3, 1.286e-3, 1.522e-3, 1.758e-3, 1.998e-3])

imsmooth_I_south = np.array([1.0207e-2, 9.638e-3, 9.206e-3, 8.768e-3, 8.333e-3, 7.907e-3, 7.495e-3, 7.101e-3])
imsmooth_I_south_rms = np.array([3.16e-4, 6.79e-4, 9.95e-4, 1.348e-3, 1.728e-3, 2.126e-3, 2.537e-3, 2.953e-3])

# total intensity within the three regions used for the master degree thesis

imsmooth_I_north_2 = np.array([6.203e-3, 5.780e-3, 5.416e-3, 5.043e-3, 4.686e-3, 4.358e-3, 4.069e-3, 3.818e-3])
imsmooth_I_north_rms_2 = np.array([2.52e-4, 5.21e-4, 7.40e-4, 9.70e-4, 1.208e-3, 1.452e-3, 1.704e-3, 1.967e-3])

imsmooth_I_south_e = np.array([5.001e-3, 4.741e-3, 4.520e-3, 4.288e-3, 4.056e-3, 3.833e-3, 3.624e-3, 3.429e-3])
imsmooth_I_south_e_rms = np.array([3.34e-4, 6.98e-4, 1.006e-3, 1.342e-3, 1.698e-3, 2.066e-3, 2.440e-3, 2.819e-3])

imsmooth_I_south_w = np.array([5.91e-4, 5.68e-4, 5.50e-4, 5.30e-4, 5.09e-4, 4.88e-4, 4.67e-4, 4.47e-4])
imsmooth_I_south_w_rms = np.array([5.9e-5, 1.32e-4, 1.98e-4, 2.73e-4, 3.55e-4, 4.43e-4, 5.34e-4, 6.29e-4])




## POLARIZATION RESULTS

# integrated results

imsmooth_INT_P_north = np.array([7.27e-4, 6.43e-4, 5.91e-4, 5.44e-4, 5.04e-4, 4.69e-4, 4.39e-4, 4.14e-4])
imsmooth_INT_P_north_rms = np.array([4.1e-5, 8.2e-5, 1.16e-4, 1.52e-4, 1.90e-4, 2.3e-4, 2.72e-4, 3.15e-4])

imsmooth_INT_P_south = np.array([6.57e-4, 5.96e-4, 5.67e-4, 5.43e-4, 5.21e-4, 5.01e-4, 4.83e-4, 4.67e-4])
imsmooth_INT_P_south_rms = np.array([2.9e-5, 5.6e-5, 8.1e-5, 1.09e-4, 1.40e-4, 1.74e-4, 2.10e-4, 2.48e-4])

# RMsynthesis results

imsmooth_RM_P_north = np.array([1.522e-3, 1.508e-3, 1.495e-3, 1.482e-3, 1.469e-3, 1.458e-3, 1.448e-3,1.440e-3])
imsmooth_RM_P_north_rms = np.array([6.8e-5, 1.59e-4, 2.46e-4, 3.5e-4, 4.72e-4, 6.12e-4, 7.68e-4, 9.42e-4])

imsmooth_RM_P_south = np.array([2.261e-3, 2.251e-3, 2.243e-3, 2.235e-3, 2.229e-3, 2.223e-3, 2.218e-3, 2.214e-3])
imsmooth_RM_P_south_rms = np.array([6.1e-5, 1.43e-4, 2.23e-4, 3.19e-4, 4.33e-4, 5.64e-4, 7.12e-4, 8.78e-4])

# RMsynthesis results with 5sigma masked I

imsmooth_RM_P_north_Imask = np.array([1.423e-3, 1.311e-3, 1.221e-3, 1.130e-3, 1.044e-3, 9.65e-4, 8.93e-4, 8.28e-4])
imsmooth_RM_P_north_Imask_rms = np.array([6.4e-5, 1.40e-4, 2.03e-4, 2.70e-4, 3.39e-4, 4.08e-4, 4.77e-4, 5.46e-4])

imsmooth_RM_P_south_Imask = np.array([2.094e-3, 2.022e-3, 1.960e-3, 1.895e-3, 1.828e-3, 1.760e-3, 1.692e-3, 1.625e-3])
imsmooth_RM_P_south_Imask_rms = np.array([5.7e-5, 1.29e-4, 1.95e-4, 2.72e-4, 3.57e-4, 4.50e-4, 5.48e-4, 6.50e-4])

# RMsynthesis results with 5sigma masked I for the regions used for the master degree thesis

imsmooth_RM_P_north_Imask_2 = np.array([1.570e-3, 1.435e-3, 1.344e-3, 1.255e-3, 1.171e-3, 1.093e-3, 1.020e-3, 9.54e-4])
imsmooth_RM_P_north_Imask_2_rms = np.array([6.1e-5, 1.32e-4, 1.93e-4, 2.58e-4, 3.27e-4, 3.97e-4, 4.69e-4, 5.40e-4])

imsmooth_RM_P_south_e_Imask_2 = np.array([9.15e-4, 8.51e-4, 8.10e-4, 7.70e-4, 7.33e-4, 6.98e-4, 6.65e-4, 6.34e-4])
imsmooth_RM_P_south_e_Imask_2_rms = np.array([5.9e-5, 1.29e-4, 1.92e-4, 2.63e-4, 3.41e-4, 4.25e-4, 5.13e-4, 6.04e-4])

imsmooth_RM_P_south_w_Imask_2 = np.array([3.24e-4, 2.76e-4, 2.55e-4, 2.35e-4, 2.17e-4, 2.02e-4, 1.87e-4, 1.75e-4])
imsmooth_RM_P_south_w_Imask_2_rms = np.array([4.8e-5, 9.7e-5, 1.39e-4, 1.85e-4, 2.32e-4, 2.80e-4, 3.29e-4, 3.78e-4])




imsmooth_I_north_err = np.zeros((8))
imsmooth_I_south_err = np.zeros((8))
imsmooth_I_north_2_err = np.zeros((8))
imsmooth_I_south_e_err = np.zeros((8))
imsmooth_I_south_w_err = np.zeros((8))

imsmooth_INT_P_north_err = np.zeros((8))
imsmooth_INT_P_south_err = np.zeros((8))
imsmooth_RM_P_north_err = np.zeros((8))
imsmooth_RM_P_south_err = np.zeros((8))
imsmooth_RM_P_north_Imask_err = np.zeros((8))
imsmooth_RM_P_south_Imask_err = np.zeros((8))
imsmooth_RM_P_north_2_Imask_err = np.zeros((8))
imsmooth_RM_P_south_e_Imask_err = np.zeros((8))
imsmooth_RM_P_south_w_Imask_err = np.zeros((8))



nbeam_true_north = np.zeros((8))
nbeam_true_south = np.zeros((8))
nbeam_true_north_2 = np.zeros((8))
nbeam_true_south_e = np.zeros((8))
nbeam_true_south_w = np.zeros((8))

area_true = np.array([30.64, 72.52, 113.31, 163.16, 222.09, 290.07, 367.12, 453.24])


nbeam_true_north[:] = np.sqrt(693./area_true[:])
nbeam_true_north_2[:] = np.sqrt(892./area_true[:])
nbeam_true_south[:] = np.sqrt(1144./area_true[:])
nbeam_true_south_e[:] = np.sqrt(609./area_true[:])
nbeam_true_south_w[:] = np.sqrt(326./area_true[:])



imsmooth_I_north_err[:] = np.sqrt((imsmooth_I_north_rms[:]*nbeam_true_north[:])**2)
imsmooth_I_south_err[:] = np.sqrt((imsmooth_I_south_rms[:]*nbeam_true_south[:])**2)

imsmooth_I_north_2_err[:] = np.sqrt((imsmooth_I_north_rms_2[:]*nbeam_true_north_2[:])**2)
imsmooth_I_south_e_err[:] = np.sqrt((imsmooth_I_south_e_rms[:]*nbeam_true_south_e[:])**2)
imsmooth_I_south_w_err[:] = np.sqrt((imsmooth_I_south_w_rms[:]*nbeam_true_south_w[:])**2)


imsmooth_INT_P_north_err[:] = np.sqrt((imsmooth_INT_P_north_rms[:]*nbeam_true_north[:])**2)
imsmooth_INT_P_south_err[:] = np.sqrt((imsmooth_INT_P_south_rms[:]*nbeam_true_south[:])**2)

imsmooth_RM_P_north_err[:] = np.sqrt((imsmooth_RM_P_north_rms[:]*nbeam_true_north[:])**2)
imsmooth_RM_P_south_err[:] = np.sqrt((imsmooth_RM_P_south_rms[:]*nbeam_true_south[:])**2)

imsmooth_RM_P_north_Imask_err[:] = np.sqrt((imsmooth_RM_P_north_Imask_rms[:]*nbeam_true_north[:])**2)
imsmooth_RM_P_south_Imask_err[:] = np.sqrt((imsmooth_RM_P_south_Imask_rms[:]*nbeam_true_south[:])**2)


imsmooth_RM_P_north_2_Imask_err[:] = np.sqrt((imsmooth_RM_P_north_Imask_2_rms[:]*nbeam_true_north_2[:])**2)
imsmooth_RM_P_south_e_Imask_err[:] = np.sqrt((imsmooth_RM_P_south_e_Imask_2_rms[:]*nbeam_true_south_e[:])**2)
imsmooth_RM_P_south_w_Imask_err[:] = np.sqrt((imsmooth_RM_P_south_w_Imask_2_rms[:]*nbeam_true_south_w[:])**2)





## POLARIZATION FRACTION AND ERROR


polf_RM_north_Imask = np.zeros((8))
polf_RM_south_Imask = np.zeros((8))
polf_RM_north_Imask_err = np.zeros((8))
polf_RM_south_Imask_err = np.zeros((8))
polf_RM_north_2_Imask = np.zeros((8))
polf_RM_south_e_Imask = np.zeros((8))
polf_RM_south_w_Imask = np.zeros((8))
polf_RM_north_2_Imask_err = np.zeros((8))
polf_RM_south_e_Imask_err = np.zeros((8))
polf_RM_south_w_Imask_err = np.zeros((8))

polf_RM_north_Imask[:] = imsmooth_RM_P_north_Imask[:]/imsmooth_I_north[:]
polf_RM_south_Imask[:] = imsmooth_RM_P_south_Imask[:]/imsmooth_I_south[:]
polf_RM_north_2_Imask[:] = imsmooth_RM_P_north_Imask_2[:]/imsmooth_I_north_2[:]
polf_RM_south_e_Imask[:] = imsmooth_RM_P_south_e_Imask_2[:]/imsmooth_I_south_e[:]
polf_RM_south_w_Imask[:] = imsmooth_RM_P_south_w_Imask_2[:]/imsmooth_I_south_w[:]



polf_RM_north_Imask_err[:] = np.sqrt((((1./imsmooth_I_north[:])*imsmooth_RM_P_north_Imask_err[:])**2)+(((imsmooth_RM_P_north_Imask[:]/(imsmooth_I_north[:]**2))*imsmooth_I_north_err[:])**2))
polf_RM_south_Imask_err[:] = np.sqrt((((1./imsmooth_I_south[:])*imsmooth_RM_P_south_Imask_err[:])**2)+(((imsmooth_RM_P_south_Imask[:]/(imsmooth_I_south[:]**2))*imsmooth_I_south_err[:])**2))

polf_RM_north_2_Imask_err[:] = np.sqrt((((1./imsmooth_I_north_2[:])*imsmooth_RM_P_north_2_Imask_err[:])**2)+(((imsmooth_RM_P_north_Imask_2[:]/(imsmooth_I_north_2[:]**2))*imsmooth_I_north_2_err[:])**2))
polf_RM_south_e_Imask_err[:] = np.sqrt((((1./imsmooth_I_south_e[:])*imsmooth_RM_P_south_e_Imask_err[:])**2)+(((imsmooth_RM_P_south_e_Imask_2[:]/(imsmooth_I_south_e[:]**2))*imsmooth_I_south_e_err[:])**2)) 
polf_RM_south_w_Imask_err[:] = np.sqrt((((1./imsmooth_I_south_w[:])*imsmooth_RM_P_south_w_Imask_err[:])**2)+(((imsmooth_RM_P_south_w_Imask_2[:]/(imsmooth_I_south_w[:]**2))*imsmooth_I_south_w_err[:])**2)) 


plt.plot(x_axis,polf_RM_south_w_Imask,marker='o', linestyle="", color='blue')
plt.errorbar(x_axis,polf_RM_south_w_Imask,polf_RM_south_w_Imask_err, linestyle="", ecolor='blue')
plt.xlabel('smooth in asec')
plt.ylabel('POLARIZATION FRACTION SOUTH WEST I masked (%)')
#plt.legend()
plt.savefig('/home/emanuele/PSZ096/immagini_tesi/test_polarizationfraction_RM_south_w_Imask.png')
plt.show()
plt.close
