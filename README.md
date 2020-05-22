# tetris
Os intuítos da criação desse jogo são:

- Construir um jogo completo, pois já havia criado outros esboços de jogos;
- Enteder os algoritmos e desafios enfrentados pela industria de jogos em seus primórdios,
o quais são bastante interessantes e me deixam realmente facinado;
- Aprimorar meus conhecimentos em Python;
- Aprimorar meus conhecimentos em criação de jogos;
- Aprimorar meus conecimentos em paradigma de programação orientada a objetos.

Observações para git clone:

- Versão do Python=3.7.3
- O projeto está sendo criado e testado em ambiente virtual "virtualenv"
- As dependências do projeto podem ser encontradas em requiriments.txt;
- Para facilitar a instalação das dependências, no terminal digite
    "pip install -r requirements.txt" ou "pip3 install -r requirements.txt";
- O diretório documentação contém modelos e diagramas criados para melhor entendimento
na construção do projeto.

Escopo:

    Cronstrução do jogo Tetris, criado por Alexey Pajitnov, Dmitry Pavlovsky e Vadim Gerasimov
e popular nas décadas de 80 e 90, utilizando Python como linguagem de programação, a biblioteca 
Pygame e paradigma orientado a objetos.

Domínio:

    A estrutura do projeto está didividida em 3 Cenas controladas por uma instância da classe
Game, a qual ficará responsável pela interação intaração destas e de objetos para uso geral.

Cena de Apresentação:
    Essa cena simplesmente executará uma apresentação do jogo com o logo que ainda definirei
e direcionará para "Cena de Menu".

Cena de Menu:
    Aqui, o jogo poderá navegar pelo menu do jogo, onde a princípio, estará disponível as opções:
"Jogar", "Recorde" e "Sair";
- Jogar: Caso o jogador escolha essa opção, ele será direcionado a "Cena Principal";
- Record: Caso o jogador escolha essa opção, uma superfície irá sobrepor parcialmente a
"Cena de Menu", apresentando as 10 melhores pontuações já feitas no jogo e seus donos;
- Sair: Aqui, o jogo será encerrado, fechando a janela e o interpretador do Python.

    Das interações presentes na Cena de Menu:
- Seta para baixo: Posiciona cursor seletor na opção abaixo da atual, caso não haja, o curso é
popsicionado na primeira opção;
- Seta para cima: Posiciona cursor seletor na opção abcima da atual, caso não haja, o curso é
popsicionado na ultima opção;
- Enter: Seleciona opção qual o cursor está posicionado;

Cena Principal:

    O jogo propriamente dito, nessa cena haverá um quadro ocupando a esquerda e centro da tela,
onde as formas do tetris devem ser montadas com o objetivo de preencher uma linha para pontuar. 
Após a queda de algumas formas, o jogo irá acelerar gradativamente.
    A direita, estaram algumas informações para o jogador, como: A próxima peça a aparecer,
a pontuação e o nivel de velocidade.

    A interação com o jogador nessa cena pode ocorrer da seguinte forma:
- Seta para baixo: A forma atual que está em queda, acelerá a descida até colidir;
- Seta para esquerda: A forma atual se move um quadro para esquerda, limitada pela área do quadro;
- Seta para direita: A forma atual se move um quadro para direita, limitada pela área do quadro;
- Espaço: Gira o forma atual 90 graus no sentido horário;
- Esc: Pausa o jogo e uma superfície sobrepõe a cena com as opções "Jogar", "Reiniciar"
e "Voltar ao Menu":
    - Jogar: A surperfície desaparece e o jogador continua a jogar;
    - Reiniciar: A superfície desaparece e cena volta a seu estado inicial;
    - Voltar ao Menu: O jogador é direcionado a "Cena de Menu".

    Das interações quando o jogo está em pause:
- Seta para baixo: Posiciona cursor seletor na opção abaixo da atual, caso não haja, o curso é
popsicionado na primeira opção;
- Seta para cima: Posiciona cursor seletor na opção abcima da atual, caso não haja, o curso é
popsicionado na ultima opção;
- Enter: Seleciona opção qual o cursor está posicionado;
- Esc: A surperfície desaparece e o jogador continua a jogar.

Obs.: Em todas as cenas o jogador poderá clicar no X de fechar a janela. Dessa forma em qualquer
situação o a janela deverá fechar, assim como o interpretador python.