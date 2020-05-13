# using submodules
To use the library in the submodule instead of the pypi one set variable:
```shell script
PYTHONPATH='./fortiosapi'
```
in python console
```python
os.environ['PYTHONPATH'] = './fortiosapi'
```
To correctly get the referenced submodules please use the --recursive option of git clone like this:
```bash
git clone https://github.com/fortinet-solutions-cse/fortiosapi-examples.git --recursive
```


pull
```
git pull --recurse-submodule
```