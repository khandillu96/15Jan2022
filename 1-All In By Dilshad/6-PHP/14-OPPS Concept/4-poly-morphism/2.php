<?php



class shape{

    function draw(){
        echo "shape";
    }
}

class circle extends shape{
    function draw(){
        echo "circle";
    }
}

class rectangle extends circle{
    function draw(){
        echo "rectangle";
    }
}

$Shape=new rectangle;
$Shape->draw();


?>