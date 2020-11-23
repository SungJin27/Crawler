import json
import time
import requests

PAGE_URL_LIST = [
    'http://example.com/1.page',
    'http://example.com/2.page',
    'http://example.com/3.page'
    ]
def fetch_pages():
    # 처리 기록 전용 로그 파일
    #f_info_log = open('crawler_info.log', 'a')

    #오류 기록 전용 로그 파일
    #f_error_log = open('crawler_error.log', 'a')
    with open('crawler_info.log', 'a') as f_info_log, \
        open('crawler_error.log', 'a') as f_error_log:

    #추출 내용 저장
        page_contents = {}

    #터미널 출력 + 로그 파일
        msg = "Start Crawling\n"
        print(msg)
        f_info_log.write(msg)

        for page_url in PAGE_URL_LIST:
            r = requests.get(page_url, timeout=30)
            try:
                r.raise_for_status()
            except requests.exceptions.RequestException as e:
                msg = "[ERROR] {exception}\n".format(exception=e)
                print(msg)
                f_info_log.write(msg)
                continue

            page_contents[page_url] = r.text
            time.sleep(1)

        f_info_log.close()
        f_error_log.close()

        return page_contents

if __name__ == '__main__':
    page_contents = fetch_pages()
    f_page_contents = open('page_contents.json', 'w')
    json.dump(page_contents, f_page_contents, ensure_ascii=False)
    f_page_contents.close()
    
