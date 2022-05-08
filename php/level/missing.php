<?php
function missed($thing){
    $al   = 'abcdefghijklmnopqrstuvwxyz';
    $some = strpos($al,$thing[0]);
    for ($i = 0; $i<strlen($thing);$i++){
        if($thing[$i] !== $al[$some+1]){
            return "this is it :".$al[$some+1];
        }
    }

}

echo missed('acd');