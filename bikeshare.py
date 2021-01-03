import time
import pandas as pd
import numpy as np
import calendar
import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop   to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York or Washington?\n").lower()
    while city.lower() not in ('chicago', 'new york', 'washington'):
        city = input('Sorry, I did not get that, please try again:')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please select a month (January - June) or all:\n").lower()
    while month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
        month = input('Sorry, I did not get that, please try again:')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please select a day of week (Monday - Sunday) or all:\n").lower()
    while day.lower() not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        day = input('Sorry, I did not get that, please try again:')

    print('-' * 40)
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

    # read data
    file = CITY_DATA.get(city)
    df = pd.read_csv(file)

    # convert time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # filter month if selected
    if month.lower() != 'all':
        month_no = list(calendar.month_name).index(month.capitalize())
        df = df.loc[df['Start Time'].dt.month == month_no]

    # filter day if selected
    if day.lower() != 'all':
        day = day.capitalize()
        df = df.loc[df['Start Time'].dt.day_name() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    topMonth = df['Start Time'].dt.month.value_counts().idxmax()
    print('Most common month:\t\t\t' + calendar.month_name[topMonth])

    # TO DO: display the most common day of week
    topDay = df['Start Time'].dt.weekday.value_counts().idxmax()
    print('Most common day of week:\t' + calendar.day_name[topDay])

    # TO DO: display the most common start hour
    topHour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most common start hour:\t\t' + str(topHour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].dtypes)
    #print(df.groupby['Trip Duration'].sum())

    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_s_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station: '+ top_s_station)

    # TO DO: display most commonly used end station
    top_e_station = df['End Station'].value_counts().idxmax()
    print('Most common end station:   '+ top_e_station)

    # TO DO: display most frequent combination of start station and end station trip
    top_route = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most frequent combination of start and end station: ' + str(top_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: '+str(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time:  '+str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nUser type  statistic:")
    print(df.groupby(['User Type']).size())

    # TO DO: Display counts of gender
    if city.lower() != "washington":
        print("\nGender statistic:")
        print(df.groupby(['Gender']).size())
    else:
        print('\nGender statistics not available for city of Washington')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city.lower() != "washington":
        print("\nAge statistic:")
        print('Earliest year of birth: '+str(int(df['Birth Year'].min())))
        print('Most recent year of birth: '+str(int(df['Birth Year'].max())))
        print('Most common year of birth: '+str(int(df['Birth Year'].value_counts().idxmax())))
    else:
        print('\nAge statistics not available for city of Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays user level data"""

    # get user response
    answer = input('\nWould you like to see 5 lines of raw user level data? Enter yes or no.\n')

    # wait for valid input, print data for yes answer, exit if no received
    while answer.lower() != 'no':
        if answer.lower()  != 'yes':
            answer = input('Sorry, i did not get that. Please answer yes or no.\n')
        else:
            print(df.sample(n=5))
            answer = input('\nWould you like to see 5 lines of raw user level data? Enter yes or no.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # input summary
        print('Getting data for\n')
        print('city:        ' +city)
        print('month:       ' + month)
        print('day of week: ' + day)

        # 1 second delay added to not print all the data at once
        time_stats(df)
        time.sleep(1)
        station_stats(df)
        time.sleep(1)
        trip_duration_stats(df)
        time.sleep(1)
        user_stats(df,city)
        time.sleep(1)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
