import matplotlib.pyplot as plt
import pandas as pd

# Data for pylint results
pylint_results = {
    "Project": ["system-design-primer", "TheAlgorithms/Python", "keras-team/keras", "youtube-dl", "scikit-learn", "ansible"],
    "Rating": [4.42, 0.00, 0.00, 0.00, 0.00, None]
}

# Data for bandit results
bandit_results = {
    "Project": ["system-design-primer", "TheAlgorithms/Python", "keras-team/keras", "youtube-dl", "scikit-learn", "ansible"],
    "Total Low Issues": [0, 743, 146, 246, 6709, 2815],
    "Total Medium Issues": [0, 4, 15, 7, 64, 134],
    "Total High Issues": [0, 2, 7, 27, 5, 35]
}

# Convert data to DataFrame
pylint_df = pd.DataFrame(pylint_results)
bandit_df = pd.DataFrame(bandit_results)

# Plotting pylint ratings
plt.figure(figsize=(10, 6))
plt.bar(pylint_df["Project"], pylint_df["Rating"], color='skyblue')
plt.title("Pylint Ratings for Python Projects")
plt.xlabel("Project")
plt.ylabel("Rating")
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 5)
plt.tight_layout()
plt.show()

# Displaying bandit results
print("Bandit Results:")
print(bandit_df)

# Saving bandit results to a CSV file
bandit_df.to_csv("bandit_results.csv", index=False)

# Data for Bandit results (replace with your actual data)
projects = ["Project 1", "Project 2", "Project 3", "Project 4", "Project 5", "Project 6"]
low_severity = [0, 743, 146, 246, 6709, 2815]
medium_severity = [0, 4, 15, 7, 64, 134]
high_severity = [0, 2, 7, 27, 5, 35]

# Create bar chart
x = range(len(projects))
plt.bar(x, low_severity, width=0.2, label='Low Severity', color='b')
plt.bar([i + 0.2 for i in x], medium_severity, width=0.2, label='Medium Severity', color='g')
plt.bar([i + 0.4 for i in x], high_severity, width=0.2, label='High Severity', color='r')

# Add labels and title
plt.xlabel('Projects')
plt.ylabel('Number of Issues')
plt.title('Bandit Results by Severity')
plt.xticks([i + 0.2 for i in x], projects)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
