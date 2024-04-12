from aima3.logic import FolKB, expr

# Define the first-order logic knowledge base
kb = FolKB()

# Add rules to the knowledge base

kb.tell(
    expr(
        'Symptom(x, "overheat") & Symptom(x, "suddenly shut down") & Symptom(x, "high fan speed") ==> Problem(x, "CPU")'
    )
)
kb.tell(
    expr(
        'Symptom(x, "blue screen") & Symptom(x, "slow performance") & Symptom(x, "frequent crashes") ==> Problem(x, "Memory")'
    )
)
kb.tell(
    expr(
        'Symptom(x, "poor performance in games") & Symptom(x, "visual artifacts") & Symptom(x, "system freezes") ==> Problem(x, "GPU")'
    )
)
kb.tell(
    expr(
        'Symptom(x, "unexpected shutdowns") & Symptom(x, "difficulty starting") & Symptom(x, "burning plastic smell") ==> Problem(x, "Power Supply")'
    )
)
kb.tell(
    expr(
        'Symptom(x, "no POST") & Symptom(x, "boots to different error messages") & Symptom(x, "no power to USB devices") ==> Problem(x, "Motherboard")'
    )
)

# Solutions
solutions = {
    "CPU": {
        "description": "The CPU might be overheating.",
        "steps": [
            "Check if the CPU fan is spinning freely and clear of dust.",
            "Clean the CPU heatsink and fan using compressed air.",
            "Reapply thermal paste between the CPU and heatsink (ensure proper application).",
            "If the issue persists, consider replacing the CPU cooler.",
        ],
    },
    "Memory": {
        "description": "There might be issues with your RAM.",
        "steps": [
            "Run a memory diagnostic tool provided by your motherboard manufacturer or use a tool like MemTest86.",
            "If errors are found, try reseating the RAM modules in their slots.",
            "If reseating doesn't help, test each RAM module individually to identify the faulty one (if possible).",
            "Replace the faulty RAM module(s) with compatible memory.",
        ],
    },
    "GPU": {
        "description": "The graphics card might be malfunctioning.",
        "steps": [
            "Update your graphics card drivers to the latest version from the manufacturer's website.",
            "Ensure proper airflow around the graphics card and clean any dust buildup.",
            "If the issue persists, consider underclocking the GPU slightly to reduce heat and stress.",
            "In severe cases, the GPU might need replacement.",
        ],
    },
    "Power Supply": {
        "description": "The power supply unit (PSU) might be failing.",
        "steps": [
            "Visually inspect the power supply unit for any bulging capacitors or burn marks.",
            "Ensure all power cables are securely connected to the motherboard, GPU, and other components.",
            "If using multiple peripherals, try disconnecting non-essential ones to reduce load on the PSU.",
            "Consider replacing the PSU with a unit with sufficient wattage for your system requirements.",
        ],
    },
    "Motherboard": {
        "description": "There might be a hardware issue with the motherboard.",
        "steps": [
            "Double-check all connections on the motherboard, including power cables, data cables, and any expansion cards.",
            "If possible, try removing unnecessary components like additional hard drives and see if the system boots (to isolate potential conflicts).",
            "Clear CMOS memory to reset BIOS settings to default (consult your motherboard manual for instructions).",
            "Due to the complexity of troubleshooting motherboard issues, consider seeking professional help from a technician.",
        ],
    },
}

# Get symptoms from the user
symptom1 = input("Enter first symptom: ")
symptom2 = input("Enter second symptom: ")
symptom3 = input("Enter third symptom: ")

# Add symptoms to the knowledge base
kb.tell(expr(f'Symptom(PC, "{symptom1}")'))
kb.tell(expr(f'Symptom(PC, "{symptom2}")'))
kb.tell(expr(f'Symptom(PC, "{symptom3}")'))

# Query the knowledge base
query = expr("Problem(PC, what)")
answer = kb.ask(query)

if answer:
    problem = answer[query.args[1]]  # Use the variable object 'what' as the key
    print(f"The problem is: {problem}")
    print(f"Description: {solutions[problem]['description']}")
    print("Steps to possibly solve the problem:")
    for i, step in enumerate(solutions[problem]["steps"], 1):
        print(f"{i}. {step}")
else:
    print("The symptoms do not match any known problems.")
