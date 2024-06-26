from aima3.logic import FolKB, expr, fol_bc_ask
from routers import schema

rules = {
    # Existing rules
    "rule1": 'Symptom(x, "A lot of crashing") & Symptom(x, "Suddenly shut down") & Symptom(x, "Coil Whine") ==> Problem(x, "CPU Problem")',
    "rule2": 'Symptom(x, "Blue screen") & Symptom(x, "Poor performance") & Symptom(x, "A lot of crashing") ==> Problem(x, "RAM Problem")',
    "rule3": 'Symptom(x, "Poor performance in games") & Symptom(x, "Visual artifacts") & Symptom(x, "System freezes") ==> Problem(x, "GPU Problem")',
    "rule4": 'Symptom(x, "Unexpected shutdowns") & Symptom(x, "Difficulty starting") & Symptom(x, "Burning plastic smell") ==> Problem(x, "Power Supply Problem")',
    "rule5": '(Symptom(x, "No post") & Symptom(x, "Boots to different error messages") & Symptom(x, "No power to USB devices")) ==> Problem(x, "Motherboard Problem")',
    "rule6": 'Symptom(x, "Slow boot time") & Symptom(x, "Frequent freezing") & Symptom(x, "Blue screen") ==> Problem(x, "Hard Drive Problem")',
    "rule7": 'Symptom(x, "No internet connection") & Symptom(x, "Slow internet speed") & Symptom(x, "Frequent disconnection") ==> Problem(x, "Network Card Problem")',
    "rule8": 'Symptom(x, "No sound") & Symptom(x, "Distorted sound") & Symptom(x, "Frequent audio cut-out") ==> Problem(x, "Sound Card Problem")',
    "rule9": 'Symptom(x, "Blurry image") & Symptom(x, "No video output") & Symptom(x, "Distorted image") ==> Problem(x, "Video Card Problem")',
    "rule10": 'Symptom(x, "PC not booting") & Symptom(x, "Incorrect date and time") & Symptom(x, "Hardware not recognized") ==> Problem(x, "BIOS Issue")',
    "rule11": 'Symptom(x, "Slow performance") & Symptom(x, "Frequent crashes") & Symptom(x, "Software compatibility issues") ==> Problem(x, "Operating System Problem")',
    "rule12": 'Symptom(x, "No power") & Symptom(x, "Burning smell") & Symptom(x, "Visible damage on power cord") ==> Problem(x, "Power Cord Problem")',
    "rule13": 'Symptom(x, "Keys not working") & Symptom(x, "Sticky keys") & Symptom(x, "Keys typing wrong characters") ==> Problem(x, "Keyboard Problem")',
    "rule14": 'Symptom(x, "Mouse not moving") & Symptom(x, "Clicks not registering") & Symptom(x, "Mouse pointer jittering") ==> Problem(x, "Mouse Problem")',
    "rule15": 'Symptom(x, "No display") & Symptom(x, "Flickering screen") & Symptom(x, "Distorted image") ==> Problem(x, "Monitor Problem")',
}


class Agenda:
    def __init__(self):
        self.agenda = []

    def add_task(self, task):
        self.agenda.append(task)

    def get_task(self):
        return self.agenda.pop()

    def is_empty(self):
        return len(self.agenda) == 0


class WorkingMemory:
    def __init__(self):
        self.memory = {}  # Change memory to a dictionary

    def add_fact(self, fact, exists):
        self.memory[fact] = exists  # Add a fact and its existence status to the memory

    def get_fact(self, fact):
        return self.memory.get(fact, None)  # Get the existence status of a fact

    def is_empty(self):
        return len(self.memory) == 0  # Check if the memory is empty

    def contains_fact(self, fact):
        return fact in self.memory  # Check if a specific fact is in the memory


agenda = Agenda()


def diagnose(symptoms: schema.UserSymptoms):

    kb = FolKB()
    working_memory = WorkingMemory()

    for rule in rules.values():
        kb.tell(expr(rule))

    for symptom in [symptoms.symptom1, symptoms.symptom2, symptoms.symptom3]:
        exists = bool(fol_bc_ask(kb, expr(f'Symptom(x, "{symptom}")')))
        kb.tell(expr(f'Symptom(x, "{symptom}")'))
        working_memory.add_fact(symptom, exists)

    problems = [
        "CPU Problem",
        "RAM Problem",
        "GPU Problem",
        "Power Supply Problem",
        "Motherboard Problem",
        "Hard Drive Problem",
        "Network Card Problem",
        "Sound Card Problem",
        "Video Card Problem",
        "BIOS Issue",
        "Operating System Problem",
        "Power Cord Problem",
        "Keyboard Problem",
        "Mouse Problem",
        "Monitor Problem",
    ]
    for problem in problems:
        agenda.add_task(problem)

    diagnosis = None

    while not agenda.is_empty():
        problem = agenda.get_task()
        solutions = fol_bc_ask(kb, expr(f'Problem(x, "{problem}")'))
        first_solution = next(solutions, None)
        if first_solution is not None:
            diagnosis = problem
            break

    return diagnosis


# def diagnose(symptoms: schema.UserSymptoms):

#     kb = FolKB()

#     for rule in rules.values():
#         kb.tell(expr(rule))

#     kb.tell(expr(f'Symptom(x, "{symptoms.symptom1}")'))
#     kb.tell(expr(f'Symptom(x, "{symptoms.symptom2}")'))
#     kb.tell(expr(f'Symptom(x, "{symptoms.symptom3}")'))

#     problems = [
#         "CPU Problem",
#         "RAM Problem",
#         "GPU Problem",
#         "Power Supply Problem",
#         "Motherboard Problem",
#         "Hard Drive Problem",
#         "Network Card Problem",
#         "Sound Card Problem",
#         "Video Card Problem",
#         "BIOS Issue",
#         "Operating System Problem",
#         "Power Cord Problem",
#         "Keyboard Problem",
#         "Mouse Problem",
#         "Monitor Problem",
#     ]
#     for problem in problems:
#         agenda.add_task(problem)

#     diagnosis = None
#     # Process each problem in the agenda
#     while not agenda.is_empty():
#         problem = agenda.get_task()
#         solutions = fol_bc_ask(kb, expr(f'Problem(x, "{problem}")'))
#         if solutions is not None:
#             break
#         diagnosis = solutions
#         # first_solution = next(solutions, None)
#         # if first_solution is not None:
#         #     diagnosis = problem
#         #     break

#     return diagnosis
