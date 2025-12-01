from fastmcp import FastMCP
from openai import OpenAI

# FastMCP サーバーインスタンス
mcp = FastMCP(name="GPT Research Server")

# OpenAI クライアント（環境変数から自動で API キーを読み込み）
client = OpenAI()


@mcp.tool
def research(query: str) -> str:
    """
    GPT-5.1とWeb検索を使用してクエリを調査します。

    Args:
        query: 調査したい質問やトピック

    Returns:
        調査結果（引用情報を含む）
    """
    # Responses API で Web Search を実行
    response = client.responses.create(
        model="gpt-5.1",
        tools=[
            {
                "type": "web_search",
                "search_context_size": "medium",  # low/medium/high
            }
        ],
        input=query,
    )

    # レスポンステキストを取得
    result_text = response.output_text

    # 引用情報を抽出してフォーマット
    citations = []
    for item in response.output:
        if hasattr(item, 'type') and item.type == "message":
            for content in item.content:
                if hasattr(content, 'annotations'):
                    for annotation in content.annotations:
                        citations.append(f"- [{annotation.title}]({annotation.url})")

    # 結果と引用を結合
    if citations:
        result_text += "\n\n## Sources\n" + "\n".join(citations)

    return result_text


if __name__ == "__main__":
    mcp.run()
