# importing the sample data for visualization
data = {
'BRO': {'BSN': { 'W': 10, 'L': 12 },'CHC': { 'W': 15, 'L': 7 },'CIN': { 'W': 15, 'L': 7 },'NYG': { 'W': 14, 'L': 8 },
        'PHI': { 'W': 14, 'L': 8 },'PIT': { 'W': 15, 'L': 7 },'STL': { 'W': 11, 'L': 11 }},
'BSN': {'BRO': { 'W': 12, 'L': 10 },'CHC': { 'W': 13, 'L': 9 },'CIN': { 'W': 13, 'L': 9 },'NYG': { 'W': 13, 'L': 9 },
        'PHI': { 'W': 14, 'L': 8 },'PIT': { 'W': 12, 'L': 10 },'STL': { 'W': 9, 'L': 13 }},
'CHC': {'BRO': { 'W': 7, 'L': 15 },'BSN': { 'W': 9, 'L': 13 },'CIN': { 'W': 12, 'L': 10 },'NYG': { 'W': 7, 'L': 15 },
        'PHI': { 'W': 16, 'L': 6 },'PIT': { 'W': 8, 'L': 14 },'STL': { 'W': 10, 'L': 12 }},
'CIN': {'BRO': { 'W': 7, 'L': 15 },'BSN': { 'W': 9, 'L': 13 },'CHC': { 'W': 10, 'L': 12 },'NYG': { 'W': 13, 'L': 9 },
        'PHI': { 'W': 13, 'L': 9 },'PIT': { 'W': 13, 'L': 9 },'STL': { 'W': 8, 'L': 14 }},
'NYG': {'BRO': { 'W': 8, 'L': 14 },'BSN': { 'W': 9, 'L': 13 },'CHC': { 'W': 15, 'L': 7 },'CIN': { 'W': 9, 'L': 13 },
        'PHI': { 'W': 12, 'L': 10 },'PIT': { 'W': 15, 'L': 7 },'STL': { 'W': 13, 'L': 9 }},
'PHI': {'BRO': { 'W': 8, 'L': 14 },'BSN': { 'W': 8, 'L': 14 },'CHC': { 'W': 6, 'L': 16 },'CIN': { 'W': 9, 'L': 13 },
        'NYG': { 'W': 10, 'L': 12 },'PIT': { 'W': 13, 'L': 9 },'STL': { 'W': 8, 'L': 14 }},
'PIT': {'BRO': { 'W': 7, 'L': 15 },'BSN': { 'W': 10, 'L': 12 },'CHC': { 'W': 14, 'L': 8 },'CIN': { 'W': 9, 'L': 13 },
        'NYG': { 'W': 7, 'L': 15 },'PHI': { 'W': 9, 'L': 13 },'STL': { 'W': 6, 'L': 16 }},
'STL': {'BRO': { 'W': 11, 'L': 11 },'BSN': { 'W': 13, 'L': 9 },'CHC': { 'W': 12, 'L': 10 },'CIN': { 'W': 14, 'L': 8 },
        'NYG': { 'W': 9, 'L': 13 },'PHI': { 'W': 14, 'L': 8 },'PIT': { 'W': 16, 'L': 6 }}
}

# getting list of team names
teams = list(data.keys())

# initializing the matrix
matrix = [["Tm"]*(len(teams)+1) for num in range(len(teams)+1)]

# adding team names to the first row and column of the matrix
for num in range(1,len(matrix)):
    matrix[num][0] = teams[num-1]
    matrix[0][num] = teams[num-1]

# getting the head-to-head values, by looping through all of the times and their opponent
for i in range(1,len(matrix)):
    for j in range(1,len(matrix)):
        # finding the winning team and who they were playing
        winning_team = matrix[i][0]
        opposing_team = matrix[0][j]
        # if the teams are the same, make their win values "-"
        if winning_team == opposing_team:
            matrix[i][j] = "-"
        # otherwise, get the correct win value from the given data
        else:
            matrix[i][j] = str(data[winning_team][opposing_team]['W'])

# printing the matrix
print(matrix)       
        
# printing row by row for visualization
for row in matrix:
    print(row)