program folan ; 
var name:string = 'mahmoud';
var name2:string;
var a:integer = 1;
var b:integer = 2;
var m:integer;
var v:integer;
var x:integer;
function both(v,x:integer): integer;
begin
writeln(v+x);
end;

// single not double quotation
begin
write('enter a name: ');
read(name2);
writeln('hey bro '+name2);
writeln('hey bro ',name2);

if a>b then
  writeln('^-^')
else
    writeln('have fun dear');

while a<b do
    a:=a+1;
    writeln('yes dear');

for m:= 1 to 10 do
begin
    writeln('atlast',m);
end;

both(3,4);

end.