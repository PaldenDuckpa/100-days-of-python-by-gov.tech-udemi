#function 
"""
Concept	            Syntax	        Purpose
Define function   	def name():	    Create reusable code
Parameters	        def name(x):	Pass inputs to function
Return value	    return x	    Get output from function
Multiple returns	return a, b	    Return multiple values
Default params	    def name(x=5):	Set default value
Docstring	        """text"""	    Document your f
"""
#defaault parameters
"""
def delivery_message(name , status="on time"):
    print(f"{name}:  delivery is {status}")
    
delivery_message("soname") #used default "on time"
delivery_message("tashi";"delivery") #override default   
"""

#function with multiple return
def get_delivery_stats(deliveries):
    """Returns total weight and average weight"""
    total = 0
    for weight in deliveries:
        total = total + weight
    
    avg = total / len(deliveries)
    return total, avg  # Returns two values!

# Using the function
weights = [10, 5, 8, 12, 7]
total_w, avg_w = get_delivery_stats(weights)
print(f"Total: {total_w}kg, Average: {avg_w}kg")