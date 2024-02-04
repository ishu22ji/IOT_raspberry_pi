from Adafruit_IO import Client
import random
from time import sleep
USERNAME = "ishinder"
KEY = "aio_HHzw59mfHqhrssff2fkfMZQqeCUV"
aio=Client(USERNAME,KEY)
ran=aio.feeds("ishinder")
while 1:
	num=random.randint(30,50)
	aio.send(ran.key,num)
	sleep(3)
	print(num)