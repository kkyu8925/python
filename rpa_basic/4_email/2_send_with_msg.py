import smtplib
from account import *
from email.message from EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."  # 제목
msg["From"] = EMAIL_ADDRESS  # 보내는 사람
msg["To"] = ""  # 받는 사람

# 여러 명에게 메일을 보낼 때
# msg["To"] = "email, email"
# or
# to_list = [email, email]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "이메일"
# 비밀참조
# msg["Bcc"] = "이메일"

msg.set_content("테스트 본문")  # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
