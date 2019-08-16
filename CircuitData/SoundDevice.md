# Sound Device

This component consists of two MIDI devices, each taking 16 bits of the data input. The bits for each device are broken up as follows:

|  Bit  | Use                                                                                                                      |
| :---: | :----------------------------------------------------------------------------------------------------------------------- |
|  15   | Force volume write                                                                                                       |
| 14 -8 | Volume Control                                                                                                           |
|   7   | Note/Instrument select. When 0, the value of bits 6-0 are used to set the note, when 1 it is used to set the instrument. |
|  6-0  | Note/Instrument data.                                                                                                    |

For each byte within the control word, a register is used to store the seven least significant bytes. Whenever the value of each byte 
is not equal to zero, the value in the register is updated. When the value of the byte is equal to zero, the value in the register is
held and is then passed to the circuit instead of the byte itself.

If the value of Note/Instrument data is zero and Note/Instrument select is low, the note that was last started on that channel is stoppes.
Both channels default to a square wave.
