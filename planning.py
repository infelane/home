import datetime


def players():

    lst = ['laurens', 'ruth', 'elien', 'camiel' ]
    return lst

def dagelijks():
    lst = ['afwas']

    return enumerate(lst)


def wekelijks():
    lst = ['planten water geven']
    lst.append('badkamer en middelste deel trap stofzuigen')
    lst.append("badkamer glas + lavabo's proper maken")
    lst.append("beneden + onderkant trap stofzuigen")
    lst.append("wc")

    return lst # enumerate(lst)

def maandelijks():
    lst = ['gasvuur deftig', 'afstoffen hoog en kasten afkuisen', 'oven + micro', 'dwijlen beneden']
    return enumerate(lst)

def dow(date):
    # date of the week
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayNumber=date.weekday()
    return days[dayNumber]

def iso_week(date):
    start_iso = date.isocalendar()
    week_nr = start_iso[1]
    return week_nr

def main():
    """ load """
    plyrs = players()
    job_week = wekelijks()

    """ should give the 'working' schedule """

    start_date = (2017, 11, 15) # start from next week
    start_datatime = datetime.date(*start_date)
    start_iso = start_datatime.isocalendar()
    week_nr = start_iso[1]
    day_nr = start_iso[2]

    delta_next_sun = datetime.timedelta(days=7-day_nr)
    first_sunday = start_datatime + delta_next_sun

    delta_week = datetime.timedelta(weeks=1)
    delta_day = datetime.timedelta(days=1)

    print(start_datatime)

    for i in range(52): # the next 52 weeks
        sunday_start = first_sunday + delta_week*i
        saterday_end =  first_sunday + delta_week*(i+1) - delta_day

        assert dow(sunday_start) == 'Sunday'
        assert dow(saterday_end) == 'Saturday'

        week_nr = iso_week(sunday_start)

        # print('week {}'.format(i))
        # print('{}'.format(start_datatime + delta_week*i))
        print('\n')
        print('Week {}: Sun {} - Sat {}'.format(week_nr, sunday_start, saterday_end))

        # weekly chores
        if 0:
            for i_job, job_i in enumerate(job_week):
                person_i = plyrs[(week_nr + i_job)%4]
                print('{} : {}'.format(person_i, job_i))

        # print('{}'.format())

        # TODO weekly chores
        # TODO check if first week of the month: ifso do some extra stuff


if __name__ == '__main__':
    main()