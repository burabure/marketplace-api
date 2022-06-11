from queick import JobQueue, SchedulingTime
from time import time

q = JobQueue()
q.enqueue(function, args=("hello",))
q.enqueue_at(time() + 5, function, args=("world",))  # Run after 5 seconds

st = SchedulingTime()
st.every(seconds=20).starting_from(time() + 10)
q.cron(st, function, args=('tick',))  # Run after 10 seconds and every 1 minute

#
