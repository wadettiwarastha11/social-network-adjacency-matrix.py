class SocialNetwork:

    def __init__(self, users):
        self.users = users
        self.n = len(users)

        # Create an adjacency matrix
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]

    # Add friendship connection
    def add_friendship(self, user1, user2):
        i = self.users.index(user1)
        j = self.users.index(user2)

        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    # Remove friendship connection
    def remove_friendship(self, user1, user2):
        i = self.users.index(user1)
        j = self.users.index(user2)

        self.matrix[i][j] = 0
        self.matrix[j][i] = 0

    # Check whether two users are friends
    def are_friends(self, user1, user2):
        i = self.users.index(user1)
        j = self.users.index(user2)

        return self.matrix[i][j] == 1

    # Display adjacency matrix
    def display_matrix(self):
        print("\nAdjacency Matrix:")
        print("     ", end="")

        for user in self.users:
            print(user, end="  ")

        print()

        for i in range(self.n):
            print(self.users[i], end="    ")
            for j in range(self.n):
                print(self.matrix[i][j], end="  ")
            print()


# Main Program

users = ["A", "B", "C", "D", "E"]

network = SocialNetwork(users)

# Add friendship connections
network.add_friendship("A", "B")
network.add_friendship("A", "C")
network.add_friendship("B", "D")
network.add_friendship("C", "D")
network.add_friendship("C", "E")
network.add_friendship("D", "E")

# Display network
network.display_matrix()

# Check friendship
print("\nFriendship Check:")

if network.are_friends("A", "B"):
    print("A and B are friends.")
else:
    print("A and B are not friends.")

if network.are_friends("A", "E"):
    print("A and E are friends.")
else:
    print("A and E are not friends.")

# Remove friendship
network.remove_friendship("A", "B")

print("\nAfter removing friendship between A and B:")
network.display_matrix()