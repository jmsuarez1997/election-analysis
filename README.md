
![ElectionPhoto](https://raw.githubusercontent.com/jmsuarez1997/election-analysis/main/Resources/Election%20Photo.jpg)
# Election Analysis
## Overview of Election Audit:
A Colorado Board of Election employee wants to find a way to generate an election audit using python for a recent congressional election. This analysis will walk through a way to generate an election audit that can be used for other elections.

Part 1: Winner of the Election
1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote

Part 2: Best County Voter Turnout

6. Get a list of counties' names
7. Calculate number of votes by county 
9. Calculate percentage of votes from each county.
8. Determine which county received the most votes.

## Resources: 
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.63.2

## Election Audit Results:
The analysis of the election shows that:

Part one:

There were 369,711 votes cast in the election. 
- Candidate 1: Charles Casper Stockham
- Candidate 2: Diana DeGette
- Candidate 3: Raymon Anthony Doane

The candidate results:
- Charles Casper Stockham received 23.0% of the vote and 85,213 votes
- Diana DeGette received 73.8% of the vote and 272,892 votes
- Raymon Anthony Doane received 3.1% of the votes and 11,606 votes

The winner of the election was:
- Candidate Diana DeGette, who received 73.8% of the vote and 272,892 votes

Part two:

County vote turnout:
- Jefferson county received 10.5% of the votes and 38,855 votes
- Denver county received 82.8% of the votes and 306,055 votes
- Arapahoe county received 6.7% of the votes and 24,801 votes

Largest County Turnout: Denver County

## Election-Audit Summary:
The election committee can use this code to perform an audit for any election. The only change needed is to replace the `("Resources", "exection_results.csv")` in the line of code below with the location of the data file desired.  

`file_to_load = os.path.join("Resources", "election_results.csv")`

To make the code easier to change the data file source, an input function can be used to easily input a different data source. 

`x=input("Enter your election data file location:")`

`file_to_load = os.path.join(x)`

To make the code easier to change the location of printed election results, an input function can be used to change the location of the printed txt file.

`y=input("Enter txt file location:")`

`file_to_save = os.path.join("y")`

Hope this code helps the election commission have a faster audit process for future elections.

