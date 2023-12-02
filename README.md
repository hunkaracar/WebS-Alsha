# WebS-Alsha Software Version-2

##
WebS-Alsha software is a script written in Python language that has the capabilities of web-based scanning, discovery, technology detection, port scanning, database detection, directory scanning, subdomin detection scanning, firewall detection and IP detection.
##

### Shows the help documentation

`python alsha.py -h` 

### It basically gives information about the site 

`python alsha.py -u http://www.example.com/`  

### It basically shows the technologies the target site is using

`python alsha.py -uT http://www.example.com/` 

### It tells the running service by scanning the ports of the most used databases on the target website.

`python alsha.py -dbs <target IP> `  

###  It may not provide definitive results that are useful for performing basic firewall detection.

`python alsha.py -fw <target IP>` 

It checks whether the robots.txt file that the developers have placed on the target website most of the time, and returns the values ​​if any.

`python alsha.py -R http://www.example.com`  

### It tries to learn and return the IP address by pinging the target site.

`python alsha.py -Pn www.example.com`   

### Scans the 35 most used ports on the target site and tries to get Version information

`python alsha.py -sS <target IP>` 

### It scans and detects existing directories and hidden directories on the target website.

`python alsha.py -D <http://example.com>`

### Performs a subdominance scan on the target system

`python alsha.py -subd example.com --protocol http or https`
  
  
## We load our computer with the following command
 
  ### cd Alsha
  
  ### for Windows => dir
  ### for Linux => ls
 
 ### pip3 install -r requirements.txt
  
 ### ================================ 
 
  ### Then;
  
  ### cd alsha
  
  ### for Windows => dirr
  ### for Linux => ls
  
  ### Let's run the code
  
  ### For windows => python alsha.py -h
  
  ### For linux => python3 alsha.py -h
  
