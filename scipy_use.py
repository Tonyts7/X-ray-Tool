from scipy.integrate import cumulative_trapezoid  # Correct import

# Replace cumtrapz with cumulative_trapezoid in your code
denominator = cumulative_trapezoid(G, s, initial=0)
numerator = cumulative_trapezoid(F, s, initial=0)
