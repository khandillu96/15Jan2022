<?php




class Animal{
    function __construct($a,$b){
        $this->age=$a;
        $this->name=$b;
    }
    

    function eats(){
        echo $this->name." eats food<br>";
    }

}


class morphy extends Animal{
    function eats(){
        echo $this-> name." eats food | age is ".$this->age;
    }
}


// $animal=new Animal(23,"Dog");
// $animal->eats();


$animal=new morphy(23,"Dog");
$animal->eats();




?>