import io
from typing import List, Optional

from nose.tools import assert_equal, assert_is_none, assert_list_equal
from equus.configuration import Configuration

class Config(Configuration):
    required_str_param: str
    optional_str_param: Optional[str]
    default_str_param: str = 'bacon'
    required_int_param: int
    list_param: List[str]


CONFIGURATION_FULL_DATA = io.StringIO("""---
required_str_param: spam
required_int_param: 42
list_param: 
    - 'Galahad'
    - 'Robin'
    - 'Lancelot'
""")



def test_load_full_data():
    config = Config.load(CONFIGURATION_FULL_DATA)
    assert_equal(config.required_str_param, 'spam')
    assert_is_none(config.optional_str_param)
    assert_equal(config.default_str_param, 'bacon')
    assert_equal(config.required_int_param, 42)
    assert_list_equal(config.list_param, [
        'Galahad',
        'Robin',
        'Lancelot',
    ])
