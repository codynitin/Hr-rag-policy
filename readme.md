 so process
 ```
 pip install uv 

 uv venv baichrrag 

 baichrrag\Scripts\activate
 ```
 downlaod all teh requirements 


 ```
 uv pip install reuirements.txt
 ```


 
 we will givw the file path using and then will be using loader to  load our data suing textloader 

 ```
 file_path = os.path.join("data","attendance_wfh_policy.txt")

 loader = TextLoader(file_path,encoding="utf-8")
 ```

we have only one document so length of document will be one , 

now after loading the data we will split the data in to small chunks 
now for chunking we have different stratagies 

```
Technique	How it works	When to use
Character-based	Splits after a fixed number of characters	Simple documents
Recursive character	Splits using paragraphs, lines, words, etc.	General-purpose RAG
Token-based	Splits based on token count rather than characters	LLM context management
Sentence-based	Splits at sentence boundaries	Articles, simple text
Semantic chunking	Groups sentences based on meaning	Context-heavy documents
Document-based	Splits according to headings, sections, pages	HR policies, manuals
Agentic chunking	Uses an LLM to decide meaningful chunk boundaries	Complex documents```
