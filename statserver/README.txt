This sockets server runs in a Docker.  For the localhost version, see /sockets/ directory

Docker container -

Build command is:
docker build -t spelling_bee_stat_server .

Run command is:
docker run --rm -p 6400:6400 spelling_bee_stat_server