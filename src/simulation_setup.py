from models.Planet import Planet
from models.Star import Star
from utils.Physics import Physics
import math
# Celestial Bodies
sun = Star(1.989e30, 6.957e8, 3.828e29, 5773.15)
mercury = Planet(3.30104e23, 2.4397e6, 0.20563593, 6.9818e10, 38860)
earth = Planet(5.972e24, 6.371e6, 0.01671123, 1.521e11, 29290, 1)
mars = Planet(6.4169e23, 3.3895e6, 0.0933941, 2.49261e11, 21971, 2)

AU = 1.5e11  # meters

# Gravitational Constants
mercury_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, mercury.mass, 1)
earth_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, earth.mass, 1) # using radius during simulation calculation
mars_gravitational_constant = Physics.law_of_universial_gravitation(sun.mass, mars.mass, 1)

# starting conditions
# Sun
sun_x, sun_y, sun_z = 0, 0, 0
sun_velocity_x, sun_velocity_y, sun_velocity_z = 0, 0, 0

# Mercury
mercury_x, mercury_y, mercury_z = mercury.aphelion, 0, 0
mercury_velocity_x, mercury_velocity_y, mercury_velocity_z = 0, mercury.min_orbit_velocity, 0

# Earth
earth_x, earth_y, earth_z = earth.aphelion, 0, 0
earth_velocity_x, earth_velocity_y, earth_velocity_z = 0, earth.min_orbit_velocity, 0

# Mars
mars_x, mars_y, mars_z = mars.aphelion, 0, 0
mars_velocity_x, mars_velocity_y, mars_velocity_z = 0, mars.min_orbit_velocity, 0

# Time
time = 0
delta_time = 1 * Physics.days_in_secs # frames move in this time

# Positions of Celestial Bodies
sun_x_list, sun_y_list, sun_z_list = [], [], []
mercury_x_list, mercury_y_list, mercury_z_list = [], [], []
earth_x_list, earth_y_list, earth_z_list = [], [], []
mars_x_list, mars_y_list, mars_z_list = [], [], []

# Simulation data
while time < 5 * 365 * Physics.days_in_secs:
    ###### Mercury ######
    # Mercury G force
    mercury_radius_x, mercury_radius_y, mercury_radius_z = mercury_x - sun_x, mercury_y - sun_y, mercury_z - sun_z
    mercury_magnitude_vector_3 = (mercury_radius_x ** 2 + mercury_radius_y ** 2 + mercury_radius_z ** 2) ** 1.5
    force_mercury_x = -mercury_gravitational_constant * mercury_radius_x / mercury_magnitude_vector_3
    force_mercury_y = -mercury_gravitational_constant * mercury_radius_y / mercury_magnitude_vector_3
    force_mercury_z = -mercury_gravitational_constant * mercury_radius_z / mercury_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    mercury_velocity_x += force_mercury_x * delta_time / mercury.mass
    mercury_velocity_y += force_mercury_y * delta_time / mercury.mass
    mercury_velocity_z += force_mercury_z * delta_time / mercury.mass

    # Update position
    mercury_x += mercury_velocity_x * delta_time
    mercury_y += mercury_velocity_y * delta_time
    mercury_z += mercury_velocity_z * delta_time

    # Save position
    mercury_x_list.append(mercury_x)
    mercury_y_list.append(mercury_y)
    mercury_z_list.append(mercury_z)

    ###### The Earth ######
    # For Earth, compute G force on Earth
    radius_x, radius_y, radius_z = earth_x - sun_x, earth_y - sun_y, earth_z - sun_z
    magnitude_vector_3 = (radius_x ** 2 + radius_y ** 2 + radius_z ** 2) ** 1.5   # magnitude of vector
    force_earth_x = -earth_gravitational_constant * radius_x / magnitude_vector_3
    force_earth_y = -earth_gravitational_constant * radius_y / magnitude_vector_3
    force_earth_z = -earth_gravitational_constant * radius_z / magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    earth_velocity_x += force_earth_x * delta_time / earth.mass
    earth_velocity_y += force_earth_y * delta_time / earth.mass
    earth_velocity_z += force_earth_z * delta_time / earth.mass

    # Update Earth position
    earth_x += earth_velocity_x * delta_time
    earth_y += earth_velocity_y * delta_time
    earth_z += earth_velocity_z * delta_time

    # Save the Earth position
    earth_x_list.append(earth_x)
    earth_y_list.append(earth_y)
    earth_z_list.append(earth_z)

    ###### Mars ######
    # Compute G force on Earth
    mars_radius_x, mars_radius_y, mars_radius_z = mars_x - sun_x, mars_y - sun_y, mars_z - sun_z
    mars_magnitude_vector_3 = (mars_radius_x ** 2 + mars_radius_y ** 2 + mars_radius_z ** 2) ** 1.5
    force_mars_x = -mars_gravitational_constant * mars_radius_x / mars_magnitude_vector_3
    force_mars_y = -mars_gravitational_constant * mars_radius_y / mars_magnitude_vector_3
    force_mars_z = -mars_gravitational_constant * mars_radius_z / mars_magnitude_vector_3

    # Update quantities (F = ma -> a = F / m)
    mars_velocity_x += force_mars_x * delta_time / mars.mass
    mars_velocity_y += force_mars_y * delta_time / mars.mass
    mars_velocity_z += force_mars_z * delta_time / mars.mass

    # Update Earth position
    mars_x += mars_velocity_x * delta_time
    mars_y += mars_velocity_y * delta_time
    mars_z += mars_velocity_z * delta_time

    # Save the Earth position
    mars_x_list.append(mars_x)
    mars_y_list.append(mars_y)
    mars_z_list.append(mars_z)

    ###### The Sun ######
    sun_velocity_x += -(force_mercury_x + force_earth_x + force_mars_x) * delta_time / sun.mass
    sun_velocity_y += -(force_mercury_y + force_earth_y + force_mars_y) * delta_time / sun.mass
    sun_velocity_z += -(force_mercury_z + force_earth_z + force_mars_z) * delta_time / sun.mass

    # Update Sun position
    sun_x += sun_velocity_x * delta_time
    sun_y += sun_velocity_y * delta_time
    sun_z += sun_velocity_z * delta_time

    # Save the Sun position
    sun_x_list.append(sun_x)
    sun_y_list.append(sun_y)
    sun_z_list.append(sun_z)

    # Update delta time
    time += delta_time

# Celestial Body Tracks for simulation plot
mercury_x_data, mercury_y_data = [], []
earth_x_data, earth_y_data = [], []
mars_x_data, mars_y_data = [], []
sun_x_data, sun_y_data = [], []