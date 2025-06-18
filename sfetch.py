import platform, subprocess, distro, os, psutil, shutil

def output(command):
	output = subprocess.getoutput(command)
	return output

def color_text(text, color):
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\u001b[36m",
	"dark-blue": "\u001b[34;1m",
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

sys_info = {
	"username": f"{output('whoami')}@{output('uname -a').split()[1]}",
	"os": f"{distro.name()}",
	"host": f"{output('cat /sys/devices/virtual/dmi/id/product_name')}",
	"kernel": f"{os.uname()[2]}",
	"uptime": f"{output('uptime').split()[0]} up",
	"shell": f"{output('echo $SHELL')}",
        "de": f"{output('printenv XDG_CURRENT_DESKTOP')}",
	"terminal": f"{output('echo $TERM')}",
	"language": f"{output('echo $LANG').split('.')[0]}",
	"encoding": f"{output('echo $LANG').split('.')[1]}",
	"cpu": f"{cpu.split(':')[-1].strip()}",
        "gpu": f'{output("glxinfo | grep \'OpenGL renderer\' | cut -d \":\" -f2-")}',
	"memory": f"{memory.used / (1024 ** 3):.2f} / {memory.total / (1024 ** 3):.2f}GB {memory.percent}%",
        "disk": f"{disk.used // (2**30)} / {disk.total // (2**30)} GB",
        "battery": f"{'Battery not detected' if battery is None else int(battery.percent)}%"
	}

sys_info_k = list(sys_info.keys())

# WIP

color = {
	"debian": "red",
	"ubuntu": "red",
	"fedora": "dark-blue",
	"arch": "blue",
	"opensuse": "green"
	}

logo = {"debian": [
			'       \u001b[00;1m_,met$$$$$gg.\t\t',
			'    \u001b[00;1m,g$$$$$$$$$$$$$$$P.\t\t',
			'  \u001b[00;1m,g$$P"     """Y$$.".\t\t',
			' \u001b[00;1m,$$P\'              `$$$.\t',
			'\u001b[00;1m,$$P       ,ggs.     `$$b:\t',
			'\u001b[00;1m`d$$\'     ,$P"\'   \u001b[31;1m.\u001b[00;1m    $$$\t',
			' \u001b[00;1m$$P      d$\'     \u001b[31;1m,\u001b[00;1m    $$P\t',
			' \u001b[00;1m$$:      $$.   \u001b[31;1m-\u001b[00;1m    ,d$$\'\t',
			' \u001b[00;1m$$;      Y$b._   _,d$P\'\t',
			' \u001b[00;1mY$$.    \u001b[31;1m`.\u001b[00;1m`"Y$$$$P"\'\t\t',
			' \u001b[00;1m`$$b      \u001b[31;1m"-.__\u001b[00;1m\t\t',
			'  \u001b[00;1m`Y$$\t\t\t\t',
			'  \u001b[00;1m`Y$$.\t\t\t\t',
			'     \u001b[00;1m`$$b.\t\t\t',
			'       \u001b[00;1m`Y$$b.\t\t\t',
			'          \u001b[00;1m`"Y$b._\t\t',
			'              \u001b[00;1m`"""\t\t'
		],
	"ubuntu": [
			'            \u001b[31;1m.-/+oossssoo+/-.\u001b[00;1m\t\t\t',
			'        \u001b[31;1m`:+ssssssssssssssssss+:`\u001b[00;1m\t\t',
		        '      \u001b[31;1m-+ssssssssssssssssssyyssss+-\u001b[00;1m\t\t',
		        '    \u001b[31;1m.ossssssssssssssssss\u001b[00;1mdMMMNy\u001b[31;1msssso.\u001b[00;1m\t\t',
		        '   \u001b[31;1m/sssssssssss\u001b[00;1mhdmmNNmmyNMMMMh\u001b[31;1mssssss/\u001b[00;1m\t\t',
		        '  \u001b[31;1m+sssssssss\u001b[00;1mhm\u001b[31;1myd\u001b[00;1mMMMMMMMNddddy\u001b[31;1mssssssss+\u001b[00;1m\t\t',
		        ' \u001b[31;1m/ssssssss\u001b[00;1mhNMMM\u001b[31;1myh\u001b[00;1mhyyyyhmNMMMNh\u001b[31;1mssssssss/\u001b[00;1m\t\t',
		        '\u001b[31;1m.ssssssss\u001b[00;1mdMMMNh\u001b[31;1mssssssssss\u001b[00;1mhNMMMd\u001b[31;1mssssssss.\u001b[00;1m\t',
		        '\u001b[31;1m+ssss\u001b[00;1mhhhyNMMNy\u001b[31;1mssssssssssss\u001b[00;1myNMMMy\u001b[31;1msssssss+\u001b[00;1m\t',
		        '\u001b[31;1moss\u001b[00;1myNMMMNyMMh\u001b[31;1mssssssssssssss\u001b[00;1mhmmmh\u001b[31;1mssssssso\u001b[00;1m\t',
		        '\u001b[31;1moss\u001b[00;1myNMMMNyMMh\u001b[31;1msssssssssssssshmmmh\u001b[31;1mssssssso\u001b[00;1m\t',
		        '\u001b[31;1m+ssss\u001b[00;1mhhhyNMMNy\u001b[31;1mssssssssssss\u001b[00;1myNMMMy\u001b[31;1msssssss+\u001b[00;1m\t',
		        '\u001b[31;1m.ssssssss\u001b[00;1mdMMMNh\u001b[31;1mssssssssss\u001b[00;1mhNMMMd\u001b[31;1mssssssss.\u001b[00;1m\t',
		        ' \u001b[31;1m/ssssssss\u001b[00;1mhNMMM\u001b[31;1myh\u001b[00;1mhyyyyhdNMMMNh\u001b[31;1mssssssss/\u001b[00;1m\t\t',
		        '  \u001b[31;1m+sssssssss\u001b[00;1mdm\u001b[31;1myd\u001b[00;1mMMMMMMMMddddy\u001b[31;1mssssssss+\u001b[00;1m\t\t',
		        '   \u001b[31;1m/sssssssssss\u001b[00;1mhdmNNNNmyNMMMMh\u001b[31;1mssssss/\u001b[00;1m\t\t',
		        '    \u001b[31;1m.ossssssssssssssssss\u001b[00;1mdMMMNy\u001b[31;1msssso.\u001b[00;1m\t\t',
		        '      \u001b[31;1m-+sssssssssssssssss\u001b[00;1myyy\u001b[31;1mssss+-\u001b[00;1m\t\t',
		        '        \u001b[31;1m`:+ssssssssssssssssss+:`\u001b[00;1m\t\t',
		        '            \u001b[31;1m.-/+oossssoo+/-.\u001b[00;1m\t\t\t'
		],
	"fedora": [
			'          \u001b[34;1m/:-------------:\\\u001b[00;0m\t\t',
        		'       \u001b[34;1m:-------------------::\u001b[00;0m\t\t',
		        '     \u001b[34;1m:-----------\u001b[00;0m/shhOHbmp\u001b[34;1m---:\\\u001b[00;0m\t\t',
        		'   \u001b[34;1m/-----------\u001b[00;0momMMMNNNMMD  \u001b[34;1m---:\u001b[00;0m\t',
        		'  \u001b[34;1m:-----------\u001b[00;0msMMMMNMNMP\u001b[34;1m.    ---:\u001b[00;0m\t',
        		' \u001b[34;1m:-----------\u001b[00;0m:MMMdP\u001b[34;1m-------\u001b[00;0m    \u001b[34;1m---\\\u001b[00;0m\t',
        		'\u001b[34;1m,------------\u001b[00;0m:MMMd\u001b[34;1m--------\u001b[00;0m    \u001b[34;1m---:\u001b[00;0m\t',
        		'\u001b[34;1m:------------\u001b[00;0m:MMMd\u001b[34;1m-------\u001b[00;0m    \u001b[34;1m.---:\u001b[00;0m\t',
        		'\u001b[34;1m:----    \u001b[00;0moNMMMMMMMMMNho\u001b[34;1m     .----:\u001b[00;0m\t',
        		'\u001b[34;1m:--     .\u001b[00;0m+shhhMMMmhhy++\u001b[34;1m   .------/\u001b[00;0m\t',
        		'\u001b[34;1m:-    -------\u001b[00;0m:MMMd\u001b[34;1m--------------:\u001b[00;0m\t',
        		'\u001b[34;1m:-   --------\u001b[00;0m/MMMd\u001b[34;1m-------------;\u001b[00;0m\t',
        		'\u001b[34;1m:-    ------\u001b[00;0m/hMMMy\u001b[34;1m------------:\u001b[00;0m\t\t',
        		'\u001b[34;1m:--\u001b[00;0m :dMNdhhdNMMNo\u001b[34;1m------------;\u001b[00;0m\t\t',
        		'\u001b[34;1m:---\u001b[00;0m:sdNMMMMNds:\u001b[34;1m------------:\u001b[00;0m\t\t',
        		'\u001b[34;1m:------\u001b[00;0m:://:\u001b[34;1m-------------::\u001b[00;0m\t\t',
        		'\u001b[34;1m:---------------------://\u001b[00;0m\t\t'
		],
	"arch": [
			'                    \u001b[36;1my:\u001b[00;0m\t\t\t\t',
       	 		'                  \u001b[36;1msMN-\u001b[00;0m\t\t\t\t',
        		'                 \u001b[36;1m+MMMm`\u001b[00;0m\t\t\t\t',
        		'                \u001b[36;1m/MMMMMd`\u001b[00;0m\t\t\t',
        		'               \u001b[36;1m:NMMMMMMy\u001b[00;0m\t\t\t',
       			'              \u001b[36;1m-NMMMMMMMMs\u001b[00;0m\t\t\t',
        		'             \u001b[36;1m.NMMMMMMMMMM+\u001b[00;0m\t\t\t',
        		'            \u001b[36;1m.mMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        		'            \u001b[36;1moNMMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        		'          \u001b[36;1m`+:-+NMMMMMMMMMMMM+\u001b[00;0m\t\t\t',
        		'          \u001b[36;1m.sNMNhNMMMMMMMMMMMM/\u001b[00;0m\t\t\t',
        		'        \u001b[36;1m`hho/sNMMMMMMMMMMMMMMM/\u001b[00;0m\t\t\t',
        		'       \u001b[36;1m`.`omMMmMMMMMMMMMMMMMMMM+\u001b[00;0m\t\t',
        		'      \u001b[36;1m.mMNdshMMMMd+::oNMMMMMMMMMo\u001b[00;0m\t\t',
		       	'     \u001b[36;1m.mMMMMMMMMM+\u001b[00;0m     \u001b[36;1m`yMMMMMMMMMs\u001b[00;0m\t\t',
       			'    \u001b[36;1m.NMMMMMMMMM/\u001b[00;0m        \u001b[36;1myMMMMMMMMMy\u001b[00;0m\t\t',
		        '   \u001b[36;1m-NMMMMMMMMMh\u001b[00;0m         \u001b[36;1m`mNMMMMMMMMd`\u001b[00;0m\t\t',
	       	        '  \u001b[36;1m/NMMMNds+:.`\u001b[00;0m             \u001b[36;1m`-/oymMMMm.\u001b[00;0m\t\t',
        		' \u001b[36;1m+Mmy/.\u001b[00;0m                          \u001b[36;1m`:smN:\u001b[00;0m\t\t',
        		'\u001b[36;1m/+.\u001b[00;0m                                  \u001b[36;1m-o.\u001b[00;0m\t'
		],
	"opensuse": []
	}

os_name = sys_info["os"].split()[0].lower()

os_logo = logo[os_name]
os_color = color[os_name]

for i in range(0, len(os_logo) if len(os_logo) > len(sys_info_k) else len(sys_info_k)):
	print(os_logo[i] if i < len(os_logo) else '', color_text(sys_info_k[i] if i < len(sys_info_k) else "", os_color) + ': ' + sys_info[sys_info_k[i]] if i < len(sys_info_k) else "")
