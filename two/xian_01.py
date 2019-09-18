import threading
import time
def hell_oword():
    time.sleep(2)
    print("helloword")

t = threading.Thread(target=hell_oword)
t.start()
print("main thread")

