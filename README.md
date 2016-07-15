# ViewSource app

Sample of a full stack app running on Flask with Python 3.5, nginx as a reverse proxy, Docker, and VueJS.

# Requirements

* Docker (for ease of use; can work without it)
* Node.js

# Installation

* Copy `docker-compose.override.sample.yml` to `docker-compose.override.yml`
* Copy `api/viewsource/localconfig.sample.py` to `api/viewsource/localconfig.py`
* Add `viewsourceit.local` and `api.viewsourceit.local` host to `/etc/hosts` pointing to wherever port 80 to your docker host is (most-likely 127.0.0.1)
* Run `npm install` in `front-end`
* Run `docker-compose up`

# License

Code may not be used or distributed for commercial purposes and may only be run on your computer in a fashion where the code is not publicly accessible to the Internet. Please view `LICENSE`.