from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# ...
# mailbox.logout()

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 전체 메일 다 가져오기
    # for msg in mailbox.fetch():
    #     print("[{}] {}").format(msg.from_, msg.subject)

    # 읽지 않은 메일
    # for msg in mailbox.fetch('(UNSEEN)'):
    # print("[{}] {}").format(msg.from_, msg.subject)

    # 특정인이 보낸 메일
    # for msg in mailbox.fetch('(FROM 이메일)', limit=3, reverse=True):
    # print("[{}] {}").format(msg.from_, msg.subject)

    # 어떤 글자를 포함하는 메일 (제목, 본문)
    # 작은 따음표로 먼저 감싸고, 실제 TEXT 부분은 큰 따움표로 감싸주세요
    # for msg in mailbox.fetch('(TEXT "test mail")'):
    # print("[{}] {}").format(msg.from_, msg.subject)

    # 어떤 글자를 포함하는 메일 (제목만)
    # for msg in mailbox.fetch('(SUBJECT "test mail")':
    # print("[{}] {}").format(msg.from_, msg.subject)

    # 어떤 글자(한글)을 포함하는 메일 필터링(제목만)
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}").format(msg.from_, msg.subject)

    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', limit=5, reverse=True):
    #     print("[{}] {}").format(msg.from_, msg.subject)

    # 특정 날짜에 온 메일
    # for msg in mailbox.fetch('(ON 07-Nov-2020)', limit=5, reverse=True):
    #     print("[{}] {}").format(msg.from_, msg.subject)

    # 2가지 이상의 조건을 모두 만족하는 메일 (and 조건)
    # for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test mail")', limit=5, reverse=True):
    #     print("[{}] {}").format(msg.from_, msg.subject)

    # 2가지 이상의 조건을 하나라도 만족하는 메일 (or 조건)
    # for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test mail")', limit=5, reverse=True):
    #     print("[{}] {}").format(msg.from_, msg.subject)
