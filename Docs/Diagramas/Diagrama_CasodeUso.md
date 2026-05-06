**Caso de Uso **
Caso de Uso: Registrar Público da Sessão

1. Descrição:
Permite que o Funcionário registre a quantidade de pessoas que compareceram a uma sessão de cinema já realizada, para fins de estatística e totalização.

2. Atores:
Funcionário / Administrador (Principal)

3. Pré-condições:
A sessão deve ter sido previamente agendada no sistema.
O horário de início da sessão já deve ter passado.

4. Fluxo Principal (O caminho feliz):
- O Funcionário acessa a opção "Registrar Público".
- O sistema exibe uma lista das sessões do dia.
- O Funcionário seleciona a sessão desejada.
- O sistema solicita a quantidade de público presente.
- O Funcionário insere o número de pessoas.
- O sistema valida se o número é menor ou igual à capacidade da sala.
- O sistema salva a informação e confirma o registro.
- O Caso de Uso termina.

5. Fluxo Alternativo:
Capacidade Excedida: Se no passo 5 o funcionário digitar um número maior que a capacidade da sala, o sistema exibe uma mensagem de erro: "Público excede a capacidade máxima da sala" e retorna ao passo 4.


**Diagrama do Caso**
<img width="496" height="396" alt="image" src="https://github.com/user-attachments/assets/ccccf02a-1f95-4d3f-897f-004b9578ddfb" />

