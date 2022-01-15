<?php


//with abstract
abstract class class1{
    abstract function draw();
}

class class2 extends class1{
    function draw(){
        echo "class 2 fun1 ";
    }
}

class class3 extends class1{
    function draw(){
        echo " class 3 fun2";
    }
}

$Shape=new class3;
$Shape->draw();
echo "<br><br><BR>";



//with Interface 
interface class11{
     function draw();
}

class class12 implements class11{
    function draw(){
        echo "class 12 fun11 ";
    }
}

class class13 implements class11{
    function draw(){
        echo " class 13 fun12";
    }
}

$Shapee=new class12;
$Shapee->draw();

?>