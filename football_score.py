"""
Matthew nichols
Module 04 Lab

This program is a class that represents the score of a football match between two teams.
"""

class FootballScore:
    """
    Represents the score of a football match between two teams.

    Attributes:
    - location (str): The location where the match is taking place.
    - home_team (str): The name of the home team.
    - away_team (str): The name of the away team.
    - home_score (int): The score of the home team.
    - away_score (int): The score of the away team.
    """

    def __init__(self, location, home_team, away_team, home_score, away_score):
        self.location = location
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score

    def touchdown(self, team):
        """
        Updates the score of the specified team by 6 points if the team is either the home team or the away team.

        Parameters:
        - team (str): The name of the team.

        Returns:
        None
        """
        if team == self.home_team:
            self.home_score += 6
        elif team == self.away_team:
            self.away_score += 6
        else:
            print("Team not found")

    def field_goal(self, team):
        """
        Updates the score of the specified team by 3 points if the team is either the home team or the away team.

        Parameters:
        - team (str): The name of the team.

        Returns:
        None
        """
        if team == self.home_team:
            self.home_score += 3
        elif team == self.away_team:
            self.away_score += 3
        else:
            print("Team not found")

    def two_point_conversion(self, team):
        """
        Updates the score by adding 2 points to the specified team.

        Parameters:
        - team (str): The name of the team to update the score for.

        Returns:
        None
        """
        if team == self.home_team:
            self.home_score += 2
        elif team == self.away_team:
            self.away_score += 2
        else:
            print("Team not found")

    def safety(self, team):
        """
        Adds 2 points to the score of the specified team in case of a safety.

        Parameters:
        - team (str): The name of the team that scored the safety.

        Returns:
        None
        """
        if team == self.home_team:
            self.home_score += 2
        elif team == self.away_team:
            self.away_score += 2
        else:
            print("Team not found")

    def extra_point(self, team):
        """
        This method is used to add an extra point to the team's score. 
        The 'team' parameter should be the name of the team (as a string) that scored the extra point.
        If the team name doesn't match the home or away team, it will print "Team not found".
        """
        if team == self.home_team:
            self.home_score += 1
        elif team == self.away_team:
            self.away_score += 1
        else:
            print("Team not found")

    def get_score(self):
        """
        This method is used to get the current score of the football match. 
        It returns a string with the format "home_team: home_score, away_team: away_score".
        """
        # Returns the score of the football match
        return f"{self.home_team}: {self.home_score}, {self.away_team}: {self.away_score}"

# Create a new instance of the FootballScore class
match = FootballScore(location='Avondale', home_team='Bears', away_team='Eagles', home_score=0, away_score=0)

# Bears score a touchdown
match.touchdown("Bears")

# Eagles score a field goal
match.field_goal("Eagles")

# Bears score an extra point
match.extra_point("Bears")

# Print the final score
print(match.get_score())

# Access the attributes
print("Location: " + match.location)
print("Final Score: " + match.get_score())  # Call the get_score() method on the match object
     
     
# Sources:
# - https://www.w3schools.com/python/python_classes.asp
# - https://docs.python.org/3.13/reference/datamodel.html#classes
# - https://peps.python.org/pep-0008/
# - https://colab.research.google.com/drive/15_0IHJ0OHPjGYtWCh1zrWLeV8dHcEJ7Q#scrollTo=YUUprR5HZS78
# - https://www.techwithtim.net/tutorials/python-programming/classes-objects-in-python
# - python discord server: https://discord.com/channels/267624335836053506/1035199133436354600"
