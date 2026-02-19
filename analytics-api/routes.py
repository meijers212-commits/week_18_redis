from fastapi import APIRouter
from redis_connection import RConnections
from mongo_connection import MConnections
import json
from dal import Dateprocessor as dp

Mconn = MConnections()
mongo = Mconn.get_mongo_collection()

Rconn = RConnections()
redis = Rconn.get_redis_conaction()



router = APIRouter()
 
# 1
@router.get("/analytics/alerts-by-border-and-priority")
async def alerts_by_border_and_priority_r():
    if redis.exists("alerts_by_border_and_priority"):
        alert = redis.get("alerts_by_border_and_priority")
        return {"source": "redis_cache", "alerts": json.loads(alert)}
    else:
        alert_in_mongo = dp.alerts_by_border_and_priority()

        if alert_in_mongo:
            redis.set("alerts_by_border_and_priorit", json.dumps(alert_in_mongo), ex=5)
            return alert_in_mongo
        

# 2
@router.get("/analytics/top-urgent-zone")
async def top_urgent_zone_r():
    if redis.exists("top_urgent-zones"):
        alert = redis.get("top_urgent-zones")
        return {"source": "redis_cache", "alerts": json.loads(alert)}
    else:
        alert_in_mongo = dp.top_urgent_zone()

        if alert_in_mongo:
            redis.set("top_urgent-zones", json.dumps(alert_in_mongo), ex=5)
            return alert_in_mongo
        


# 3
@router.get("/analytics/distance-distribution")
async def distance_distribution_r():
    if redis.exists("distance_distribution"):
        alert = redis.get("distance_distribution")
        return {"source": "redis_cache", "alerts": json.loads(alert)}
    else:
        alert_in_mongo = dp.distance_distribution()

        if alert_in_mongo:
            redis.set("distance_distribution", json.dumps(alert_in_mongo), ex=5)
            return alert_in_mongo
        
# 4
@router.get("/analytics/low-visibility-high-activity")
async def low_visibility_high_activity_r():
    if redis.exists("low_visibility_high_activity"):
        alert = redis.get("low_visibility_high_activity")
        return {"source": "redis_cache", "alerts": json.loads(alert)}
    else:
        alert_in_mongo = dp.low_visibility_high_activity()

        if alert_in_mongo:
            redis.set("low_visibility_high_activity", json.dumps(alert_in_mongo), ex=5)
            return alert_in_mongo
        

# 5
@router.get("/analytics/hot-zones")
async def hot_zones_r():
    if redis.exists("hot_zones"):
        alert = redis.get("hot_zones")
        return {"source": "redis_cache", "alerts": json.loads(alert)}
    else:
        alert_in_mongo = dp.hot_zones()

        if alert_in_mongo:
            redis.set("hot_zones", json.dumps(alert_in_mongo), ex=5)
            return alert_in_mongo
      
