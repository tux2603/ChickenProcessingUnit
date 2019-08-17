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

| Number of Chickens | Double Wide | Name        | Chicken Name |          Clock Ticks          | Description                                                                                                                                                                                                                |
| :----------------: | :---------: | :---------- | :----------- | :---------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         0          |     no      | return/exit | axe          | 16 (return) / infinite (exit) | Returns from the current subroutine, or if no subroutine exits the program.                                                                                                                                                |
|         1          |     yes     | push        | lay (an egg) |               6               | Pushes the value of the second portion of the instruction to the stack.                                                                                                                                                    |
|         2          |     no      | pop         | pluck        |               6               | Pops the topmost value from the stack and discards it.                                                                                                                                                                     |
|         3          |     no      | add         | hatch        |               8               | Pops the two values from the top of the stack, adds them together, and pushes the result back onto the stack.                                                                                                              |
|         4          |     no      | subtract    | fox          |               8               | Pops the top two values from the stack, subtracts the second from the first, and pushes the result back onto the stack.                                                                                                    |
|         5          |     no      | multiply    | rooster      |               8               | Pops the top two stack values, multiplies them, and pushes the result to the top of the stack.                                                                                                                             |
|         6          |     no      | divide      | divide       |               8               | Pops the top two values from the stack, divides the first by the second using integer division, and pushes the result back onto the stack.                                                                                 |
|         7          |     no      | negate      | anti-chicken |               7               | Pops the top value from the stack, negates it, and pushes the result back onto the stack.                                                                                                                                  |
|         8          |     no      | read        | cookbook     |            blocks             | Reads a single char from usrin and pushes it to the stack. Blocks until a char is available.                                                                                                                               |
|         9          |     no      | char        | squawk       |               6               | Pops the topmost char from the stack and prints it to usrout.                                                                                                                                                              |
|         10         |     no      | memchar     | BBQ          |               9               | Pops the top two values from the stack, then prints a value from memory to usrout, using the first value as device ID and the second value as the address.                                                                 |
|         11         |     no      | draw        | scratch      |              11               | Pops the top three values from the stack, and draws the color specified by the thord value on the screen at the x-y coordinates specified by the first and second values.                                                  |
|         12         |     no      | load        | pick         |               8               | Pops the top two values (_a_ and _b_) off the stack, and then pushes the data stored at address _a_ of memory device _b_.                                                                                                  |
|         13         |     no      | store       | peck         |               9               | Pops the top three values (_a_, _b_, and _c_) off the stack, then writes _c_ to address _a_ on memory device _b_.                                                                                                          |
|         14         |     yes     | compare     | compare      |              10               | Pops the top two values (_a_ and _b_) off of the stack and computes a - b. If the PZN value of the result matches any of the PZN bits given in the next line, a 1 is pushed to the stack, else a 0 is pushed to the stack. |
|         15         |     no      | jump        | jump         |    8 (jump) / 7 (no jump)     | Pops the top two values (_a_ and _b_) from the stack, and sets PC to _a_ if _b_ is not equal to zero.                                                                                                                      |
