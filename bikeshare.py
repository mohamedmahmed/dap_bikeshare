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
        (str) month - name of the month to filter by,
        or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
        or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select a city to explore, options are\n' +
                     '"chicago", \n' +
                     '"new york city", or\n'
                     '"washington":\n')
        if city.lower() in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('that is not an acceptable input, please try again')
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to filter your results' +
                      ' by a specific month, ex "january",' +
                      ' if not please enter "all": \n')
        if month.lower() in ['all', 'january', 'february', 'march', 'april',
                             'may', 'june']:
            break
        else:
            print("Incorrect Input, Please try again," +
                  " correct values are 'all','january', 'february', 'march'," +
                  " 'april', 'may', 'june':\n")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Finally, would you like to filter by a specific day,' +
                    ' if not, just enter "all":\n')
        if day.lower() in ['all', 'saterday', 'sunday', 'monday', 'tuesday',
                           'wednesday', 'thursday', 'friday']:
            break
        else:
            print('that is not a correct entry, either enter "all",' +
                  ' or a day ex:"friday":\n')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if
    applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
              or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
              or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower())

        # filter by month to create the new dataframe
        df = df[df['month'] == month+1]

    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saterday']
        day = days.index(day.lower())
        df = df[df['day_of_week'] == day+1]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        print('Most Common Month: {}'.format((df['month'].mode())[0]))
    else:
        print('Data is Month Filtered, most common month is filter Month: {}'
              .format(month).title())
    # display the most common day of week
    if day == 'all':
        print('\nMost Common Day: {}'.format((df['day_of_week'].mode())[0]))
    else:
        print('\nData is Day Filtered, most common Day is filter Day: {}'
              .format(day).title())
    # display the most common start hour
    print('\nMost Common Starting Hour: {}'.format((df['hour'].mode())[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most Common Starting Station is: {}'
          .format(df['Start Station'].mode()[0]))
    # display most commonly used end station
    print('\nMost Common Ending Station is: {}'
          .format(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    df['Start_End Station'] = df['Start Station']+' - '+df['End Station']
    print('\nMost Frequent Combination of Start/End Stations: {}'
          .format(df['Start_End Station'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    Date Calcualtion performed as presented in resource
    https://www.w3resource.com/python-exercises/python-basic-exercise-65.php
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = sum(df['Trip Duration'])

    ttt_day = total_travel_time // (24 * 3600)
    total_travel_time = total_travel_time % (24 * 3600)
    ttt_hour = total_travel_time // 3600
    total_travel_time %= 3600
    ttt_minutes = total_travel_time // 60
    total_travel_time %= 60
    ttt_seconds = total_travel_time

    mean_travel_time = df['Trip Duration'].mean()

    mtt_day = mean_travel_time // (24 * 3600)
    mean_travel_time = mean_travel_time % (24 * 3600)
    mtt_hour = mean_travel_time // 3600
    mean_travel_time %= 3600
    mtt_minutes = mean_travel_time // 60
    mean_travel_time %= 60
    mtt_seconds = mean_travel_time

    # display total travel time
    print('Total Travel Time d:h:m:s: %d:%d:%d:%d'
          % (ttt_day, ttt_hour, ttt_minutes, ttt_seconds))

    # display mean travel time
    print('\nMean Travel Time d:h:m:s: %d:%d:%d:%d'
          % (mtt_day, mtt_hour, mtt_minutes, mtt_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Types: \n{}'.format(df['User Type'].value_counts()))
    # Display counts of gender

    try:
        print('\nGender Count: \n{}'.format(df['Gender'].value_counts()))
    except KeyError:
        print('\nNo Gender Information found')

    # Display earliest, most recent, and most common year of birth
    try:
        print('\nEarlist Year of Birth: {}'.format(int(min(df['Birth Year']))))
        print('\nMost Recent Year of Birth: {}'
              .format(int(max(df['Birth Year']))))
        print('\nMost Common Year of Birth: {}'
              .format(int(df['Birth Year'].mode()[0])))
    except KeyError:
        print('\nNo Year of Birth Information found.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):
    """
    A Method to Display Raw Data used in Calculating required statistics
    Data is printed in chunks.    
    Method is Similar to that presented in Course Forum Post 
    https://nfpdiscussions.udacity.com/t/problem-showing-the-sample-data-if-requested-bike-share-project/26827
    Args:
        (str) city - name of the city to analyze
    """
    while True:
        try:
            chunk_size = int(input('\nHow many records' +
                                   ' would you like to view, at a time:\n'))
            break
        except ValueError:
            print('\nPlease input a number, and not a string')

    another_set = 'yes'
    while another_set == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city.lower()],
                                     chunksize=chunk_size):
                print(chunk)
                another_set = input('\nDisplay another Set of {}'
                                    .format(chunk_size) +
                                    ' records, [y]es or [n]o\n')
                if another_set.lower() in ['no', 'yes', 'y', 'n']:
                    if another_set.lower() in ['no', 'n']:
                        break
                else:
                    another_set = input('\nIncorrect input, please enter' +
                                        ' either [y]es or [n]o.\n')
            break
        except KeyboardInterrupt:
            print('\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_display = input('\nWould you like to view the Raw Data,' +
                            ' used in the Calcualtion, [y]es or [n]o.\n')
        if raw_display.lower() == 'yes' or raw_display.lower() == 'y':
            display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
