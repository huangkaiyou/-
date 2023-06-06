import time

start= time.perf_counter()
end= start

while (end-start<5):
  print(end-start)
  time.sleep(1)
  end= time.perf_counter()

print(end-start)