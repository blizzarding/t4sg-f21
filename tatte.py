import os
hostname = "tattebakery.com"
response = os.system("ping -c 1" + hostname)

# Check the response
if response == 0:
  print(hostname, "is up!")
else:
  print(hostname, "is down!")