from logging import (
    getLogger,
    Formatter,
    FileHandler,
    StreamHandler,
    DEBUG,
    ERROR,
)
import requests

#로거
logger = getLogger(__name__)

#print format
default_format = '[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)d %(message)s'
default_formatter = Formatter(default_format)
funcname_foramtter = Formatter(default_format + ' (%(funcName)s)')

#log handler for console
log_stream_handler = StreamHandler()
log_stream_handler.setFormatter(default_formatter)
log_stream_handler.setLevel(DEBUG)

#log handler for file
log_file_handler = FileHandler(filename="crawler.log")
log_file_handler.setFormatter(funcname_foramtter)
log_file_handler.setLevel(ERROR)

#set level
logger.setLevel(DEBUG)
logger.addHandler(log_file_handler)
logger.addHandler(log_stream_handler)

def logging_example():
    logger.info('크롤링을 시작했습니다.')
    logger.warning('외부 사이트 링크는 크롤링하지 않습니다.')
    logger.error('페이지를 찾을 수 없습니다.')

    try:
        r = requests.get('#invalid_url', timeout=1)
    except requests.exceptions.RequestException as e:
        logger.exception('요청 중에 예외가 발생했습니다: %r', e)


if __name__ == '__main__':
    logging_example()
