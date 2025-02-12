import random

def objective_function(x):
    return -x**2 + 10*x 

def hill_climb():
    current_x = random.uniform(0, 10)  
    step_size = 0.1 
    max_iterations = 100

    for _ in range(max_iterations):
        new_x = current_x + random.choice([-step_size, step_size])  
        if new_x < 0 or new_x > 10:  
            continue
        
        if objective_function(new_x) > objective_function(current_x): 
            current_x = new_x

    return current_x, objective_function(current_x)

best_x, best_value = hill_climb()
print(f"Best x: {best_x}, Best value: {best_value}")
