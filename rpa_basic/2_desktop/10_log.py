import logging
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s [%(levelname)s] %(message)s")

# # debug < info < warning < error < critical
# logging.debug("아 이거 누가 짠거야~~")
# logging.info("자동화 수행 준비")
# logging.warning("실행중에 문제가 있을 수 있음")
# logging.error("에러 발생")
# logging.critical("치명타!!")

# 터미널과 파일에 함께 로그 남기기
# 시간 [로그레벨] 메시지 형태로 로그를 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime(
    "mylogfile_%Y%m%d%H%M%S.log")  # mylogfile_20201010.log
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그 남기는 테스트 start")
