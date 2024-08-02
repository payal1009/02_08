import os
import signal
import time
import psutil   
import asyncio
pid=os.getpid()
print(f'parent process : {pid}')
async def fun1():
    print("fun1 start...")
    asyncio.create_task(fun2())
    #await asyncio.sleep(5)
    os.system('python process_id2.py &')
    await asyncio.sleep(25)
    print("**")
    print("fun1 end....")
async def fun2():
    try:
        print("fun2 start...")
        await asyncio.sleep(15)
        f=open("file2.txt",'r')
        x=int(f.read().strip())
        f.close()
        print(f"x : {x}")
        child_process = psutil.Process(x)
        child_process.terminate()
        print("donrrrrrrrrrrrrrr")
        #await asyncio.sleep(60)  
        if psutil.pid_exists(x):
            print("a process with pid %d exists" % x)
            child_process = psutil.Process(x)
            child_process.terminate()
            print("Terminating process...")
            child_process.wait()
        else:
            print("a process with pid %d does not exist" % x)
    except psutil.NoSuchProcess:
        print(f"No such process: {x}")
    except psutil.AccessDenied:
        print(f"Access denied when trying to kill process: {x}")
    except psutil.Error as e:
        print(f"An error occurred: {e}")
    print("fun2 end....")
asyncio.run(fun1())
