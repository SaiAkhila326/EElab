import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

w_c=11904.76
w=np.linspace(1, 100000, 10000)
A_v=1
Q=1/2
H=(A_v*(w**2))/(np.sqrt((w**2-w_c**2)**2+w**2*w_c**2/Q**2))

y_plot = 20 * np.log10(H)

plt.figure(figsize=(10, 6))
plt.semilogx(w, y_plot)
plt.title('20*log(y) vs log(x)')
plt.xlabel('x (log scale)')
plt.ylabel('20*log(y)')
plt.grid(True)



zero_crossing_index = np.argmin(np.abs(y_plot))  # Find index with minimum absolute value
w_zero = w[zero_crossing_index]  # Get the corresponding value of w

print(f"The value of x (w) where the function value is closest to zero: {w_zero}")


plt.axhline(y=0, color='r', linestyle='--')
plt.axvline(x=1, color='r', linestyle='--')
print(y_plot[9999])
plt.show()
