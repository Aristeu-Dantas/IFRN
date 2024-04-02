# Open Systems Administration Activity (ASA) - Web server implementation

# What to do:

Public repository on github (asa-web)
Dockerfile (Container image definition)
Custom HTML page
Container creation script (shell)
PPT presentation

# What to deliver:

Complete repository (Github)
Presentation (PDF)

# Commands to start the project:

The "./run.sh" command runs all other commands:

```./run.sh```

Other commands:

```echo "Creating images..."```
```docker build -t c01 -f c01/Dockerfile c01/```
```docker build -t c02 -f c02/Dockerfile c02/```
```docker build -t c03 -f c03/Dockerfile c03/```

```docker build -t proxy -f Dockerfile.proxy .```
```docker image ls```

```echo "Creating the network..."```
```docker network create -d bridge asa-net```

```echo "Creating containers..."```
```docker run -dp 8001:80 --name c01 c01```
```docker run -dp 8002:80 --name c02 c02```
```docker run -dp 8003:80 --name c03 c03```
