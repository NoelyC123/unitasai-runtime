"""
Pytest configuration for UnitasAI runtime.

This file ensures that the runtime root is on sys.path so that
observatory modules can be imported in tests exactly as they are
during normal runtime execution.

This is test-only infrastructure.
No runtime or observatory logic is affected.
"""

import sys
from pathlib import Path

# Add runtime root (parent of tests/) to sys.path
RUNTIME_ROOT = Path(__file__).resolve().parents[1]

if str(RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(RUNTIME_ROOT))
