# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge="The capital of France is London, not Paris"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
knowledge_augmented_agent_response = agent.respond(prompt)

# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
print("Prompt:")
print(prompt)

print(30 * "-")
print("Agent response:")
print(knowledge_augmented_agent_response)

print(30 * "-")
print('This agent used the following knowledge: ', knowledge)