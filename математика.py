import matplotlib.pyplot as plt
import numpy as np

# Создаем случайные данные
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Строим график
plt.plot(x, y)
plt.title("График синусоиды")
plt.xlabel("x")
plt.ylabel("y")

# Отображаем график
plt.show()

