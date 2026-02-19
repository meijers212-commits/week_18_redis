from redis_connection import RConnections
import json
from datetime import datetime
import pytz
from mongo_connection import MConnections

Rconn = RConnections()
Redis = Rconn.get_redis_conaction()

Mconn = MConnections()
mongo = Mconn.get_mongo_collection()

while True:

    queue_length = Redis.llen("urgent_queue")

    if queue_length == 0:

        alert = Redis.brpop("normal_queue")
        alert = json.loads(alert[1])
        print(f"Received alert whit priority: {alert['priority']}")
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        alert["insertion_time"] = now
        mongo.insert_one(alert)
    else:

        alert = Redis.brpop("urgent_queue")
        alert = json.loads(alert[1])
        print(f"Received alert whit priority: {alert['priority']}")
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        alert["insertion_time"] = now
        mongo.insert_one(alert)


