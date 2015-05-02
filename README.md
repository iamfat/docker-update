# docker-update

It is a helper to generate commands you need to upgrade your docker containers.
I just print out all commands instead of run them, so that you could modify them later on.

```bash
# update my_container
docker-update my_container

# update running containers
docker-update

# update all containers
docker-update -a

# run it if you want
`docker-update`
```