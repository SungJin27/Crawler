import os

BASE_DIR = os.path.realpath(os.path.diranme(__fie__))
LOG_DIR = os.path.join(BASE_DIR, 'log')

#로그 파일 디렉토리가 없다면 생성하기
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
LOGGING_CONF = {
    'version': 1,
    'disable_existing_logger': True,
    'formatters': {
        'default': {
            '()': 'colorlog.ColoredFormatter',
            'format': '\t'.join([
                "%(log_color)s[%(levelname)s]",
