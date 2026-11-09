"""Model a social network with an adjacency list."""


class Person:
    """A person and the Person objects they are friends with."""

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Do not store the same friendship twice.
        if friend is not self and friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """An undirected graph of people and their friendships."""

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"Person not added. {name} already exists!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        missing = [
            name for name in dict.fromkeys((person1_name, person2_name))
            if name not in self.people
        ]
        if missing:
            print(f"Friendship not created. {', '.join(missing)} doesn't exist!")
            return
        if person1_name == person2_name:
            print("Friendship not created. A person cannot friend themselves!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            names = ", ".join(friend.name for friend in person.friends)
            print(f"{person.name} is friends with: {names or 'No friends yet'}")


def main():
    network = SocialNetwork()

    # Six people are the graph's vertices.
    for name in ("Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"):
        network.add_person(name)

    # Eight distinct, bidirectional friendships are the graph's edges.
    for name1, name2 in (
        ("Alex", "Jordan"),
        ("Alex", "Morgan"),
        ("Jordan", "Taylor"),
        ("Morgan", "Casey"),
        ("Taylor", "Riley"),
        ("Casey", "Riley"),
        ("Morgan", "Riley"),
        ("Alex", "Taylor"),
    ):
        network.add_friendship(name1, name2)

    # Test missing people, duplicate people, repeated edges, and self-friendship.
    original_alex = network.people["Alex"]
    network.add_friendship("Jordan", "Johnny")
    network.add_person("Alex")
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Alex")
    assert network.people["Alex"] is original_alex
    assert len(network.people) == 6
    assert sum(len(person.friends) for person in network.people.values()) == 16
    assert network.people["Alex"].friends.count(network.people["Jordan"]) == 1
    for person in network.people.values():
        assert person not in person.friends
        for friend in person.friends:
            assert person in friend.friends

    print("\nFinal network:")
    network.print_network()


if __name__ == "__main__":
    main()
