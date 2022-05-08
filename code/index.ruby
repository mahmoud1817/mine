name = "mahmoudd"
x = 10
y = Array("mahmoud,anas,yusef")
z = {"name1"=>"mahmoud","name2"=>"ans"}
# string + int =  error
x.to_s
x.class
x.object_id
name.upcase.downcase
name.length
name.strip()
name.include? "m"
name.index("m")
name[0,2]
name[0..6]
name[0...7]
sentence = "my name is #{name}"
puts "*" * 40
for i in 1..10 do
    puts "hey bro"
end
puts "*" * 40
while x<15 do
    puts "hey man"
    x+=1
end
y.each do |some|
    puts some + "///"
end
puts "*" * 40
print("enter the new name: ")
name2 = gets.chomp()
if name2 == "mahmoudd" then
    puts "my dear"
end
print('_____________')
5.times do |j|
    puts "hey 70da"
end

def thing(n="folan")
    puts("hey bro "+n)
end

thing()

case name2
when "mahmoud"
    puts "hey bro"
when "ans"
    puts "you r a man"
when "yusef"
    puts "you r a new bro"
else
    puts 'whatever'
end

File.open("C:/users/mahmoud/desktop/learn/ruby/code/thing.txt","r") do |myfile|
    puts myfile.read()
end

begin
    puts "insider"
rescue => exception
    puts exception
end