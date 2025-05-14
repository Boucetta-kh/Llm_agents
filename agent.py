import requests

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.messages = []

    def system_prompt(self):
        if self.role == "Project Manager":
            return (
                "You are a strict and organized Project Manager. Always:\n"
                "1. Present project features in a clear Markdown table with Function and Assigned To columns.\n"
                "2. Assign roles to Backend and Frontend Developers clearly.\n"
                "3. Ask developers to reply with only questions about their parts.\n"
                "4. When replying to questions, be concise and structured.\n"
            )
        elif self.role == "Frontend Developer":
          return (
        "You are a Frontend Developer.\n"
        "Respond only with actual frontend code using HTML, CSS, and JavaScript.\n"
        "When you receive API specs from the backend, build a UI to connect to those APIs.\n"
        "Use basic components like forms, buttons, input fields, and fetch calls to the backend.\n"
        "DO NOT include any explanation, comments, or markdown — just clean and working code.\n"
        "Return the complete HTML + JS for each feature you are assigned."
             )

        elif self.role == "Backend Developer":
            return (
                "You are a Backend Developer. When assigned features:\n"
                "1. Ask questions to clarify the functionality.\n"
                "2. Respond only with FastAPI code: routes, models, and Pydantic schemas.\n"
                "No explanation or extra text — only code."
            )
        return f"You are a helpful {self.role}."

    def chat(self, input_message):
        self.messages.append({"role": "user", "content": input_message})
        response = self.ask_llm()
        self.messages.append({"role": "assistant", "content": response})
        return response

    def ask_llm(self):
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "deepseek-coder",
                "messages": [{"role": "system", "content": self.system_prompt()}] + self.messages,
                "stream": False,
            }
        )
        return response.json()['message']['content']
