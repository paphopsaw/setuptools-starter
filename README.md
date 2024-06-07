```
script/build.sh
python -m venv env
source env/bin/activate
pip install build numpy
./script/build.sh
pip install exported_lib/calc-1.0-py3-none-any.whl
python
>>> import calc
>>> calc.run_function()
```
