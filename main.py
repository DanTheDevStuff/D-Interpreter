# Dans custom language interpreter
# Library imports
from sys import argv as argument

print("D# Interpreter V0.1\n\n")

if len(argument) == 2:
	filename = argument[1]
	lines = []
else: 
	print("No file found")
	
with open(filename, "r") as interpret:
	for line in interpret:
		lines.append(line.strip())

for line in lines:
	if line.startswith("bobsay(\"") and line.endswith("\")"):
		print(line[8: -2])

	elif line.startswith("bobsay(\"") and line.endswith("\", nonew)"):
		print(line[8: -9], end="")
	
	elif line.startswith("/:)"):
		pass
	
	elif line.startswith("bobread(") and line.endswith(")"):
		input()