import datetime


def players():

    lst = ['Laurens', 'Ruth', 'Elien', 'Camiel' ]
    return lst

def dagelijks():
    lst = ['afwas']

    return enumerate(lst)


def wekelijks():
    lst = {'plant': 'planten water geven',
           'midden': 'badkamer en middelste deel trap stofzuigen',
           "lavabo": "badkamer glas + lavabo's proper maken",
           "beneden": 'beneden + onderkant trap stofzuigen',
           "wc" : "toilet"
           }
    
    return lst

def maandelijks():
    lst = {'gasvuur' : 'gasvuur deftig',
           'afstoffen' : 'afstoffen hoog en kasten afkuisen beneden',
           'oven' : 'oven + micro',
           'dwijlen' : 'dwijlen beneden'
           }
    
    return lst

def dow(date):
    # date of the week
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayNumber=date.weekday()
    return days[dayNumber]

def iso_week(date):
    start_iso = date.isocalendar()
    week_nr = start_iso[1]
    return week_nr

def day_of_month(date):
    return date.day


def month(date):
    return date.month


def main():
    """ load """
    plyrs = players()
    job_week = wekelijks()
    job_month = maandelijks()

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
    
    date_list = []
    date_list_times = []

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

        date_list_times.append('{} - {}'.format(sunday_start, saterday_end))

        person_jobs = [[] for _ in range(4)]
        
        # weekly chores
        if 1:
            for i_job, job_i in enumerate(job_week):
                i_person = (week_nr + i_job)%4
                person_i = plyrs[i_person]
                # print('{} : {}'.format(person_i, job_i))
                (person_jobs[i_person]).append(job_i)
        
        # Monthly chores
        if day_of_month(saterday_end) <= 7:
            for i_job, job_i in enumerate(job_month):
                i_person = (month(saterday_end) + i_job) % 4
                (person_jobs[i_person]).append(job_i)
                
        for i_person, person_i in enumerate(plyrs):
            print('{} : {}'.format(person_i, person_jobs[i_person]))

        date_list.append(person_jobs)
            

        # print('{}'.format())

        # TODO weekly chores
        # TODO check if first week of the month: ifso do some extra stuff

    import csv
    
    with open('testfile.csv', 'w') as f:
        f.write('KUISPLAN\n\n')
        
        for a in job_week:
            f.write('{} = {}\n'.format(a, job_week[a]))
            
        for a in job_month:
            f.write('{} = {}\n'.format(a, job_month[a]))

        f.write('\n')
        
        spamwriter = csv.writer(f, delimiter=';',
                                quotechar='#', quoting=csv.QUOTE_MINIMAL)

        # str_list = ', '.join(plyrs)
        
        
        spamwriter.writerow([None] + plyrs)
        
        for i_dat in range(len(date_list)):
            
            str_list = [date_list_times[i_dat]] + [', '.join(a) for a in date_list[i_dat]]

            spamwriter.writerow(str_list)
            
            # str =  ' | '.join(str_list)
            # f.write(str)
    # print(date_list)


if __name__ == '__main__':
    main()