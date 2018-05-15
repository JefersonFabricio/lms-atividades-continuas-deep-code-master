function vazio(id) {
    var input = document.getElementById(id);
    if (input.value == "")
        return true;
}

function validacaoNovoAluno() {
    if (vazio("n_login")
            || vazio("n_nomec")
            || vazio("n_email")
            || vazio("n_nasc")
            || vazio("n_cpf")
            || vazio("n_senha")
            || vazio("n_csenha"))
    {
        alert('É necessário preencher todos os campos');
        return false;
    }

    //Função de calculo da idade
      var birthDate =document.getElementById('n_nasc').value;
        
      var mdate = birthDate.toString();
      var yearThen = parseInt(mdate.substring(0,4), 10);
      var monthThen = parseInt(mdate.substring(5,7), 10);
      var dayThen = parseInt(mdate.substring(8,10), 10);
             
      var today = new Date();
      var birthday = new Date(yearThen, monthThen-1, dayThen);
      var differenceInMilisecond = today.valueOf() - birthday.valueOf();    
      var year_age = Math.floor(differenceInMilisecond / 31536000000);

      if (year_age<17){
            alert('Idade invalida')
            return false
      }
 
    senha = document.n_aluno.n_senha.value;
    senhaRepetida = document.n_aluno.n_csenha.value;
    if (senha != senhaRepetida){
        alert("Repita a senha corretamente");
        document.n_aluno.n_csenha.focus();		
          return false;
      }
      else if (senha.match(/[0-9]/g)== null){
          alert('deve conter no minimo um número!');
          return false;
     }
      else if (senha.match(/[a-z]/g)== null && senha.match(/[A-Z]/g)== null){
          alert('deve conter no minimo uma letra!');
          return false;
    frm.submit();
        }
}

function validaCPF(cpf)
{
  var numeros, digitos, soma, i, resultado, digitos_iguais;
  digitos_iguais = 1;
  if (cpf.length < 11)
        return false;        
  for (i = 0; i < cpf.length - 1; i++)
        if (cpf.charAt(i) != cpf.charAt(i + 1))
              {
              digitos_iguais = 0;
              break;
              }
  if (!digitos_iguais)
        {
        numeros = cpf.substring(0,9);
        digitos = cpf.substring(9);
        soma = 0;
        for (i = 10; i > 1; i--)
              soma += numeros.charAt(10 - i) * i;
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(0))
              return false;
        numeros = cpf.substring(0,10);
        soma = 0;
        for (i = 11; i > 1; i--)
              soma += numeros.charAt(11 - i) * i;
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(1))
              return false;
        return true;
        }
  else
      return false;
}

function confirmaCPF(cpf){
      if (!validaCPF(cpf))
      alert("cpf invalido")
    frm.submit();
}

  
    //
    // INSIRA O SEU CODIGO AQUI
    //       



