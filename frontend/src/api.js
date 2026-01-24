export async function echoMessage(message) {
    const response = await fetch("http://localhost:8000/api/echo/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
  
    return response.json();
  }
  