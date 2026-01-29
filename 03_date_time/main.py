# ============================================
# PYTHON DATE & TIME MODULE - COMPLETE NOTES
# ============================================


# --------------------------------------------
# 1️⃣ Parsing ISO datetime string
# --------------------------------------------
from datetime import datetime

dt = datetime.strptime(
    "2026-01-23T23:58:09",
    "%Y-%m-%dT%H:%M:%S"
)
print(dt)


# --------------------------------------------
# 2️⃣ Timezone-aware datetime (JST)
# --------------------------------------------
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))
dt = datetime(2026, 1, 1, 12, 0, 0, tzinfo=JST)

print(dt)
print(dt.tzname())


# --------------------------------------------
# 3️⃣ Computing time difference
# --------------------------------------------
from datetime import datetime, timedelta

now = datetime.now()
then = datetime(2016, 5, 23)

delta = now - then

print(delta.days)
print(delta.seconds)


# --------------------------------------------
# 4️⃣ N days AFTER a given date
# --------------------------------------------
from datetime import datetime, timedelta

def get_n_days_after_date(start_date, date_format="%d %B %Y", add_days=180):
    base_date = datetime.strptime(start_date, date_format)
    future_date = base_date + timedelta(days=add_days)
    return future_date.strftime(date_format)

print(get_n_days_after_date("01 January 2026", add_days=180))


# --------------------------------------------
# 5️⃣ N days BEFORE today (auto-pick now)
# --------------------------------------------
from datetime import datetime, timedelta

def get_n_days_before_date(date_format="%d %B %Y", days_before=123):
    past_date = datetime.now() - timedelta(days=days_before)
    return past_date.strftime(date_format)

print(get_n_days_before_date())


# --------------------------------------------
# 6️⃣ Basic datetime objects
# --------------------------------------------
import datetime

today = datetime.date.today()
new_year = datetime.date(2027, 1, 1)

noon = datetime.time(12, 0, 0)
now = datetime.datetime.now()

millennium_turn = datetime.datetime(2026, 1, 1, 0, 0, 0)
today_midnight = datetime.datetime(today.year, today.month, today.day)

print(
    "Time since the millennium at today's midnight:",
    today_midnight - millennium_turn
)


# --------------------------------------------
# 7️⃣ Switching between time zones
# --------------------------------------------
from datetime import datetime
from dateutil import tz

utc = tz.tzutc()
local = tz.tzlocal()

utc_now = datetime.now(tz=utc)
local_now = utc_now.astimezone(local)

print("UTC Time   :", utc_now)
print("Local Time :", local_now)


# --------------------------------------------
# 8️⃣ Simple date arithmetic
# --------------------------------------------
import datetime

today = datetime.date.today()
print(f"Today : {today}")

tomorrow = today + datetime.timedelta(days=1)
print(f"Tomorrow : {tomorrow}")

yesterday = today - datetime.timedelta(days=1)
print(f"Yesterday : {yesterday}")

print(f"Time between tomorrow and yesterday : {tomorrow - yesterday}")


# --------------------------------------------
# 9️⃣ Converting timestamp to datetime
# --------------------------------------------
from datetime import datetime, timezone
import time

seconds_since_epoch = time.time()
utc_date = datetime.fromtimestamp(seconds_since_epoch, tz=timezone.utc)

print(utc_date)


# --------------------------------------------
# 🔟 Adding / Subtracting months safely
# --------------------------------------------
import calendar
from datetime import date

def monthdelta(base_date, delta):
    new_month = (base_date.month + delta) % 12
    new_year = base_date.year + (base_date.month + delta - 1) // 12

    if new_month == 0:
        new_month = 12

    new_day = min(base_date.day, calendar.monthrange(new_year, new_month)[1])
    return base_date.replace(year=new_year, month=new_month, day=new_day)

next_month = monthdelta(date.today(), 1)
previous_month = monthdelta(date.today(), -1)

print("Next month     :", next_month)
print("Previous month :", previous_month)


# --------------------------------------------
# 1️⃣1️⃣ Parsing timezone abbreviations (EST, PST)
# --------------------------------------------
from dateutil import tz
from dateutil.parser import parse

ET = tz.gettz("US/Eastern")
CT = tz.gettz("US/Central")
MT = tz.gettz("US/Mountain")
PT = tz.gettz("US/Pacific")

us_tzinfos = {
    "CST": CT, "CDT": CT,
    "EST": ET, "EDT": ET,
    "MST": MT, "MDT": MT,
    "PST": PT, "PDT": PT
}

dt_est = parse("2026-01-30 04:00:00 EST", tzinfos=us_tzinfos)
dt_pst = parse("2026-01-30 12:00:03 PST", tzinfos=us_tzinfos)

print(dt_est)
print(dt_pst)


# --------------------------------------------
# 1️⃣2️⃣ Extract datetime from free text
# --------------------------------------------
from dateutil.parser import parse

dt = parse("Today is january 30, 2026 at 2:21:00AM", fuzzy=True)
print(dt)


# --------------------------------------------
# 1️⃣3️⃣ Iterating over a date range
# --------------------------------------------
import datetime
from datetime import timedelta

day_delta = timedelta(days=1)
start_date = datetime.date.today()
end_date = start_date + 7 * day_delta

for i in range((end_date - start_date).days):
    print(start_date + i * day_delta)
