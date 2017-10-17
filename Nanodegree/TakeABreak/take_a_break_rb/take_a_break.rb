i = 3
time1 = Time.now
puts "This program started on " + time1.strftime("%A %B %d %H:%M:%S %Y")
while i > 0
  sleep(3)
  system("open 'http://www.google.com'")
  i -= 1
end


