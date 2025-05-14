class Pet:
    def __init__(self, name):
        # Set up the pet with a name and default levels for hunger, energy, and happiness
        self.name = name
        self.hunger = 5  # Medium hunger level to start with
        self.energy = 5  # Medium energy level
        self.happiness = 5  # Neutral happiness
        self.tricks = []  # Empty list to store tricks the pet learns

    def eat(self):
        # Eating makes the pet less hungry and a little happier
        self.hunger = max(0, self.hunger - 3)  # Prevent hunger from going below 0
        self.happiness = min(10, self.happiness + 1)  # Cap happiness at 10
        print(f"{self.name} is eating...")

    def sleep(self):
        # Sleeping restores energy
        self.energy = min(10, self.energy + 5)  # Cap energy at 10
        print(f"{self.name} is sleeping...")

    def play(self):
        # Playing uses energy and makes the pet happier, but also hungrier
        if self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")
        else:
            # Pet is too tired to play
            print(f"{self.name} is too tired to play!")

    def train(self, trick):
        # Teach the pet a new trick
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        # Show all tricks the pet has learned
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        # Show a summary of the pet's current state
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        self.show_tricks()  # Include tricks in the status report
