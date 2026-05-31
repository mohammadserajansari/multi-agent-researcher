from crewai import LLM
from threading import Lock

from core.config import settings

from core.logger import logger
class LLMManager:

    _instance = None
    _lock = Lock()

    def __new__(cls):

        if cls._instance is None:

            with cls._lock:

                if cls._instance is None:

                    cls._instance = super(
                        LLMManager,
                        cls
                    ).__new__(cls)

                    cls._instance.llm = (
                        cls._instance._initialize_llm()
                    )

        return cls._instance

    def _initialize_llm(self):

        # =================================
        # OLLAMA
        # =================================
        try:

            logger.info("Trying Ollama...")

            llm = LLM(
                model=f"ollama/{settings.OLLAMA_MODEL}",
                base_url=settings.OLLAMA_BASE_URL,
                temperature=settings.TEMPERATURE,
            )

            llm.call("Hi")

            logger.info("Ollama Loaded")

            return llm

        except Exception as e:

            logger.error(f"Ollama Failed: {e}")

        # =================================
        # GROQ
        # =================================
        try:

            print("Trying Groq...")

            llm = LLM(
                model=settings.GROQ_MODEL,
                api_key=settings.GROQ_API_KEY,
                temperature=settings.TEMPERATURE,
            )

            llm.call("Hi")

            logger.info("Groq Loaded")

            return llm

        except Exception as e:

            logger.error(f"Groq Failed: {e}")

        # =================================
        # OPENAI
        # =================================
        try:

            print("Trying OpenAI...")

            llm = LLM(
                model=settings.OPENAI_MODEL,
                api_key=settings.OPENAI_API_KEY,
                temperature=settings.TEMPERATURE,
            )

            llm.call("Hi")

            logger.info("OpenAI Loaded")

            return llm

        except Exception as e:

            logger.error(f"OpenAI Failed: {e}")

        raise Exception("All LLM providers failed.")

    def get_llm(self):

        return self.llm


# =================================
# Singleton Instance
# =================================

llm_manager = LLMManager()

llm = llm_manager.get_llm()