<?php
$name = "mahmoud";
Print substr($name,0,2)."\n" ;
var_dump($name);
getType ($name);
const job = "programmer";
define("name","anas",false);
echo __FILE__;
if ($name == "mahmoud"){
    echo "<br>"."yes bro";
} elseif($name == "anas"){
    echo "yes ans";
}
$name2 = "1";
$name2 .= $name;
$name3 = str_replace("mahmoud","anas",$name1);
$thing = var_export($name3);
print($name2);
define("myname","mahmoud");
const name2 = "anas";
if ($name2 = "anas"){
    echo "\n hey bro ";
} elseif ("name" == "yusef"){
    echo " hey me";
} else {
    echo " who r u man? \n";
}

switch($name2){
    case "mahmoud": echo "\nhey mahmoud \n";break;
    case "anas": echo "\nhey ans \n"; break;
    default: echo "anyway";
}

while($name2 == "mahmoud"){echo "sa7by";}
do {echo "sa7by";} while ($name2 == "mahmoud");

$a=array("mahmoud","anas","yusef");
foreach($a as $b){echo $b . "\n";}

// strlength() sizeof()

for($i=0;$i<count($a);$i++){echo $a[$i]."\n";}


$c=array("name1"=>"mahmoud","name2"=>"anas","name3"=>"yusef");
foreach( $c as $d => $e){echo $d ." is "."$e\n";}
echo date("\nm/y\n");
echo rand(1,10);

function myname($name10){return "\nhello ".$name10;}
echo myname("ali");


echo '================';


@(include 'folan') or die("what is this bro?");