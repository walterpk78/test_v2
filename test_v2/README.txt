===========
Python tasks V2
===========

Python tasks is a nice test provided by AGT to evaluate new candidates. You might find
it most useful for tasks involving handle files and searching for strings, a nice demo for creating task in a timely manner.
Typical usage
often looks like this::

    #!/usr/bin/env python

    Under __name__ == "__main__" see and example to run it

   There are two test created from methods merge_dictionaries_recursive and
    schedule_method_calls:

    from python_tasks_v2 import TestSchedule, TestMergeDictionaries

    TestMergeDictionaries().simple_test()
    TestSchedule().test_all()


(Note the double-colon and 4-space indent formatting above.)

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.

Installations notes:
copy package and run:
pip install pythonTask.tar.gz


Sections:
=========
Task 1: Problem solving:
        Complete missing functionality on methods marked with "TODO".
        Identify bugs in methods marked with "FIXME".
        Expected functionality is described in the method documentation.
Task 2: Architecture / code style:
        Refactor the existing code for readability, best practices, style, validation and documentation etc.
Task 3: Tests:
        Write some meaningful unit test(s) for the methods marked with "TEST MISSING"
Task 4: Ops:
        Reorganize files, directories and add setup information / scripts
        in order to the create a redistributable python package with some simple commands
        Provide an example script on the platform of your choice.
Rules:
======
Use Python 3.5 or above
- Avoid all platform specific code
  The code should run on either a recent Windows and/or common Linux distributions. Preferably all.
- You may use any built-in python library
- You may use third party libraries - if they fulfill these conditions:
- available at: https://pypi.python.org/pypi and open source
- well known and documented (use your judgement)
- pure python only (e.g. no compiled plugins written in C or FORTRAN)




Urls are https://www.dropbox.com/sh/7zkqzcmh3bbx13v/AAB0EuPwL_5-x0OrhJ9uez0oa?dl=0 and links can be
written `like this <https://www.dropbox.com/sh/7zkqzcmh3bbx13v/AAB0EuPwL_5-x0OrhJ9uez0oa?dl=0&preview=python_task_v2.zip>`_.
downloaded from https://www.dropbox.com/sh/7zkqzcmh3bbx13v/AAB0EuPwL_5-x0OrhJ9uez0oa?dl=0&preview=python_task_v2.zip

