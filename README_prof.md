# Sistema Para Biblioteca
## _Grupo 1: Nayra Kaline, Pedro Baleeiro e Matheus Paladini_

O sistema para a Biblioteca consiste do gerenciamento dos empréstimos de obras literárias, bem como da devolução dessas obras.

Abaixo, o diagrama de classes do sistema:
![](https://user-images.githubusercontent.com/72228482/192165050-70cc90ca-fe5f-44bc-8703-54f25fcebe75.png)

## Detalhes técnicos
| Item | Ferramenta |
| ------ | ------ |
| Linguagem | Python |
| Banco de Dados | Arquivo de Texto |
| API | Flask + Werkzeug + Gunircorn |

## Arquitetura
Utilizamos o conceito de clean architecture no nosso sistema, o que transparece em nossa separação de pacotes:
1. **Casos de Uso**
Camada responsável por implentar as regras de negócio específicas desse sistema. Disponível em ```.pooa/casos_de_uso```
2. **Entidades**
O conceito principal é de que esta camada deve conter tudo que seja pertinente ao sistema em relação a lógica de negócios, de modo mais genérico possível, ou seja, que tenham menor probabilidade de alterações quando houverem mudanças externas. 
Disponível em ```.pooa/entidades```
3. **Controladores**
Esta camada tem como responsabilidade, realizar a conversão dos dados, de modo que seja mais acessível e conveniente possível, para as camadas de Entidades e Casos de Uso.
Disponível em ```.pooa/controladores```
## Execução
Para rodar o código, primeiro clone o repositório na sua máquina por meio do terminal com o comando ```git clone https://github.com/nyrkln/POOA-Trabalho.git```
ou por meio de outro aplicativo como Github Desktop. Após isso abra o projeto na sua máquina com o python3 instalado.
A partir disso vá no arquivo execucao.py, descomente os trechos de código comentados que tem interesse de rodar, salve e digite ```python3 execucao.py``` no terminal para rodar.

## Integrações
####  Com outros projetos
- **Grupos Acadêmicos** 
Para verificar a participação de certo aluno em um Grupo Acadêmico, basta acessar **https://api-grupo7.herokuapp.com/api/v1/grupoAcademico/buscarRA/791085** com o RA do aluno, que lhe será retornado todos os detalhes do grupo.
- **Disciplinas**
Para verificar se o servidor está funcionando, primeiro acesse **https://inscricaodisciplinas.herokuapp.com/**. Para verificar a quantidade de disciplinas de determinado aluno, vá em **https://inscricaodisciplinas.herokuapp.com/aluno/[ID]/disciplinas** substituindo ID por **3fa85f64-5717-4562-b3fc-2c963f66afa6** ou **03dec7a5-9b4e-4d73-a87f-c00ff03d71b7**.

#### Com o nosso projeto
É possível **retornar todas as obras em nosso banco**, **https://rest-api-projeto-pooa-grupo1.herokuapp.com/obras**, e **também checar um CPF por pendências**, **https://rest-api-projeto-pooa-grupo1.herokuapp.com/situacao?cpf=[CPF]**, substituindo [CPF] por 41905743840, 41905743842 (sem pendências) ou 41905743844 e 41905743846 (com pendências).
