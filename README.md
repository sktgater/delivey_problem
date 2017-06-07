# delivey_problem
Delivery Problem with Midway Checkpoints

Author: Li Wang

Description of the Question:
A postman is delivering mails in a square-shaped town. He starts from the start (S) and would arrive at the goal (G). 
On the way, he has to deliver mails at some checkpoints (X).
One possible configuration of the town is like:
########
#...G.X#
#.##.X.#
#S.X...#
########
Calculate the minimum distance the postman has to travel from the start to the goal while passing all the checkpoints. 

Remarks:
'S' = start point
'G' = goal point
'X' = checkpoint
'.' = open-block that the postman can pass
'#' = closed-block that the postman cannot pass
- A movement means a vertical or horizontal step (up, down, left or right)
- Other types of movements, such as moving diagonally, or skipping one or more blocks, are NOT allowed.
- The postman cannot get out of the map.
- Distance is defined as the number of movements
- The postman CAN pass opened-blocks, checkpoints, the start, and the goal more than once if necessary.
- You can assume 1<=width<=100, 1<=height<=100.
- The maximum number of checkpoints is 18.
- Return -1 if given arguments do not satisfy specifications, or players cannot arrive at the goal from the start by
passing all the checkpoints. 

Idea: BFS. Steps are as follow:
1. find locations of S, all checkpoints X (in a list), and goal G
2. use BFS to get shortest paths from S to each checkpoint X. Save in List.
Each checkpoint is matched under the same list index
Return -1 if not reachable
3. get shortest paths from each X to each other X
4. get shortest path from each X to the G
5. find shortest distance from starting point, via all midway checkpoints to the ending point

Assumptions: only has one goal point and one starting point.