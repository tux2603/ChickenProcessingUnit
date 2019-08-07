# Data Path

The data path of the Chicken Processing Unit takes a 28- bit control word and two 32-bit constant values.
Internal memory consists of a dual-channel register file with 8 32-bit registers and one special purpose 
6-bit register used to specify the active memory device.

# Control word

The control word is broken into 13 subsections, outlined below:

| Bits  | Name         | Description                                                                                                                                      |
| -----:|:------------:|:------------------------------------------------------------------------------------------------------------------------------------------------ |
| 27    | Enable       | Enables the data path. When low, all inputs are pulled to zero, and all outputs except for PZN are in a high impedance state. PZN will be 0x000. |
| 26-24 | A Address    | The address to be used for the register A in the internal register file.                                                                         |
| 23    | Const Select | Selects whether to use the value of register B or ConstIn for internal computations. Zero selects register B, one selects ConstIn.               |
| 22-20 | B Address    | The address to be used for the register B in the internal register file.                                                                         |
| 19    | D Write      | When one, the result value is written to register D in the register file.                                                                        |
| 18-16 | D Address    | The address to be used for the register D in the internal register file.                                                                         |
| 15-12 | Function     | Specifies the function to be performed by the internal ALU. See [ALU.md](./ALU.md) for more details.                                             |
| 11-10 | Result Select| Selects the value to use as the result. Zero selects ALU output, one selects NextLine, two selects MemoryIn, and three pops result from the stack.|
| 9     | Push Result  | When asserted, the result will be pushed to the stack.                                                                                           |
| 8     | Store Result | When asserted, the result will be saved to MemDev at MemAddr.                                                                                    |
| 7     | Device Select| Selects whether the value at DeviceRegister or Device Constant (see below) will be used to select the active memory device.                      |
| 6     | Write Device | When asserted, the result will be stored in DeviceRegister.                                                                                      |
| 5-0   | Device Constant | Used to specify the active memory device when used in conjunction with Device Select                                                          |

This is after the table.