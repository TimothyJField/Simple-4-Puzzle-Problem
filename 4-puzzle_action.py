"""
Created on Tue Jan 10 17:13:01 2017

@author: xfang13 (Instructor) + Timothy Field
4-puzzle problem implementation in Python 
"""
import numpy as np
import copy

def solvable(state):
    explored = []
    search_history = []
    explored.append(state)
    search_history.append(state)
    results = action(state)  
    flag1 = True
    search_history.append(results[-1])
    search_history.append(results[0])
    explored.append(results[-1])
    explored.append(results[0])
   # # explored.append()
   # print search_history
    while flag1:
        all_possible_states = []  
        possible_states = action(search_history[-1])

        # print possible_states
        for j in range (0, possible_states.__len__()):
            flag2 = False
 
            for  k in range (0, explored.__len__()):
 
                if  (np.array_equal(possible_states[j], explored[k])):
                    flag2 = True
                    break
                
            if flag2 is False:
                explored.append(possible_states[j])  # #(use append)
                all_possible_states.append(possible_states[j])  # #(use append)
                 
        if (all_possible_states.__len__() == 0):
            print 'Search complete'
            flag1 = False         
                
        else:
             search_history.append(all_possible_states[0])  # #(use append)

    return explored        
 
def action(state):
    x, y = np.where(state == 0)
    x = x[0]
    y = y[0]
    result = []
    if x + 1 <= 1:
        state_copy = copy.deepcopy(state)
        temp = state_copy[x][y]
        state_copy[x][y] = state_copy[x + 1][y]
        state_copy[x + 1][y] = temp
        result.append(state_copy)
    if x - 1 >= 0:
        state_copy = copy.deepcopy(state)
        temp = state_copy[x][y]
        state_copy[x][y] = state_copy[x - 1][y]
        state_copy[x - 1][y] = temp
        result.append(state_copy)
    if y + 1 <= 1:
        state_copy = copy.deepcopy(state)
        temp = state_copy[x][y]
        state_copy[x][y] = state_copy[x][y + 1]
        state_copy[x][y + 1] = temp
        result.append(state_copy)
    if y - 1 >= 0:
        state_copy = copy.deepcopy(state)
        temp = state_copy[x][y]
        state_copy[x][y] = state_copy[x][y - 1]
        state_copy[x][y - 1] = temp
        result.append(state_copy)
       
    return result

if __name__ == '__main__':
  
     # Returns Results of possible moves       
    goalArray = (np.asarray([[0, 1], [2, 3]]))
    goal = solvable(goalArray)
    print "\n"
    print goal
 