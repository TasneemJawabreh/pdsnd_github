import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',               'saturday', 'sunday', 'all']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("please enter the city name (chicago, new york city,washington): ").lower()
        if city in cities:
            break
        else:
            print("Invalid city. Please try again.")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("please enter a month from January to June, or 'all' : ").lower()
        if month in months:
            break
        else:
            print("Invalid month. Please try again.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("please enter the name of the day or all if no need for days filtering: ").lower()
        if day in days:
            break
        else:
            print("Invalid day. Please try again.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    
    print('the most common month is:', popular_month)
    


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    popular_day = df['day'].mode()[0]
    
    print('Most Popular Start Hour:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most Popular Start Station:', popular_start_station)



    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('Most Popular End Station:', popular_end_station)



    # TO DO: display most frequent combination of start station and end station trip
    df['combination_station']=df['Start Station']+"-"+df['End Station']
    popular_combination = df['combination_station'].mode()[0]
    
    print('Most Popular End Station:', popular_combination)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
     
    
    print('Total travel time:', total_travel_time)
        


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('Total travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        count_user_types = df['User Type'].value_counts()
        print('counts of user types:', count_user_types)
    except KeyError:
        print('user type data is not available.')


    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('counts of gender:', count_gender)
    except KeyError:
        print('gender data is not available.')    


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
    
        print('earliest year of birth:', earliest_birth_year)
    
        most_recent = int(df['Birth Year'].max())
    
        print('most recent year of birth:', most_recent)
    
        most_common = int(df['Birth Year'].mode()[0])
    
        print('most common year of birth:', most_common)
    except KeyError:
        print('Birth Year data is not available.')    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("do you want to see the first five rows enter 'yes'or no: ").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            i += 5
            raw = input("do you want to see the next five rows enter 'yes'or no").lower() # TO DO: convert the user input to lower case using lower() function
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no': \n").lower()
    
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