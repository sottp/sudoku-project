In this project, we will develop a sudoku solver that uses a more friendly interface than the one used in the first project.
For instance, the following corresponds to the new input and output format of a sudoku problem.
```
Input:                                               Output:
5 3 -  - 7 -  - - -                                  5 3 4  6 7 8  9 1 2
6 - -  1 9 5  - - -                                  6 7 2  1 9 5  3 4 8
- 9 8  - - -  - 6 -                                  1 9 8  3 4 2  5 6 7

8 - -  - 6 -  - - 3                                  8 5 9  7 6 1  4 2 3
4 - -  8 - 3  - - 1                                  4 2 6  8 5 3  7 9 1
7 - -  - 2 -  - - 6                                  7 1 3  9 2 4  8 5 6

- 6 -  - - -  2 8 -                                  9 6 1  5 3 7  2 8 4
- - -  4 1 9  - - 5                                  2 8 7  4 1 9  6 3 5
- - -  - 8 -  - 7 9                                  3 4 5  2 8 6  1 7 9
```
The dash symbol "```-```" is used to represent that in a position there is no number.

## Formalities.
You can work on the solution alone or in groups of two people. Different groups have to submit different solutions. In case of plagiarism, all groups involved will fail the project.

Your code will be autograded for technical correctness. However, the correctness of your implementation -- not the autograder's judgments -- will be the final judge of your score. If necessary, we will review and grade assignments individually to ensure that you receive due credit for your work.

The content of the **main** branch of your GitHub repository at the time of the due date will be considered your submission. Any modifications after the due date will be ignored. So will be any previous code that you committed before. Note that the autograder will give you the evaluation of your last commit, so be sure that it is what you expect.

**Start as soon as possible to avoid running out of time.**

Do not modify the file ```autograder.py``` nor any of the content of the directories ```.git```, ```.github``` and  ```tests```. Modifying some of these directories may prevent your code from working or cause a loss of your progress.

**Academic Dishonesty**: We will be checking your code against other submissions in the class for logical redundancy. If you copy someone else's code and submit it with minor changes, we will know. These cheat detectors are quite hard to fool, so please don't try. Modifying the behavior of the autograder in any way is also cheating. We trust you all to submit your own work only and to do it honestly; please don't let us down. If you do, we will pursue the strongest consequences available to us.

## Framework

This project requires Python 3.9 and the ```clingo``` Python package with version 5.6.2. You can check your installation by running the following commands:
```bash
python --version
python -c "import clingo; print(clingo.__version__)"
```
If you are missing the ```clingo``` package, you can install it with ```pip```:
```bash
python -m pip install clingo==5.6.2
```

Start by cloning this repository and add a file named ```group.txt``` containing the names of each of the members of the group. Each name should be in a separate line. Recall that without this file, we may not be able to identify your repository as yours.
The autograder in GitHub will give you no grade in that case.

The framework is composed of the following files:
| file               | description           |
| ------------------ | ----------------------|
| sudoku_board.py    | This is the only file that you need to modify |
| autograder.py      | The autrograder |


Do not modify any other existing files. Modifying any files may cause the autograder to fail. You will need to add new files.

We recommend that you create new commits frequently when doing this project. If at some point you realize you made a mistake, you can revert to a previous commit. Pushing to the GitHub repository may also help you in case you accidentally lose your local copy. 


## Question 1: A Sudoku Solver

We start by creating a Soduku solver that uses the same input and output format that we used in the first project. The first difference concerning the first project is that our new solver will receive only one file containing the input. You will write the code for this question in a new file named ```sudoku1.py``` that you need to create. 
For instance, by running the following command
```bash
python sudoku1.py instances/lp/ex00.lp
```
the solver should print the output:
```
clingo version 5.6.2
Reading from instances/lp/ex00.lp
Solving...
Answer: 1
sudoku(1,1,5) sudoku(1,2,3) sudoku(1,3,4) sudoku(1,4,6) sudoku(1,5,7) sudoku(1,6,8) sudoku(1,7,9) sudoku(1,8,1) sudoku(1,9,2) sudoku(2,1,6) sudoku(2,2,7) sudoku(2,3,2) sudoku(2,4,1) sudoku(2,5,9) sudoku(2,6,5) sudoku(2,7,3) sudoku(2,8,4) sudoku(2,9,8) sudoku(3,1,1) sudoku(3,2,9) sudoku(3,3,8) sudoku(3,4,3) sudoku(3,5,4) sudoku(3,6,2) sudoku(3,7,5) sudoku(3,8,6) sudoku(3,9,7) sudoku(4,1,8) sudoku(4,2,5) sudoku(4,3,9) sudoku(4,4,7) sudoku(4,5,6) sudoku(4,6,1) sudoku(4,7,4) sudoku(4,8,2) sudoku(4,9,3) sudoku(5,1,4) sudoku(5,2,2) sudoku(5,3,6) sudoku(5,4,8) sudoku(5,5,5) sudoku(5,6,3) sudoku(5,7,7) sudoku(5,8,9) sudoku(5,9,1) sudoku(6,1,7) sudoku(6,2,1) sudoku(6,3,3) sudoku(6,4,9) sudoku(6,5,2) sudoku(6,6,4) sudoku(6,7,8) sudoku(6,8,5) sudoku(6,9,6) sudoku(7,1,9) sudoku(7,2,6) sudoku(7,3,1) sudoku(7,4,5) sudoku(7,5,3) sudoku(7,6,7) sudoku(7,7,2) sudoku(7,8,8) sudoku(7,9,4) sudoku(8,1,2) sudoku(8,2,8) sudoku(8,3,7) sudoku(8,4,4) sudoku(8,5,1) sudoku(8,6,9) sudoku(8,7,6) sudoku(8,8,3) sudoku(8,9,5) sudoku(9,1,3) sudoku(9,2,4) sudoku(9,3,5) sudoku(9,4,2) sudoku(9,5,8) sudoku(9,6,6) sudoku(9,7,1) sudoku(9,8,7) sudoku(9,9,9)
SATISFIABLE

Models       : 1+
Calls        : 1
Time         : 0.016s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.016s
```
This is the same solution as we can obtain with the command
```bash
clingo sudoku.lp instances/lp/ex00.lp
```
where ```sudoku.lp``` is the file that contains the encoding of the sudoku problem.

The content of ```ex00.lp``` is the partially filled sudoku board shown above and described as facts:
```
%%file instances/lp/ex00.lp
initial(1,1,5). initial(1,2,3). initial(1,5,7).
initial(2,1,6). initial(2,4,1). initial(2,5,9). initial(2,6,5).
initial(3,2,9). initial(3,3,8). initial(3,8,6).
initial(4,1,8). initial(4,5,6). initial(4,9,3).
initial(5,1,4). initial(5,4,8). initial(5,6,3). initial(5,9,1).
initial(6,1,7). initial(6,5,2). initial(6,9,6).
initial(7,2,6). initial(7,7,2). initial(7,8,8).
initial(8,4,4). initial(8,5,1). initial(8,6,9). initial(8,9,5).
initial(9,5,8). initial(9,8,7). initial(9,9,9).
```

### Question 1a: A Sudoku Solver (10 points)

You should implement this solver using the ```clingo.ClingoApp``` class. This will allow us to use all the features of the ```clingo``` command line interface. For instance, we can use the option ```--outf=2``` to print the output in ```json``` format. For instance, by running the following command
```bash
python sudoku1.py instances/lp/ex00.lp --outf=2
```
we obtain the output
```
{
  "Solver": "clingo version 5.6.2",
  "Input": [
    "instances/lp/ex00.lp"
  ],
  "Call": [
    {
      "Witnesses": [
        {
          "Value": [
            "sudoku(1,1,5)", "sudoku(1,2,3)", "sudoku(1,5,7)", "sudoku(2,1,6)", "sudoku(2,4,1)", "sudoku(2,5,9)", "sudoku(2,6,5)", "sudoku(3,2,9)", "sudoku(3,3,8)", "sudoku(3,8,6)", "sudoku(4,1,8)", "sudoku(4,5,6)", "sudoku(4,9,3)", "sudoku(5,1,4)", "sudoku(5,4,8)", "sudoku(5,6,3)", "sudoku(5,9,1)", "sudoku(6,1,7)", "sudoku(6,5,2)", "sudoku(6,9,6)", "sudoku(7,2,6)", "sudoku(7,7,2)", "sudoku(7,8,8)", "sudoku(8,4,4)", "sudoku(8,5,1)", "sudoku(8,6,9)", "sudoku(8,9,5)", "sudoku(9,5,8)", "sudoku(9,8,7)", "sudoku(9,9,9)", "sudoku(3,1,1)", "sudoku(7,1,9)", "sudoku(8,1,2)", "sudoku(9,1,3)", "sudoku(2,2,7)", "sudoku(4,2,5)", "sudoku(5,2,2)", "sudoku(6,2,1)", "sudoku(8,2,8)", "sudoku(9,2,4)", "sudoku(1,3,4)", "sudoku(2,3,2)", "sudoku(4,3,9)", "sudoku(5,3,6)", "sudoku(6,3,3)", "sudoku(7,3,1)", "sudoku(8,3,7)", "sudoku(9,3,5)", "sudoku(1,4,6)", "sudoku(3,4,3)", "sudoku(4,4,7)", "sudoku(6,4,9)", "sudoku(7,4,5)", "sudoku(9,4,2)", "sudoku(3,5,4)", "sudoku(5,5,5)", "sudoku(7,5,3)", "sudoku(1,6,8)", "sudoku(3,6,2)", "sudoku(4,6,1)", "sudoku(6,6,4)", "sudoku(7,6,7)", "sudoku(9,6,6)", "sudoku(1,7,9)", "sudoku(2,7,3)", "sudoku(3,7,5)", "sudoku(4,7,4)", "sudoku(5,7,7)", "sudoku(6,7,8)", "sudoku(8,7,6)", "sudoku(9,7,1)", "sudoku(1,8,1)", "sudoku(2,8,4)", "sudoku(4,8,2)", "sudoku(5,8,9)", "sudoku(6,8,5)", "sudoku(8,8,3)", "sudoku(1,9,2)", "sudoku(2,9,8)", "sudoku(3,9,7)", "sudoku(7,9,4)"
          ]
        }
      ]
    }
  ],
  "Result": "SATISFIABLE",
  "Models": {
    "Number": 1,
    "More": "yes"
  },
  "Calls": 1,
  "Time": {
    "Total": 0.023,
    "Solve": 0.000,
    "Model": 0.000,
    "Unsat": 0.000,
    "CPU": 0.023
  }
}
```
Once you have implemented the solver, you can run the autograder to check if your solution is correct. To do so, run the following command
```bash
python autograder.py --question=1a
```
### Question 1b: Sorting the output (10 points)

Recall that an answer set is a set of atoms with no particular order. Clingo does not sort the output in any particular way. To make the output easier to read, we are going to sort the output. Note the output printed in [Question 1a](#question-1a-a-audoku-solver) is alphabetically sorted. We are going to sort the output in the same way. To do so, we are going to overwrite the function ```print_model``` of the ```clingo.ClingoApp``` class. You can test your implementation by running the following command
```bash
python autograder.py --question=1b
```

## Question 2: Parsing models (10 points)

We will now parse a ```clingo.solving.Model``` object into a ```Sudoku``` object.
Please check the API documentation for details of this class (https://potassco.org/clingo/python-api/current/clingo/solving.html#clingo.solving.Model). You should write your implementation in the method 
```python
   @classmethod
   def from_model(cls, model: clingo.solving.Model) -> 'Sudoku':
       board = {}
       # YOUR CODE HERE
       return cls(board)
```
of the class ```Sudoku```. You can find this class in the file ```sudoku_board.py```. This method takes a ```clingo.solving.Model``` object as input and returns a ```Sudoku``` object. You can assume that the input ```clingo.solving.Model``` object represents a valid sudoku solution.

Method ```model.symbols(shown=True)``` returns a list of ```clingo.symbol.Symbol``` objects that represent the atoms in the model as they will be printed by ```clingo```.
For instance, if the model contains facts
```
sudoku(1,1,5) sudoku(1,2,3) sudoku(1,3,4) sudoku(1,4,6) sudoku(1,5,7) sudoku(1,6,8) sudoku(1,7,9) sudoku(1,8,1) sudoku(1,9,2).
sudoku(2,1,6) sudoku(2,2,7) sudoku(2,3,2) sudoku(2,4,1) sudoku(2,5,9) sudoku(2,6,5) sudoku(2,7,3) sudoku(2,8,4) sudoku(2,9,8).
sudoku(3,1,1) sudoku(3,2,9) sudoku(3,3,8) sudoku(3,4,3) sudoku(3,5,4) sudoku(3,6,2) sudoku(3,7,5) sudoku(3,8,6) sudoku(3,9,7).
sudoku(4,1,8) sudoku(4,2,5) sudoku(4,3,9) sudoku(4,4,7) sudoku(4,5,6) sudoku(4,6,1) sudoku(4,7,4) sudoku(4,8,2) sudoku(4,9,3).
sudoku(5,1,4) sudoku(5,2,2) sudoku(5,3,6) sudoku(5,4,8) sudoku(5,5,5) sudoku(5,6,3) sudoku(5,7,7) sudoku(5,8,9) sudoku(5,9,1).
sudoku(6,1,7) sudoku(6,2,1) sudoku(6,3,3) sudoku(6,4,9) sudoku(6,5,2) sudoku(6,6,4) sudoku(6,7,8) sudoku(6,8,5) sudoku(6,9,6).
sudoku(7,1,9) sudoku(7,2,6) sudoku(7,3,1) sudoku(7,4,5) sudoku(7,5,3) sudoku(7,6,7) sudoku(7,7,2) sudoku(7,8,8) sudoku(7,9,4).
sudoku(8,1,2) sudoku(8,2,8) sudoku(8,3,7) sudoku(8,4,4) sudoku(8,5,1) sudoku(8,6,9) sudoku(8,7,6) sudoku(8,8,3) sudoku(8,9,5).
sudoku(9,1,3) sudoku(9,2,4) sudoku(9,3,5) sudoku(9,4,2) sudoku(9,5,8) sudoku(9,6,6) sudoku(9,7,1) sudoku(9,8,7) sudoku(9,9,9)
```
representing the solution displayed at the beginning of this page, then the attribute ```board``` should contain the following dictionary
```python
{
   (1, 1): 5, (1, 2): 3, (1, 3): 4, (1, 4): 6, (1, 5): 7, (1, 6): 8, (1, 7): 9, (1, 8): 1, (1, 9): 2,
   (2, 1): 6, (2, 2): 7, (2, 3): 2, (2, 4): 1, (2, 5): 9, (2, 6): 5, (2, 7): 3, (2, 8): 4, (2, 9): 8, 
   (3, 1): 1, (3, 2): 9, (3, 3): 8, (3, 4): 3, (3, 5): 4, (3, 6): 2, (3, 7): 5, (3, 8): 6, (3, 9): 7,
   (4, 1): 8, (4, 2): 5, (4, 3): 9, (4, 4): 7, (4, 5): 6, (4, 6): 1, (4, 7): 4, (4, 8): 2, (4, 9): 3, 
   (5, 1): 4, (5, 2): 2, (5, 3): 6, (5, 4): 8, (5, 5): 5, (5, 6): 3, (5, 7): 7, (5, 8): 9, (5, 9): 1, 
   (6, 1): 7, (6, 2): 1, (6, 3): 3, (6, 4): 9, (6, 5): 2, (6, 6): 4, (6, 7): 8, (6, 8): 5, (6, 9): 6, 
   (7, 1): 9, (7, 2): 6, (7, 3): 1, (7, 4): 5, (7, 5): 3, (7, 6): 7, (7, 7): 2, (7, 8): 8, (7, 9): 4, 
   (8, 1): 2, (8, 2): 8, (8, 3): 7, (8, 4): 4, (8, 5): 1, (8, 6): 9, (8, 7): 6, (8, 8): 3, (8, 9): 5, 
   (9, 1): 3, (9, 2): 4, (9, 3): 5, (9, 4): 2, (9, 5): 8, (9, 6): 6, (9, 7): 1, (9, 8): 7, (9, 9): 9, 
}
```
Note that, internally, the sudoku is represented by a dictionary stored in the attribute ```board``` that maps each position to its value:
```python
   def __init__(self, board: dict[(int, int), int]):
       self.board = board
```
The keys of the dictionary are tuples of two integers that represent the position of a cell in the sudoku. The first integer is the row and the second integer is the column. The values of the dictionary are integers that represent the number in the cell. Cells, rows and values are represented by numbers between ```1``` and ```9```.

You can check your implementation by running
```
python autograder.py --question=2
```



## Question 3: Formating Sudokus (10 points)

Start by filling in the method 
```python
def __str__(self) -> str:
   s = ""
   # YOUR CODE HERE
   return s
``` 
in the class ```Sudoku```. This method should return a string that represents the sudoku in the format illustrated above. To be precise,
- each row of the sudoku should be in a separate line,
   - there should be no empty lines between rows that belong to the same block,
   - there should be one empty line between each two rows that belong to different blocks,
- numbers in a line should be separated by one or two blank spaces,
   - there should be one blank space between two numbers that belong to the same block,
   - there should be two blank spaces between two numbers that belong to different blocks.

For instance, if the attribute ```board``` of the ```Sudoku``` object is the dictionary
```python
{
   (1, 1): 5, (1, 2): 3, (1, 3): 4, (1, 4): 6, (1, 5): 7, (1, 6): 8, (1, 7): 9, (1, 8): 1, (1, 9): 2,
   (2, 1): 6, (2, 2): 7, (2, 3): 2, (2, 4): 1, (2, 5): 9, (2, 6): 5, (2, 7): 3, (2, 8): 4, (2, 9): 8, 
   (3, 1): 1, (3, 2): 9, (3, 3): 8, (3, 4): 3, (3, 5): 4, (3, 6): 2, (3, 7): 5, (3, 8): 6, (3, 9): 7,
   (4, 1): 8, (4, 2): 5, (4, 3): 9, (4, 4): 7, (4, 5): 6, (4, 6): 1, (4, 7): 4, (4, 8): 2, (4, 9): 3, 
   (5, 1): 4, (5, 2): 2, (5, 3): 6, (5, 4): 8, (5, 5): 5, (5, 6): 3, (5, 7): 7, (5, 8): 9, (5, 9): 1, 
   (6, 1): 7, (6, 2): 1, (6, 3): 3, (6, 4): 9, (6, 5): 2, (6, 6): 4, (6, 7): 8, (6, 8): 5, (6, 9): 6, 
   (7, 1): 9, (7, 2): 6, (7, 3): 1, (7, 4): 5, (7, 5): 3, (7, 6): 7, (7, 7): 2, (7, 8): 8, (7, 9): 4, 
   (8, 1): 2, (8, 2): 8, (8, 3): 7, (8, 4): 4, (8, 5): 1, (8, 6): 9, (8, 7): 6, (8, 8): 3, (8, 9): 5, 
   (9, 1): 3, (9, 2): 4, (9, 3): 5, (9, 4): 2, (9, 5): 8, (9, 6): 6, (9, 7): 1, (9, 8): 7, (9, 9): 9, 
}
```
the call to ```___str__()``` on this object should return the string shown as output at the beginning of this page:
```
5 3 4  6 7 8  9 1 2
6 7 2  1 9 5  3 4 8
1 9 8  3 4 2  5 6 7

8 5 9  7 6 1  4 2 3
4 2 6  8 5 3  7 9 1
7 1 3  9 2 4  8 5 6

9 6 1  5 3 7  2 8 4
2 8 7  4 1 9  6 3 5
3 4 5  2 8 6  1 7 9
```

You can check your implementation by running
```
python autograder.py --question=3
```




## Question 4: Solving and printing Sudokus (30 points)

We will now build the second iteration of the sudoku solver. This solver reads the input board in the format of Project 1 and outputs the solution in the format illustrated at the top of this page.
Create a file called ```sudoku4.py``` by copying `sudoku1.py` and modifying it to print the required format.


<!-- For instance, the above input sudoku is represented by the following facts.
```
%%file instances/lp/ex00.lp
initial(1,1,5). initial(1,2,3). initial(1,5,7).
initial(2,1,6). initial(2,4,1). initial(2,5,9). initial(2,6,5).
initial(3,2,9). initial(3,3,8). initial(3,8,6).
initial(4,1,8). initial(4,5,6). initial(4,9,3).
initial(5,1,4). initial(5,4,8). initial(5,6,3). initial(5,9,1).
initial(6,1,7). initial(6,5,2). initial(6,9,6).
initial(7,2,6). initial(7,7,2). initial(7,8,8).
initial(8,4,4). initial(8,5,1). initial(8,6,9). initial(8,9,5).
initial(9,5,8). initial(9,8,7). initial(9,9,9).
``` -->
Running the command
```bash
$python sudoku4.py 0 instances/lp/ex00.lp 
```
should produce an output similar to the following:
```bash
clingo version 5.6.2
Reading from instances/lp/ex00.lp
Solving...
Answer: 1
5 3 4  6 7 8  9 1 2
6 7 2  1 9 5  3 4 8
1 9 8  3 4 2  5 6 7

8 5 9  7 6 1  4 2 3
4 2 6  8 5 3  7 9 1
7 1 3  9 2 4  8 5 6

9 6 1  5 3 7  2 8 4
2 8 7  4 1 9  6 3 5
3 4 5  2 8 6  1 7 9
SATISFIABLE

Models       : 1
Calls        : 1
Time         : 0.014s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.014s
```
We can use the formatting function that we developed in [Question 3](#Question-3:-Formating-Sudokus-(10-points)). The only thing that we need to do is to modify the solver to output the solution in the required format. 
Recall that you have learned how to modify the format printed in [Question 1b](#Question-1b:-Sorting-the-output-(10-points)).
You can check your implementation by running
```bash
python autograder.py --question=4
```


## Question 5: Reading Sudokus (10 points)

Fill now the class method 
```python
   @classmethod
   def from_str(cls, s: str) -> 'Sudoku':
      sudoku = {}
      #YOUR CODE HERE
      return cls(sudoku)
```
in the class ```Sudoku```. This method takes as its argument a string, parses it and returns a ```Sudoku``` object that represents the sudoku in the string ```s```. Internally this ```Sudoku``` object should have its attribute ```board``` filled appropriately. For each cell in the sudoku that has a value, the dictionary should contain an entry with the position of the cell as the key and the value of the cell as the value. Please check [Question 2](#question-2-parsing-models-10-points) for more details about the format.
There should not be entries for cells that contain no value.
For instance, for the input at the beginning of the page, we obtain the dictionary object:
```python
{
   (1, 1): 5, (1, 2): 3, (1, 5): 7, 
   (2, 1): 6, (2, 4): 1, (2, 5): 9, (2, 6): 5, 
   (3, 2): 9, (3, 3): 8, (3, 8): 6, 
   (4, 1): 8, (4, 5): 6, (4, 9): 3, 
   (5, 1): 4, (5, 4): 8, (5, 6): 3, (5, 9): 1, 
   (6, 1): 7, (6, 5): 2, (6, 9): 6, (7, 2): 6, 
   (7, 7): 2, (7, 8): 8, (8, 4): 4, 
   (8, 5): 1, (8, 6): 9, (8, 9): 5, 
   (9, 5): 8, (9, 8): 7, (9, 9): 9
}
```
The input format is similar to the one used in the method ```__str__``` with an important difference. Each cell may contain either a number or a dash symbol "```-```", which is used to represent that in a position there is no number.
You can check your implementation by running
```
python autograder.py --question=5
```


## Question 6: Solving Sudokus with custom input (20 points)

We will now build the third iteration of the sudoku solver. This solver reads the input board in the format specified in the previous question and outputs the solution in the same format illustrated above. Create a file called ```sudoku6.py``` by copying ```sudoku4.py```. We will modify it to read the input in the required format.

### Question 6a: The Context Class (10 points)
We start by creating a class ```Context``` in the file ```sudoku6.py```.
```python
class Context:

    def __init__(self, board: Sudoku):
        # YOUR CODE HERE
        
    def initial(self) -> list[clingo.symbol.Symbol]:
        # YOUR CODE HERE
```
This class should have a method ```initial``` that returns a ```list``` of ```clingo.symbol.Symbol``` objects that represent the initial state of the board.
Check the lecture slides for more details on how to construct this list.
This initial state of the board is provided as a ```Sudoku``` object at the creation time of the ```Context``` object. 

You can check your implementation by running the following command:
```bash
python autograder.py --question=6a
```

### Question 6b: Putting all together (10 points)

It is time to put all our progress together and complete the solver. Add a file ```sudoku_py.lp``` with the bridge rules between Python and the logic programming. These rules should produce facts of the form ```initial(a,b,c)``` for each cell ```(a,b)``` that has a value ```c```. This uses the method ```initial``` of the class ```Context``` to obtain the list of facts. We need to modify the file ```sudoku6.py``` to use our ```Context``` object. The lecture slides explain in more detail how to do this.

Once you completed the solver you can run it as follows
```bash
python sudoku6.py instances/txt/ex00.txt 
```
and you should expect the following answer
```bash
clingo version 5.6.2
Reading from instances/txt/ex00.txt
Solving...
Answer: 1
5 3 4  6 7 8  9 1 2
6 7 2  1 9 5  3 4 8
1 9 8  3 4 2  5 6 7

8 5 9  7 6 1  4 2 3
4 2 6  8 5 3  7 9 1
7 1 3  9 2 4  8 5 6

9 6 1  5 3 7  2 8 4
2 8 7  4 1 9  6 3 5
3 4 5  2 8 6  1 7 9
SATISFIABLE

Models       : 1
Calls        : 1
Time         : 0.014s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.014s
```
You can try several other examples from the directory ```instances/txt/``` to observe the behavior of your implementation.

Once you are confident in your implementation, you can check it by running the following command:
```bash
python autograder.py --question=6b
```

You can check all your progress by simply running the following command:
```bash
python autograder.py
```
If you obtained 100 points, you are done. Congratulations!

## Submission recall

**Remember to commit and push your code to your GitHub repository**. The content of the main branch of your GitHub repository at the time of the deadline will be considered your submission. Any modifications after the due date will be ignored. So will be any previous code that you committed before. Note that **the autograder will give you the evaluation of your last commit, so be sure that it is what you expect**.
