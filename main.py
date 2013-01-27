#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import database

class MainHandler(database.webapp2.RequestHandler):
  def get(self):
    user = database.users.get_current_user()
    if user:
      logout_url = database.users.create_logout_url('/')
      template_values = {
        'user': user,
        'logout': logout_url
      }
      template = database.jinja_environment.get_template('index.html')
      self.response.out.write(template.render(template_values))
    else:
      self.redirect(database.users.create_login_url(self.request.uri))
    
app = database.webapp2.WSGIApplication([('/', MainHandler)], debug=True)