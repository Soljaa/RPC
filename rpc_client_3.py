import rpyc 
import sys
import time

start = time.time()

if len(sys.argv) < 2: 
   exit("Usage {} SERVER".format(sys.argv[0])) 
  
server = sys.argv[1]
    
if len(sys.argv) < 3:
   exit(f"Usage {sys.argv[0]} {sys.argv[1]} N") 

array_max = sys.argv[2]

try:
   array_max = int(array_max)
except:
   exit("Second argument should be a number") 

array = list(range(array_max))
  
conn = rpyc.connect(server,18861)

print(conn.root.array_sum(array))

end = time.time()

print(end-start)

