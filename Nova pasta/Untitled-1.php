<?php

class Conexao {

    private $host; 
    private $dbname; 
    private $user; 
    private $password;
    private $pdo; 

public function create(){
    // Gera um código único
    $codigo = rand(10000, 99999) . date("Y");
    
    // Recupera os dados do formulário
    $nome = $_REQUEST["txtnome"];
    $senha = $_REQUEST["txtsenha"];
    $idade = $_REQUEST["txtidade"];
  
}
}

$situacao = Conexao();
situacao.create();
?>