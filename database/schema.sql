-- ============================================================
-- database: user.db
-- ============================================================

-- 使用者
CREATE TABLE IF NOT EXISTS users (
    id     INTEGER PRIMARY KEY,
    banner INTEGER DEFAULT 1
);

-- 事件
CREATE TABLE IF NOT EXISTS events (
    id      TEXT    NOT NULL PRIMARY KEY,
    title   TEXT    NOT NULL,
    type    TEXT    NOT NULL,
    done    INTEGER,
    dt      TEXT,
    tag     TEXT,
    user_id INTEGER REFERENCES users (id)
);

-- 標籤
CREATE TABLE IF NOT EXISTS tags (
    id   TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL
);

-- 事件 ↔ 標籤（多對多）
CREATE TABLE IF NOT EXISTS event_tag (
    event_id TEXT NOT NULL REFERENCES events (id),
    tag_id   TEXT NOT NULL REFERENCES tags   (id)
);