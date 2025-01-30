from multiprocessing import Process, Pipe

def worker(conn):
    data = conn.recv()
    print(f"Process received in worker1: {data}")
    conn.send("Hello from worker1")  # Отправляем данные обратно

def worker2(conn, conn2):
    conn.send("Hello from worker2")  # Отправляем данные в канал
    data = conn.recv()
    print(f"Process received in worker2: {data}")

def worker3(conn):
    conn.send("Hello from worker2")  # Отправляем данные в канал
    data = conn.recv()
    print(f"Process received in worker2: {data}")

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    parent_conn1, child_conn1 = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p2 = Process(target=worker2, args=(parent_conn, parent_conn1))
    p2 = Process(target=worker3, args=(child_conn1))
    
    p.start()
    p2.start()
    
    p.join()
    p2.join()