# 📋 Sistema de Cadastro em Python

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Um sistema de cadastro via terminal com persistência em CSV, desenvolvido como projeto final do **Mundo 3** do Curso em Vídeo.

## ✨ Funcionalidades

- ✅ **Menu interativo** com cores personalizadas
- 📥 **Cadastro** de usuários (nome e idade)
- 📤 **Consulta** de registros salvos em CSV
- 🛡️ **Tratamento de erros** para entradas inválidas
- 💾 **Persistência de dados** em arquivo CSV

## 🛠️ Tecnologias

- Python 3.9+
- Módulos nativos:
  - `csv` para manipulação de arquivos
  - `os` para verificação de caminhos
- ANSI escape codes para cores no terminal

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cadastro-python.git
```

2. Acesse a pasta do projeto:
```bash
cd cadastro-python
```
3. Execute o programa:
```bash
python app.py
```

## 📂 Estrutura do Projeto:

cadastro-python/
├── src/
│   ├── data/          # Lógica de manipulação de CSV
│   └── layout/        # Componentes de interface
├── app.py             # Ponto de entrada
├── requirements.txt   # Dependências
└── README.md          # Documentação


### 🔍 Elementos Incluídos:
1. **Badges** - Ícones visuais para versão/licença
2. **GIF/Imagem** *(opcional)* - Adicione um screenshot do terminal em ação
3. **Seção de Features** - Destaque suas inovações
4. **Passos claros** para execução
5. **Mapa do projeto** - Mostra organização profissional

### 💡 Dicas Extras:
- Adicione um **gif demonstrativo** usando [ScreenToGif](https://www.screentogif.com/)
- Inclua um **exemplo de uso** na seção de Features:
  ```python
  >>> Name: João
  >>> Age: 25
  [SUCCESS] João adicionado(a) com sucesso!
