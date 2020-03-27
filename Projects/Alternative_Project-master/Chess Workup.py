# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 01:49:39 2019

@author: Matthew Heino
"""

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

player_name = []
player_rate = []

# create an empty data frame with player data
column_names1 = ['Player Number','Player Name', 'Total Points','Round 1', 
                'Round 2', 'Round 3', 'Round 4','Round 5','Round 6','Round 7' ]

column_names2 = ['Player State', 'Pre Rating','Post Rating'] 

player_data1 = pd.DataFrame(columns=column_names1) 
player_data2 = pd.DataFrame(columns=column_names2)

with open('tournamentinfo.txt') as chess:
    
    line_count = 1
    for _ in range(4):
        next(chess)
    for chess_line in chess:
        if chess_line.startswith("-------------"):
            line_count = 1
        elif line_count == 1:
            #add string to player name
            player_name.append(chess_line)
            line_count = 2
        elif line_count == 2:
            player_rate.append(chess_line)
            line_count == 1
        else:
            print("ERROR!!!!!")

chess.close()

#print the list
for pn in player_name:
    
    player_num = pn[1:6].strip()
    player_name = pn[8:40].strip()
    total_points = float(pn[41:44])
    round1 = pn[48:52].strip()
    round2 = pn[54:58].strip()
    round3 = pn[60:64].strip()
    round4 = pn[66:70].strip()
    round5 = pn[72:76].strip()
    round6 = pn[78:82].strip()
    round7 = pn[84:88].strip()
    
    # Add to the frame.
    player_data1 = player_data1.append({'Player Number': player_num,
                                            'Player Name': player_name, 
                                            'Total Points':total_points,
                                            'Round 1': round1,'Round 2': round2,
                                            'Round 3': round3,'Round 4': round4,
                                            'Round 5': round5,'Round 6': round6,
                                            'Round 7': round7}, ignore_index=True)
   
# process the player state and other needed da
for pr in player_rate:
    
    player_state = pr[1:6]#.strip()
    player_prev = pr[22:26]
    player_post = pr[31:35]
    
    player_data2 = player_data2.append({'Player State':player_state,
                                        'Pre Rating': player_prev,
                                        'Post Rating': player_post}, ignore_index=True)
    
#merge the two frame together
player_data_all = pd.merge(player_data1, player_data2, right_index=True, left_index=True)

print(player_data_all.head(3))

# Extract the player numbers.

player_num_lst = player_data_all['Player Number'].tolist()

rating_list = []
opponent_avg = []

for num in player_num_lst:
    
    #retrieve the opponets for each player
    opponents = player_data_all[['Round 1','Round 2', 'Round 3','Round 4','Round 5','Round 6','Round 7']].loc[ player_data_all['Player Number'] == num]
    
    rat1 =  opponents['Round 1'].values[0]
    rat2 =  opponents['Round 2'].values[0]
    rat3 =  opponents['Round 3'].values[0]
    rat4 =  opponents['Round 4'].values[0]
    rat5 =  opponents['Round 5'].values[0]
    rat6 =  opponents['Round 6'].values[0]
    rat7 =  opponents['Round 7'].values[0]
    
    if rat1 != "":
        rating1 = (player_data_all[['Pre Rating']].loc[ player_data_all['Player Number'] 
        == rat1]).values[0]
        rating_list.append(int(rating1))
    
    if rat2 != "":
        rating2 = (player_data_all[['Pre Rating']].loc[ player_data_all['Player Number'] 
        == rat2]).values[0]
        rating_list.append(int(rating2))
    
    if rat3 != "":
        rating3 = (player_data_all[['Pre Rating']].loc[ player_data_all['Player Number'] 
        == rat3]).values[0]
        rating_list.append(int(rating3))
    
    if rat4 != "":
        rating4 = (player_data_all[['Pre Rating']].loc[ player_data_all['Player Number'] 
        == rat4]).values[0]
        rating_list.append(int(rating4))

    
    if rat5 != "":
        rating5 = (player_data_all[['Pre Rating']].loc[ player_data_all['Player Number'] 
        == rat5]).values[0]
        rating_list.append(int(rating5))
        
    if rat6 != "":
        rating6 = (player_data_all[['Pre Rating']].loc[ player_data_all['Player Number'] 
        == rat6]).values[0]
        rating_list.append(int(rating6))
        
    if rat7 != "":
        rating7 = (player_data_all[['Pre Rating']].loc[ player_data_all['Player Number'] 
        == rat7]).values[0]
        rating_list.append(int(rating7))
    
    #Calculate the average of the opponents
    average = sum(rating_list) / len(rating_list)
    opponent_avg.append(int(average))
    
    
    #clear the list for next interation
    rating_list.clear()
    
#add to the data frame
player_data_all['Opponent Average'] = opponent_avg


print (player_data_all.head())

#Drop the unneeded columns from the frame.
player_data_all.drop(['Round 1', 'Round 2', 'Round 3', 'Round 4','Round 5','Round 6','Round 7', 'Post Rating'],
                     axis=1, inplace=True)


#re-order the columns
reorder_col = ["Player Number", "Player Name", 'Player State', "Total Points", "Prev Rating", "Opponent Average" ]
player_data_all.reindex(columns=reorder_col)

print (player_data_all.head())



