#!/usr/bin/python3

import sys
if "-v" in sys.argv:
	print("Version 0.1")
	sys.exit(0)

sys.stderr.write("Esto es un error")
print("Continuar con la aplicacion")
