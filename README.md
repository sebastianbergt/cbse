# Code Based Systems Engineering

Lightweight code centric library for requirements definition and tracebility.

## Intro

Automotive and other safety critical development force engineers to have solid requirements and keep their software code in sync with those documents. A myriad of tools exist to solve this problem, but the moment two or more work products exist it is hard to keep them in sync.

One could trace to individual lines of code. In practice more than one line is usually needed to achieve a specified functionality. This is why tracing to a function is considered enough granularity. Good practice teaches us to keep our functions small anyway.

The language traced to is expected to be C or C++ for now.

## Goals
1. Define Requirements with Code

Both should be kept in the same repo, so they can never get out of sync.

2. Achieve Traceability

Requirements are typically traced to software units.

2. Force Review on code changes

This is solved by hashing a given function (ignoring its whitespaces) and comparing the result to earlier hashes. Running the requirements document with python3 (e.g. in CI/CD) will now produce warnings

3. Produce a .pdf document as an artifact

Currently this is a super simplified table export.

# Get the code and install requirements

git clone git@github.com:sebastianbergt/cbse.git

pip3 install -r reqs/cbse/requirements.txt 

# Usage

python3 reqs/module1_requirements.py

The file module1_requirements.py is a tiny example which shows you how to create requirements and trace them to code.
The program will issue warnings on untraced requirements. If you change the code of the linked function (src/module1.cpp isValueEven ) it will warn you about the changed code hash and you need to manually replace it with the one provided to acknowledge everything is still has intended.