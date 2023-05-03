# SDR lab portal

## Requirements

1. Docker environment
2. The jupyter notebook service is running on the host machine with port 8888.

## Jupyter notebook setup

1. Locate the Jupyter configuration directory: You can find the Jupyter configuration directory by running the following command:

```bash
jupyter --config-dir
```

This will output the path to the configuration directory, which typically is ~/.jupyter for the current user. 2. Create or modify the jupyter_notebook_config.py file: In the configuration directory, look for a file named jupyter_notebook_config.py. If the file doesn't exist, create it. 3. Open the jupyter_notebook_config.py file with your favorite text editor and add or modify the following lines:

```python
c.NotebookApp.allow_origin = '*'
c.NotebookApp.base_url = '/notebook/'
```

4. Restart the Jupyter Notebook server.
5. Modify token file

## How to use it

1. Download this repo and go to the path in terminal.
2. Run the following command:

```bash
docker-compose up -d --build nginx
```

## How to manage the service

1. Modify token when restart jupyter notebook service.
2. Edit `members.json` directly for adding/editing/deleting member.
