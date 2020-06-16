

## Running Locally

```bash
git clone https://github.com/G0RD0NTHEGREAT/T2O.git
```
```
git checkout localserver
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver 0.0.0.0:8000
```

### Modification

Change the content of `run_remote_single.sh` and `run_remote_multi.sh` 

- `Demoindir`: change the directory to your own repo directory
- `demooutdir`: change the directory to your own repodirectory
- `bash /u/jshi31/project/T2ONet/demo/run_demo_FiveK.sh` change to your own repo directory

## Running Remotely
Follow the previous step, but do not checkout to localserver.
