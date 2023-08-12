from action import Action

action_handler = Action()

class InputParser:
    def __init__(self):
        # Here, you can initialize any common commands or synonyms.
        # This is a very basic mapping, but you can expand it as needed.
        self.commands = {
            "look": {
                "synonyms":["look", "examine", "inspect", "see"],
                "action": action_handler.look
            },
            "go": {
                "synonyms": ["go", "walk", "move", "head", "travel"],
                "action": action_handler.go
            },
            "take":{
                "synonyms": ["take", "pick up", "grab", "collect"],
                "action": action_handler.take
            },
            "use": {
                "synonyms": ["use", "apply", "utilize"],
                "action": action_handler.use
            },
            "quit": {
                "synonyms": ["quit"],
                "action": action_handler.quit
            }
        }

    def add_commands(self, command_dict):
        for command, details in command_dict.items():
            self.commands[command] = details['synonyms']

    def parse(self, input_text):
        # Convert input to lowercase for easier matching
        input_text = input_text.lower().strip()
        print(input_text)
        # Check for a match in our command mapping
        for command, details in self.commands.items():
            #print(command, synonyms)
            for synonym in details["synonyms"]:
                if synonym in input_text:
                    return command
        
        return "-1"

# Testing the parser
parser = InputParser()
while True:
    user_input = input("What do you do: ")
    interpreted_command = parser.parse(user_input)
    if interpreted_command.lower() in parser.commands["quit"]["synonyms"]:
        parser.commands["quit"]["action"]()
    elif interpreted_command.lower() == "go":
        print("you run quickly")
    else:
        print("I can't do that!")
