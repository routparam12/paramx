from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rag.retriever import test_retrieval
from llm.factory import get_llm


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
        docs = test_retrieval(question)

        context = "\n\n".join(d.page_content for d in docs[:3])

        llm = get_llm()
        answer = llm.generate_answer(question, context)

        return Response({
            "answer": answer,
            "sources": list(set(d.metadata.get("source", "unknown") for d in docs))
        })

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
