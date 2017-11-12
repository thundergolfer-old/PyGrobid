# PyGrobid [![Build Status](https://travis-ci.com/thundergolfer/PyGrobid.svg?token=yHGWQ42iK2BPk1FjaUMc&branch=master)](https://travis-ci.com/thundergolfer/PyGrobid) [![Code Climate](https://codeclimate.com/repos/58fb912ffa56d30291001e98/badges/daaf3216427e8db61d09/gpa.svg)](https://codeclimate.com/repos/58fb912ffa56d30291001e98/feed) [![Issue Count](https://codeclimate.com/repos/58fb912ffa56d30291001e98/badges/daaf3216427e8db61d09/issue_count.svg)](https://codeclimate.com/repos/58fb912ffa56d30291001e98/feed) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

-----

A Python wrapper for the Grobid scholarly information extraction library

-----

## Simple Demo

**Note**: For `pygrobid` to function the Java server must be started and running. `pygrobid` does not (yet) start Java side of things up itself. Currently it can be started from the root directory with:

```bash
cd pygrobid && mvn exec:exec -Pstart_grobid`
```

Then you can do:

```python
from pygrobid import Grobid, start_server

start_server()
g = Grobid()
g.process_references('some_pdf_file.pdf')
g.shutdown()
```

## About Grobid

**GROBID** (or Grobid) means **G**ene**R**ation Of **BI**bliographic **D**ata.

GROBID is a machine learning library for extracting, parsing and re-structuring raw documents such as PDF into structured TEI-encoded documents with a particular focus on technical and scientific publications. First developments started in 2008 as a hobby. In 2011 the tool has been made available in open source. Work on GROBID has been steady as side project since the beginning and is expected to continue until at least 2020 :)

**For a list of features and more information, see the [Kermitt2/Grobid repo](https://github.com/kermitt2/grobid).**

## Installation

#### Java Dependencies

These are required for running **Grobid**.

* Java 1.8+
* [Apache Maven](https://maven.apache.org/)

#### Package Installation

`pip install pygrobid && python -c 'import pygrobid; pygrobid.get_dependencies()'`

## License

This package is license under [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/), the same license as the base Java library.
