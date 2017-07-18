import webbrowser
import time
total_breaks=3
break_count=0
print("this program start on"+time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.xiami.com/play?ids=/song/playlist/id/2100352527/type/1#loaded")
    break_count=break_count+1
