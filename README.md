# ChickenProcessingUnit

A CPU that uses Chicken++ as its assembly language, implemented using hneemann's [Digital](https://github.com/hneemann/Digital) circuit simulator.

# Things discovered

Digital 'Program memory' utility uses little endian format to store and load data.

# Oddnesses, abnormalities, and peculiarities

- In order to read a new character from user in, you must first write to user in. The value that you try to write will be thrown away.
  This is implemented internally with the READ opcode, but must be done manually if using LOAD or PRINTMEM. This is due to the internal
  construction of the memory unit that interfaces with user input and output.
- Another line?

# Chicken++

The valid instructions for Chicken++ are as follows

| Number of Chickens | Implemented | Double Wide | Name        | Chicken Name    | Description                                                                                                                                                               |
| :----------------: | :---------: | :---------: | :---------- | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|         0          |     yes     |     no      | return/exit | axe             | Returns from the current subroutine, or if no subroutine exits the program.                                                                                               |
|         1          |     yes     |     yes     | push        | lay (an egg)    | Pushes the value of the second portion of the instruction to the stack.                                                                                                   |
|         2          |     yes     |     no      | pop         | pluck           | Pops the topmost value from the stack and discards it.                                                                                                                    |
|         3          |     yes     |     no      | add         | hatch           | Pops the two values from the top of the stack, adds them together, and pushes the result back onto the stack.                                                             |
|         4          |     yes     |     no      | subtract    | fox             | Pops the top two values from the stack, subtracts the second from the first, and pushes the result back onto the stack.                                                   |
|         5          |     yes     |     no      | multiply    | rooster         | Pops the top two stack values, multiplies them, and pushes the result to the top of the stack.                                                                            |
|         6          |     yes     |     no      | divide      | divide          | Pops the top two values from the stack, divides the first by the second using integer division, and pushes the result back onto the stack.                                |
|         7          |     yes     |     no      | negate      | anti-chicken    | Pops the top value from the stack, negates it, and pushes the result back onto the stack.                                                                                 |
|         8          |     yes     |     no      | read        | cookbook        | Reads a single char from usrin and pushes it to the stack. Blocks until a char is available.                                                                              |
|         9          |     yes     |     no      | char        | BBQ             | Pops the topmost char from the stack and prints it to usrout.                                                                                                             |
|         10         |     yes     |     no      | memchar     | blindfolded BBQ | Pops the top two values from the stack, then prints a value from memory to usrout, using the first value as device ID and the second value as the address.                |
|         11         |     yes     |     no      | draw        | scratch         | Pops the top three values from the stack, and draws the color specified by the thord value on the screen at the x-y coordinates specified by the first and second values. |
