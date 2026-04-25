#!/usr/bin/env python3
"""
Database migration script to add user_id column to responses table.
Run this once to update the database schema.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from db.database import Base

load_dotenv(override=True)

db_url = os.getenv("DATABASE_URL")

if not db_url:
    print("❌ ERROR: DATABASE_URL not found in .env")
    exit(1)

engine = create_engine(db_url)

migration_sql = """
-- Add user_id column to responses table if it doesn't exist
DO $$ 
BEGIN
    IF NOT EXISTS(
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'responses' AND column_name = 'user_id'
    ) THEN
        ALTER TABLE responses ADD COLUMN user_id INTEGER;
        ALTER TABLE responses ADD CONSTRAINT fk_responses_user_id 
            FOREIGN KEY (user_id) REFERENCES users(id);
        RAISE NOTICE 'Added user_id column to responses table';
    ELSE
        RAISE NOTICE 'user_id column already exists';
    END IF;
END $$;
"""

try:
    with engine.connect() as connection:
        connection.execute(text(migration_sql))
        connection.commit()
        print("✅ Migration completed successfully!")
        print("   - Added user_id column to responses table")
        print("   - Set up foreign key constraint")
except Exception as e:
    print(f"❌ Migration failed: {e}")
    exit(1)
