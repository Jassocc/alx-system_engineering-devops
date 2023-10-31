#!/usr/bin/env ruby
#parse and put work to stdout
puts ARGV[0].scan(/\[(from:|to:|flags:)(.*?)\]/).join(",")
