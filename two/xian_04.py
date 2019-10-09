import threading, queue
import time


numconsumers = 20
numproducers = 20
nummessages = 4

lock = threading.Lock()
dataQueue = queue.Queue()


def producer(idnum):
    for msgnum in range(nummessages):
        dataQueue.put("producer id=%d, count=%d" % (idnum, msgnum))


def consumer(idnum):
    while True:
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            break
        with lock:
            print("consumer", idnum, "got => ", data)
        time.sleep(0.1)
        dataQueue.task_done()


if __name__ == "__main__":
    consumerThreads = []
    producerThreads = []
    for i in  range(numproducers):
        t = threading.Thread(target=producer, args=(i,))
        producerThreads.append(t)
        t.start()
    for i in range(numconsumers):
        t = threading.Thread(target=consumer, args=(i,))
        consumerThreads.append(t)
        t.start()

    dataQueue.join()