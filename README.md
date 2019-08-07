# ChickenProcessingUnit
A CPU that uses Chicken++ as its assembly language, implemented using hneemann's [Digital](https://github.com/hneemann/Digital) circuit simulator.

# Things discovered

Digital 'Program memory' utility uses little endian format to store and load data.

# Oddnesses, abnormalities, and peculiarities

- In order to read a new character from user in, you must first write to user in. The value that you try to write will be thrown away.
This is implemented internally with the READ opcode, but must be done manually if using LOAD or PRINTMEM. This is due to the internal
construction of the memory unit that interfaces with user input and output.
- Another line?