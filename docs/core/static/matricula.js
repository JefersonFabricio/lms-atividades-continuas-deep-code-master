function validacaoMatricula() {
    var linhas = document.getElementsByClassName("linha");

    for(var i = 1; i < linhas.length; i++) {
        var radio = document.getElementsByName("selecao" + i)
        
        if (!(radio[0].checked || radio[1].checked)) {
            alert('É necessário informar se aluno foi aprovado ou reprovado. Um ou mais alunos não foram informados');
            return false;
        }
    }

    var aprovados = document.getElementsByClassName("InputAprovado");
    var i;
    var total_aprovados = 0;

    for (i = 0; i < aprovados.length; i++) {
      if (aprovados[i].checked){
        total_aprovados=total_aprovados+1
      }
    }

    if (total_aprovados<20){
      alert('aprovados precisa ter no minino 20 alunos')
      return false
    }
    
    else{
        if (total_aprovados>60){
          alert('aprovados ultrapassou limite de 60 alunos')
          return false
        }
    }
    

    var enviar=document.getElementById("enviar");
    var valor, contA=0, ContR=0;
    
    valor = document.getElementsByTagName('input');
    for (var i=0;i < valor.length;i++){
        if(valor[i].checked ==  true){
            if(valor[i].value == "aprovado") { 
                contA++;
            }
            else {
                ContR++;
            }
        }
            
    } 

    alert("quantidade de aprovados "+contA+"\nquantidade de Reprovados "+ContR);
    frm.submit();
}
