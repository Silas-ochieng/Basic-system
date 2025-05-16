# Define classes
class Attachee:
    def __init__(self, name, division):# initialize the object attribute
        # Tracks attachees details and performance metrics.
        self.name = name #attribute: attachee's name stores attachees full name
        self.division = division #attribute: attachee's division
        self.tasks = [] #attribute: list of tasks assigned to the attachee
        self.feedback = [] #attribute: list of feedbacks received by the attachee
        self.scores = [] #attribute: list of scores received by the attachee

# Method to assign a task
    def assign_task(self, task):
        self.tasks.append(task)
# Method to give feedback
    def give_feedback(self, feedback):
        self.feedback.append(feedback)
# Method to add score
    def add_score(self, score):
        self.scores.append(score)
# Method to get performance details
    def get_performance(self):
        return {
            "name": self.name,
            "division": self.division,
            "tasks": self.tasks,
            "feedback": self.feedback,
            "scores": self.scores
        }

# Class division for the manager
class Division:
    def __init__(self, name):
        self.name = name
        self.attachees = []

    def add_attachee(self, attachee):
        self.attachees.append(attachee)

    def display_attachees(self):
        print(f"\nAttachees in {self.name} Division:")
        for attachee in self.attachees:
            performance = attachee.get_performance()
            print(f"Name: {performance['name']}")
            print(f"Tasks: {', '.join(performance['tasks'])}") # use left join to display the list of task
            print(f"Feedback: {', '.join(performance['feedback'])}") ##
            print(f"Scores: {', '.join(map(str, performance['scores']))}") ##


# Example Usage
if __name__ == "__main__":
    # Create divisions
    engineering = Division("Engineering")
    tech_programs = Division("Tech Programs")
    radio_support = Division("Radio Support")
    hub_support = Division("Hub Support")

    # Create attachees
    attachee_1 = Attachee("Victor", "Engineering")
    attachee_2 = Attachee("mohammed", "Tech Programs")
    attachee_3 = Attachee("Nyachae", "Radio Support")
    attachee_4 = Attachee("Silas","Hub Support")

    # Assign tasks and feedback
    attachee_1.assign_task("Build a prototype")
    attachee_1.give_feedback("Great progress!")
    attachee_1.add_score(85)

    attachee_2.assign_task("Manage workshop")
    attachee_2.give_feedback("Well organized.")
    attachee_2.add_score(90)

    attachee_3.assign_task("Support radio transmission")
    attachee_3.give_feedback("Needs improvement.")
    attachee_3.add_score(70)

    attachee_4.assign_task("Organize workshop")
    attachee_4.give_feedback("Well organised")
    attachee_4.add_score(80)

    # Add attachees to divisions
    engineering.add_attachee(attachee_1)
    tech_programs.add_attachee(attachee_2)
    radio_support.add_attachee(attachee_3)
    hub_support.add_attachee(attachee_4)

    # Display attachees per division
    engineering.display_attachees()
    tech_programs.display_attachees()
    radio_support.display_attachees()
    hub_support.display_attachees()