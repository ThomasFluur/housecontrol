import smtplib # Varför ger både * och  SMTP varning?
# import datetime  #  Görs på flera ställen ta  bort när de skall ihop
from email.mime.multipart import MIMEMultipart  #  Problem med exempel på 2.7
from email.mime.text import MIMEText
debuglevel = 1  #  Från exempel kod  behövs  den?
msg = MIMEMultipart()
# smtp = SMTP()
#  smtp.set_debuglevel(debuglevel)# Om det fungera prova att ta  bort
msg['From']= 'thomas.fluur@telia.com'
msg ['To'] = 'fluur.bergkvist@telia.com'
msg ['Subject'] = "simple email test2"
message = "Info 1"
msg.attach(MIMEText(message))


mailserver = smtplib.SMTP()
mailserver.set_debuglevel(debuglevel)
telia = 'mailout.telia.com' #  Gmail doesn't work even if usecure app is used
#  gmail = 'smtp.gmail.com'
mailserver= smtplib.SMTP(telia ,587)

mailserver.ehlo()
mailserver.starttls
mailserver.ehlo()
mailserver.login('thomas.fluur@telia.com', '99LuftBallong')
mailserver.sendmail("thomas.fluur@telia.com","fluur.bergkvist@telia.com",msg.as_string())
mailserver.quit()

