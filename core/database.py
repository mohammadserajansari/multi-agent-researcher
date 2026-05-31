import sqlite3
from sqlite3 import Connection
from datetime import datetime
from pathlib import Path

from core.logger import logger



DB_DIR = Path("database")
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "research_agent.db"


class DatabaseManager:

    _instance = None

    # =====================================================
    # Singleton
    # =====================================================
    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.connection = sqlite3.connect(
                DB_PATH,
                check_same_thread=False
            )

            cls._instance.connection.row_factory = sqlite3.Row

            cls._instance.create_tables()

        return cls._instance

    # =====================================================
    # Get Connection
    # =====================================================
    def get_connection(self) -> Connection:

        return self.connection

    # =====================================================
    # Create Tables
    # =====================================================
    def create_tables(self):

        cursor = self.connection.cursor()

        # =================================================
        # Research Sessions
        # =================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS research_sessions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            query TEXT NOT NULL,

            status TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # =================================================
        # Sources
        # =================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sources (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            source_type TEXT,

            source_name TEXT,

            content TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(session_id)
            REFERENCES research_sessions(id)
        )
        """)

        # =================================================
        # Extracted Insights
        # =================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS extracted_insights (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            extracted_text TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(session_id)
            REFERENCES research_sessions(id)
        )
        """)

        # =================================================
        # Comparisons
        # =================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS comparisons (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            comparison_result TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(session_id)
            REFERENCES research_sessions(id)
        )
        """)

        # =================================================
        # Reports
        # =================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            report_content TEXT,

            confidence_score REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(session_id)
            REFERENCES research_sessions(id)
        )
        """)

        self.connection.commit()

        logger.info("✅ Database tables created successfully")

    # =====================================================
    # Create Research Session
    # =====================================================
    def create_research_session(
        self,
        query: str,
        status: str = "STARTED"
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT INTO research_sessions (
            query,
            status
        )
        VALUES (?, ?)
        """, (query, status))

        self.connection.commit()

        session_id = cursor.lastrowid

        logger.info(
            f"✅ Research session created: {session_id}"
        )

        return session_id

    # =====================================================
    # Save Source Data
    # =====================================================
    def save_source(
        self,
        session_id: int,
        source_type: str,
        source_name: str,
        content: str
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT INTO sources (
            session_id,
            source_type,
            source_name,
            content
        )
        VALUES (?, ?, ?, ?)
        """, (
            session_id,
            source_type,
            source_name,
            content
        ))

        self.connection.commit()

        logger.info("✅ Source saved")

    # =====================================================
    # Save Extracted Insights
    # =====================================================
    def save_extracted_insights(
        self,
        session_id: int,
        extracted_text: str
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT INTO extracted_insights (
            session_id,
            extracted_text
        )
        VALUES (?, ?)
        """, (
            session_id,
            extracted_text
        ))

        self.connection.commit()

        logger.info("✅ Extracted insights saved")

    # =====================================================
    # Save Comparison Result
    # =====================================================
    def save_comparison(
        self,
        session_id: int,
        comparison_result: str
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT INTO comparisons (
            session_id,
            comparison_result
        )
        VALUES (?, ?)
        """, (
            session_id,
            comparison_result
        ))

        self.connection.commit()

        logger.info("✅ Comparison result saved")

    # =====================================================
    # Save Final Report
    # =====================================================
    def save_report(
        self,
        session_id: int,
        report_content: str,
        confidence_score: float
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT INTO reports (
            session_id,
            report_content,
            confidence_score
        )
        VALUES (?, ?, ?)
        """, (
            session_id,
            report_content,
            confidence_score
        ))

        self.connection.commit()

        logger.info("✅ Final report saved")

    # =====================================================
    # Get Full Research Session
    # =====================================================
    def get_research_session(
        self,
        session_id: int
    ):

        cursor = self.connection.cursor()

        cursor.execute("""
        SELECT *
        FROM research_sessions
        WHERE id = ?
        """, (session_id,))

        return dict(cursor.fetchone())

    # =====================================================
    # Close Database
    # =====================================================
    def close(self):

        self.connection.close()

        logger.info("✅ Database connection closed")


# =========================================================
# Global Singleton Instance
# =========================================================

db = DatabaseManager()