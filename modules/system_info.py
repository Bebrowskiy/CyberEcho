import os
import subprocess


# !!! ARCH LINUX !!!

def get_installed_packages():
    """Retrieves a list of installed packages (for Arch Linux)"""
    result = subprocess.run(["pacman", "-Q"], capture_output=True, text=True)
    return result.stdout.split("\n") if result.stdout else []

def get_available_commands():
    """Retrieves a list of available system commands from $PATH"""
    paths = os.environ["PATH"].split(":")  # Get directories where binaries are stored
    commands = set()

    for path in paths:
        if os.path.isdir(path):  # Check if the directory exists
            for file in os.listdir(path):
                commands.add(file)

    return sorted(commands)

def get_system_info():
    """Gathers system information"""
    uname = subprocess.run(["uname", "-a"], capture_output=True, text=True).stdout.strip()
    return {
        "os": uname,
        "installed_packages": get_installed_packages(),
        "available_commands": get_available_commands()
    }

# Function to output system information
def out_info():
    print("System information requested")
    info = get_system_info()

    # Format installed packages for better readability
    installed_packages = ", ".join(info['installed_packages'][:10]) + ("..." if len(info['installed_packages']) > 10 else "")

    data = (f"📌 System Information:\n"
            f" 🔹 OS: {info['os']}\n"
            f" 🔹 Installed Packages: {installed_packages}\n"
            f" 🔹 Available Commands: {len(info['available_commands'])}")  # Display count instead of full list
    return data
