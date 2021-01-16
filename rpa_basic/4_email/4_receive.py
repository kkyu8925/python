# pip install imap-tools
from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# limit : 최대 메일 갯수
# revers : True 일 경우 최근 매일부터, False 일 경우 과거 메일부터
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("HTML 메시지", msg.html)
    pritn("-"*100)

mailbox.logout()
