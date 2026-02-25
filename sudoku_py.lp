% Domain
row(1..9).
col(1..9).
num(1..9).

% Each instance contains exactly one number
1 { instance(R, C, N) : num(N) } 1 :- row(R), col(C).

% Row constraint
:- instance(R, C1, N), instance(R, C2, N), C1 != C2.

% Column constraint
:- instance(R1, C, N), instance(R2, C, N), R1 != R2.

% Block definition
block(BR, BC, R, C) :-
    BR = 1..3, BC = 1..3,
    R = 3*(BR-1)+1 .. 3*BR,
    C = 3*(BC-1)+1 .. 3*BC.

% Block constraint
:- instance(R1, C1, N), instance(R2, C2, N),
   block(BR, BC, R1, C1),
   block(BR, BC, R2, C2),
   (R1, C1) != (R2, C2).

#show instance/3.

% Enforce initial clues
:- initial(R, C, N), not instance(R, C, N).

% Sudoku bits
5 3 -  - 7 -  - - -  
6 - -  1 9 5  - - -  
- 9 8  - - -  - 6 -  

8 - -  - 6 -  - - 3  
4 - -  8 - 3  - - 1  
7 - -  - 2 -  - - 6  

- 6 -  - - -  2 8 -  
- - -  4 1 9  - - 5  
- - -  - 8 -  - 7 9  
