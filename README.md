How to use
----------
You can simply run scpwatch with the follwing parameteres and it will send the file to the remote server if it is modified:

```
./scpwatch.py ./target/test.jar user@example.com
```

You may specify the path in which the file should be copied on the server as you do with scp command:

```
   ./scpwatch.py ./target/test.jar user@example.com:Downloads
```

License
---------
[The MIT License](http://opensource.org/licenses/MIT)
