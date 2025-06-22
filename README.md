
# 🕵️‍♂️ Caso CSI - Desafio Interativo no Console

Um jogo interativo de raciocínio lógico, mistério e suspense, totalmente jogável via **CMD/Terminal**.

## 📜 Sobre o Projeto

**Caso CSI** é um desafio estilo *escape room digital*, com narrativa investigativa. O jogador assume o papel de um detetive tentando capturar um assassino em série. Cada fase do jogo envolve charadas, leitura atenta de pistas e interação com pastas e arquivos gerados no próprio computador.

O game conta com:

- Introdução narrativa imersiva 📖  
- Animações de digitação e carregamento ⏳  
- Criação automática de pastas no sistema de arquivos 💾  
- Charadas e fases com múltiplas tentativas 🎯  
- Revelações dramáticas com arquivos confidenciais desbloqueados 🔍  

---

## 🎮 Como Jogar

### Requisitos:

- Sistema operacional: **Windows** ou **Linux**
- Python 3.x instalado
- Execução via CMD ou Terminal

### Passo a passo:

1. **Baixe ou clone o projeto:**

```bash
git clone https://github.com/seu-usuario/caso-csi.git
```

2. **Navegue até a pasta do projeto:**

```bash
cd caso-csi
```

3. **Execute o jogo:**

```bash
python CSI.py
```

---

## 🔎 Fases do Jogo:

### 1️⃣ Introdução ao Caso:
Apresentação dramática da história e do perfil psicológico do assassino.

### 2️⃣ Primeira Charada - "O Fogo":
O jogador deve resolver uma charada clássica de lógica com apenas 3 tentativas.

### 3️⃣ Segunda Charada - "O Filho":
O script cria uma pasta automática com o enigma e dicas escondidas. O jogador precisa explorar o computador.

### 4️⃣ Revelações Confidenciais:
Informações sobre as vítimas desbloqueadas com direito a espaço reservado para adicionar **imagens reais** das vítimas no diretório `imagens_vitimas`.

### 5️⃣ Contexto Meio:
Descubra como o pendrive chegou até o detetive.

### 6️⃣ Pergunta Final:
Quem será a próxima vítima? Uma única chance de salvar a vida dela.

---

## ✨ Recursos Usados:

- **Python**  
- **CMD / Terminal**  
- Manipulação de pastas com `os` e `pathlib`  
- Efeitos de digitação com `time` e `sys.stdout`  

---

## 📌 Observação Importante:

Esse jogo não é recomendado para pessoas sensíveis a temas como violência ou suspense psicológico.

---

## ✅ Status Atual:

**Versão:** 1.0  
**Última atualização:** Junho/2025  
**Desenvolvido por:** Petter Santos 🎮👨‍💻  
