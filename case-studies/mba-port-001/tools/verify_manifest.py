"""Verify published files using the SHA-256 manifest (excluding manifest itself)."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'MANIFEST_SHA256.txt'

def verify():
    records = [line for line in MANIFEST.read_text('utf-8').splitlines() if line.strip() and not line.startswith('#')]
    if len(records) < 10:
        raise RuntimeError('MANIFEST_TOO_SMALL')
    for record in records:
        digest, relpath = record.split('  ', 1)
        candidate = (ROOT / relpath).resolve()
        if not candidate.is_relative_to(ROOT.resolve()) or not candidate.is_file():
            raise RuntimeError(f'INVALID_MANIFEST_PATH:{relpath}')
        actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
        if actual != digest:
            raise RuntimeError(f'HASH_MISMATCH:{relpath}')
    print(f'MANIFEST_OK {len(records)} files')

if __name__ == '__main__':
    verify()
