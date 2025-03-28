import schedule
import time

def job1():
    print("I'm working 1...")

def job2():
    print("I'm working 2...")

#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
#schedule.every().minute.at(":17").do(job)



schedule.every(3).seconds.do(job1)
schedule.next_run
while True:
    schedule.run_pending()
    time.sleep(1)
    

#schedule.run_all()