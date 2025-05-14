from pet import Pet

# Step 1: Create your digital pet
my_pet = Pet("Max")
print(f"Creating pet: {my_pet.name}")

# Step 2: Interact with your pet using the defined methods
my_pet.eat()         # Pet eats to reduce hunger
my_pet.play()        # Pet plays to increase happiness
my_pet.sleep()       # Pet sleeps to restore energy
my_pet.train("roll over")   # Teach a new trick
my_pet.train("play dead")   # Teach another trick

# Step 3: Check how your pet is doing overall
my_pet.get_status()
