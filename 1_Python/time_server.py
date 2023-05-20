from datetime import datetime
from flask import Flask


app = Flask(__name__)


@app.route('/')


#flask 형식의 파이썬 문법 def
def currenttime(): 
    now = datetime.now()
    time_string = now.strftime("%Y년 %m월 %D일 %H시 %M분 %S초 ")
    return f"현재 시간은: {time_string}"

#if __name__ == '__main__' 
# :은 프로그램을 실행할 수 있는 메인 함수를 만들어줌
if __name__ == '__main__' :
    app.run()

#javascript npm, python pip으로 다운로드하면 2023-05-03일 경
#해킹당할 우려가 큼