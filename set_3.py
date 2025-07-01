#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def relationship_status(from_member, to_member, social_graph):
    #go to social_graph and check if from_member is in social graph *else return empty dictionary*
    # [2] go to from_member's "following" list and check if to_member is in it. else, return empty list 
    follows_to:to_member in social_graph.get(from_member,{}).get("following",[])
    
    # vice versa 
    follows_from:from_member in social_graph.get(to_member,{}).get("following",[])

    #if both true,
    if follows_to and follows_from:
        return "friends"
    #if only from_member is "following"/true then from_member is the one following,
    elif follows_to:
        return "follower"
    elif follows_from:
        return "followed by"
    else:
        return "no relationship"


# In[5]:


def tic_tac_toe(board):
    #how many columns and rows. works because square but what if not square?
    size=len(board)
    
    #check rows one by one
    for row in board:
        #if all the elements of the set is the same and is not equal to a blank
        if len(set(row))==1 and row[0] != '':
            return row[0]
        
    for col in range(size):
        #build the elements by collecting from each row...[1][0]=get the first element of row 2
        column=[board[row][col] for row in range(size)]
        if len(set(column))==1 and column[0] != '':
            return column[0]
            
    #note: only 2 diagonal in a square
    #left to right diagonal
    diagonalA=[board[i][i] for i in range(size)]
    if len(set(diagonalA))==1 and diagonalA[0] != '':
            return diagonalA[0]
    
    #right to left diagonal
    diagonalB=[board[i][size-1-i] for i in range(size)]
    if len(set(diagonalB))==1 and diagonalB[0] != '':
            return diagonalB[0]

    return "NO WINNER"


# In[ ]:


def eta(first_stop, second_stop, route_map):
    if first_stop == second_stop:
        return 0

    current_stop = first_stop
    total_time = 0

    while True:
        for (start, end), time in route_map.items():
            if start == current_stop:
                total_time += time['travel_time_mins']
                #updating...
                current_stop = end
                #since a->b then b->c...
                break
        #if last stop na
        if current_stop == second_stop:
            return total_time
        #para hindi ikot
        if current_stop == first_stop:
            return total_time

