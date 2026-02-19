from scemas import Alerts
import json
from redis_connection import Connections
import os

conn = Connections()

Redis = conn.get_redis_conaction()


class DataProcessor:

    @staticmethod
    def get_alert_list():
        path = os.path.join("app", "border_alerts.json")
        with open(path, "r", encoding="utf-8") as file:
            data = file.read()
            return data

    @staticmethod
    def get_json_validetion(contecxt):
        json_file = json.loads(contecxt)
        alerts_list = []
        for alerts in json_file:
            alerts = Alerts(**alerts)
            alerts_list.append(alerts.model_dump())
        return alerts_list

    @staticmethod
    def Add_required_values_to_alert(alerts_list):
        for alert in alerts_list:
            if (
                alert["weapons_count"] > 0
                or alert["distance_from_fence_m"] <= 50
                or alert["visibility_quality"] < 0.5
                or alert["people_count"] >= 8
                or alert["vehicle_type"] == "truck"
            ):
                alert["priority"] = "URGENT"
            elif alert["people_count"] >= 4 and alert["distance_from_fence_m"] <= 150:
                alert["priority"] = "URGENT"
            elif alert["people_count"] >= 3 and alert["vehicle_type"] == "jeep":
                alert["priority"] = "URGENT"
            else:
                alert["priority"] = "NORMAL"
        return alerts_list

    @staticmethod
    def send_alerts_to_redis(alerts_list):
        for alerts in alerts_list:
            if alerts["priority"] == "URGENT":
                Redis.lpush("urgent_queue", json.dumps(alerts))
                print(f"alert whit priority: {alerts['priority']} pushed to queue")
            else:
                Redis.lpush("normal_queue", json.dumps(alerts))
                print(f"alert whit priority: {alerts['priority']} pushed to queue")
