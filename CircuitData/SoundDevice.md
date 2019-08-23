# Sound Device dev{0}[8]

This component consists of two MIDI channel devices, each of which takes a 16 bit word from the memory input as a control word. The bits for each device are broken up as follows:

| Bits | Use                |
| :--: | :----------------- |
|  15  | Force volume write |
| 14-8 | Volume             |
|  7   | Program control    |
| 6-0  | Note/Program       |

The volume of the MIDI channel will be reassigned to Volume whenever any bits in the range 15-8 are high.

If Program Control is high, the value of Note/Program is used to set the current program (instrument) that channel will play.

If Program Control is low and Note/Program is greater than one, the channel will start playing the note specified by Note/Program.

If Program Control is low and Note/Program is equal to one, whatever note was last started on that channel will be stopped.

If Program Control is low and Note/Program is equal to zero, no new note will start and no note will stop.

Both channels default to a volume of 48 and program 0 (Grand Piano).

For best results, set a volume on both channels when your program starts.