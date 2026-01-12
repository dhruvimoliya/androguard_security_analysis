import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import logging
logging.basicConfig(level=logging.ERROR, force=True)

logging.disable(logging.CRITICAL)

import io
old_stderr = sys.stderr
sys.stderr = io.StringIO()

from androguard.misc import AnalyzeAPK
from androguard.core.analysis.analysis import Analysis

sys.stderr = old_stderr

class SuppressOutput:
    def __enter__(self):
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr

apk_path = sys.argv[1]

with SuppressOutput():
    a, d, dx = AnalyzeAPK(apk_path)

logging.disable(logging.NOTSET)

print(f"Package Name: {a.get_package()}")
print(f"Total Activities: {len(a.get_activities())}")
print(f"Total Services: {len(a.get_services())}")
print(f"Total Providers: {len(a.get_providers())}")
print(f"Total Receivers: {len(a.get_receivers())}")
print(f"Total Permissions: {len(a.get_permissions())}")
print(f"Total Classes: {len(list(dx.get_classes()))}")

intent_filters = 0
for activity in a.get_activities():
    intent_filters += len(a.get_intent_filters("activity", activity))
for service in a.get_services():
    intent_filters += len(a.get_intent_filters("service", service))
for receiver in a.get_receivers():
    intent_filters += len(a.get_intent_filters("receiver", receiver))
print(f"Total Intent Filters: {intent_filters}")

has_crypto = False
for cls in dx.get_classes():
    if 'crypto' in cls.name.lower() or 'security' in cls.name.lower():
        has_crypto = True
        break
print(f"Has crypto code: {'Yes' if has_crypto else 'No'}")

has_dynamic = False
for cls in dx.get_classes():
    if 'DexClassLoader' in cls.name or 'PathClassLoader' in cls.name:
        has_dynamic = True
        break
print(f"Has dynamic code: {'Yes' if has_dynamic else 'No'}")

has_reflection = False
for method in dx.get_methods():
    if 'java/lang/reflect' in str(method.get_method()):
        has_reflection = True
        break
print(f"Has reflection code: {'Yes' if has_reflection else 'No'}")

risk = len(a.get_permissions()) * 2
if has_dynamic:
    risk += 20
if has_reflection:
    risk += 10
print(f"Risk Score: {min(risk, 100)}")