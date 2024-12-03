#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np


# In[11]:


data = pd.read_csv(r"C:\Users\oboma\Downloads\Bird_strikes.csv")
df = pd.DataFrame(data)
print(df)


# In[15]:


# Frequency by airport
airport_strikes = df['AirportName'].value_counts().head(20)

# Frequency by operator (airline)
operator_strikes = df['Operator'].value_counts().head(20)

# Flight phase impact
flight_phase_strikes = df['FlightPhase'].value_counts()

# Wildlife species involved
wildlife_species_strikes = df['WildlifeSpecies'].value_counts()

print("Top Airports by Bird Strikes:\n", airport_strikes)
print("\nTop Operators by Bird Strikes:\n", operator_strikes)
print("\nBird Strikes by Flight Phase:\n", flight_phase_strikes)
print("\nTop Wildlife Species in Bird Strikes:\n", wildlife_species_strikes)


# In[ ]:





# In[21]:


# Remove symbols like '$' or ','
df['Cost'] = df['Cost'].str.replace('[\$,]', '', regex=True)

# Convert to numeric, coerce invalid values to NaN
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')


# In[23]:


# Damage severity distribution
damage_severity = df['Damage'].value_counts()

# Average cost by damage type
avg_cost_by_damage = df.groupby('Damage')['Cost'].mean()

print("Bird Strikes by Damage Severity:\n", damage_severity)
print("\nAverage Cost by Damage Type:\n", avg_cost_by_damage)


# In[25]:


# Most frequent wildlife species
wildlife_species = df['WildlifeSpecies'].value_counts().head(10)

# Wildlife size and damage impact
species_size_damage = df.groupby(['WildlifeSpecies', 'WildlifeSize'])['Damage'].value_counts().unstack().fillna(0)

print("Top Wildlife Species:\n", wildlife_species)
print("\nDamage by Wildlife Size and Species:\n", species_size_damage)


# In[27]:


# Convert flight date to datetime
df['FlightDate'] = pd.to_datetime(df['FlightDate'])

# Yearly bird strike trends
yearly_trend = df['FlightDate'].dt.year.value_counts().sort_index()

# Monthly trends (seasonal variation)
monthly_trend = df['FlightDate'].dt.month.value_counts().sort_index()

print("Yearly Bird Strike Trends:\n", yearly_trend)
print("\nMonthly Bird Strike Trends:\n", monthly_trend)


# In[29]:


# Flight phase risk
flight_phase_risk = df.groupby('FlightPhase')['Damage'].value_counts().unstack().fillna(0)

# Altitude bin analysis
altitude_damage = df.groupby('AltitudeBin')['Damage'].value_counts().unstack().fillna(0)

print("Damage by Flight Phase:\n", flight_phase_risk)
print("\nDamage by Altitude Bin:\n", altitude_damage)


# In[31]:


# Bird strikes by state
state_strikes = df['OriginState'].value_counts()

# Prepare data for visualization (using a hypothetical map tool)
print("Bird Strikes by Origin State:\n", state_strikes)


# In[33]:


# Pilot warning effectiveness
pilot_warned_effectiveness = df.groupby('PilotWarned')['Damage'].value_counts().unstack().fillna(0)

# Precipitation and sky conditions
precipitation_impact = df.groupby('ConditionsPrecipitation')['Damage'].value_counts().unstack().fillna(0)
sky_conditions_impact = df.groupby('ConditionsSky')['Damage'].value_counts().unstack().fillna(0)

print("Impact of Pilot Warnings:\n", pilot_warned_effectiveness)
print("\nImpact of Precipitation:\n", precipitation_impact)
print("\nImpact of Sky Conditions:\n", sky_conditions_impact)


# In[38]:


import matplotlib.pyplot as plt

# Damage severity distribution
damage_severity = df['Damage'].value_counts()

# Plot
plt.figure(figsize=(8, 5))
damage_severity.plot(kind='bar', color='skyblue')
plt.title('Bird Strikes by Damage Severity', fontsize=14)
plt.xlabel('Damage Type', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[40]:


# Ensure 'Cost' is numeric
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')

# Average cost by damage type
avg_cost_by_damage = df.groupby('Damage')['Cost'].mean()

# Plot
plt.figure(figsize=(8, 5))
avg_cost_by_damage.sort_values().plot(kind='barh', color='salmon')
plt.title('Average Cost by Damage Type', fontsize=14)
plt.xlabel('Average Cost ($)', fontsize=12)
plt.ylabel('Damage Type', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# In[42]:


# Convert FlightDate to datetime
df['FlightDate'] = pd.to_datetime(df['FlightDate'])

# Extract year and count strikes
yearly_trend = df['FlightDate'].dt.year.value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 6))
yearly_trend.plot(kind='line', marker='o', color='green')
plt.title('Yearly Bird Strike Trends', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Bird Strikes', fontsize=12)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.show()


# In[44]:


# Wildlife size distribution
wildlife_size = df['WildlifeSize'].value_counts()

# Plot
plt.figure(figsize=(8, 8))
wildlife_size.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'coral'])
plt.title('Bird Strikes by Wildlife Size', fontsize=14)
plt.ylabel('')  # Remove default y-label
plt.show()


# In[46]:


# Most frequent wildlife species
wildlife_species = df['WildlifeSpecies'].value_counts().head(10)

# Plot
plt.figure(figsize=(10, 6))
wildlife_species.sort_values().plot(kind='barh', color='purple')
plt.title('Top 10 Wildlife Species Involved in Bird Strikes', fontsize=14)
plt.xlabel('Number of Strikes', fontsize=12)
plt.ylabel('Wildlife Species', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# In[49]:


# Ensure numeric data
df['Altitude'] = pd.to_numeric(df['Altitude'], errors='coerce')
df['NumberStruck'] = pd.to_numeric(df['NumberStruck'], errors='coerce')

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Altitude'], df['NumberStruck'], alpha=0.5, color='teal')
plt.title('Altitude vs Number of Birds Struck', fontsize=14)
plt.xlabel('Altitude (ft)', fontsize=12)
plt.ylabel('Number of Birds Struck', fontsize=12)
plt.grid(alpha=0.5)
plt.show()


# In[51]:


import seaborn as sns

# Pivot table for heatmap
heatmap_data = df.pivot_table(index='AltitudeBin', columns='FlightPhase', values='Damage', aggfunc='count', fill_value=0)

# Plot
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu", linewidths=0.5)
plt.title('Frequency of Damage by AltitudeBin and FlightPhase', fontsize=14)
plt.xlabel('Flight Phase', fontsize=12)
plt.ylabel('Altitude Bin', fontsize=12)
plt.show()


# In[ ]:


import pandas as pd

# Load bird strike data
bird_strike_data = df  # Assuming df is your bird strike dataset

# Load airport location data (ensure this contains AirportName, Latitude, Longitude)
airport_locations = pd.read_csv(r"C:\Users\oboma\Downloads\Bird_strikes.csv")  # Replace with actual dataset path

# Merge datasets on AirportName
merged_data = bird_strike_data.merge(
    airport_locations, 
    on='AirportName', 
    how='left'
)

# Check for missing values in Latitude and Longitude
missing_coords = merged_data[merged_data['Latitude'].isna()]
print("Airports with missing coordinates:\n", missing_coords['AirportName'].unique())


# In[ ]:





# In[ ]:





# In[ ]:




