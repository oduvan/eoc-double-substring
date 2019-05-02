from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "double_substring"
    FUNCTION_NAMES = {
        "python_3": "double_substring",
        "js_node": "doubleSubstring"
    }
    ENV_COVERCODE = {
        
    }