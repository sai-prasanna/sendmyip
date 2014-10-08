import urllib2,smtplib,sys,time,datetime 
from ConfigParser import SafeConfigParser

#Parsing Config File 
parser = SafeConfigParser()
parser.read('config.cfg')

smtpUrl= parser.get('MMI', 'smtpUrl')
username = parser.get('MMI', 'username')
password = parser.get('MMI', 'password')

fromaddr = parser.get('MMI', 'fromAddress') 
toaddrs  = parser.get('MMI', 'toAddress')

intreval= parser.get('MMI', 'timerInterval')


#Main
while True:
   pub_ip = urllib2.urlopen("http://ipecho.net/plain").read()#grabs ip from http://ipecho.net/plain
   ip_log=open("iplog.txt","r")
   prev_ip=ip_log.read()
   print prev_ip
   ip_log.close()
   if prev_ip == pub_ip: #check wether the ip has changed or not
      print "\n Your Ip %s didnot change so mail is not sent"%prev_ip 
   else:    
      ip_log=open("iplog.txt","w")
      ip_log.write(pub_ip) #write the ip to the log 
      ip_log.close()
      now = datetime.datetime.now()#gets time
      day = now.strftime("%Y%m%d_%H")
      print "\n The New IP: %s ip is being sent" %pub_ip
      msg = "The new ip is-"+ pub_ip  #email body 
      # The actual mail send  
      server = smtplib.SMTP(smtpUrl)  
      server.starttls()  
      server.login(username,password)  
      server.sendmail(fromaddr, toaddrs, """Subject: %s\r\n\r\n%s\r\n.\r\n""" % (
    'IP address-homepc'+day,msg))  
      server.quit()  
   time.sleep(float(intreval)) #timer

