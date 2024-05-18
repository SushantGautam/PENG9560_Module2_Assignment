import numpy as np
import pandas as pd
# Set the random seed for reproducibility
np.random.seed(42)

import argparse
parser = argparse.ArgumentParser(description="Arguments for the dataser creation.")
parser.add_argument("--n_arms", type=int, default=20, help="Number of arms for the experiment.") 

args = parser.parse_args()
print(args)

# Number of teams
n_arms= args.n_arms
# Generate team features
team_features = np.random.uniform(0.5, 1.0, (n_arms, 4))
# Boost the features of the first team to ensure it's the Condorcet winner
team_features[0] += 0.5  # Increase the strength of the first team
# Create a DataFrame to hold team features
teams_df = pd.DataFrame(team_features, columns=[
                        'AttackStrength', 'DefenseStrength', 'MidfieldControl', 'HomeAdvantage'])
teams_df['TeamName'] = ['Team_' + str(i+1) for i in range(n_arms)]
# Adjust function to predict match outcomes probabilistically


def predict_outcome_probabilistically(team_a_features, team_b_features):
    # Apply home advantage to team A's features
    # Adjust team A's features for home advantage
    team_a_adjusted = team_a_features * (1 + team_a_features[3])
    # Compute a simple score for both teams
    # For Team A, consider Attack, Defense, and Midfield
    score_a = np.dot(team_a_adjusted[:3], np.array([1, -1, 1]))
    # For Team B, ignore Home Advantage
    score_b = np.dot(team_b_features[:3], np.array([1, -1, 1]))
    # Convert scores to probabilities
    # Sigmoid function for probability
    prob_a_wins = 1 / (1 + np.exp(score_b - score_a))
    return prob_a_wins


# Generate win probabilities matrix
# Initialize a matrix to hold win probabilities
win_probabilities = np.zeros((n_arms, n_arms))
for i in range(n_arms):
    for j in range(n_arms):
        if i == j:
            # Probability of an arm against itself is 0.5
            win_probabilities[i, j] = 0.5
        else:
            # Get features for both teams
            team_a_features = team_features[i]
            team_b_features = team_features[j]
            # Calculate the probability of team A winning against team B
            win_prob = predict_outcome_probabilistically(
                team_a_features, team_b_features)
            # Update the matrix with win probabilities (A vs. B)
            win_probabilities[i, j] = win_prob
preference_matrix = np.array(win_probabilities)
teams_df.head(), preference_matrix[:5, :5]
print(preference_matrix[:5, :5])
np.savetxt("data/soccer_data.txt", preference_matrix, fmt='%.2f')
print("Data saved successfully to data/soccer_data.txt")