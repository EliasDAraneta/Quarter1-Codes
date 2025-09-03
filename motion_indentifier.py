def convert_velocity(value, unit): 
    if unit == 'm/s' :
        return value * 1
    elif unit == 'ft/s' :
        return value * 0.3048
    elif unit == 'km/s' :
        return value * 1000
    elif unit == 'mi/s' :
        return value * 1609.34
        
def convert_acceleration(value, unit):
    if unit == 'm/s^2' :
        return value * 1
    elif unit == 'ft/s^2' :
        return value * 0.3048
    elif unit == 'km/s^2' :
        return value * 1000
    elif unit == 'mi/s^2' :
        return value * 1609.34
    
def motion_type(v, a):
    """
    Determine the type of motion based on velocity and acceleration
    Rules:
    - v > 0 and a = 0 → "Uniform Motion"
    - v > 0 and a > 0 → "Accelerated Motion"
    - v > 0 and a < 0 → "Decelerated Motion"
    - v = 0 → "At Rest"
    """
    # Using a small tolerance for floating-point comparisons
    if abs(v) < 1e-9:
        return "At Rest"
    elif v > 0 and abs(a) < 1e-9:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    else:
        # Catch other cases, like negative velocity
        return "Complex or non-standard motion"

v_value = float(input("Enter velocity value: "))
v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

a_value = float(input("Enter acceleration value: "))
a_unit = input("Enter acceleration unit (m/s^2, ft/s^2, km/s^2, mi/s^2): ")

v_si = convert_velocity(v_value, v_unit)
a_si = convert_acceleration(a_value, a_unit)