import { echoMessage } from "./api";

function App() {
  const send = async () => {
    const res = await echoMessage("Hello from React");
    alert(res.message);
  };

  return <button onClick={send}>Test Backend</button>;
}

export default App;
