<?php
Class Add{
      var $modal;     // <---- var define or not define dosent metter
	function get_data(){  
		echo "modal number : $this->model<br>";
	}
}
$plus=new add;
$plus->model="dilshad";
$plus->get_data();

$lg = new  add;
$lg->model="khan";
$lg->get_data();


echo "<br><Br><br><Br>";



class mobile{
	var $model; //global valiable;
	function showmodel($number){
		global $model;
		$model=$number;
		echo "modal number : $model<br>";
	}

}
$samsung=new mobile;
$samsung->showmodel("M31s");
$lg = new mobile;
$lg-> showmodel("LG81");
echo "<br><Br><Br><br><Br>";







class mobiles{
	var $model; //global valiable;
	function showmodel($number){
		$this->model=$number;
		echo "modal number :$this->model<br>";
	}
}
$samsung=new mobiles;
$samsung->showmodel("M31s");
$lg = new mobiles;
$lg-> showmodel("LG81");
echo "<br><Br><Br><br><Br>";











 
?>