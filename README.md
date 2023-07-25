# Code Assist

### Phase 1
Building the LM that understands the code base. Will need to
investigate if it can be language agnostic. This will help answer
various questions about the code like:
* What a certain part of the code is doing
* What the edge case could be that we need to be aware of.

### Phase 2
With the help of GitHub integration, using the commit history, it can
tell us when a certain part of the code was added and why. It can 
also help with code reviews at every pull request as it can 
compare the previous and the new version of the code and explain 
the additions

### Phase 3
With the help of Rally integration and well written commit 
messages, the LLM can tell why a some code was added. Having the 
knowledge of user stories and acceptance criteria, as each commit 
will have a  story number and as the code snippets will have 
corresponding commits, the LLM could answer complex questions 
about what business requirements the code snippet is meant to handle/



# Research points
* Model
* What we can from GitHub (non Ford code)
* Once we have the code: actions to perform
  * Best practices
  * Test edge cases
  * secrets / vulnerabilities
  * PR comparison
    * What changed - explanation
    * Quality of change
* Functionality of fossa, 42Crunch, sonarqube, checkmarx to 
  provide a unified platform
* Displaying the results



# Talking Points
* Why Ford specific model? 
  * Dedicated to Ford Use and libraries
  * Security concerns
  * Can be trained on Ford Architectural Diagrams / Documentation??
  * 