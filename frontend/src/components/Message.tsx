type Props = {
  role: "user" | "assistant";
  content: string;
};

export default function Message({ role, content }: Props) {
  return (
    <div className={`message ${role}`}>
      <div className="bubble">{content}</div>
    </div>
  );
}