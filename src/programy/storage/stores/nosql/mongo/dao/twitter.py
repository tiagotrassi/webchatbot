"""
Copyright (c) 2016-2019 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from programy.storage.stores.utils import DAOUtils


class Twitter(object):

    def __init__(self, last_direct_message_id, last_status_id):
        self.id = None
        self.last_direct_message_id = last_direct_message_id
        self.last_status_id = last_status_id

    def __repr__(self):
        return "<Twitter(id='%s', last_direct_message_id='%s', last_status_id='%s')>" % \
               (DAOUtils.valid_id(self.id), self.last_direct_message_id, self.last_status_id)

    def to_document(self):
        document = {"last_direct_message_id": self.last_direct_message_id,
                    "last_status_id": self.last_status_id}
        if self.id is not None:
            document['_id'] = self.id
        return document

    @staticmethod
    def from_document(data):
        lookup = Twitter(None, None)
        if '_id' in data:
            lookup.id = data['_id']
        if 'last_direct_message_id' in data:
            lookup.last_direct_message_id = data['last_direct_message_id']
        if 'last_status_id' in data:
            lookup.last_status_id = data['last_status_id']
        return lookup