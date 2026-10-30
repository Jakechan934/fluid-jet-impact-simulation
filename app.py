import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Fluid Jet Impact Simulator",
    page_icon="💧",
    layout="wide"
)

st.title("AI-Based Fluid Jet Impact Force Simulator")
st.subheader("Force Exerted by a Fluid Jet on a Flat Plate")

st.write(
    "This simulation calculates the force exerted by a "
    "fluid jet striking a stationary flat plate normally."
)

st.sidebar.header("Input Parameters")

density = st.sidebar.slider(
    "Fluid Density (kg/m³)", 500, 1500, 1000
)

velocity = st.sidebar.slider(
    "Jet Velocity (m/s)", 1.0, 30.0, 5.0, 0.5
)

diameter = st.sidebar.slider(
    "Nozzle Diameter (mm)", 5, 50, 10
)

# Convert diameter from mm to m
d = diameter / 1000

# Calculations
area = np.pi * d**2 / 4
discharge = area * velocity
mass_flow = density * discharge

# Momentum equation for a normal stationary flat plate
force = mass_flow * velocity

st.header("Simulation Results")

col1, col2, col3 = st.columns(3)

col1.metric("Jet Force", f"{force:.3f} N")
col2.metric("Discharge", f"{discharge:.6f} m³/s")
col3.metric("Mass Flow Rate", f"{mass_flow:.4f} kg/s")

st.header("Calculation Details")

st.latex(r"F = \dot{m}(V_1 - V_2)")

st.latex(r"F = \rho A V^2")

st.latex(r"A = \frac{\pi d^2}{4}")

st.write(f"Nozzle Area: {area:.8f} m²")
st.write(f"Mass Flow Rate: {mass_flow:.5f} kg/s")

# Force vs velocity graph
st.header("Graph 1: Force vs Jet Velocity")

velocities = np.linspace(1, 30, 100)
forces_velocity = density * area * velocities**2

fig1, ax1 = plt.subplots()
ax1.plot(velocities, forces_velocity)
ax1.scatter([velocity], [force])
ax1.set_xlabel("Jet Velocity (m/s)")
ax1.set_ylabel("Force (N)")
ax1.set_title("Force vs Jet Velocity")
ax1.grid(True)
st.pyplot(fig1)

# Force vs diameter graph
st.header("Graph 2: Force vs Nozzle Diameter")

diameters = np.linspace(5, 50, 100) / 1000
areas = np.pi * diameters**2 / 4
forces_diameter = density * areas * velocity**2

fig2, ax2 = plt.subplots()
ax2.plot(diameters * 1000, forces_diameter)
ax2.scatter([diameter], [force])
ax2.set_xlabel("Nozzle Diameter (mm)")
ax2.set_ylabel("Force (N)")
ax2.set_title("Force vs Nozzle Diameter")
ax2.grid(True)
st.pyplot(fig2)

st.success("Simulation completed successfully.")

st.caption(
    "Assumption: Ideal jet impact on a stationary flat plate. "
    "The outlet velocity component normal to the plate is zero."
)
