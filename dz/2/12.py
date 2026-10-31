import matplotlib.pyplot as plt
import numpy as np

# Исходные данные
N0, dt = 1400, 1000
delta_n = np.array([71, 44, 33, 29, 28, 29, 32, 37, 45, 58])
N_t = np.array([1329, 1285, 1252, 1223, 1195, 1166, 1134, 1097, 1052, 994])
t = np.arange(1, 11) * dt
N_t_prev = np.insert(N_t[:-1], 0, N0)

# Расчёты
P_star = N_t / N0
Q_star = 1 - P_star
f_star = delta_n / (N0 * dt)
N_sr = (N_t_prev + N_t) / 2
lambda_star = delta_n / (N_sr * dt)

# Настройка шрифтов 
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 12

# Рисунок 1: Графики P*(t) и Q*(t)
plt.figure(figsize=(8, 5))
plt.plot(t, P_star, 'o-', label='P*(t)', linewidth=2, markersize=6)
plt.plot(t, Q_star, 's-', label='Q*(t)', linewidth=2, markersize=6)
plt.legend()
plt.grid(True)
plt.ylabel('Вероятность')
plt.xlabel('Время t, час')
plt.title('Рисунок 1 — Графики P*(t) и Q*(t)')
plt.tight_layout()
# Сохраняем в файл
plt.savefig('fig1_PQ.png', dpi=300, bbox_inches='tight')

# Рисунок 2: Гистограмма плотности f*(t)
plt.figure(figsize=(8, 5))
plt.bar(t, f_star * 10**5, width=500, color='green', alpha=0.7)
plt.ylabel('f*(t) × 10⁵, ч⁻¹')
plt.xlabel('Время t, час')
plt.title('Рисунок 2 — Гистограмма плотности f*(t)')
plt.grid(True, axis='y')
plt.tight_layout()
# Сохраняем в файл
plt.savefig('fig2_f.png', dpi=300, bbox_inches='tight')

# Рисунок 3: График интенсивности отказов λ*(t)
plt.figure(figsize=(8, 5))
plt.plot(t, lambda_star * 10**5, '^-', color='purple', linewidth=2, markersize=8)
plt.ylabel('λ*(t) × 10⁵, ч⁻¹')
plt.xlabel('Время t, час')
plt.title('Рисунок 3 — График интенсивности отказов λ*(t)')
plt.grid(True)
plt.tight_layout()
# Сохраняем в файл
plt.savefig('fig3_lambda.png', dpi=300, bbox_inches='tight')

plt.show()