fastAPI Demo (WIP)
-------------

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

- GET
- POST
- CRUD (Create, Read, Update, Delete)
- Type hints
- localhost/redoc
- localhost/docs

### Prerequisites

```bash
pip install fastapi
```

```bash
pip install uvicorn[standard]
```

### Overview

### Run

```bash
uvicorn main:app
```

If you made changes in your code --reload a the end of the command

```bash
uvicorn main:app --reload
```

By default, the port is 8000. To change port (to 4000, for example)

```bash
uvicorn main:app --port 4000
```

- go to localhost to check the get
- To stop the application press Ctrl+C in the terminal


### Get
### Post
### Put
### Delete
### Further reading:
- https://fastapi.tiangolo.com/
- https://pydantic-docs.helpmanual.io/