import matplotlib.pyplot as plt
import numpy as np
import math

def hartmann_number(
    b: float,
    l: float,
    sigma: float,
    mu: float
) -> float:
    return b * l * math.sqrt(sigma/mu)

def hartmann_analytical_velocity_profile(
    hartmann_number: float,
    coordinate: float,
    char_length: float
) -> float:
    numerator: float = math.cosh(hartmann_number) - math.cosh((hartmann_number * coordinate) / char_length)
    denominator: float = math.cosh(hartmann_number) - 1
    return numerator / denominator


# Transport properties
B1 = 1.0  # Magnetic field density B (tesla T)
B20 = 20.0  # Magnetic field density B (tesla T)
SIGMA = 1.0  # Electrical conductivity (S/m)
MU = 1.0  # dynamic viscosity (Pa s)

# Characteristic length scale
L = 1.0  # Channel spans from y = -1.0m to y = 1.0m (Total width = 2m)

# Hartmann number
M1 = hartmann_number(B1, L, SIGMA, MU)
M20 = hartmann_number(B20, L, SIGMA, MU)


# Ux velocity profiles at By = 1 T and By = 20 T

y_coordinates = np.linspace(-L, L, 200)

ux_b1 = []
ux_b20 = []

for _, y_coordinate in enumerate(y_coordinates):
    ux_b1.append(hartmann_analytical_velocity_profile(M1, y_coordinate, L))
    ux_b20.append(hartmann_analytical_velocity_profile(M20, y_coordinate, L))

# Save data
data_to_save = np.column_stack((y_coordinates, ux_b20))
np.savetxt(
    "analytical_solution_b20.xy",
    data_to_save,
    fmt="%.6e",
    delimiter=" ",
)

plt.plot(ux_b1, y_coordinates)
plt.plot(ux_b20, y_coordinates)
plt.show()
