import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# LISTS OF TIMEZONE 

TIME_ZONE = [
    "UTC",
    "US/Pacific",
    "US/Eastern",
    "Asia/Dubai",
    "Asia/Kolkata",
    "America/Los Angeles",
    "Europe/Berlin",
    "Australia/Sydney",
    "America/New_York",
    "Asia/Tokyo",
    "Europe/London",
    "America/Chicago",
    "Asia/Karachi"
]

st.title("⏲ Time Zone App")
#  Create a  multiselect widget for selected timezone
selected_timezone = st.multiselect(" Select Time Zone", TIME_ZONE , default=["Asia/Karachi"])


#  Display the selected timezone
st.subheader("Selected Timezones")
for timezone in selected_timezone:

#  Get and format the current time in the selected timezone
    current_time = datetime.now(ZoneInfo(timezone)).strftime(" %Y-%m-%d %I %H:%M:%S %p")
    st.write(f"{timezone}: {current_time}")

st.subheader("🔁 Convert Time Between TimeZones")

# Create a time input for current time
current_time = st.time_input("Current Time" , value = datetime.now().time())

# Create a selectbox for selecting timezone to convert form
from_timezone = st.selectbox(" From Timezone", TIME_ZONE , index=0)

# Create a selectbox for selecting timezone to convert to
to_timezone = st.selectbox("To TimeZone " , TIME_ZONE, index=0)

#  Convert the current time to the selected timezone
if st.button("Convert Time"):
    datetime = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_timezone))
    converted_time = datetime.astimezone(ZoneInfo(to_timezone)).strftime(" %Y-%m-%d %I %H:%M:%S %p")

    st.success(f"Converted Time in {to_timezone} is {converted_time}") 