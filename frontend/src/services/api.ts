import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
export async function queryRag(question: string) {
  console.log("API URL:", API_URL);
  const response = await axios.post(`${API_URL}/rag/invoke`, {
    input: {
      question,
    },
  });

  return response.data.output;
}