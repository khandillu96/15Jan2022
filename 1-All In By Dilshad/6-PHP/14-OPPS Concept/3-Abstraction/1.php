<?php

// Abstract class contain Atleast one abstract funtion 
//Abstract function must deaclear but not implement
//Abstract class could not creat object
//Abstract class,child must contain abstract function



//suppose perent class ka 1 function use karna hai child class me toh parent class ko abstract class banado.
abstract class class1{
    abstract function test1();
}

class class2 extends class1{
    function test1(){
        echo "test 1";
    }
}

$abs=new class2;
$abs->test1();
?>