# Sort integer arguments (ascending)

result = []
ARGV.each do |arg|
    i_arg = arg.to_i

    # Only include valid integers
    result << i_arg if i_arg.to_s == arg
end

# Sort the integers in ascending order
result.sort!

# Print the sorted list
result.each { |num| puts num }

