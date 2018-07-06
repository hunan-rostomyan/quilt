#!/usr/bin/env python3.6

import quilt

import const
import util


node1 = quilt.load(const.PKG, hash=const.HASH1)
node2 = quilt.load(const.PKG)  # latest

# Read jsonl
jsonl1 = node1.dump_json()
jsonl2 = node2.dump_json()

print(util.read_jsonl(jsonl1))
print(util.read_jsonl(jsonl2))

# Read text
text1 = node1.dump_txt()
text2 = node2.dump_txt()

print(util.read_text(text1))
print(util.read_text(text2))
