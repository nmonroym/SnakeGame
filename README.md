# SnakeGame
Snake Game

Clone Repository

First get to the existing directory
$ cd my/folder/

Now start a new git repository
$ git init

Identify if the current elements on the directory are needed or not and add them to the .gitignore file. When ready...
$ vim .gitignore

When ready create the first commit on the server
$ git add .;git commit -m'my first commit'

Now add the remote from where you want to clone
$ git remote add origin https|ssh:path/to/the/repository.git

Now just pull and merge with local git
$ git pull origin master
