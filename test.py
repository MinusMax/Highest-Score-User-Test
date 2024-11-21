class UserScores:
    def __init__(self):
        self.scores = {}

    def add_or_update_score(self, name, score):
        if name in self.scores:
            self.scores[name] += score
            print(f"Updated {name}'s score to {self.scores[name]}.")
        else:
            self.scores[name] = score
            print(f"Added {name} with a score of {score}.")

    def get_highest_score(self):
        if not self.scores:
            print("No scores available.")
            return None
        
        highest_score_user = max(self.scores, key=self.scores.get)
        print(f"{highest_score_user} has the highest score: {self.scores[highest_score_user]}.")
        return highest_score_user, self.scores[highest_score_user]


def main():
    user_scores = UserScores()

    while True:
        print("\nOptions:")
        print("1. Add/Update Score")
        print("2. See Highest Score")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the user's name: ")
            try:
                score = int(input("Enter the score to add/update: "))
                user_scores.add_or_update_score(name, score)
            except ValueError:
                print("Please enter a valid integer for the score.")

        elif choice == '2':
            user_scores.get_highest_score()

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
