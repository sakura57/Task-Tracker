This is a simple task tracker app I created as a project to improve my programming skills. It simply uses a CLI so users can add, update, delete tasks, as well as mark them as in-progress or done. 
There is also a list function to view all tasks, with available filters depending on current task status.

Instructions:
In order to use the CLI, you have to enter the commands as displayed below, keeping in mind case sensitivity and quotes.

- add "TaskName": adds a new task with the description between quotes

- update TaskID "TaskName": update the task description for an existing task, requires the task's ID number, which can be found by using the list command.

- delete TaskID: deletes the task, requires the task's ID number. NOTE: upon using this command, all other task IDs will be updated.

- mark in-progress TaskID: changes the task's status to in-progress, requires the task's ID number.

- mark done TaskID: changes the task's status to done, requires the task's ID number.

- list: will provide a list of every task that has been added.

 The list appears as follows:

 Task #TaskID:
 id : TaskID
 description : TaskName
 status : TaskStatus
 createdAt : Time the task was created.
 updatedAt : Time the task was last updated.

- list todo: lists all tasks with status as "todo".

- list in-progress: lists all tasks with status as "in-progress".

- list done: lists all tasks with status as "done".

I have tested all features to ensure they work as required, though I cannot be certain there are no bugs or errors.

Project URL: https://roadmap.sh/projects/task-tracker
