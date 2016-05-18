
import smtplib
import urllib.request
from bs4 import BeautifulSoup


def fetch_info():
    link = urllib.request.urlopen('http://www.fcbarcelona.com/')
    soup = BeautifulSoup(link, "html.parser")
    match_body = soup.find('div', {'class': 'match__body'})

    competition = match_body.find('span', {'class': 'match__main__competition'}).text.strip()
    phase = match_body.find('span', {'class': 'match__main__phase'}).text.strip()
    day_time = match_body.find('time').text
    day_time_splited = day_time.split('|')
    day_time_splited[1] = day_time_splited[1].strip()
    day_time_splited[0] = day_time_splited[0].strip()

    teams = match_body.findAll('span', {'class': 'scoreboard__team__name'})
    team=[]
    for t in teams:
        team.append(t.text.strip())

    #team names must be in English else unexpected output will be generated

    print(team)
    print(competition + ' | ' + phase)
    print(day_time_splited[0])
    print(day_time_splited[1])
    Subject = competition + ' | ' + phase
    Content =  team[0] +' will be up against ' + team[1] + ' on ' + day_time_splited[0] + ' at ' + \
              day_time_splited[1]

    return Subject,Content


def send_mail(Subject,Content):
    To = ['TO_EMAIL_ID']
    From = 'FROM_EMAIL_ID'
    
    '''
    Google blocks sign-in attempts from apps which do not use modern security standards (mentioned on their support page). 
    You can however, turn on/off this safety feature by going to the link below:
    Go to this link and select Turn On
    https://www.google.com/settings/security/lesssecureapps
    
    '''
    
    Content=Content.encode('utf-8') #smtp does not support UNICODE
    message = 'Subject: %s\n\n%s' % (Subject, Content)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('FROM_EMAIL_ID', 'PASSWORD')
    mail.sendmail(From, To, message)
    mail.close()


def main():
    sub,con=fetch_info()
    send_mail(sub,con)

main()
