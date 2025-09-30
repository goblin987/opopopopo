-- Force enable YOLO mode immediately
UPDATE emergency_settings SET hide_green_emoji = 1, hide_eur_symbol = 1 WHERE id = 1;

-- Verify the change
SELECT 
    CASE WHEN hide_green_emoji = 1 THEN '🔴 ON (HIDDEN)' ELSE '🟢 OFF (VISIBLE)' END as green_emoji_status,
    CASE WHEN hide_eur_symbol = 1 THEN '🔴 ON (HIDDEN)' ELSE '🟢 OFF (VISIBLE)' END as eur_symbol_status
FROM emergency_settings WHERE id = 1;
