import numpy as np
import math
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

area_true = np.array([30.64, 72.52, 113.31, 163.16, 222.09, 290.07, 367.12, 453.24])
kpc_scales = np.array([57.85, 89.0, 111.25, 133.5, 155.75, 178.0, 200.25, 222.5])   # in kpc



i_north = np.array([6.10e-3, 5.56e-3, 5.14e-3, 4.73e-3, 4.37e-3, 4.05e-3, 3.78e-3, 3.56e-3])
i_rms_north = np.array([1.60e-4, 1.39e-4, 1.26e-4, 1.14e-4, 1.04e-4, 9.61e-5, 8.96e-5, 8.43e-5])

i_south_e=np.array([5.04e-3, 4.71e-3, 4.44e-3, 4.17e-3, 3.91e-3, 3.67e-3, 3.44e-3, 3.24e-3])
i_rms_south_e = np.array([2.16e-4, 1.92e-4, 1.77e-4, 1.63e-4, 1.51e-4, 1.39e-4, 1.29e-4, 1.20e-4])

i_south_w=np.array([5.89e-4, 5.62e-4, 5.40e-4, 5.16e-4, 4.92e-4, 4.68e-4, 4.45e-4, 4.24e-4])
i_rms_south_w = np.array([3.95e-5, 3.73e-5, 3.56e-5, 3.38e-5, 3.20e-5, 3.04e-5, 2.88e-5, 2.74e-5])


i_err_e = np.zeros((8))
i_nbeam_true_e = np.zeros((8))

i_err_w = np.zeros((8))
i_nbeam_true_w = np.zeros((8))

i_err_n = np.zeros((8))
i_nbeam_true_n = np.zeros((8))


i_nbeam_true_n[:] = np.sqrt(892./area_true[:])
i_err_n[:] = np.sqrt((i_rms_north[:]/i_nbeam_true_n[:])**2)


i_nbeam_true_e[:] = np.sqrt(609./area_true[:])
i_err_e[:] = np.sqrt((i_rms_south_e[:]/i_nbeam_true_e[:])**2)
print('FLUSSO I NORTH')
print(i_north)
print('ERRORE FLUSSO I NORTH')
print(i_err_n)
print()

i_nbeam_true_w[:] = np.sqrt(326./area_true[:])
i_err_w[:] = np.sqrt((i_rms_south_w[:]/i_nbeam_true_w[:])**2)
#print('FLUSSO I WEST')
#print(i_south_w)
#print('ERRORE FLUSSO I WEST')
#print(i_err_w)
#print()


RM_north = np.array([1.24e-3, 1.03e-3, 9.37e-4, 8.57e-4, 7.87e-4, 7.25e-4, 6.70e-4, 6.24e-4])
RM_rms_north = np.array([3.06e-5, 2.54e-5, 2.30e-5, 2.08e-5, 1.90e-5, 1.74e-5, 1.61e-5, 1.49e-5]) 

RM_flux_density_south_e=np.array([6.79e-4, 5.00e-4, 4.45e-4, 3.96e-4, 3.53e-4, 3.15e-4, 2.86e-4, 2.63e-4])
RM_rms_south_e = np.array([2.52e-5, 1.86e-5, 1.61e-5, 1.41e-5, 1.24e-5, 1.10e-5, 9.92e-6, 9.09e-6])

RM_flux_density_south_w=np.array([3.04e-4, 2.02e-4, 1.69e-4, 1.46e-4, 1.27e-4, 1.12e-4, 9.99e-5, 9.13e-5])
RM_rms_south_w = np.array([1.98e-5, 1.33e-5, 1.12e-5, 9.62e-6, 8.34e-6, 7.34e-6, 6.54e-6, 5.95e-6])


RM_err_north = np.zeros((8))

RM_err_south_e = np.zeros((8))
RM_nbeam_true_e = np.zeros((8))

RM_err_south_w = np.zeros((8))
RM_nbeam_true_w = np.zeros((8))


RM_err_north[:] = np.sqrt((RM_rms_north[:]/i_nbeam_true_n[:])**2)

print('FLUSSO RM NORTH')
print(RM_north)
print('ERRORE FLUSSO RM NORTH')
print(RM_err_north)
print()
print()



RM_nbeam_true_e[:] = np.sqrt(609./area_true[:])
RM_err_south_e[:] = np.sqrt((RM_rms_south_e[:]/RM_nbeam_true_e[:])**2)
#print('FLUSSO RM EAST')
#print(RM_flux_density_south_e)
#print('ERRORE FLUSSO RM EAST')
#print(RM_err_south_e)
#print()

RM_nbeam_true_w[:] = np.sqrt(326./area_true[:])
RM_err_south_w[:] = np.sqrt((RM_rms_south_w[:]/RM_nbeam_true_w[:])**2)
#print('FLUSSO RM WEST')
#print(RM_flux_density_south_w)
#print('ERRORE FLUSSO RM WEST')
#print(RM_err_south_w)
#print()


p_RM_err_w = np.zeros((8))
p_RM_err_w[:] = np.sqrt((((1./i_south_w[:])*RM_err_south_w[:])**2)+(((RM_flux_density_south_w[:]/(i_south_w[:]**2))*i_err_w[:])**2))
#print('Error on polarization fraction for WEST region:')
#print(100*p_RM_err_w)


p_RM_err_e = np.zeros((8))
p_RM_err_e[:] = np.sqrt((((1./i_south_e[:])*RM_err_south_e[:])**2)+(((RM_flux_density_south_e[:]/(i_south_e[:]**2))*i_err_e[:])**2))
#print('Error on polarization fraction for EAST region:')
#print(100*p_RM_err_e)



frac_RM_n = np.zeros((8))
frac_RM_err_n = np.zeros((8))
frac_RM_n[:] = RM_north[:]/i_north[:]
frac_RM_err_n[:] = np.sqrt((((1./i_north[:])*RM_err_north[:])**2)+(((RM_north[:]/(i_north[:]**2))*i_err_n[:])**2))

print('RMSYNTHESIS POLARIZATION FRACTION FOR NORTH')
print(100.*frac_RM_n)
print('ERROR ON RMSYNTHESIS POLARIZATION FRACTION NORTH')
print(100.*frac_RM_err_n)
print()
print()



### integrated analysis at 13"

p_INT_n = np.array([7.99e-4, 6.99e-4, 6.30e-4, 5.68e-4, 5.14e-4, 4.67e-4, 4.28e-4, 3.94e-4])
p_INT_n_rms = np.array([2.09e-5, 1.76e-5, 1.56e-5, 1.39e-5, 1.25e-5, 1.13e-5, 1.03e-5, 9.49e-6])

p_INT_e = np.array([3.90e-4, 3.09e-4, 2.63e-4, 2.26e-4, 1.95e-4, 1.71e-4, 1.50e-4, 1.34e-4])
p_INT_e_rms = np.array([1.66e-5, 1.26e-5, 1.04e-5, 8.66e-6, 7.30e-6, 6.25e-6, 5.42e-6, 4.76e-6])

p_INT_w = np.array([1.63e-4, 1.41e-4, 1.25e-4, 1.11e-4, 9.89e-5, 8.91e-5, 8.12e-5, 7.47e-5])
p_INT_w_rms = np.array([1.09e-5, 9.27e-6, 8.22e-6, 7.30e-6, 6.51e-6, 5.87e-6, 5.35e-6, 4.91e-6])

frac_INT_n = np.zeros((8))
frac_INT_e = np.zeros((8))
frac_INT_w = np.zeros((8))

frac_INT_n[:] = p_INT_n[:]/i_north[:]
frac_INT_e[:] = p_INT_e[:]/i_south_e[:]
frac_INT_w[:] = p_INT_w[:]/i_south_w[:]

INT_err_north = np.zeros((8))
INT_err_south_e = np.zeros((8))
INT_err_south_w = np.zeros((8))

p_INT_err_n = np.zeros((8))
p_INT_err_w = np.zeros((8))
p_INT_err_e = np.zeros((8))

INT_err_north[:] = np.sqrt((p_INT_n_rms[:]/i_nbeam_true_n[:])**2)
INT_err_south_e[:] = np.sqrt((p_INT_e_rms[:]/RM_nbeam_true_e[:])**2)
INT_err_south_w[:] = np.sqrt((p_INT_w_rms[:]/RM_nbeam_true_w[:])**2)


print('FLUSSO INT NORTH')
print(p_INT_n)
print()
print('ERRORE FLUSSO INT NORTH')
print(INT_err_north)

print()
print()


p_INT_err_n[:] = np.sqrt((((1./i_north[:])*INT_err_north[:])**2)+(((p_INT_n[:]/(i_north[:]**2))*INT_err_north[:])**2))
p_INT_err_w[:] = np.sqrt((((1./i_south_w[:])*INT_err_south_w[:])**2)+(((p_INT_w[:]/(i_south_w[:]**2))*INT_err_south_w[:])**2))
p_INT_err_e[:] = np.sqrt((((1./i_south_e[:])*INT_err_south_e[:])**2)+(((p_INT_e[:]/(i_south_e[:]**2))*INT_err_south_e[:])**2))


print('The INTEGRATED polarization fraction for NORTH region at is:')
print(100.*frac_INT_n)
print('ERROR FOR POLARIZATION FRACTION FOR NORTH')
print(100.*p_INT_err_n)
print()

#print('The INTEGRATED polarization fraction for WEST region at 13" is:')
#print(100.*frac_INT_w)
#print(100.*p_INT_err_w)

plt.plot(kpc_scales,100.*frac_INT_n,label='RM north', marker='o', linestyle="", color='green')
plt.errorbar(kpc_scales, 100.*frac_INT_n, 100.*p_INT_err_n, capsize=6, ecolor='green', linestyle='')
plt.xlabel('beamsize in kpc')
plt.ylabel('polarization fraction')
##plt.legend()
#plt.savefig('/home/emanuele/Tesi/PSZ096_RMsynth/PSZ096_RM_polf_vs_beamsize_NORTH.png')
#plt.show()
plt.close() 


