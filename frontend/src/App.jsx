import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setError("");
    setAnswer("");
    setSources([]);

    try {
      const response = await fetch("http://127.0.0.1:8000/api/ask/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      if (!response.ok) {
        throw new Error("API request failed");
      }

      const data = await response.json();
      setAnswer(data.answer);
      setSources(data.sources || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "800px", margin: "0 auto" }}>
      <h2>Ask about me</h2>

      <textarea
        rows="4"
        style={{ width: "100%" }}
        placeholder="Ask something about me..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askQuestion} disabled={loading} style={{ marginTop: "1rem" }}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {answer && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Answer</h3>
          <pre style={{ whiteSpace: "pre-wrap" }}>{answer}</pre>

          {sources.length > 0 && (
            <>
              <h4>Sources</h4>
              <ul>
                {sources.map((s, i) => (
                  <li key={i}>{s}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
