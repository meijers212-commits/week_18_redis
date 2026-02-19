from priority_logic import DataProcessor as dp



data = dp.get_json_validetion(dp. get_alert_list())
udated_datat_to_redis = dp.Add_required_values_to_alert(data)
dp.send_alerts_to_redis(udated_datat_to_redis)

    
 