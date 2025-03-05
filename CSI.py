import os
import time
import sys
import random
import pathlib
import subprocess
import sys 
import time 


def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_carregamento(mensagem):
    """Cria uma animação simples de carregamento"""
    for i in range(4):
        sys.stdout.write(f"\r{mensagem}" + "." * (i + 1))
        sys.stdout.flush()
        time.sleep(1.5)
    print()
    
def efeito_digitacao(texto, velocidade=0.05):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def introducao():
    """
    Introdução dramática do desafio
    """
    limpar_tela()
    print("-" * 80)
    print("BEM - VINDO AO CASO DE CSI".center(80))
    print("-" * 80)
    
    print("=" * 80)
    texto_intro = (
        "\nVocê é um detetive e precisa capturar um assassino em série antes que ele faça sua próxima vítima.\n"
        "Para começar, vamos aprender um pouco sobre nosso assassino. Ele é um psicopata narcisista,"
        "traumatizado, e possui um complexo de salvador.\n"
        
        "Na infância, ele foi brutalmente maltratado por sua mãe. No entanto, o que mais lhe despertava ódio não eram as surras,\ntorturas, maus-tratos ou desprezo."
        "\nO que realmente o revoltava eram os elogios que sua mãe recebia. Isso o fazia perceber como as pessoas ignoravam detalhes importantes."
        
        
        "\nTodos sempre elogiavam a aparência dela como se apenas isso importasse: 'Que cabelos morenos,"
        "\nlisos e sedosos os seus!', 'Que pele morena reluzente!', 'Que olhos castanhos lindos!','Nossa, nem parece ter quase trinta anos!'"
        "\nMas, dentre todos os elogios, o que mais o incomodava eram os direcionados aos olhos. Enquanto todos viam beleza, ele enxergava raiva, maldade e terror."
        
        "\nNosso assassino chegou à conclusão de que mulheres como sua mãe jamais deveriam ter filhos, pois nenhuma criança mereceria tal condenação."
        "\nE, ao chegar a essa conclusão, ele começou sua jornada de crimes."
        
        "\nAgora, voltamos a você. Neste exato momento, você está diante de um notebook com um pendrive conectado. Na tela, há uma mensagem escrita:"
    )
    efeito_digitacao(texto_intro, velocidade=0.05)
    input("\nPressione ENTER para continuar...")
    

def obter_diretorio_base():
    """
    Obtém o diretório base onde o script está localizado.
    """
    if getattr(sys, 'frozen', False):  # Executável criado (PyInstaller)
        return pathlib.Path(sys.executable).parent
    else:  # Script sendo executado diretamente
        return pathlib.Path(__file__).parent

def abrir_pasta(diretorio):
    """
    Abre a pasta no gerenciador de arquivos.
    """
    if os.name == 'nt':  # Windows
        os.startfile(diretorio)
    elif os.name == 'posix':  # macOS/Linux
        subprocess.Popen(['open', diretorio])

def primeira_charada():
    """
    Primeira fase do desafio - Charada do fogo
    """
    limpar_tela()
    print("--- PRIMEIRA CHARADA ---")
    texto_intro = (
        "Uma Charada, três chances, 4 letras."
        "\nCharada: Dei-me comida e viverei, dei-me água e morrerei\n"
    )
    efeito_digitacao(texto_intro, velocidade=0.05)
    
    tentativas = 3
    while tentativas > 0:
        resposta = input(f"Tentativa {4 - tentativas}. Qual é a resposta? ").lower().strip()
        
        if resposta == "fogo":
            animacao_carregamento("Descriptografando")
            print("\n✅ Descriptografado! Você achou que seria tão fácil?")
            input("\nPressione ENTER para continuar...")
            return True
        
        tentativas -= 1
        print(f"❌ Resposta incorreta. Você tem mais {tentativas} tentativas.")
    
    print("\n❌ GAME OVER: O conteúdo do pen drive foi deletado.")
    input("\nPressione ENTER para sair...")
    return False

def segunda_charada():
    """
    Segunda fase do desafio - Charada do filho com pasta no pen drive.
    """
    limpar_tela()
    print("--- SEGUNDA CHARADA ---")
    texto_intro = (
        "Charada: Nasci sendo e morrerei sendo. O que eu sou?\n"
        "26 possibilidades de começar, 26 chances de errar....\n"
        "-Ao virar a sexta página, você verá o começo de algo.\n"
        "-Um salto ao nono galho da árvore revelará um fragmento perdido.\n"
        "-A décima segunda estrela brilha com uma pista valiosa, mas só os atentos a perceberão.\n"
        "-Antes que o ciclo se complete, o oitavo som do vento sussurrará um segredo.\n"
        "-E finalmente, contemple o décimo quinto raio de sol ao amanhecer, onde tudo se alinhará.\n"
        
    )
    efeito_digitacao(texto_intro, velocidade=0.05)
    
    # Diretório base onde o script está localizado
    base_dir = obter_diretorio_base()
    
    # Caminho da pasta para o código
    pasta_codigo = base_dir / "codigo_segunda_charada"
    if not os.path.exists(pasta_codigo):
        os.makedirs(pasta_codigo)
    
    print(f"A pasta foi criada/aberta em: {pasta_codigo}")
        
    # Tenta abrir a pasta automaticamente
    abrir_pasta(pasta_codigo)
    
    tentativas = 2
    while tentativas > 0:
        resposta = input(f"Tentativa {3 - tentativas}. Qual é a resposta? ").lower().strip()
        
        if resposta == "filho":
            animacao_carregamento("Descriptografando")
            texto_intro = (
                "Meus parabéns, pegue-me se for capaz."
            )
            efeito_digitacao(texto_intro, velocidade=0.5)
            mostrar_arquivos_confidenciais()
            return True
        
        tentativas -= 1
        print(f"❌ Resposta incorreta. Você tem mais {tentativas} tentativas.")
    
    print("\n❌ GAME OVER: O conteúdo do pen drive foi deletado.")
    input("\nPressione ENTER para sair...")
    return False

def mostrar_contexto_meio():
    limpar_tela()
    print("--- HISTÓRIA POR TRÁS DO PEN DRIVE ---")
    texto_intro = (
        "Pera aí, pulei uma parte. Afinal, como você conseguiu o pendrive? Vou relembrá-lo, caso tenha esquecido:\numa mulher ensanguentada chegou à porta da delegacia com ele embrulhado como se fosse um presente.\n"
        "\nEra uma sobrevivente que escapou? Não. Apenas uma vítima que ele decidiu deixar ir. Ainda não sabemos o porquê,\nmas sabemos que ele queria jogar com você. Ao libertá-la, decidiu enviar um 'presentinho'.\n"
        "\nEla o descreveu como um maníaco, louco, lunático. Ele a torturou e machucou incessantemente, a tal ponto que, grávida, perdeu o bebê.\nQuando ela achou que finalmente morreria, ele simplesmente parou.\n"
        "\nEla relata:\nÉ como se, para ele, por algum motivo, tivesse perdido a graça me fazer sofrer."
    )
    efeito_digitacao(texto_intro, velocidade=0.05)
    
    

def mostrar_arquivos_confidenciais():
    """
    Mostra os arquivos confidenciais e espaço para imagens
    """
    limpar_tela()
    print("--- ARQUIVOS CONFIDENCIAIS DESBLOQUEADOS ---")
    animacao_carregamento("Abrindo pasta")
    
    # Cria a pasta de imagens das vítimas
    base_dir = obter_diretorio_base()
    pasta_imagens = base_dir / "imagens_vitimas"
    if not os.path.exists(pasta_imagens):
        os.makedirs(pasta_imagens)
    
    print("\n[RELATÓRIO CONFIDENCIAL]") 
    print("=" * 50)
    print("CASO: Série de Assassinatos")
    print("STATUS: EVIDÊNCIAS ENCONTRADAS")
    print("=" * 50)
    
    print("\nFOTOS DAS VÍTIMAS:")
    print(f"* Diretório para imagens criado: {pasta_imagens}")
    texto_intro = (
        "-Vítima N°1 = Uma linda garota na faixa dos 23 anos cabelos morenos cacheados lindos,\nbelíssimos olhos castanhos, pele morena, mãe de um garoto de 2 anos."
        "\n-Vítima N°2 = Pele morena, aparenta uns 28 anos, lindos cabelos morenos e lisos,\nolhos castanhos lindos, porém sem filhos, seu filho está na barriga ainda com somente 3 meses de gestação."
        "\n-Vítima N°3 = Pele morena, cabelos lisos sedosos e morenos, aproximadamente 30 anos,\nolhos castanhos lindos, mãe de 2 crianças, uma de 6 meses e outra de 4 anos."
    )
    efeito_digitacao(texto_intro, velocidade=0.05)
    
    abrir_pasta(pasta_imagens)
    
    # Lista de imagens já existentes
    imagens = [f for f in os.listdir(pasta_imagens) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if imagens:
        print("Imagens encontradas:")
        for img in imagens:
            print(f"- {img}")
    else:
        print("Nenhuma imagem encontrada.")
    
    input("\nPressione ENTER...")

def resposta_final():
    
    limpar_tela()
    print("--- PERGUNTA FINAL ---")
    print("Parabéns, você chegou até aqui.\n")
    animacao_carregamento("Mas")
    print("Quem é a próxima vítima?\n")
    animacao_carregamento("Lembre-se, você tem APENAS 1 chance de salvá-la")
    
    tentativas = 0
    while tentativas == 0:
        resposta = input(f"Quem será a vítima? vítima N° 1 ? vítima N° 2? ou a vítima N° 3?\nDigite o número:").lower().strip()
        
        if resposta == "2":
            animacao_carregamento(".")
            print("\n✅ Parabéns.... Você desvendou quem era a vítima. VOCÊ A SALVOU!")
            input("\nFim de Jogo!")
            return True
        else:
            tentativas += 1 
    
    print("\n❌ GAME OVER: A vítima morreu. Você não conseguiu salvá-la... ")
    return False

def main():
    """
    Função principal que executa o desafio de raciocínio lógico
    """
    introducao()
    
    # Primeira fase
    if not primeira_charada():
        return
    
    # Segunda fase
    segunda_charada()
    
    #Contexto do pen drive
    mostrar_contexto_meio()
    
    #Parte final
    resposta_final()
    return

# Executa o desafio
if __name__ == "__main__":
    main()