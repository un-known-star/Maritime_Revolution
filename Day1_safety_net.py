'''

MARITIME AI LAB - DAY 1: Advanced Vessel Telemetry Validtor
Author: Purushottam Singh
Purpose: 

'''
def validate_vessel_data(vessel_name,lat,lon,speed,course,status,anchor_pos=None):
    #radius for swinging circle in degrees (approx 0.02 = -1.2 Nautical Miles)
    swing_radius = 0.02
    
    #---level 1: GLOBAL PHYSICAL LIMITS---
    if not (-90 <= lat <= 90 and -180 <= lon <=180):
        return "CRITICAL: GPS Out of Bounds for "  + vessel_name
    
    if speed < 0 or speed > 50 :
        return "CRITICAL: Log Sensor Failure for " + vessel_name
   
   #---Level 2: State-Based Logic---
    status = status.strip().lower()
   
   #Scenario A: Vessel is at Anchor 
    if status == "at anchor":
       if speed > 1.5 :
           return "ALERT: Dragging Anchor! (Speed: " + str(speed) + "kts)"
      
       if anchor_pos is not None:
           a_lat,a_lon = anchor_pos
           if abs(lat-a_lat) > swing_radius or abs(lon-a_lon) > swing_radius:
               return "ALERT: Dragging Anchor! (Position Shift Detected)"
    #Scenario B: Vessel is Underway
    elif status == "underway":
       if speed < 0.1:
           return "ADVISORY: Vessel Underway but not Making Way (NUC/Drifting?)"
       if not (0 <= course <= 360):
           return "CRITICAL: Gyro/Heading Sensor Error"
    return "STATUS OK: " + vessel_name + " telemetry verified."
#---PROJECT TEST CASES ---
# 1. Healthy Anchor
print(validate_vessel_data("Tanker_alpha",18.91,72.83,0.4,0,"at anchor",(18.91,72.83)))

# 2. Dragging Anchor
print(validate_vessel_data("Bulk_beta",18.95,72.83,2.1,0,"at anchor",(18.91,72.83)))

# 3. Underway Sensor Error
print(validate_vessel_data("Roro_charlie",1.29,103.85,15.5,450,"underway"))

   