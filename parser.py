from action import Action

action_handler = Action()

class InputParser:
    def __init__(self):
        # Here, you can initialize any common commands or synonyms.
        # This is a very basic mapping, but you can expand it as needed.
        self.commands = {
            "look": ["look", "examine", "inspect", "see"],
            "go": ["go", "walk", "move", "head", "travel"],
            "take": ["take", "pick up", "grab", "collect"],
            "use": ["use", "apply", "utilize"],
            "quit": ["quit", "exit", "leave", "stop"]
        }
        command_actions = {
            "look": action_handler.look()
        }

    def parse(self, input_text):
        # Convert input to lowercase for easier matching
        input_text = input_text.lower().strip()
        print(input_text)
        # Check for a match in our command mapping
        for command, synonyms in self.commands.items():
            #print(command, synonyms)
            for synonym in synonyms:
                if synonym in input_text:
                    return command
        
        return "-1"

# Testing the parser
parser = InputParser()
while True:
    user_input = input("What do you do: ")
    interpreted_command = parser.parse(user_input)
    if interpreted_command.lower() == "quit":
        print("Goodbye!")
        break
    elif interpreted_command.lower() == "go":
        print("you run quickly")
    else:
        print("I can't do that!")
