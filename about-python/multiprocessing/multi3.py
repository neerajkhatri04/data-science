import multiprocessing

def sender(conn, msg) :
    for i in msg:
        conn.send(i)
    conn.close()

def receive(conn) :
    while True:
        try:
            msg = conn.recv()
        except Exception as e:
            print(e)
            break
        print(msg)

if __name__ == '__main__' :
    msg = ["hello", "How r you", "Good morning", "Good night"]
    parent_con, chile_con = multiprocessing.Pipe()
    m1 = multiprocessing.Process(target=sender, args=(chile_con, msg))
    m2 = multiprocessing.Process(target=receive, args=(parent_con,))
    m1.start()
    m2.start()
    m1.join()
    chile_con.close()
    m2.join()
    parent_con.close()
