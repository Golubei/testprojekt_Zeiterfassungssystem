import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import sortiereListe
from models import Zeitbuchung, User, Client
from datetime import datetime, timedelta, UTC

def test_sortiereSessions_by_created_at():
    now = datetime.now(UTC)
    s1 = Zeitbuchung(id=1, user_id=1, client_id=1, start_time=now, created_at=now)
    s2 = Zeitbuchung(id=2, user_id=1, client_id=1, start_time=now, created_at=now - timedelta(days=1))
    s3 = Zeitbuchung(id=3, user_id=1, client_id=1, start_time=now, created_at=now - timedelta(days=2))
    result = sortiereListe([s1, s2, s3], key=lambda s: s.created_at)
    assert [s.id for s in result] == [3, 2, 1]