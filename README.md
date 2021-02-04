# validadorCPF
Este projeto tem o objetivo de validar um ou vários CPF contendo dígitos numéricos ou não.

Para começar, devemos levar em consideração que para a validação de um CPF, devemos pegar
os 9 primeiros dígitos e multiplicar cada um por um número respectivo em uma escala decrescente a partir de 10.

Portanto, vamos supor:
CPF = ABC.DEF.GHI-JK
Então devemos realizar a seguinte operação:
A * 10
B * 9
C * 8
D * 7
E assim sucessivamente...

A partir daí somaremos o produto de cada multiplicação dessas.
e aplicaremos à seguinte expressão:
11 - (SOMA % 11) = RESULTADO

Se o RESULTADO for MAIOR QUE 9, o primeiro dígito após o hífen do CPF será zero.
Caso contrário, manterá o valor real do RESULTADO.
A partir daí repetiremos as multiplicações, mas dessa vez pegaremos o primeiro dígito após o hífen
e colocaremos ele nessa listagem de multiplicações, mas dessa vez começaremos com o 11

A * 11
B * 10
C * 9
...
J * 2

E repetiremos aquela mesma expressão 
11 - (SOMA % 11) = RESULTADO.
Dessa vez manteremos o RESULTADO, sem um passo extra de validação.

Neste projeto podemos receber valores com pontuação, sem pontuação, errado.
Em caso de um CPF correto, iremos exibí-lo conforme o formato padrão brasileiro ABC.DEF.GHI-JK
e ofereceremos a verificação de outro CPF.

Se o usuário disser qualquer palavra que contenha 'n' ou 'N', saíremos do loop.
Caso contrário o loop será executado novamente pedindo outro CPF.
O usuário também pode dizer 'sair' na hora de digitar o CPF.
