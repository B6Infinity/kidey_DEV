# from colorama import init as colorama_init
# from colorama import Fore
# from colorama import Style

# colorama_init()



HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def printG(s):
	print(f'\u001b[32m{s}\u001b[0m')

def printB(s):
	print(f'\u001b[34m{s}\u001b[0m')

def printM(s):
	print(f'\u001b[35m{s}\u001b[0m')

def printC(s):
	print(f'\u001b[36m{s}\u001b[0m')

def printR(s):
	print(f'{WARNING}{s}\u001b[0m')

def printBOLD(s, color = 'Y'):
	if color == 'Y':
		print(f'{WARNING}{BOLD}{s}\u001b[0m')

def warn_console(s):
	print(f'{WARNING}{s}\u001b[0m')
