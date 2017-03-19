## Developer Notes

**If you get a java.net.BindException**

* Find what's on the port with `sudo lsof -i :<PORT NUMBER>` (default for `py4j` is `25333`)
* Remove that process by its `PID number` with `sudo kill -9 <PID>`
