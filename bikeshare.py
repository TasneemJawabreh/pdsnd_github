import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - city to analyze
        (str) month - month to filter by, or "all"
        (str) day - day of week to filter by, or "all"
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    cities = list(CITY_DATA.keys())
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        city = input("Please enter the city name (Chicago, New York City, Washington): ").lower()
        if city in cities:
            break
        print("Invalid city. Please try again.")

    while True:
        month = input("Please enter a month from January to June, or 'all': ").lower()
        if month in months:
            break
        print("Invalid month. Please try again.")

    while True:
        day = input("Please enter the day of the week, or 'all': ").lower()
        if day in days:
            break
        print("Invalid day. Please try again.")

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month_index = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_index]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    df['day'] = df['Start Time'].dt.day_name()
    popular_day = df['day'].mode()[0]
    print('Most Common Day of Week:', popular_day)

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Most Commonly Used Start Station:', df['Start Station'].mode()[0])
    print('Most Commonly Used End Station:', df['End Station'].mode()[0])

    df['Trip'] = df['Start Station'] + " -> " + df['End Station']
    print('Most Frequent Trip Combination:', df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Total Travel Time:', df['Trip Duration'].sum())
    print('Mean Travel Time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        print('User Types:\n', df['User Type'].value_counts())
    except KeyError:
        print('User Type data is not available.')

    try:
        print('\nGender Counts:\n', df['Gender'].value_counts())
    except KeyError:
        print('Gender data is not available.')

    try:
        print('\nEarliest Year of Birth:', int(df['Birth Year'].min()))
        print('Most Recent Year of Birth:', int(df['Birth Year'].max()))
        print('Most Common Year of Birth:', int(df['Birth Year'].mode()[0]))
    except KeyError:
        print('Birth Year data is not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_raw_data(df):
    """Displays 5 rows of raw data upon user request."""
    i = 0
    pd.set_option('display.max_columns', 200)
    raw = input("Would you like to view the first 5 rows of raw data? Enter yes or no: ").lower()

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])
            i += 5
            raw = input("Would you like to view the next 5 rows? Enter yes or no: ").lower()
        else:
            raw = input("Invalid input. Please enter only 'yes' or 'no': ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
