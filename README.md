# MonoRepo Demo

## Usage

- Do a change, for instance: change the backend.
- Commit
- `bin/build` will now ONLY build the backend
- `docker-compose up` will now deploy versions as in versions.json/.env

### Cleanup docker images

```shell
docker rmi $(docker images | grep demo | awk '{print $1":"$2}')
```
