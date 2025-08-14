from crewai.tools import BaseTool
from serpapi import GoogleSearch
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

embedding_function = OpenAIEmbeddings()

class IndexNewsTool(BaseTool):
    name: str = "IndexNewsTool"
    description: str = "Fetches and stores latest news for a stock index using SerpAPI and Yahoo Finance."

    def _run(self, index_name: str) -> str:
        try:
            params = {
                "q": f"{index_name} latest news",
                "api_key": os.getenv("SERPAPI_KEY"),
                "num": 5,
                "hl": "en"
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            links = [res.get("link") for res in results.get("organic_results", []) if res.get("link")]

            if not links:
                return f"❌ No URLs found from SerpAPI for: {index_name}"

            all_splits = []
            for url in links:
                try:
                    loader = WebBaseLoader(url)
                    docs = loader.load()
                    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                    splits = splitter.split_documents(docs)
                    all_splits.extend(splits)
                except Exception:
                    continue  # skip if page can't be loaded

            if all_splits:
                vectorstore = Chroma.from_documents(all_splits, embedding=embedding_function, persist_directory="./chroma_db")
                vectorstore.persist()
                return f"✅ Stored {len(all_splits)} chunks from news URLs for {index_name}"
            else:
                return "❌ No valid article content could be processed."

        except Exception as e:
            return f"⚠️ Failed to fetch and process news for {index_name}: {str(e)}"
