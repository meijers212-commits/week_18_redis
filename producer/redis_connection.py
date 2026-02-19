import os
import redis


class Connections:
    
    def __init__(self):
        self.redis_host = os.getenv("REDIS_HOST", "redis")
        self.redis_port = os.getenv("REDIS_PORT", 6379)
        
        self.redis_client = redis.Redis(host=self.redis_host, port=self.redis_port, decode_responses=True)

        print("connection to Redis is ready!")


    def get_redis_conaction(self):
        return self.redis_client

  
 

