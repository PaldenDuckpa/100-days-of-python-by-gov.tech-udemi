# tech_utils.py - Your personal tech toolkit

def check_battery(level):
    if level < 20:
        return "Critical - Charge immediately!"
    elif level < 50:
        return "Low - Charge soon"
    elif level < 80:
        return "Good"
    else:
        return "Excellent"

def check_storage(used, total):
    percentage = (used / total) * 100
    if percentage > 90:
        return "Critical - Almost full!"
    elif percentage > 70:
        return "Warning - Low storage"
    else:
        return "Storage is fine"

def calculate_repair_cost(device, parts_cost, labor_hours):
    labor_rate = 500  # Per hour
    labor_cost = labor_hours * labor_rate
    total = parts_cost + labor_cost
    
    if device.lower() == "laptop":
        total = total * 1.1  # 10% tax for laptops
    elif device.lower() == "mobile":
        total = total * 1.05  # 5% tax for mobiles
    
    return round(total, 2)

def device_status(device_type, age_years):
    if device_type.lower() == "laptop":
        if age_years < 2:
            return "Like new"
        elif age_years < 4:
            return "Good condition"
        elif age_years < 6:
            return "Needs attention"
        else:
            return "Consider replacement"
    elif device_type.lower() == "mobile":
        if age_years < 1:
            return "Like new"
        elif age_years < 3:
            return "Good condition"
        elif age_years < 5:
            return "Needs attention"
        else:
            return "Consider replacement"
    else:
        return "Unknown device"
