""" This can be used while iterating (i is the iterator)
this code makes sure to repeat the action inside the if expression 10 times (or less if num_iters<10)

# Print cost every at intervals 10 times or as many iterations if < 10
if i% math.ceil(num_iters/10) == 0:
    w_history.append(w)
    print(f"Iteration {i:4}: Cost {float(J_history[-1]):8.2f}   ")
        
