# Java-One-Line
This is a small tool which condenses all of the \t's and the \n's from your regular .java file into "" so that it saves on space. This is for two reasons. The first being that not everyone has as much space on their laptop/pc and would like to make the most of their storage. Secondly, with bigger projects there are too many unnecessary bytes being used, for the average java user this is fine, but should you want to make an application for other to download one of your goals would be to make it as small as possible


This is currently just for linux, sorry windows and mac

To use you want to open terminal "cd" into the direcotry which you installed this file then you will want to type the following command

```sh 
python3 one_line.py {path to your java file}
```

What this will do is create a new file called new_{old file name}.java, it will also change the public class declaration to the new file, this way you can compile without new errors

Enjoy, pls send issues if found
