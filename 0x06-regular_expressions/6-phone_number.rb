#!/usr/bin/env ruby
#must match a 10 digit number
puts ARGV[0].scan(/^[0-9]{10}$/).join
