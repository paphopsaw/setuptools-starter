python -m build
rm -r calc.egg-info
mv dist/calc-1.0-py3-none-any.whl lambda
rm -r dist