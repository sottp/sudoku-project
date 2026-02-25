% Domain
row(1..9).
col(1..9).
num(1..9).

% Each cell contains exactly one number
1 { cell(R, C, N) : num(N) } 1 :- row(R), col(C).

% Row constraint
:- cell(R, C1, N), cell(R, C2, N), C1 != C2.

% Column constraint
:- cell(R1, C, N), cell(R2, C, N), R1 != R2.

% Block definition
block(BR, BC, R, C) :-
    BR = 1..3, BC = 1..3,
    R = 3*(BR-1)+1 .. 3*BR,
    C = 3*(BC-1)+1 .. 3*BC.

% Block constraint
:- cell(R1, C1, N), cell(R2, C2, N),
   block(BR, BC, R1, C1),
   block(BR, BC, R2, C2),
   (R1, C1) != (R2, C2).

#show cell/3.

% Sudoku bits
