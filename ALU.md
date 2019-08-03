# ALU of the CPU (Chicken Processing Unit)

The data path takes three inputs

## Available Functions

- x0 -- Output <= A
- x1 -- Output <= B
- x2 -- Output <= A & B
- x3 -- Output <= A | C
- x4 -- Output <= ~A
- x5 -- Output <= A >> B
- x6 -- Output <= A << B
- x7 -- Output <= A >>> B
- x8 -- Output <= -A
- x9 -- Output <= A + B
- xA -- Output <= A - B
- xB -- Output <= A * B
- xC -- Output <= A / B
- xD -- Output <= (A != 0) ? 0 : 1
- xE -- Output <= (A != 0) ? 1 : 0
- xF -- Output <= (A > 0 && B[2] || A == 0 && B[1] || A < 0 && B[0]) ? 1 : 0