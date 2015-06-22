#!/usr/bin/env python

from __future__ import absolute_import
from rct import configure, twt

def main():
    config = {k:v for k,v in configure.getkeys()}
    api = twt.api(config)

    query = raw_input("What do you want to tweet about?\n")
    res = twt.search(api, query)
    print("\n".join(twt.list_of_statuses_to_str(twt.filter_ats(res))))

if __name__ == "__main__":
    main()
