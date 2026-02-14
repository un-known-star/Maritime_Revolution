import pandas as pd
import numpy as np

def calculate_voyage_distance(df):
  """
  Maritime AI Lab: Navigation Engine
  Calculate the distance between consecutive AIS points in a DataFrame.
  """
  R = 3444.065

  # Vectorized Radian Conversion
  lat1 = np.radians(df['lat'].shift(1))
  lon1 = np.radians(df['lon'].shift(1))
  lat2 = np.radians(df['lat'])
  lon2 = np.radians(df['lon'])

  # Haversine Formula (Vectorized)
  dlat = lat2 - lat1
  dlon = lon2 - lon1
  a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
  c = 2 * np.arcsin(np.sqrt(a))

  # Create a new column for distance of each leg
  df['leg_distance_nm'] = R * c
  return df

# --- SIMULATING A REAL AIS VOYAGE ---
data = {
    'timestamp': ['12.00', "12.30", '13.00', '13.30'],
    'lat': [18.95, 18.98, 19.05, 19.12],
    'lon': [72.94, 72.96, 73.02, 73.08]
}
voyage_df = pd.DataFrame(data)
Voyage_df = calculate_voyage_distance(voyage_df)
print("Voyage Analysis Complete:")
print(voyage_df)
print("\nTotal Distance Traveled: " + str(voyage_df['leg_distance_nm'].sum()) + " NM")
