## Insights on the approach:
1.  The Waterfall model of software development used here is quite basic and outdated. At the very least, there should be a feedback loop from subsequent roles to update previous ones. For example, when reviewing an engineer's feedback that "Implementation of Solving Sudoku is not mentioned," this should be fed back to the Product Manager or Architect.

2. The model is lacking in information, especially when trying to create something new. One-line prompts are not sufficient as they do not provide enough detail. The workflow could be enhanced by including an additional call to understand how the project works. For instance, when developing a Sudoku game, an API call could be made to "Explain the workings and rules of the Sudoku game step by step." This information, along with the BOSS's idea, could then be passed on to the Product Manager.

3. Due to the specific implementation of Environment Memory and Role Memory, it is not possible to provide user feedback between steps. It would have been preferable to have a system where the user could provide feedback or make edits at any stage before passing the output to the next level. While this user feedback could potentially disrupt the workflow, it does not outweigh the need for a supervisor. 

4. I was unable to determine what the QA Engineer was doing. During my runs, I couldn’t find any ‘tests’ directory.

5. The Quadrant/Comparison Chart (Mermaid) is quite general and arbitrary. The axis and quadrant labels could be made more specific to the project. For example, Reach and Engagement may not be relevant metrics for a B2B product.

6. Prompts are harcoded. Could be YAML/JSON file.

7. Several times, MetaGPT failed to generate a main or entry file for the project.

8.  It begins with the entry file, importing functions/classes that need to be defined later, but then fails to implement those functionalities.

9. When creating a web app that requires multiple ports, such as for the backend and database, conflicts in port allocation can arise.

10. More Specific Roles could be added like Frontend & Backend Developer.

11. I would have liked a funcitonality of writing a Dockerfile for the project.

12. Python only support, if you ask for other language specifically, "Build a Sudoku game in JavaScript", still doesn't work. Even after modifying/removing the inbuilt ("Follow PEP8 standard") prompt.
 


## Changes in the code:

1. Modified the code to take custom input from file defining the profile, goal and constraints.
2. Modified the prompts to specifically create the entry "main.py" file.
3. I tested to generate different programming langauge codes, but generated ones were also not complete. 
4. Trying to write code for running a subprocess within the project to execute the generated workspace (In progress). However, there is difficulty in extracting the workspace folder details from the environment memory. The idea is to run the code, catch any errors that occur, and then report these errors to the Engineer and ProjectManager so that they can take them into account in the next iteration. Ideally, the errors should be propagated back without having to restart the entire process.
5. Other than Sudoku Project, I also tried with 2048 game, as it was the example mentioned in the paper. It didn't ran out of box.
6. I also tried with a project which would not be very general, "Courses Review Webapp like IMDB". Didn't created any entry file, metaGPT missed multiple DataModels definitions, API definition, import error, etc. Also it didn't defined an entrypoint to insert a new course.
When I gave a more explained prompt for making different end points and functionalities of insert, update, post review etc. It created the architecture for them but still lacked in the DataModel definition, import error, etc.
  

Complete Logs:
> [Old Log](workspace/old/sudoku_game/log.txt)

> [New Log](workspace/new/sudoku_game/log.txt)


The shared image for the OpenAI usage is not the total usage. I also used someone else API and the total is less than $10.