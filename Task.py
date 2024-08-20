import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
medals_df = pd.read_csv('medals.csv')

# Specify the country you want to analyze
selected_country = 'United States'  # Replace 'USA' with the country of your choice

# Filter the DataFrame for the selected country
country_data = medals_df[medals_df['country'] == selected_country]

# Check if there is any data for the selected country
if country_data.empty:
    print(f"No data available for country: {selected_country}")
else:
    # 1. Calculate Medal Counts
    medal_count = country_data['medal_type'].value_counts()

    # 2. Calculate Participation by Gender
    participation_by_gender = country_data.groupby('gender')['discipline'].nunique()

    # Create subplots
    fig, ax = plt.subplots(1, 2, figsize=(18, 8))

    # Plot Medal Counts
    ax[0].bar(medal_count.index, medal_count.values, color=['gold', 'silver', 'brown'])
    ax[0].set_title(f'{selected_country}: Medal Counts')
    ax[0].set_xlabel('Medal Type')
    ax[0].set_ylabel('Number of Medals')

    # Plot Participation by Gender
    ax[1].bar(participation_by_gender.index, participation_by_gender.values, color=['blue', 'pink'])
    ax[1].set_title(f'{selected_country}: Number of Games Played by Gender')
    ax[1].set_xlabel('Gender')
    ax[1].set_ylabel('Number of Games')

    # Adjust layout
    plt.tight_layout()

    # Display the plots
    plt.show()
