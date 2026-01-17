def chatbot_response(gobar, eating, activity, milk, temp, dung, body_cond):
    """
    Generate a chatbot response based on cattle health parameters.
    
    Args:
        gobar: Gobar (dung) characteristics
        eating: Eating behavior
        activity: Activity level
        milk: Milk production
        temp: Temperature
        dung: Dung characteristics
        body_cond: Body condition
    
    Returns:
        str: A response string based on the health parameters
    """
    health_issues = []
    
    if eating and eating.lower() != "normal":
        health_issues.append(f"Eating abnormality detected: {eating}")
    
    if activity and activity.lower() != "normal":
        health_issues.append(f"Activity level concern: {activity}")
    
    if dung and dung.lower() != "normal":
        health_issues.append(f"Dung abnormality detected: {dung}")
    
    if body_cond and body_cond.lower() != "good":
        health_issues.append(f"Body condition issue: {body_cond}")
    
    if temp:
        try:
            temp_val = float(temp)
            if temp_val > 39.5 or temp_val < 38.0:
                health_issues.append(f"Abnormal temperature: {temp}°C")
        except ValueError:
            pass
    
    if milk and milk.lower() != "normal":
        health_issues.append(f"Milk production concern: {milk}")
    
    if health_issues:
        response = "Health concerns detected:\n" + "\n".join(health_issues)
        response += "\n\nRecommendation: Consult a veterinarian for proper diagnosis and treatment."
    else:
        response = "The cattle appears to be in good health based on the provided information."
    
    return response
