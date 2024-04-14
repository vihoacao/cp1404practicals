class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Initialise a Band."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        member_strings = [str(member) for member in self.members]
        return f"{self.name} ({', '.join(member_strings)})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a member to the band."""
        self.members.append(member)

    def play(self):
        """Return a string showing each member playing their instrument."""
        play_strings = [member.play() for member in self.members]
        return '\n'.join(play_strings)
