<?php 

class addition{
      var $a;
      var $b;   //can remove var $a, var $b program will be run
	function __construct($x,$y){
            $this->a=$x;
		    $this->b=$y;
	}

	function display(){
	      $c=$this->a+$this->b;
		  echo $c."<br>";
	}

	function __destruct(){  //objec ke scop  ko khtm karne ke lie distructor use karte hai
		echo "object distoryed<br>";
	}
}
$add=new addition(13,12);
$add->display();
echo "<br><Br><Br><br><Br>";









class add{
      var $a;
      var $b;
	function __construct($x,$y){
        $this->a=$x;
		$this->b=$y;
		$c=$this->a+$this->b;
		echo $c."<br>";
	}
	function __destruct(){
		echo "object distoryed";
	}
}
$add=new add(12,12);

?>