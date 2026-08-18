import json
from typing import Optional

import httpx

from backend.config import settings
from backend.prompts.prompts import (
    TUTOR_SYSTEM_PROMPT,
    QUIZ_GENERATOR_PROMPT,
    EXAM_EVALUATOR_PROMPT,
    KNOWLEDGE_ASSESSOR_PROMPT,
    DAILY_LEARNING_PROMPT,
    VOCABULARY_EXPLAINER_PROMPT,
)


async def call_llm(system_prompt: str, user_message: str, temperature: float = 0.7) -> str:
    if not settings.OPENAI_API_KEY:
        return _mock_response(user_message)

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
            json={
                "model": settings.OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                "temperature": temperature,
                "max_tokens": 2000,
            },
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]


async def generate_tutor_response(
    user_message: str,
    topic_context: str = "",
    user_knowledge: str = "",
    chat_history: str = "",
    action: str = "",
) -> str:
    context_parts = []
    if topic_context:
        context_parts.append(f"TOPIC CONTEXT:\n{topic_context}")
    if user_knowledge:
        context_parts.append(f"USER KNOWLEDGE PROFILE:\n{user_knowledge}")
    if chat_history:
        context_parts.append(f"CONVERSATION HISTORY:\n{chat_history}")

    action_instruction = ""
    if action == "explain_simpler":
        action_instruction = "\nThe user asked to explain this more simply. Use a simpler explanation or a real-world analogy. Use no jargon."
    elif action == "analogy":
        action_instruction = "\nThe user asked for an analogy. Create a relatable, non-technical comparison that makes the concept intuitive."
    elif action == "example":
        action_instruction = "\nThe user asked for an example. Provide a concrete, practical scenario that illustrates the concept clearly."
    elif action == "go_deeper":
        action_instruction = "\nThe user wants to go deeper. Provide more technical detail, internal mechanisms, and advanced aspects."
    elif action == "terminology":
        action_instruction = "\nThe user asked to explain the terminology. List all technical terms in the current topic and define each one clearly."
    elif action == "test_me":
        action_instruction = "\nThe user wants to be tested. Create a question appropriate for their level to check understanding."
    elif action == "real_world":
        action_instruction = "\nThe user wants a real-world case. Describe a known incident, CVE, or actual attack that demonstrates the concept."
    elif action == "attack_flow":
        action_instruction = "\nThe user wants to see the attack flow. Describe step-by-step how an attacker would exploit this vulnerability."
    elif action == "defense":
        action_instruction = "\nThe user wants to see the defense. Describe defensive measures, mitigations, and best practices."

    prompt_parts = [f"USER MESSAGE: {user_message}{action_instruction}"]
    if context_parts:
        prompt_parts.insert(0, "\n\n".join(context_parts))

    full_message = "\n\n---\n\n".join(prompt_parts)

    return await call_llm(TUTOR_SYSTEM_PROMPT, full_message)


async def generate_quiz(topic_name: str, difficulty: str, count: int = 5) -> str:
    prompt = f"""Generate {count} cybersecurity quiz questions about {topic_name}.

Difficulty level: {difficulty}

For each question provide:
- question_text
- question_type (multiple_choice, true_false, or scenario)
- options (array of possible answers)
- correct_answer (the correct option text)
- explanation (why this answer is correct)

Return ONLY valid JSON array. No markdown fences."""
    return await call_llm(QUIZ_GENERATOR_PROMPT, prompt)


async def evaluate_answer(question: str, user_answer: str, correct_answer: str) -> str:
    prompt = f"""Evaluate this quiz answer:

Question: {question}
User's Answer: {user_answer}
Correct Answer: {correct_answer}

Provide:
- is_correct (boolean)
- score (0.0 to 1.0)
- feedback (explain why it's correct or incorrect, and what to study)
- misconception (if wrong, what did the user misunderstand?)

Return ONLY valid JSON."""
    return await call_llm(EXAM_EVALUATOR_PROMPT, prompt)


async def generate_daily_learning(user_knowledge: str) -> str:
    prompt = f"""Generate a personalized daily cybersecurity lesson.

User's current knowledge profile:
{user_knowledge}

Return valid JSON with fields:
- new_concept: {{"name", "explanation", "category"}}
- review: {{"name", "explanation", "reason"}}
- news: [{{"title", "summary", "source", "url"}}]
- vulnerability: {{"name", "description", "severity", "cve"}}
- exam_question: {{"question", "options", "correct", "explanation"}}
- scenario: {{"title", "description", "question", "hint"}}
"""
    return await call_llm(DAILY_LEARNING_PROMPT, prompt, temperature=0.8)


async def explain_vocabulary(term: str) -> str:
    prompt = f"""Explain the cybersecurity term: {term}

Return valid JSON with:
- term
- definition (simple, beginner-friendly)
- example (practical example of how it's used)
- related_terms (array of related cybersecurity terms)
- category (e.g., networking, web security, cloud, crypto)
"""
    return await call_llm(VOCABULARY_EXPLAINER_PROMPT, prompt)


def _mock_response(user_message: str) -> str:
    lower = user_message.lower()
    if "ssrf" in lower:
        return json.dumps({
            "message": "**SSRF** stands for **Server-Side Request Forgery**.\n\nLet me start with one simple idea:\n\n**A server can make requests to other systems.**\n\nWhen you visit a website, your browser makes a request to the server. But servers also make requests to other servers all the time.\n\nFor example, when a website lets you enter a URL to fetch a preview (like Slack unfurling a link), the server makes that request on your behalf.\n\n**SSRF happens when an attacker tricks a server into making a request for them.**\n\nThe attacker controls the URL the server fetches. Since the server is usually inside a trusted network, it can reach things the attacker normally can't.\n\nThink of it this way:\n> You can't walk into a restricted building. But if you trick a building employee into fetching something from inside for you, you've bypassed the security.\n\nBefore we go deeper:\n\nDo you understand what an **internal network** is?",
            "terms": [
                {"term": "Server-Side Request Forgery", "definition": "An attack where an attacker makes a server send requests to unintended locations."},
                {"term": "Internal Network", "definition": "The private network inside an organization, not accessible from the public internet."},
                {"term": "Endpoint", "definition": "A specific URL or address where a service can be reached."}
            ],
            "topic": "SSRF",
            "suggested_questions": ["What is an internal network?", "Can you give me an example?", "How does the attack work step by step?"]
        })
    elif "simpler" in lower or "easier" in lower:
        return json.dumps({
            "message": "Let me try a simpler explanation.\n\nImagine you work at a hotel front desk. Guests sometimes ask you to call a room number for them. You do it because they're a guest.\n\nNow imagine someone walks in, looks like a guest, and asks you to call the **manager's private office**. You don't know the difference - you just make the call.\n\nThat's SSRF. The attacker looks legitimate, so the server makes a request to a place it shouldn't.",
            "terms": [],
            "topic": "SSRF",
            "suggested_questions": ["That makes more sense!", "What happens next?", "How do we prevent this?"]
        })
    elif "analogy" in lower:
        return json.dumps({
            "message": "**Restaurant Analogy:**\n\nImagine a restaurant where the waiter (the server) takes your order and goes to the kitchen.\n\nYou tell the waiter: \"Please bring me the food from the table behind the counter.\"\n\nThe waiter goes to get it, because that's what waiters do - they fetch food from places you can't access.\n\nBut that table behind the counter is where the **chef's secret recipes** are kept. You weren't supposed to access that.\n\nSSRF works exactly like this. The attacker tells the server to \"fetch\" something from a place the attacker can't reach directly, and the server does it because it has access.",
            "terms": [],
            "topic": "SSRF",
            "suggested_questions": ["That's clear! What's next?", "How do we stop this?", "Show me a real-world case"]
        })
    elif "quiz" in lower or "test" in lower or "question" in lower:
        return json.dumps({
            "question": "A web application allows users to enter a URL to generate a preview thumbnail. A security engineer notices the server making unexpected connections to internal IP addresses. What vulnerability is this most likely?",
            "options": [
                "A) Cross-Site Scripting (XSS)",
                "B) SQL Injection",
                "C) Server-Side Request Forgery (SSRF)",
                "D) Cross-Site Request Forgery (CSRF)"
            ],
            "correct": "C) Server-Side Request Forgery (SSRF)",
            "explanation": "When a server makes requests to internal IP addresses based on user-controlled input, this is a classic SSRF vulnerability. The attacker is using the server as a proxy to reach internal resources.",
            "difficulty": "intermediate"
        })
    elif "prevention" in lower or "defend" in lower or "prevent" in lower:
        return json.dumps({
            "message": "**How to prevent SSRF:**\n\n1. **Validate URLs** - Only allow requests to approved domains and IP ranges\n2. **Block internal IPs** - Prevent requests to 127.0.0.1, 10.x.x.x, 172.16-31.x.x, 192.168.x.x, and 169.254.169.254\n3. **Use allowlists** - Only permit known-safe URLs, block everything else\n4. **Network segmentation** - Limit what the server can reach\n5. **Disable unused URL schemes** - Block file://, gopher://, dict:// etc.\n\nThe most important rule: **Never trust user-supplied URLs.**\n\nWant to test your understanding?",
            "terms": [
                {"term": "Allowlist", "definition": "A list of approved items. Everything not on the list is blocked."},
                {"term": "Network Segmentation", "definition": "Dividing a network into isolated zones to limit what can communicate with what."}
            ],
            "topic": "SSRF",
            "suggested_questions": ["Test me!", "Go deeper", "Show me the attack flow"]
        })
    elif "deeper" in lower or "advanced" in lower:
        return json.dumps({
            "message": "**Advanced SSRF:**\n\nSSRF becomes especially dangerous in cloud environments because of the **metadata service**.\n\nMost cloud providers (AWS, GCP, Azure) run a service at `169.254.169.254` that returns instance metadata - including **temporary credentials**.\n\n**Attack chain:**\n1. Attacker finds a web app with a URL parameter\n2. Sends: `http://169.254.169.254/latest/meta-data/iam/security-credentials/`\n3. Server fetches the metadata, returns IAM role credentials\n4. Attacker uses those credentials to access AWS services\n\n**Advanced techniques:**\n- **DNS rebinding** - Attacker's DNS server returns an internal IP after initial validation\n- **Protocol smuggling** - Using `gopher://` or `dict://` protocols to interact with internal services\n- **Blind SSRF** - Where the response isn't directly visible, but side effects can be observed\n- **Cloud-specific SSRF** - Exploiting cloud metadata, internal DNS, and service discovery endpoints\n\nWant to see how to test for this?",
            "terms": [
                {"term": "Metadata Service", "definition": "A service running at 169.254.169.254 that provides cloud instance information, often including credentials."},
                {"term": "DNS Rebinding", "definition": "An attack where a DNS response changes to point to an internal IP after initial validation."},
                {"term": "Protocol Smuggling", "definition": "Using non-HTTP protocols (gopher, dict) through HTTP proxies to reach internal services."},
                {"term": "Blind SSRF", "definition": "SSRF where the attacker cannot directly see the response but can infer information through side effects."}
            ],
            "topic": "SSRF",
            "suggested_questions": ["Show me a real-world CVE", "How do I test for SSRF?", "Show me the defense"]
        })
    elif "define" in lower or "what is" in lower or "explain the cybersecurity term" in lower:
        term_name = user_message.split(":")[-1].strip().strip('"').strip("'") if ":" in user_message else "this term"
        return json.dumps({
            "term": term_name,
            "definition": f"{term_name} is a cybersecurity concept that is important to understand.",
            "example": f"For example, {term_name} is commonly used in security assessments.",
            "related_terms": ["security", "vulnerability", "authentication"],
            "category": "general"
        })
    else:
        return json.dumps({
            "message": f"Let me help you learn about that. I'll start from the basics.\n\n**What do you already know about this topic?**\n\nThis helps me tailor my explanation to your level.\n\nOr, if you'd like, you can:\n- Say **\"Teach me [topic]\"** to start a focused lesson\n- Say **\"Quiz me\"** to test your knowledge\n- Ask me to **\"Explain [term]\"** for any cybersecurity term",
            "terms": [],
            "topic": "",
            "suggested_questions": ["Teach me SSRF", "Teach me OAuth", "Quiz me on web security"]
        })
