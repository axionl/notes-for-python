from time import localtime, mktime, strftime, strptime
from datetime import datetime, timezone
import pytz

def test_for_time_module():
    now = 1507694710
    local_tuple = localtime(now)
    print(local_tuple)
    time_format = '%Y-%m-%d %H:%M:%S'
    time_str = strftime(time_format, local_tuple)
    print(time_str)

    time_tuple = strptime(time_str, time_format)
    print(time_tuple)
    utc_now = mktime(time_tuple)
    print(utc_now)

def test_for_datetime_module():
    now = datetime(2018, 8, 10, 18, 18, 30)
    now_utc = now.replace(tzinfo=timezone.utc)
    now_local = now_utc.astimezone()
    print(now_local)
    
    time_str = '2018-08-11 23:33:33'
    time_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.strptime(time_str, time_format)
    time_tuple = now.timetuple()
    utc_now = mktime(time_tuple)
    print(utc_now)

def test_for_pytz_module():
    arrival_nyc = '2018-08-11 23:33:33'
    time_format = '%Y-%m-%d %H:%M:%S'
    nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
    eastern = pytz.timezone('US/Eastern')
    nyc_dt = eastern.localize(nyc_dt_naive)
    utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
    print(utc_dt)

    pacific = pytz.timezone('US/Pacific')
    sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
    print(sf_dt)

    nepal = pytz.timezone('Asia/Katmandu')
    nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
    print(nepal_dt)

def main():
    test_for_time_module()
    test_for_datetime_module()
    test_for_pytz_module()

if __name__ == '__main__':
    main()
