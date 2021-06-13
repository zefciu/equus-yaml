import typing
import io

import yaml
from yaml.scanner import ScannerError

def _load_input(input_: io.TextIOBase) -> dict[str, typing.Any]:
    try:
        return yaml.load(input_)
    except ScannerError:
        raise TypeError('Not a valid yaml')

def yaml_loader(input_: typing.Any) -> dict[str, typing.Any]:
    if isinstance(input_, str):
        with open(input_) as f:
            return _load_input(f)
    elif isinstance(input_, io.TextIOBase):
        return _load_input(input_)
    else:
        raise TypeError('Input unrecognized')
