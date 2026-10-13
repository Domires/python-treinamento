# Site de Treinamento – Cadastro de Produtos

Site + API para treinamento de automação com **PyAutoGUI** e **Rest API**.

## Instalação e execução

```bash
pip install -r requirements.txt
python main.py
```

| Endereço | O que é |
|---|---|
| http://127.0.0.1:8000/login | Tela de login |
| http://127.0.0.1:8000/cadastro | Formulário de cadastro |
| http://127.0.0.1:8000/produtos | Lista de produtos (editar/excluir) |
| http://127.0.0.1:8000/docs | Documentação Swagger |

**Usuário:** `treinamento` · **Senha:** `12345678`

Os dados ficam no arquivo `produtos.db` (SQLite). Para zerar a base, pare o servidor e apague esse arquivo.

## Tela web (PyAutoGUI)

- Se o usuário já estiver logado (token salvo no navegador), ao abrir `/login` o site vai direto para `/cadastro`. O login dura 8 horas; o botão **Sair** desloga.
- No login o foco já começa no campo **Usuário**: `usuario` → `Tab` → `senha` → `Enter`.
- No cadastro o foco começa em **Fábrica** e os campos seguem a ordem do `Tab`:
  Fábrica → Código do Material → Nome do Material → Lote → Data de Produção → Data de Validade → Quantidade → Unidade de Medida → Observação → Salvar.
- **Unidade de Medida** é uma lista de escolha (KG, T, L): com o campo em foco, basta digitar `K`, `T` ou `L` para selecionar.
- **Observação** é opcional e tem várias linhas, então `Enter` nele quebra a linha em vez de salvar. Para salvar, use `Tab` (vai para o botão **Salvar**) e depois `Enter`.
- Datas na tela: `dd/mm/aaaa` (pode digitar `12/10/2026` ou só `12102026`).
- Após salvar com sucesso não aparece nenhuma mensagem: o formulário é limpo e o foco volta para o primeiro campo (Fábrica), pronto para o próximo cadastro. Mensagens só aparecem em caso de erro.

## API (Rest)

Todas as rotas de `/api/produtos` exigem o header `Authorization: Bearer <token>`.
Na API as datas usam o formato ISO `AAAA-MM-DD`.

| Método | Rota | Descrição |
|---|---|---|
| POST | `/api/auth/login` | Login → retorna `access_token` |
| GET | `/api/auth/me` | Valida o token |
| GET | `/api/produtos` | Lista (filtros: `codigo_material`, `lote`, `fabrica`) |
| GET | `/api/produtos/{id}` | Consulta um produto |
| POST | `/api/produtos` | Cadastra |
| PUT | `/api/produtos/{id}` | Atualiza (todos os campos) |
| PATCH | `/api/produtos/{id}` | Atualiza parcialmente (só os campos enviados) |
| DELETE | `/api/produtos/{id}` | Exclui |

Exemplo com `requests`:

```python
import requests

BASE = "http://127.0.0.1:8000"

r = requests.post(f"{BASE}/api/auth/login", json={"usuario": "treinamento", "senha": "12345678"})
token = r.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

produto = {
    "fabrica": "Fábrica São Paulo",
    "codigo_material": "MAT-0001",
    "nome_material": "Parafuso Sextavado M8",
    "lote": "L2026-10",
    "data_producao": "2026-10-01",
    "data_validade": "2027-10-01",
    "quantidade": 150,
    "unidade_medida": "KG",          # KG, T ou L
    "observacao": "Armazenar em local seco",  # opcional
}
r = requests.post(f"{BASE}/api/produtos", json=produto, headers=headers)
print(r.status_code, r.json())
```
