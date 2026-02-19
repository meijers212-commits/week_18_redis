from mongo_connection import MConnections

Mconn = MConnections()
mongo = Mconn.get_mongo_collection()


class Dateprocessor:

    @staticmethod
    def alerts_by_border_and_priority():
        pipeline = [
            {
                "$group": {
                    "_id": {"border": "$border", "priority": "$priority"},
                    "count": {"$sum": 1},
                }
            }
        ]
        result = list(mongo.aggregate(pipeline))
        return result

    @staticmethod
    def top_urgent_zone():
        pipeline = [
            {"$group": {"_id": "$zone", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 5},
        ]
        result = list(mongo.aggregate(pipeline))
        return result

    @staticmethod
    def distance_distribution():
        pipeline = []
            
        result = list(mongo.aggregate(pipeline))
        return {"Written by: Elazar Meyers , Message": "I have no idea how to do this"}

    @staticmethod
    def low_visibility_high_activity():
        pipeline = [
            {"$match": {"visibility_quality": {"$gt": 0.5}}},
            {"$group": {"_id": "$zone", "count": {"$sum": 1}, "avg_people": {"$avg": "$people_count"}}},
            {"$match": {"avg_people": {"$gt": 5}}},
            {"$sort": {"count": -1}},
            {"$limit": 5},
        ]
        result = list(mongo.aggregate(pipeline))
        return result
    
    @staticmethod
    def hot_zones():
        pipeline = [
            {"$match": {"priority": "URGENT"}},
            {"$group": {"_id": "$zone", "count": {"$sum": 1}, "avg_alert": {"$avg": {"priority": "URGENT"}}}},
            {"$match": {"count": {"$gt":"avg_alert"},"distance_from_fence_m":{"$let":300}}}
            
        ]
        result = list(mongo.aggregate(pipeline))
        return result
        
