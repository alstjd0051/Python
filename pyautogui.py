import pyautogui as m
import time
import datetime
import schedule

try:

    def job():
        # 2초후에
        time.sleep(2)
        # 좌표 위치 입력 (x,y, 버튼, 횟수, 간격)
        # SQL Server(MSSQLSERVER)서비스 클릭
        m.click(419, 188, button='left', clicks=1, interval=1)
        # 2초 후에
        time.sleep(2)
        # 다시 시작 클릭
        m.click(197, 160, button='left', clicks=1, interval=1)
        # 2초 후에
        time.sleep(2)
        # 예 클릭
        m.click(300, 318, button='left', click=1, interval=1)
        now = time.localtime()
        print("%04d/%02d/%02d %02d:%02d:%02d 클릭\n" % (now.tm_year,
              now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

        schedule.every().day.at("07:00").do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)
except KeyboardInterrupt:
    print('\b\bCtrl+C 를 눌러서 프로그램을 종료합니다.')
