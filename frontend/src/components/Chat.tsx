import { useState } from "react";
import Message from "./Message";
import ChatInput from "./ChatInput";
import { queryRag } from "../services/api";

type ChatMessage = {
  role: "user" | "assistant";
  content: string;
};

export default function Chat() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async (question: string) => {
    setMessages((prev) => [...prev, { role: "user", content: question }]);
    setLoading(true);

    try {
      const answer = await queryRag(question);

      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: answer },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Error contacting API. Try again later." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map(({role, content}, i) => (
          <Message key={i} role={role} content={content} />
        ))}
      </div>

      <ChatInput onSend={handleSend} loading={loading} />
    </div>
  );
}