import logging
import os
import random
import string
import subprocess

import pytest

from ansible_bender.builders.buildah_builder import buildah
from ansible_bender.utils import set_logging


set_logging(level=logging.DEBUG)


tests_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(tests_dir)
data_dir = os.path.abspath(os.path.join(tests_dir, "data"))
buildah_inspect_data_path = os.path.join(data_dir, "buildah_inspect.json")
basic_playbook_path = os.path.join(data_dir, "basic_playbook.yaml")
multiplay_path = os.path.join(data_dir, "multiplay.yaml")
non_ex_pb = os.path.join(data_dir, "non_ex_pb.yaml")
b_p_w_vars_path = os.path.join(data_dir, "b_p_w_vars.yaml")
p_w_vars_files_path = os.path.join(data_dir, "p_w_vars_files.yaml")
full_conf_pb_path = os.path.join(data_dir, "full_conf_pb.yaml")
basic_playbook_path_w_bv = os.path.join(data_dir, "basic_playbook_with_volume.yaml")
dont_cache_playbook_path_pre = os.path.join(data_dir, "dont_cache_playbook_pre.yaml")
dont_cache_playbook_path = os.path.join(data_dir, "dont_cache_playbook.yaml")
small_basic_playbook_path = os.path.join(data_dir, "small_basic_playbook.yaml")
change_layering_playbook = os.path.join(data_dir, "change_layering.yaml")
bad_playbook_path = os.path.join(data_dir, "bad_playbook.yaml")
base_image = "docker.io/library/python:3-alpine"


def random_word(length):
    # https://stackoverflow.com/a/2030081/909579
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
