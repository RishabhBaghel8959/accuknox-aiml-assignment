import requests
import matplotlib.pyplot as plt


API_URL = "https://mocki.io/v1/6c9b8a63-9c2e-4f36-9c6d-6f2c2e2c9e4a"
response = requests.get(API_URL)

try:
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()
    students = response.json()
except Exception as e:
    print("API failed, using fallback data")
    students = [
        {"name": "Rahul", "score": 85},
        {"name": "Raj", "score": 78},
        {"name": "Rishabh", "score": 92}
    ]


if not students:
    print("No student data received from API.")
    exit()

names = [student["name"] for student in students]
scores = [student["score"] for student in students]

average_score = sum(scores) / len(scores)
print("Average Score:", average_score)


plt.bar(names, scores)
plt.axhline(average_score, linestyle="--", label="Average Score")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.legend()
plt.show()
