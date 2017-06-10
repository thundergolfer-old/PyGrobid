## Developer Notes

**If you get a java.net.BindException**

  * Find what's on the port with `sudo lsof -i :<PORT NUMBER>` (default for `py4j` is `25333`)
* Remove that process by its `PID number` with `sudo kill -9 <PID>`

#### Run it from command line

From within `Pygrobid/pygrobid` run:

`mvn exec:exec -Pprocess_header_bibtex` (yeah yeah, will change the process name later)

The above starts the Java server, which is essential because Py4J will not start it itself.
From there you should be able to just use the python library like:

```
from pygrobid import grobid
g = Grobid()
g.process_references('mypdffile.pdf')
```
