<?php


abstract class bank{
    abstract function id_card($a);
    function test(){
        echo "<h2>welcome to bank</h2>";
    }
}

class sbi extends bank{
    function id_card($a){
        $this->a=$a;
        echo "please submit SBI ID card : ".$this->a."<br>";
    }
}


class hdfc extends bank {
    function id_card($a){
        $this->b=$a;
        echo "pleae submit HDFC ID card : ".$this->b;
    }
}

$sbi=new sbi;
$sbi->test();
$sbi->id_card(13);




$hdfc=new hdfc;
$hdfc->id_card(14);
$hdfc->test();
?>