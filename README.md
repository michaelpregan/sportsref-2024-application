# sportsref-2024-application
 Sports Reference Engineering Internship 2024 - Michael Regan

This problem was fun! For my solution I used Python. It starts with a data variable, which in this case used the sample data provided, but can be reformatted to use any JSON file. Using that data, it first gets a list of the team names. Then, it creates a matrix based on the amount of teams found. It adds the names of the teams to the matrix for the headers of the rows and columns, then it loops through each inside cell and finds the amount of wins that the cell's "row header" has against the corresponding "column header" based on the data provided. 

The following is an example of the matrix output provided with the sample data:

[
    ['Tm', 'BRO', 'BSN', 'CHC', 'CIN', 'NYG', 'PHI', 'PIT', 'STL'], 
    ['BRO', '-', '10', '15', '15', '14', '14', '15', '11'], 
    ['BSN', '12', '-', '13', '13', '13', '14', '12', '9'], 
    ['CHC', '7', '9', '-', '12', '7', '16', '8', '10'], 
    ['CIN', '7', '9', '10', '-', '13', '13', '13', '8'], 
    ['NYG', '8', '9', '15', '9', '-', '12', '15', '13'], 
    ['PHI', '8', '8', '6', '9', '10', '-', '13', '8'], 
    ['PIT', '7', '10', '14', '9', '7', '9', '-', '6'], 
    ['STL', '11', '13', '12', '14', '9', '14', '16', '-']
]

Row by row:

['Tm', 'BRO', 'BSN', 'CHC', 'CIN', 'NYG', 'PHI', 'PIT', 'STL']

['BRO', '-', '10', '15', '15', '14', '14', '15', '11']

['BSN', '12', '-', '13', '13', '13', '14', '12', '9']

['CHC', '7', '9', '-', '12', '7', '16', '8', '10']

['CIN', '7', '9', '10', '-', '13', '13', '13', '8']

['NYG', '8', '9', '15', '9', '-', '12', '15', '13']

['PHI', '8', '8', '6', '9', '10', '-', '13', '8']

['PIT', '7', '10', '14', '9', '7', '9', '-', '6']

['STL', '11', '13', '12', '14', '9', '14', '16', '-']