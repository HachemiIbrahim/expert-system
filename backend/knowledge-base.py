from aima3.logic import FolKB, expr

kb = FolKB()
kb.tell(
    expr(
        'Symptom(x, "A lot of crashing") & Symptom(x, "Suddenly shut down") & Symptom(x, "Coil Whine") ==> Problem(x, "CPU")'
    )
)
kb.tell(
    expr(
        'Symptom(x, "Blue screen") & Symptom(x, "Poor performance") & Symptom(x, "A lot of crashing") ==> Problem(x, "Memory")'
    )
)
kb.tell(
    expr(
        'Symptom(x, "Poor performance in games") & Symptom(x, "Visual artifacts") & Symptom(x, "System freezes") ==> Problem(x, "GPU")'
    )
)
kb.tell(
    expr(
        'Symptom(x, "Unexpected shutdowns") & Symptom(x, "Difficulty starting") & Symptom(x, "Burning plastic smell") ==> Problem(x, "Power Supply")'
    )
)
kb.tell(
    expr(
        'Symptom(x, "No post") & Symptom(x, "Boots to different error messages") & Symptom(x, "No power to USB devices") ==> Problem(x, "Motherboard")'
    )
)

solutions = {
    "CPU Problem": {
        "description": "The CPU might be overheating.",
        "steps": "Check if the CPU fan is spinning freely and clear of dust.Clean the CPU heatsink and fan using compressed air.Reapply thermal paste between the CPU and heatsink (ensure proper application).If the issue persists, consider replacing the CPU cooler.",
    },
    "RAM Problem": {
        "description": "There might be issues with your RAM.",
        "steps": "Run a memory diagnostic tool provided by your motherboard manufacturer or use a tool like MemTest86.If errors are found, try reseating the RAM modules in their slots.If reseating doesn't help, test each RAM module individually to identify the faulty one (if possible).Replace the faulty RAM module(s) with compatible memory.",
    },
    "GPU Problem": {
        "description": "The graphics card might be malfunctioning.",
        "steps": "Update your graphics card drivers to the latest version from the manufacturer's website.Ensure proper airflow around the graphics card and clean any dust buildup.If the issue persists, consider underclocking the GPU slightly to reduce heat and stress.In severe cases, the GPU might need replacement.",
    },
    "Power Supply Problem": {
        "description": "The power supply unit (PSU) might be failing.",
        "steps": "Visually inspect the power supply unit for any bulging capacitors or burn marks.Ensure all power cables are securely connected to the motherboard, GPU, and other components.If using multiple peripherals, try disconnecting non-essential ones to reduce load on the PSU.Consider replacing the PSU with a unit with sufficient wattage for your system requirements.",
    },
    "Motherboard Problem": {
        "description": "There might be a hardware issue with the motherboard.",
        "steps": "Double-check all connections on the motherboard, including power cables, data cables, and any expansion cards.If possible, try removing unnecessary components like additional hard drives and see if the system boots (to isolate potential conflicts).Clear CMOS memory to reset BIOS settings to default (consult your motherboard manual for instructions).Due to the complexity of troubleshooting motherboard issues, consider seeking professional help from a technician.",
    },
    "Hard Drive Problem": {
        "description": "There might be issues with your hard drive.",
        "steps": "Check the hard drive for errors using a tool like CHKDSK on Windows.Ensure the hard drive cables are securely connected.Try defragmenting the hard drive if it's an HDD (not necessary for SSDs).If the issue persists, consider replacing the hard drive.",
    },
    "Network Card Problem": {
        "description": "There might be issues with your network card.",
        "steps": "Update the network card drivers to the latest version from the manufacturer's website.Ensure the network cables are securely connected.Try resetting your router or modem.If the issue persists, consider replacing the network card.",
    },
    "Sound Card Problem": {
        "description": "There might be issues with your sound card.",
        "steps": "Update the sound card drivers to the latest version from the manufacturer's website.Ensure the audio cables are securely connected.Try using different speakers or headphones to rule out issues with those devices.If the issue persists, consider replacing the sound card.",
    },
    "Video Card Problem": {
        "description": "There might be issues with your video card.",
        "steps": "Update the video card drivers to the latest version from the manufacturer's website.Ensure the video cables are securely connected.Try using a different monitor to rule out issues with the display.If the issue persists, consider replacing the video card.",
    },
    "BIOS Issue": {
        "description": "There might be issues with your BIOS.",
        "steps": "Try resetting the BIOS settings to default.Ensure the motherboard battery is not dead.Update the BIOS to the latest version from the motherboard manufacturer's website.If the issue persists, consider seeking professional help from a technician.",
    },
    "Operating System Problem": {
        "description": "There might be issues with your operating system.",
        "steps": "Try running a system file check (like SFC /scannow on Windows).Ensure your operating system is up to date with the latest patches and updates.Consider performing a system restore or repair install.If the issue persists, you may need to reinstall the operating system.",
    },
    "Power Cord Problem": {
        "description": "There might be issues with your power cord.",
        "steps": "Inspect the power cord for any visible damage or burn marks.Ensure the power cord is securely connected to the power supply unit and the wall outlet.Try using a different power cord that you know works.If the issue persists, consider replacing the power cord.",
    },
    "Keyboard Problem": {
        "description": "There might be issues with your keyboard.",
        "steps": "Check if the keyboard is properly connected to the computer.Try using the keyboard on a different computer to see if the problem persists.Clean the keyboard to remove any dust or debris that might be affecting key presses.If the issue persists, consider replacing the keyboard.",
    },
    "Mouse Problem": {
        "description": "There might be issues with your mouse.",
        "steps": "Check if the mouse is properly connected to the computer.Try using the mouse on a different surface or use a mouse pad.Clean the mouse to remove any dust or debris that might be affecting its movement.If the issue persists, consider replacing the mouse.",
    },
    "Monitor Problem": {
        "description": "There might be issues with your monitor.",
        "steps": "Check if the monitor cables are securely connected.Try adjusting the monitor settings, such as brightness and contrast.Ensure the graphics card drivers are up to date.If the issue persists, consider replacing the monitor.",
    },
}


symptom1 = input("Enter first symptom: ")
symptom2 = input("Enter second symptom: ")
symptom3 = input("Enter third symptom: ")
kb.tell(expr(f'Symptom(PC, "{symptom1}")'))
kb.tell(expr(f'Symptom(PC, "{symptom2}")'))
kb.tell(expr(f'Symptom(PC, "{symptom3}")'))
query = expr("Problem(PC, what)")
answer = kb.ask(query)
if answer:
    problem = answer[query.args[1]]
    print(f"The problem is: {problem}")
    print(f"Description: {solutions[problem]['description']}")
    print("Steps to possibly solve the problem:")
    for i, step in enumerate(solutions[problem]["steps"], 1):
        print(f"{i}. {step}")
else:
    print("The symptoms do not match any known problems.")
