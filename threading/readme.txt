When to use threading
------------------------
- when our task/code is I/O bound tasks 
- hence our code will run asyncrounously at the time of waiting/sleeping and IO
- still it will run linearly (only one stream of code execution)

- code will run linearly even during the time of I/O operation and wait/sleep


When to use concurrency
--------------------------
- when our task/code is processor/CPU bound tasks
- multiple streams of code execution 