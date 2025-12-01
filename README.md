# GPT Research MCP Server

OpenAI GPT-5.1 の Responses API と組み込み Web Search ツールを活用したリサーチ MCP サーバーです。

## 機能

- `research(query)`: GPT-5.1 の Web Search 機能を使用してクエリを調査し、引用情報付きの結果を返します

## 必要要件

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) パッケージマネージャー
- OpenAI API キー

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/your-username/gpt-research-mcp.git
cd gpt-research-mcp
```

### 2. 依存関係のインストール

```bash
uv sync
```

### 3. 環境変数の設定

```bash
export OPENAI_API_KEY="sk-..."
```

## MCP サーバーとしてのインストール

### Claude Desktop への登録

`~/.claude/claude_desktop_config.json` を編集して以下を追加:

```json
{
  "mcpServers": {
    "gpt-research": {
      "command": "uv",
      "args": ["run", "python", "/path/to/gpt-research-mcp/main.py"],
      "env": {
        "OPENAI_API_KEY": "sk-..."
      }
    }
  }
}
```

`/path/to/gpt-research-mcp` を実際のパスに置き換えてください。

### Claude Code への登録

```bash
claude mcp add gpt-research -- uv run python /path/to/gpt-research-mcp/main.py
```

または `~/.claude/settings.json` に直接追加:

```json
{
  "mcpServers": {
    "gpt-research": {
      "command": "uv",
      "args": ["run", "python", "/path/to/gpt-research-mcp/main.py"],
      "env": {
        "OPENAI_API_KEY": "sk-..."
      }
    }
  }
}
```

## 使用方法

### スタンドアロン実行

```bash
uv run python main.py
```

### MCP ツールとして使用

MCP クライアント（Claude Desktop 等）から `research` ツールを呼び出します:

```
research("2024年の AI トレンドについて教えてください")
```

## ツール仕様

### `research(query: str) -> str`

| パラメータ | 型 | 説明 |
|-----------|-----|------|
| `query` | `str` | 調査したい質問やトピック |

**戻り値**: GPT-5.1 が生成したリサーチ結果（引用情報を含む）

## 技術スタック

| コンポーネント | 技術 |
|---------------|------|
| パッケージ管理 | uv |
| Python バージョン | 3.12 |
| MCP フレームワーク | FastMCP 2.0 |
| OpenAI クライアント | openai (公式ライブラリ) |
| モデル | gpt-5.1 |

## ライセンス

MIT
