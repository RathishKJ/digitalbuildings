# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""GUID generator runner."""
from __future__ import print_function

from typing import List
from guid_generator import guid_generator


def Generate(filenames: List[str]) -> None:
  """Runner method for GUID generation.

  Args:
    filenames: file paths for Building Coniguration instances.
  """
  generator = guid_generator.GuidGenerator()
  for filename in filenames:
    print(f'Generating GUIDs for {filename}')
    generator.GenerateGuids(filename)
