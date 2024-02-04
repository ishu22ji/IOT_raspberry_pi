import sys
import RPi.GPIO as GP
import time
import datetime
import random
import gspread
from ds18b20 import DS18B20
import dht11
from oauth2client.service_account import ServiceAccountCredentials

GDOCS_SPREADSHEET_NAME = "myiot"
GDOCS_OAUTH_JSON = 'myiot.json'

# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS = 30
GP.setmode(GP.BCM)
GP.setup(25, GP.IN)
GP.setwarnings(False)
req = dht11.DHT11(pin=25)

def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1 # pylint: disable=redefined-outer-name
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet. Check OAuth credentials, spreadsheet name, '
              'and make sure the spreadsheet is shared with the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)

print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet = None
humd2 = None  # Initialize with a default value

while True:
    # Login if necessary.
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    # Attempt to get sensor reading.
    result = req.read()
    if result.is_valid():
        print("Reading Started")
        temp0 = result.temperature
        humd0 = result.humidity
        if temp0 > 0:
            temp1 = temp0
            humd2 = humd0
        else:
            pass
        time.sleep(2)  # Add a small delay to avoid excessive printing

    # Skip to the next reading if a valid measurement couldn't be taken.
    # This might happen if the CPU is under a lot of load and the sensor
    # can't be reliably read (timing is critical to read the sensor).
    if humd2 is None or temp1 is None:
        time.sleep(2)
        continue

    tempx = DS18B20().get_temperature()
    rntemp = random.randint(30, 40)
    rnhumd = random.randint(30, 40)

    print("Temperature = %0.2f°C" % temp1)
    print("Humidity = %0.2f%%" % humd2)
    print('ik oor temp:    {0:0.1f} C'.format(tempx))
    print("Random Temp : %0.2f°C" % rntemp)
    print("Random Humidity : %0.2f " % rnhumd)

    # Append the data in the spreadsheet, including a timestamp
    try:
        worksheet.append_row((datetime.datetime.now().isoformat(), tempx, temp1, humd2, rntemp, rnhumd))
    except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue

    # Wait 30 seconds before continuing
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)
