# robot-framework-listener

### Description
	This listener sends report-mail on your email address after each test

### How to run:
	1. Add in mail_config.ini file addresses:
		1. sender username
		2. sender password
		3. receiver username
	2. Run
		> sudo pip install --user poetry
		> poetry install
		> poetry shell
		> robot --listener EmailSenderListener.py --outputdir ./results QuickStart.rst


#### Email Report format:
	Suite - "suite name" 
	Test name - "Test name" 
	Start time - 03/17/2020, 18:06:29
	End time - 03/17/2020, 18:06:29 
	Result - "test status"
	Error - "if result was FAIL" 
