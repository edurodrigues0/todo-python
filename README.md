# 📋 Gerenciador de Tarefas

Um sistema simples e eficiente para gerenciar suas tarefas diárias através da linha de comando, desenvolvido em Python.

## ✨ Funcionalidades

- ➕ **Adicionar tarefas** - Crie novas tarefas com nome e descrição
- 👀 **Visualizar tarefas** - Veja todas as suas tarefas com status detalhado
- ✏️ **Atualizar tarefas** - Edite o nome e descrição de tarefas existentes
- ✅ **Marcar como concluída** - Marque tarefas como finalizadas
- 🗑️ **Deletar tarefas concluídas** - Remova todas as tarefas já finalizadas
- 🖥️ **Interface limpa** - Terminal limpo a cada operação para melhor experiência

## 🚀 Como usar

### Pré-requisitos

- Python 3.6 ou superior instalado em seu sistema

### Executando o programa

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/gerenciador-tarefas.git
```

2. Navegue até o diretório do projeto:

```bash
cd gerenciador-tarefas
```

3. Execute o programa:

```bash
python gerenciador.py
```

## 📖 Menu de Opções

Ao executar o programa, você verá o seguinte menu:

```
Menu de Gerenciador de Tarefas:
1. Adicionar tarefa
2. Ver tarefas
3. Atualizar tarefa
4. Completar tarefa
5. Deletar tarefas completadas
6. Sair
```

### 1. Adicionar Tarefa

- Digite o nome da tarefa
- Digite a descrição da tarefa
- A tarefa será criada com status "Pendente"

### 2. Ver Tarefas

Exibe todas as tarefas com as seguintes informações:

- ID da tarefa
- Nome
- Descrição
- Status (Pendente/Concluída)

### 3. Atualizar Tarefa

- Digite o ID da tarefa que deseja modificar
- Digite o novo nome
- Digite a nova descrição

### 4. Completar Tarefa

- Digite o ID da tarefa
- A tarefa será marcada como "Concluída"

### 5. Deletar Tarefas Completadas

Remove todas as tarefas que estão marcadas como concluídas

### 6. Sair

Encerra o programa

## 🛠️ Estrutura do Código

O programa é organizado nas seguintes funções principais:

- `clear_terminal()` - Limpa o terminal (compatível com Windows e Unix)
- `add_tasks()` - Adiciona uma nova tarefa à lista
- `show_tasks()` - Exibe todas as tarefas
- `update_task()` - Atualiza uma tarefa existente
- `complete_task()` - Marca uma tarefa como concluída
- `delete_tasks()` - Remove tarefas concluídas

## 💾 Estrutura dos Dados

Cada tarefa é armazenada como um dicionário com a seguinte estrutura:

```python
{
    "id": 1,
    "name": "Nome da tarefa",
    "description": "Descrição da tarefa",
    "is_completed": "Pendente"
}
```

## 🔧 Compatibilidade

- ✅ Windows
- ✅ macOS
- ✅ Linux

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Possíveis Melhorias

- [ ] Persistência de dados (salvar em arquivo)
- [ ] Interface gráfica
- [ ] Categorias de tarefas
- [ ] Datas de vencimento
- [ ] Prioridades
- [ ] Busca e filtros

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ por Eduardo Rodrigues

---

⭐ Se este projeto te ajudou, considere dar uma estrela!
