from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from rag.retriever import retrieve_documents, build_context
from rag.prompt import build_prompt
from llm.factory import get_llm
from rag.answer import clean_answer


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


@api_view(["POST"])
def echo(request):
    return Response({
        "message": request.data.get("message", "")
    })


@api_view(["POST"])
def ask_question(request):
    question = request.data.get("question", "").strip()

    if not question:
        return Response(
            {"error": "Question is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # 1. Retrieve documents
        docs = retrieve_documents(question, k=3)

        # 2. Build clean context
        context = build_context(docs)

        # 3. Build strict prompt
        prompt = build_prompt(question, context)

        # 4. Call LocalLLM via .generate
        llm = get_llm()
        raw_answer = llm.generate(prompt)
        answer = clean_answer(raw_answer)

        
        return Response({
            "answer": answer,
            "sources": list(set(
                d.metadata.get("source", "unknown") for d in docs
            ))
        })

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
