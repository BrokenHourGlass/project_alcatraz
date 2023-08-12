
class VerbDictionary:
    def __init__(self):
        self.verbs = {
            'run': ['sprint', 'jog', 'dash', 'race'],
            'eat': ['consume', 'devour', 'ingest', 'feast'],
            'read': ['peruse', 'scan', 'skim', 'examine'],
            "look": ["look", "examine", "inspect", "see"],
            "go": ["go", "walk", "move", "head", "travel"],
            "take": ["take", "pick up", "grab", "collect"],
            "use": ["use", "apply", "utilize"],
            "quit": ["quit", "exit", "leave", "stop"],
            'write': ['compose', 'draft', 'scribe', 'record'],
            'talk': ['speak', 'converse', 'chat', 'discuss'],
            'jump': ['leap', 'bound', 'hop', 'spring'],
            'sleep': ['rest', 'slumber', 'doze', 'nap'],
            'laugh': ['chuckle', 'giggle', 'snicker', 'smile'],
            'cry': ['weep', 'sob', 'bawl', 'wail'],
            'learn': ['study', 'educate', 'acquire', 'absorb'],
            'swim': ['float', 'dive', 'paddle', 'wade'],
            'dance': ['twirl', 'prance', 'shuffle', 'swing'],
            'sing': ['croon', 'harmonize', 'serenade', 'warble'],
            'cook': ['prepare', 'chef', 'bake', 'grill'],
            'paint': ['illustrate', 'sketch', 'draw', 'color'],
            'climb': ['ascend', 'scale', 'mount', 'rise'],
            'drive': ['steer', 'operate', 'navigate', 'maneuver'],
            'ride': ['cycle', 'pedal', 'travel', 'journey'],
            'build': ['construct', 'assemble', 'create', 'fabricate'],
            'fight': ['battle', 'combat', 'struggle', 'confront'],
            'plant': ['sow', 'cultivate', 'seed', 'nurture'],
            "walk": ["stroll", "saunter", "amble", "mosey"],
            "see": ["observe", "view", "watch", "glimpse"],
            "hear": ["listen", "overhear", "eavesdrop", "catch"],
            "touch": ["feel", "tap", "poke", "caress"],
            "build": ["construct", "erect", "assemble", "forge"],
            "destroy": ["demolish", "ruin", "shatter", "obliterate"],
            "sit": ["perch", "settle", "lounge", "repose"],
            "stand": ["rise", "erect", "mount", "ascend"],
            "give": ["offer", "donate", "bestow", "grant"],
            "begin": ["commence", "initiate", "launch", "originate"],
            "end": ["conclude", "terminate", "finish", "wrap"],
            "think": ["ponder", "contemplate", "muse", "reflect"],
            "know": ["recognize", "understand", "comprehend", "grasp"],
            "teach": ["instruct", "educate", "tutor", "coach"],
            "sell": ["market", "trade", "vend", "peddle"],
            "buy": ["purchase", "acquire", "obtain", "procure"],
            "drive": ["steer", "pilot", "operate", "navigate"],
            "fly": ["soar", "glide", "hover", "flit"],
            "throw": ["hurl", "fling", "toss", "cast"],
            "catch": ["grab", "snatch", "seize", "clasp"],
            "cut": ["slice", "chop", "carve", "hack"],
            "grow": ["expand", "swell", "enlarge", "mature"],
            "shrink": ["diminish", "reduce", "contract", "decline"],
            "move": ["shift", "transfer", "relocate", "migrate"],
            "stop": ["halt", "cease", "desist", "pause"],
            "create": ["produce", "craft", "invent", "establish"],
            "destroy": ["annihilate", "ruin", "demolish", "wreck"],
            "live": ["exist", "reside", "dwell", "survive"],
            "die": ["perish", "decease", "expire", "succumb"],
            "love": ["adore", "cherish", "treasure", "esteem"],
            "hate": ["despise", "loathe", "abhor", "detest"],
            "include": ["incorporate", "contain", "comprise", "embrace"],
            "exclude": ["omit", "leave out", "discard", "neglect"],
            "increase": ["augment", "multiply", "amplify", "escalate"],
            "decrease": ["diminish", "reduce", "dwindle", "lessen"],
            "rise": ["ascend", "climb", "soar", "elevate"],
            "fall": ["descend", "plummet", "tumble", "drop"],
            "break": ["fracture", "shatter", "smash", "split"],
            "fix": ["mend", "repair", "restore", "correct"],
            "find": ["discover", "locate", "detect", "uncover"],
            "lose": ["misplace", "forfeit", "drop", "mislay"],
            "bring": ["fetch", "carry", "transport", "deliver"],
            "leave": ["depart", "exit", "vacate", "abandon"],
            "make": ["craft", "produce", "forge", "fabricate"],
            "keep": ["retain", "preserve", "maintain", "withhold"],
            "save": ["preserve", "rescue", "store"],
        }

    def get_synonyms(self, verb):
        if verb in self.verbs:
            return self.verbs[verb]
        else:
            return []

# Create an instance of the VerbDictionary class
verb_dict = VerbDictionary()

# Get synonyms for a specific verb
verb = input("Tell me a verb, Ill give you the synonyms: ")
synonyms = verb_dict.get_synonyms(verb)
print(f"Synonyms of '{verb}': {', '.join(synonyms)}")

