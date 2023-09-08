import schedule, time, os, smtplib, random, linecache
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# password = os.environ['mailPassword']
# username = os.environ['mailUsername']

def printMe():
  random_line = random.randint(1, 1623)
  top_found = False
  quote_to_print = ""
  while True:
    quote = linecache.getline("quotes.txt", random_line)

    if top_found == False:
      if quote != "" and quote != "\n":
        random_line -= 1
      else:
        top_found = True
        random_line += 1
    else:
      if quote != "" and quote != "\n":
        quote_to_print += quote
        random_line += 1
      else:
        print(quote_to_print)
        return quote_to_print
  
    #sendMail(quote_to_print)

def sendMail(quote_to_print):
  email = "Quote of the day" 
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 

  msg = MIMEMultipart() 
  msg['To'] = "recipient@email.com" 
  msg['From'] = username 
  msg['Subject'] = quote_to_print
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg) 
  del msg 

schedule.every(24).hours.do(printMe) 

while True:
  schedule.run_pending()
  time.sleep(1)
