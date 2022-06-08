# LAB - Class 04
## Project: Pythonic Garage Band
### Author: Lama Radwan


### Links and Resources
**Setup**

- No PORT or DATABASE URL

**How to initialize/run your application (where applicable)**

- python ./band.py


**How to use your library (where applicable)**
- No Libraries

**Tests**
- How do you run tests? 

Navigate to each test file then run it either from the UI of the code editor or the terminal
- Any tests of note? 

No
- Describe any tests that you did not complete, skipped, etc

Actually, I still have 2 out of 16 test cases are failed, they are about resetting the Band instances.
Although there is a function to clean the instances with @pytest.fixture(autouse=True) before each test
but I'm not sure if it's working properly with my project