# 0x0F. Python - Object-relational mapping

## Overview

- **Language:** Python
- **Concepts:** Object-Oriented Programming (OOP), SQL, MySQL, Object Relational Mapping (ORM)
- **Library:** SQLAlchemy
- **Author:** Guillaume
- **Weight:** 1
- **Project Start:** Jan 11, 2024, 6:00 AM
- **Project End:** Jan 15, 2024, 6:00 AM
- **Checker Release:** Jan 12, 2024, 6:00 AM
- **Auto Review Deadline:** At the project deadline

## Before You Start

- Make sure your MySQL server is in version 8.0.
- [How to install MySQL 8.0 in Ubuntu 20.04](<link-to-installation-guide>)

## Background Context

In this project, the goal is to bridge the gap between Databases and Python using Object-Relational Mapping (ORM).

### Part 1 - MySQLdb

Connect to a MySQL database and execute SQL queries using the `MySQLdb` module.

Example without ORM:

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

# Resources

**Read or watch:**

- [Object-relational mappers](<link-to-orm-info>)
- [mysqlclient/MySQLdb documentation](<link-to-mysqldb-doc>)
- [MySQLdb tutorial](<link-to-mysqldb-tutorial>)
- [SQLAlchemy tutorial](<link-to-sqlalchemy-tutorial>)
- [Introduction to SQLAlchemy](<link-to-intro-to-sqlalchemy>)
- [Flask SQLAlchemy](<link-to-flask-sqlalchemy>)
- [10 common stumbling blocks for SQLAlchemy newbies](<link-to-sqlalchemy-stumbling-blocks>)
- [Python SQLAlchemy Cheatsheet](<link-to-sqlalchemy-cheatsheet>)
- [SQLAlchemy ORM Tutorial for Python Developers](<link-to-sqlalchemy-orm-tutorial>)

# Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

# Copyright - Plagiarism

- Solutions must be developed independently to meet learning objectives.
- Publishing project content is not allowed.
- Plagiarism is strictly forbidden and will result in removal from the program.

# Requirements

## General

- Editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- Executed with MySQLdb version 2.0.x
- Executed with SQLAlchemy version 1.4.x
- Files end with a new line
- First line of all files: `#!/usr/bin/python3`
- Mandatory README.md file at the project root
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- Length of files tested using `wc`
- All modules, classes, and functions must have documentation

