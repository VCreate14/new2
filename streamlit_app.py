import os
from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key= "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" ),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True
)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
message = input("ENTER YOUR QUERY :")
agent.print_response(message)

