import sys
try:
    from langchain.agents.agent import AgentExecutor
    print("✅ AgentExecutor trovato in langchain.agents.agent")
except ImportError:
    print("❌ Non trovato in .agent, provo in .agent_executor")
    try:
        from langchain.agents.agent_executor import AgentExecutor
        print("✅ AgentExecutor trovato in langchain.agents.agent_executor")
    except ImportError:
        print("❌ AgentExecutor è introvabile. Verifico installazione...")

try:
    from langchain.agents.react.agent import create_react_agent
    print("✅ create_react_agent trovato!")
except ImportError:
    print("❌ create_react_agent non trovato!")
