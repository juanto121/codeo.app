"""
todo:
	- Detect changes to files in directory
	- Run run tests with a standardized format from file given the change in file changed.
		- format:
			in:
			test case 1
			can be multiple lines
			out:
			output of testcase 1
			can be multiple lines
			in:
			test case 2
			out:
			output of test case 2
eg.
	0x78.py changed ->
	 triggers runner ->
	  runner reads/parses 0x78.test file ->
	   runner executes 0x78.py and writes output to 0x78.out ->
	    runner checks outputs match
"""