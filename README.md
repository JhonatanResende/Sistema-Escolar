# 🎓 Sistema Escolar

Projeto desenvolvido em Python para verificar a situação escolar de um aluno com base em sua média final.

O sistema identifica se o aluno está:

- ✅ Aprovado
- 📚 Recuperação
- ❌ Reprovado

Além disso, o projeto também:

- 🔊 Reproduz um áudio quando o aluno é aprovado
- 📅 Trabalha com datas de recuperação
- 🛡️ Faz validação de entrada de dados
- ⏳ Verifica prazo limite para recuperação

---

# 🚀 Tecnologias Utilizadas

- 🐍 Python
- 🎵 playsound3

---

# ⚙️ Funcionalidades

## ✅ Aprovação Automática

Se a média do aluno for maior ou igual a `7.0`:

- o sistema informa aprovação
- um áudio é reproduzido automaticamente

---

## 📚 Recuperação

Se a média estiver entre `4.0` e `6.9`:

- o sistema informa recuperação
- mostra o prazo da prova
- solicita a data da prova
- valida o formato da data
- solicita a nota da recuperação

Se a nota da recuperação for maior ou igual a `7.0`:

- ✅ aluno aprovado
- 🔊 áudio reproduzido

Caso contrário:

- ❌ aluno reprovado

---

## ❌ Reprovação Automática

Se a média for menor que `4.0`:

- o aluno é reprovado automaticamente

---

# 📦 Como Instalar

Clone o repositório:

```bash
git clone https://github.com/JhonatanResende/Sistema-Escolar
```

Entre na pasta do projeto:

```bash
cd Sistema-Escolar
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# ▶️ Como Executar

Execute o arquivo Python:

```bash
python Sistema-Escolar.py
```

---

# 📁 Estrutura do Projeto

```txt
Sistema-Escolar/
│
├── Sistema-Escolar.py
├── song.mp3
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📝 Observações

O arquivo `song.mp3` precisa estar na mesma pasta do arquivo Python para que o áudio funcione corretamente.

---

# 👨‍💻 Autor

Desenvolvido por Jhonatan Resende.
