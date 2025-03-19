import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

w_c=11904.76
w=np.linspace(1, 100000, 10000)
A_v=2.79
Q=1/(3-A_v)
H=(A_v*(w_c)*(w_c))/(np.sqrt((w**2-w_c**2)**2+w**2*w_c**2/Q**2))

y_plot = 20 * np.log10(H)

plt.figure(figsize=(10, 6))
plt.semilogx(w, y_plot)
plt.title('20*log(y) vs log(x)')
plt.xlabel('x (log scale)')
plt.ylabel('20*log(y)')
plt.grid(True)

plt.axhline(y=0, color='r', linestyle='--')
plt.axvline(x=1, color='r', linestyle='--')

print(y_plot[700])

plt.show()
