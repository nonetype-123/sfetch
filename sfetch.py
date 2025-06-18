import platform, subprocess, distro, os, psutil, shutil

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

# everything related to collecting system information

class sys_info:

	def __init__(self):

		self._data = {}
		self.refresh()

	def refresh(self):

		battery = psutil.sensors_battery()
		memory = psutil.virtual_memory()
		cpu = os.popen("cat /proc/cpuinfo | grep 'model name' | head -1").read()
		disk = shutil.disk_usage("/")
		lang = subprocess.getoutput('echo $LANG').split('.')

		self._data = {

		"username": f"{subprocess.getoutput('whoami')}@{subprocess.getoutput('uname -a').split()[1]}",
	        "os": distro.name(),
	        "host": subprocess.getoutput('cat /sys/devices/virtual/dmi/id/product_name'),
	        "kernel": os.uname()[2],
	        "uptime": subprocess.getoutput('uptime').split()[0] + " up",
	        "shell": subprocess.getoutput('echo $SHELL'),
	        "de": os.getenv('XDG_CURRENT_DESKTOP'),
	        "terminal": subprocess.getoutput('echo $TERM'),
	        "language": lang[0],
	        "encoding": lang[1],
	        "cpu": cpu.split(':')[-1].strip(),
	        "gpu": subprocess.getoutput("glxinfo | grep \'OpenGL renderer\' | cut -d \":\" -f2-"),
	        "memory": f"{memory.used / (1024 ** 3):.2f} / {memory.total / (1024 ** 3):.2f} GB {memory.percent}%",
		"disk": f"{disk.used // (2**30)} / {disk.total // (2**30)} GB",
        	"battery": "Battery not detected" if battery is None else str(int(battery.percent)) + "%"

	      	}

data = sys_info()
data_k = list(data._data.keys())

# everything related to the utility style

color = {

	"debian": "red",
	"ubuntu": "red",
	"fedora": "dark-blue",
	"arch": "blue",
	"opensuse": "green",
	"linux": "white"

	}

logo = {

	"debian": [
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
	"opensuse": [
                        '    \033[32m.,cdxxxoc,.               .:kKMMMNWMMMNk:.\u001b[00;0m\t\t',
                        '    \033[32mcKMMN0OOOKWMMXo. ;        ;0MWk:.      .:OMMk.\u001b[00;0m\t',
                        ' \033[32m;WMK; .       .lKMMNM,     :NMK,             .OMW.\u001b[00;0m\t',
                        ' \033[32mcMW;            "WMMMN   ,XMK,                 oMM"\u001b[00;0m\t',
                        '\033[32m.MMc               ..;l. xMN:                    KM0\u001b[00;0m\t',
                        '\033[32m"MM.                   "NMO                      oMM\u001b[00;0m\t',
                        '\033[32m.MM,                 .kMMl                       xMN\u001b[00;0m\t',
                        ' \033[32mKM0               .kMM0. .dl:,..               .WMd\u001b[00;0m\t',
                        ' \033[32m.XM0.           ,OMMK,    OMMMK.              .XMK\u001b[00;0m\t',
                        '  \033[32moWMO:.    .;xNMMk,       NNNMKl.          .xWMx\u001b[00;0m\t',
                        '    \033[32m:ONMMNXMMMKx;          .  ,xNMWKkxllox0NMWk,\u001b[00;0m\t',
                        '        \033[32m.....                    .:dOOXXKOxl,\u001b[00;0m\t\t',
			'\t\t\t\t\t\t\t',
			'\t\t\t\t\t\t\t',
			'\t\t\t\t\t\t\t'

		],
	"linux": [
			'        \u001b[30;1m#####\u001b[00;1m\t\t',
        		'       \u001b[30;1m#######\u001b[00;1m\t\t',
        		'       \u001b[30;1m##\u001b[00;1mO\u001b[30;1m#\u001b[00;1mO\u001b[30;1m##\u001b[00;1m\t\t',
       			'       \u001b[30;1m#\u001b[33;1m#####\u001b[30;1m#\u001b[00;1m\t\t',
	       		'     \u001b[30;1m##\u001b[00;1m##\u001b[33;1m###\u001b[00;1m##\u001b[30;1m##\u001b[00;1m\t',
        		'    \u001b[30;1m#\u001b[00;1m##########\u001b[30;1m##\u001b[00;1m\t',
        		'   \u001b[30;1m#\u001b[00;1m############\u001b[30;1m##\u001b[00;1m\t',
        		'   \u001b[30;1m#\u001b[00;1m############\u001b[30;1m###\u001b[00;1m\t',
        		'  \u001b[33;1m##\u001b[30;1m#\u001b[00;1m###########\u001b[30;1m#\u001b[33;1m##\u001b[00;1m\t',
        		'\u001b[33;1m######\u001b[30;1m#\u001b[00;1m#######\u001b[30;1m#\u001b[33;1m######\u001b[00;1m\t',
        		'\u001b[33;1m#######\u001b[30;1m#\u001b[00;1m#####\u001b[30;1m#\u001b[33;1m#######\u001b[00;1m\t',
        		'  \u001b[33;1m#####\u001b[30;1m#######\u001b[33;1m#####\u001b[00;1m\t',
        		'\t\t\t',
        		'\t\t\t',
        		'\t\t\t',
        		'\t\t\t'
		]

	}

os_name = data._data["os"].split()[0].lower()

if os_name not in logo.keys():
	os_name = "linux"

os_logo = logo[os_name]
os_color = color[os_name]


for i in range(0, len(os_logo) if len(os_logo) > len(data_k) else len(data_k)):

	print(os_logo[i] if i < len(os_logo) else '', f"{color_text(data_k[i] + ': ', os_color) if i < len(data_k) else ''} {data._data[data_k[i]] if i < len(data_k) else ''}")
