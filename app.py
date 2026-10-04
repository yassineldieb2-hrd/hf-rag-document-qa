import gradio as gr
from rag import ask


def answer_question(question):
    answer, sources = ask(question)
    source_text = ", ".join(sources) if sources else "None"
    return answer, source_text


demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(label="Your question", placeholder="e.g. How long does shipping take?"),
    outputs=[gr.Textbox(label="Answer"), gr.Textbox(label="Sources")],
    title="Document Q&A (RAG)",
    description="Ask questions about the documents in the docs folder.",
)

if __name__ == "__main__":
    demo.launch()
