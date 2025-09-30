#!/usr/bin/env python3
"""
Emergency script to enable YOLO mode (turn ON both emergency protections)
"""
import sqlite3

DB_PATH = 'shop.db'

def enable_yolo_mode():
    """Enable YOLO mode by setting both emergency settings to 1 (ON/HIDDEN)."""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        # Update emergency settings to ON (1 = hidden/active protection)
        c.execute("""
            UPDATE emergency_settings 
            SET hide_green_emoji = 1, hide_eur_symbol = 1
            WHERE id = 1
        """)
        
        conn.commit()
        
        # Verify the change
        c.execute("SELECT hide_green_emoji, hide_eur_symbol FROM emergency_settings WHERE id = 1")
        result = c.fetchone()
        
        conn.close()
        
        if result:
            print("✅ YOLO MODE ENABLED!")
            print(f"   🟢 Hide Green Emoji: {'ON' if result[0] == 1 else 'OFF'}")
            print(f"   💶 Hide EUR Symbol: {'ON' if result[1] == 1 else 'OFF'}")
            print("\n⚡ Both protections are now ACTIVE!")
        else:
            print("❌ Failed to verify settings")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    enable_yolo_mode()
