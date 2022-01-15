<?php

//interface can only one  contain abstract function without body .
//Abstract function must deaclear but not implement
//in interface we cannot define  varibale
//in interface no constructor 
//All function must be public.
//interface support multiple inheritance

//way1
interface class1{
  function test();
}
class class2 implements class1{
   function test(){
       echo "hello interface";
   }
}

$inter=new class2;
$inter->test();
echo"<br><br><br>";





//suppot multiple inheritance
interface class11{
    function test1();
  }
  
  interface class12{
   function test2 ();
  }
  class class13 implements class11,class12{
     function test1(){
         echo "hello interface 1<br>";
     }
     function test2(){
      echo "hello interface 2";
     }
  }
  
  $inter=new class13;
  $inter->test1();
  $inter->test2();
?>