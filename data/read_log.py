import time

LastLog = "LastLog"
CurrentLog = "CurrentLog"
LoopCount = 0

while LoopCount < 10:
   fileHandle = open ('last_update.log', encoding="utf8")
   lineList = fileHandle.readlines()
   fileHandle.close()
   CurrentLog = lineList[-1].rstrip()
   if CurrentLog != LastLog: 
      print (CurrentLog)
      LastLog = CurrentLog
   else:
      LoopCount = LoopCount + 1
   time.sleep(1)
