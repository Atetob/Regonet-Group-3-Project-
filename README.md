# Regonet-Group-3-Project-
import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\oboma\Downloads\Bird_strikes.csv")
df = pd.DataFrame(data)
print(df)

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


# Damage severity distribution
damage_severity = df['Damage'].value_counts()

# Average cost by damage type
avg_cost_by_damage = df.groupby('Damage')['Cost'].mean()

print("Bird Strikes by Damage Severity:\n", damage_severity)
print("\nAverage Cost by Damage Type:\n", avg_cost_by_damage)


# Most frequent wildlife species
wildlife_species = df['WildlifeSpecies'].value_counts().head(10)

# Wildlife size and damage impact
species_size_damage = df.groupby(['WildlifeSpecies', 'WildlifeSize'])['Damage'].value_counts().unstack().fillna(0)

print("Top Wildlife Species:\n", wildlife_species)
print("\nDamage by Wildlife Size and Species:\n", species_size_damage)


# Convert flight date to datetime
df['FlightDate'] = pd.to_datetime(df['FlightDate'])

# Yearly bird strike trends
yearly_trend = df['FlightDate'].dt.year.value_counts().sort_index()

# Monthly trends (seasonal variation)
monthly_trend = df['FlightDate'].dt.month.value_counts().sort_index()

print("Yearly Bird Strike Trends:\n", yearly_trend)
print("\nMonthly Bird Strike Trends:\n", monthly_trend)


# Flight phase risk
flight_phase_risk = df.groupby('FlightPhase')['Damage'].value_counts().unstack().fillna(0)

# Altitude bin analysis
altitude_damage = df.groupby('AltitudeBin')['Damage'].value_counts().unstack().fillna(0)

print("Damage by Flight Phase:\n", flight_phase_risk)
print("\nDamage by Altitude Bin:\n", altitude_damage)



# Bird strikes by state
state_strikes = df['OriginState'].value_counts()

# Prepare data for visualization 
print("Bird Strikes by Origin State:\n", state_strikes)


# Pilot warning effectiveness
pilot_warned_effectiveness = df.groupby('PilotWarned')['Damage'].value_counts().unstack().fillna(0)

# Precipitation and sky conditions
precipitation_impact = df.groupby('ConditionsPrecipitation')['Damage'].value_counts().unstack().fillna(0)
sky_conditions_impact = df.groupby('ConditionsSky')['Damage'].value_counts().unstack().fillna(0)

print("Impact of Pilot Warnings:\n", pilot_warned_effectiveness)
print("\nImpact of Precipitation:\n", precipitation_impact)
print("\nImpact of Sky Conditions:\n", sky_conditions_impact)



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




import matplotlib.pyplot as plt

## Ensure 'Cost' is numeric
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')

# Average cost by damage type
avg_cost_by_damage = df.groupby('Damage')['Cost'].mean()

## Define colors
colors = ['green' if damage == 'No damage' else 'red' for damage in avg_cost_by_damage.index]

## Plot
plt.figure(figsize=(8, 5))
avg_cost_by_damage.sort_values().plot(kind='barh', color=colors, edgecolor='black')
plt.title('Average Cost by Damage Type', fontsize=14)
plt.xlabel('Average Cost ($)', fontsize=12)
plt.ylabel('Damage Type', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

## Add a legend
plt.legend(['No Damage', 'Other Damage'], loc='lower right')

plt.show()



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




# Wildlife size distribution
wildlife_size = df['WildlifeSize'].value_counts()

# Plot
plt.figure(figsize=(8, 8))
wildlife_size.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'coral'])
plt.title('Bird Strikes by Wildlife Size', fontsize=14)
plt.ylabel('')  # Remove default y-label
plt.show()



# Most frequent wildlife species
wildlife_species = df['WildlifeSpecies'].value_counts().head(10)

# Plot
plt.figure(figsize=(10, 6))
wildlife_species.sort_values().plot(kind='barh', color=['purple','pink','blue', 'yellow','brown','orange','teal','black','indigo', 'skyblue'])
plt.title('Top 10 Wildlife Species Involved in Bird Strikes', fontsize=14)
plt.xlabel('Number of Strikes', fontsize=12)
plt.ylabel('Wildlife Species', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.savefig('Top_10_Wildlife_Species_Involved_in_Bird_Strikes.png', format='png', dpi=400)
plt.show()




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



