#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np


# In[11]:


data = pd.read_csv(r"C:\Users\oboma\Downloads\Bird_strikes.csv")
df = pd.DataFrame(data)
print(df)

#dropna(axis=1) this entry removes the row instead of the column if they display missing values
data_drop_row = df.dropna(axis=0)
data_drop_row


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
# Ensure 'Cost' is numeric
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')

# Fill or drop missing values (optional, depending on your use case)
df['Cost'] = df['Cost'].fillna(0)  # Replace NaN with 0

# Calculate damage severity distribution
damage_severity = df['Damage'].value_counts()

# Average cost by damage type
avg_cost_by_damage = df.groupby('Damage')['Cost'].mean()

# Print the results
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
# Group data for pilot warnings, precipitation, and sky conditions
pilot_warned_effectiveness = df.groupby('PilotWarned')['Damage'].value_counts().unstack().fillna(0)
precipitation_impact = df.groupby('ConditionsPrecipitation')['Damage'].value_counts().unstack().fillna(0)
sky_conditions_impact = df.groupby('ConditionsSky')['Damage'].value_counts().unstack().fillna(0)

# Plotting Pilot Warning Effectiveness
plt.figure(figsize=(8, 6))
pilot_warned_effectiveness.plot(kind='bar', stacked=True, color=['green', 'orange', 'red'], edgecolor='black')
plt.title('Effect of Pilot Warnings on Damage', fontsize=14)
plt.xlabel('Pilot Warned', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Damage Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Pilot_Warning_Effectiveness.png', format='png', dpi=400)
plt.show()

# Plotting Precipitation Impact
plt.figure(figsize=(8, 6))
precipitation_impact.plot(kind='bar', stacked=True, color=['blue', 'purple', 'pink'], edgecolor='black')
plt.title('Impact of Precipitation on Damage', fontsize=14)
plt.xlabel('Conditions Precipitation', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Damage Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Precipitation_Impact.png', format='png', dpi=400)
plt.show()

# Plotting Sky Conditions Impact
plt.figure(figsize=(8, 6))
sky_conditions_impact.plot(kind='bar', stacked=True, color=['cyan', 'gray', 'yellow'], edgecolor='black')
plt.title('Impact of Sky Conditions on Damage', fontsize=14)
plt.xlabel('Conditions Sky', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Damage Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Sky_Conditions_Impact.png', format='png', dpi=400)
plt.show()

#Use heatmaps for a different perspective
plt.figure(figsize=(10, 6))
sns.heatmap(pilot_warned_effectiveness, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Heatmap of Pilot Warnings and Damage Types', fontsize=14)
plt.xlabel('Damage Type', fontsize=12)
plt.ylabel('Pilot Warned', fontsize=12)
plt.savefig('Pilot_Warnindg_Effectiveness_Heatmap.png', format='png', dpi=400)
plt.show()

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
damage_severity.plot(kind='barh', color=['skyblue', 'red'])
plt.title('Bird Strikes by Damage Severity', fontsize=14)
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Damage Type', fontsize=12)
plt.xticks(rotation=30)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.savefig('Bird_Strikes_by_Damage_Severity.png', format='png', dpi=300)
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


# Ensure 'Damage' is categorized properly and clean missing values
df['Damage'] = df['Damage'].fillna('Unknown')  # Replace NaN with 'Unknown'
df['MakeModel'] = df['MakeModel'].fillna('Unknown')  # Replace NaN with 'Unknown'

# Grouping data by MakeModel and Damage
damage_by_make_model = df.groupby(['MakeModel', 'Damage']).size().unstack(fill_value=0)

# Top 10 MakeModels with the highest number of incidents for better visualization
top_make_models = df['MakeModel'].value_counts().head(10).index
filtered_damage_by_make_model = damage_by_make_model.loc[top_make_models]

# Plotting a stacked bar chart
plt.figure(figsize=(12, 8))
filtered_damage_by_make_model.plot(kind='bar', stacked=True, figsize=(12, 8), cmap='tab20c', edgecolor='black')
plt.title('Impact of MakeModel on Damage Level', fontsize=16)
plt.xlabel('MakeModel', fontsize=12)
plt.ylabel('Number of Bird Strikes', fontsize=12)
plt.legend(title='Damage Level', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Impact_of_MakeModel_on_Damage_Level.png', format='png', dpi=400)
plt.show()

# Plotting a heatmap for a different perspective
plt.figure(figsize=(12, 8))
sns.heatmap(filtered_damage_by_make_model, annot=True, fmt="d", cmap='YlGnBu', linewidths=0.5)
plt.title('Heatmap of Damage by MakeModel', fontsize=16)
plt.xlabel('Damage Level', fontsize=12)
plt.ylabel('MakeModel', fontsize=12)
plt.tight_layout()
plt.savefig('Heatmap_of_Damage_by_MakeModel.png', format='png', dpi=400)
plt.show()



