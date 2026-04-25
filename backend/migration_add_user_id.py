"""
Migration script to add user_id column to responses table.
Run this once to update the schema.
"""

from sqlalchemy import text, create_engine
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

def migrate():
    """Add user_id column to responses table"""
    with engine.connect() as conn:
        try:
            # Check if column already exists
            result = conn.execute(
                text("""
                SELECT COUNT(*)
                FROM information_schema.columns
                WHERE table_name='responses' AND column_name='user_id'
                """)
            )
            
            if result.scalar() == 0:
                # Column doesn't exist, add it
                print("Adding user_id column to responses table...")
                conn.execute(text("""
                    ALTER TABLE responses
                    ADD COLUMN user_id INTEGER REFERENCES users(id)
                """))
                conn.commit()
                print("✅ Migration successful! user_id column added.")
            else:
                print("✓ Column already exists, no migration needed.")
                
        except Exception as e:
            print(f"❌ Migration failed: {e}")
            raise

if __name__ == "__main__":
    migrate()
