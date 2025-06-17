import platform, subprocess, distro, os

def output(command):
        output = subprocess.getoutput(command)
        return output

info = {"username": f"{output('whoami')}@{output('uname -a').split()[1]}",
        "os": f"{distro.name()}",
        "host": f"{output('cat /sys/devices/virtual/dmi/id/product_name')}",
        "kernel": f"{os.uname()[2]}",
        "uptime": f"{output('uptime').split()[0] + 'up'}",
        "shell": f"{output('echo $SHELL')}",
        "terminal": f"{output('echo $TERM')}",
        }

info_keys = info.keys()

print(info)
