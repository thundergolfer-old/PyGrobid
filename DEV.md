## Developer Notes

### Current challenge

At the moment I need a way to get the massive Java dependencies downloaded after running
`pip install` because they are too big to put in the Python package.

Once I can get a script going that downloads them all, then I just have to do the following:

* Make sure it downloads them into the right place (`venv/lib/python3.X/site-packages/pygrobid/` most likely,
  where `venv` is just a virtualenv we're currently in)

* Make sure that this downloading can run during `pip` installation or make it run as part of a packaged script.

**If you get a java.net.BindException**

  * Find what's on the port with `sudo lsof -i :<PORT NUMBER>` (default for `py4j` is `25333`)
* Remove that process by its `PID number` with `sudo kill -9 <PID>`

#### Run it from command line

From within `Pygrobid/pygrobid` run:

`mvn exec:exec -Pstart_grobid`

The above starts the Java server, which is essential because Py4J will not start it itself.
From there you should be able to just use the python library like:

```
from pygrobid import grobid
g = Grobid()
g.process_references('mypdffile.pdf')
```
