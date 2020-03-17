# robot-framework-listener

### Description
	This listener send report-mail on your email address after each test

### How to run:
	> sudo pip install poetry
	> poetry shell
	> robot --listener EmailSenderListener.py --outputdir ./results QuickStart.rst


#### Email Report format:
	Suite - "suite name" 
	Test name - "Test name" 
	Start time - 03/17/2020, 18:06:29
	End time - 03/17/2020, 18:06:29 
	Result - "test status"
	Error - "if result was FAIL" 