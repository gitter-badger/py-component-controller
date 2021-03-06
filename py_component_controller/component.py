# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from resource import Resource


class Component(Resource): 
  """
  :Description: Base for web components.
  :param webdriver: Webdriver instance to reference.
  :type webdriver: WebDriver
  :param env: Additional variables to be used in properties.
  :type env: dict
  """
  def __init__(self, **kwargs):
    super(Resource, self).__init__(self, **kwargs)
    self.__selectors = {}
    
  def register_elements(self, elements):
    self.__selectors.update(elements)
  
  def fetch(self, key):
    try:
      return self.browser.find_element_by_css_selector(self.__selectors.get(key))
    except Exception:
      return None
  
  meta = {'required_fields': ['webdriver', 'logger', 'env']}
