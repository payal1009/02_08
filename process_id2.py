import os
import time
import signal
import asyncio
async def fun(a,b):
    sum=a+b
    #print(sum)
    pid=os.getpid()
    print(f"2nd pid fun: {pid}")
    print(sum)
    await asyncio.sleep(10)
    print("Doraaaaa")
    try:
        f=open("file2.txt",'w')
        f.write(str(pid))
        f.close()
    except Exception as e:
        print(e)
    await asyncio.sleep(10)
    print("Last")
    # for i in range(0,50):
    #     print(i)
    #     time.sleep(1)
    # print("#######")
if __name__ == "__main__":
    asyncio.run(fun(10,20))












