# Let's Practice TDD
Here i am going to practice TDD prgraming concept, by default it looks very simple but it needs a huge amount of **practice**

so i made the dirctory ``tests`` that contains the basic tests of all the programs i am gonna make, but first things first lets take a closer look at the concept of TDD. 
## What is TDD? 
It also known as Test Driven Devolopment, it is a software development approach that emphasizes writing automated tests before writing the actual code.

### The process typically goes as the following steps:
 1. **Write a test that fails**: we write a small test case for our program and it should fails so that we can start the next step.
 2. **Run that test:** we sould run the test to see it fails, **Why?**
 so that we can make sure that our program dosent pass that test case, otherwise it mean that our program is **not** beahving as we excpected, which leads us to think why did it passed..
 3. **Make the test pass:** now we start writing some code, we should write the necessary amount of code to make the test pass. our focus is on making the test case pass, rather than writing the complete implementation of the program.
4. **Refactor:** Once we make the test pass we foucs now on the design of the code, *what should make the design better?* while we do this we should make sure after each refactor that our tests still passes,  refactoring helps ensure that the code remains clean and manageable.
5. **Repeat:** Repeat each step of the above untill all of the test cases you have implemnted passed
## Cons of TDD
 ### It has several benefits including: 
 1. **Time consuming:**
 TDD can be time-consuming, especially for developers who are new to the practice. Writing tests before writing the actual code requires additional effort and can slow down the development process, particularly in the beginning. It may take more time upfront, but it can save time in the long run by reducing the likelihood of introducing bugs and facilitating easier maintenance.

2. **Learning curve:** TDD requires a mindset shift and a certain level of discipline. Developers need to learn how to write effective tests, understand the principles of TDD, and embrace the iterative development cycle. This learning curve can be challenging for those who are unfamiliar with the approach, and it may take time for teams to adapt and become proficient in TDD.

3. **Overemphasis on testing:** TDD's focus on testing can sometimes lead to an overemphasis on test coverage and quantity rather than focusing on the quality of the tests. Developers may be inclined to write tests that merely check implementation details rather than focusing on the desired behavior and functionality. This can result in brittle tests that are tightly coupled to the implementation, making it harder to refactor and maintain the codebase.

4. **Incomplete coverage:** While TDD encourages high test coverage, it doesn't guarantee complete coverage of all possible scenarios. Developers may inadvertently overlook certain edge cases or fail to consider all possible outcomes. Additional testing techniques, such as integration testing and exploratory testing, may be necessary to complement TDD and ensure comprehensive coverage.

5. **Maintenance overhead:** As the codebase grows and evolves, maintaining a large suite of tests can become challenging. Tests may need to be updated or rewritten to accommodate changes in requirements or modifications to the code. Without proper maintenance, tests can become outdated or even misleading, potentially resulting in false positives or false negatives.

6. **Design constraints:** TDD can influence the design of the codebase, sometimes leading to design decisions driven primarily by testability rather than overall system architecture. While this can result in more modular and loosely coupled code, it may also introduce unnecessary complexity if not carefully managed.
