import platform, subprocess, distro, os, psutil, shutil

def output(command):
    output = subprocess.getoutput(command)
    return output

def color_text(text, color):
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "purple": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

battery = psutil.sensors_battery()
memory = psutil.virtual_memory()
cpu = os.popen("cat /proc/cpuinfo | grep 'model name' | head -1").read()
disk = shutil.disk_usage("/")

info = {"username": f"{output('whoami')}@{output('uname -a').split()[1]}",
    "os": f"{distro.name()}",
    "host": f"{output('cat /sys/devices/virtual/dmi/id/product_name')}",
    "kernel": f"{os.uname()[2]}",
    "uptime": f"{output('uptime').split()[0]} up",
    "shell": f"{output('echo $SHELL')}",
    "de": f"output('printenv XDG_CURRENT_DESKTOP')",
    "terminal": f"{output('echo $TERM')}",
    "language": f"{output('echo $LANG').split('.')[0]}",
    "encoding": f"{output('echo $LANG').split('.')[1]}",
    "cpu": f"{cpu.split(':')[-1].strip()}",
    "gpu": f'{output("glxinfo | grep \'OpenGL renderer\' | cut -d \":\" -f2-")}',
    "memory": f"{memory.used / (1024 ** 3):.2f} / {memory.total / (1024 ** 3):.2f}GB {memory.percent}%",
    "disk (/)": f"{disk.used // (2**30)} / {disk.total // (2**30)} GB",
    "battery": f"{'Battery not detected' if battery is None else int(battery.percent)}%"
    }

info_keys = list(info.keys())

for i in range(0, len(info_keys)):
    print(color_text(f"{info_keys[i]}: ", "purple") + f"{info[info_keys[i]]}")
