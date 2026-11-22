from langchain.tools import tool
def create_tools(retriever):

    """ it will gonna return a tool function which we will onna use in agent """
    
    @tool
    def search_policy_tool(question:str)->str:
        """search for hr policy and leaves """
        matching_chunk = retriever.invoke(question)
        return "\n\n".join(chunk.page_content for chunk in matching_chunk )
    return search_policy_tool