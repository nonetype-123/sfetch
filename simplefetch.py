import platform, subprocess, distro, os, psutil

def output(command):
        output = subprocess.getoutput(command)
        return output

battery = psutil.sensors_battery()
memory = psutil.virtual_memory()
cpu = os.popen("cat /proc/cpuinfo | grep 'model name' | head -1").read()

info = {"username": f"{output('whoami')}@{output('uname -a').split()[1]}",
        "os": f"{distro.name()}",
        "host": f"{output('cat /sys/devices/virtual/dmi/id/product_name')}",
        "kernel": f"{os.uname()[2]}",
        "uptime": f"{output('uptime').split()[0] + 'up'}",
        "shell": f"{output('echo $SHELL')}",
        "terminal": f"{output('echo $TERM')}",
        "language": f"{output('echo $LANG').split('.')[0]}",
        "encoding": f"{output('echo $LANG').split('.')[1]}",
        "cpu": f"{cpu.split(':')[-1].strip()}",
        "memory": f"{memory.used / (1024 ** 3):.2f} / {memory.total / (1024 ** 3):.2f}GB {memory.percent}%",
        "battery": f"{'Battery not detected' if battery is None else int(battery.percent)}%"
        }

info_keys = info.keys()

print(info)
