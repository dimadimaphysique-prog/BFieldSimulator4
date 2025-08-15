import numpy as np
import matplotlib.pyplot as plt

def simulate_motion(q, m, v0, B, t_max, dt):
    t = np.arange(0, t_max, dt)
    r = np.zeros((len(t), 2))
    v = np.zeros((len(t), 2))
    v[0] = v0
    r[0] = [0, 0]
    
    for i in range(1, len(t)):
        a = (q / m) * np.cross(np.append(v[i-1], 0), np.append(B, 0))[:2]
        v[i] = v[i-1] + a * dt
        r[i] = r[i-1] + v[i] * dt
    
    return r

if __name__ == "__main__":
    q = 1.6e-19
    m = 9.11e-31
    v0 = np.array([1e6, 0])
    B = np.array([0, 0, 1e-3])
    t_max = 1e-6
    dt = 1e-9
    
    r = simulate_motion(q, m, v0, B, t_max, dt)
    
    plt.plot(r[:, 0], r[:, 1])
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Mouvement d'une particule chargée dans un champ B uniforme")
    plt.axis("equal")
    plt.show()
