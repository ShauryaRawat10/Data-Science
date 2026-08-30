## LLM Application in Production

- Runtime
    - Multiple calls to LLM sequentially, each one waiting for previous one
    - Very long running application and many reasoning steps
    - Solution: Semantic Cache, LLM cache
- Context Window
    - Even with 32K tokens, it can surpass that limit.
    - LLM forgetting what's in the middle (Paper: Losing in the middle)
- Hallucination
    - Forgetting information
    - Solution: Choosing correct tool
        - Tool 1: P(0.9), Tool 2: p(0.9)
        - So, 0.9 * 0.6 = 0.54 (probability to getting good answer drops to 0.5)
    - Fine tuning LLM for tool selection
- Fine Tuning
- Pricing
    - prompts become enormous in each step.
    - Solution: Semantic cache, Retrieval Augmentation for tool selection
- Response Validation
    - Testing response
    - Check latency and LLM Evaluation
- Security
    - If prompt injection or API key is leaked, then we have problem
    - Solution: Guardrails on prompts - LLM Guard
- Overkilling
    - Think if can implement it in deterministic code already instead of LLM


## LLM Application Landscape

- Complex Application: Vector Store (RAG), Semantic search
- Auto-GPT, GPT Engineer Project (Autonomous agent with long term memory)


## LLM in Production: Privacy and Data Retention

- Open AI API will not be used to train the Open AI models
- They have 30 days retention policy to identify abuse


## Generative UI/UX Featuring CopilotKit

- Transparency -> Trust (User need to know which tool and reasoning behind, to get how final answer is generated)
- CopilotKit -> OpenSource


## Open Source LLM vs Managed LLM Providers

- Open Source Models: DeepSeek
- LLM + Curated dataset = Fine-tuned LLM (Proprietary open source models)
- Open source models shifts lots of responsibility to us, may use Groq (managed services) but the price is high
- Managed Proprietary LLM: Easy to use, Reliable, Support and Compliance


## Confidence in AI results - CAIR

- CAIR = Value of success / (Perceived consequence of Error * Effort to correct)
- Smart Product, CAIR = High / (low * low) = Very high
- High CAIR can be get when user is asked for permission to do/undo changes


## LLOps (LangSmith solves below problems (Not open source), Pezzo for open source)

- Prompt management
- Monitoring
- Debugging
- Evaluation


## Follow Langchain blogs

## Join twitter for new use cases
