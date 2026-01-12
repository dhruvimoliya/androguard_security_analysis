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

if len(sys.argv) != 2 :
	print("Usage: python permission_checker.py <apk_file>")
	sys.exit(1)
	
Permissions_of_interest = [ 
    "SEND_SMS",
    "READ_SMS",
    "RECEIVE_SMS",
    "READ_CONTACTS",
    "WRITE_CONTACTS",
    "ACCESS_FINE_LOCATION",
    "RECORD_AUDIO",
    "READ_PHONE_STATE",
    "INTERNET"
]

apk_path = sys.argv[1]

try:
	a, d, dx = AnalyzeAPK(apk_path)
	
	print(f"Analyzing: {apk_path}")
	print("="*40)
	
	all_permissions = a.get_permissions()
	
	count = 0 
	for perm in Permissions_of_interest:
		found = False
		for apk_perm in all_permissions:
			if perm in apk_perm:
				print(f" ✓ {perm}")
				count += 1
				found = True
				break
	print("="*40)
	print(f"Total: {count} out of {len(Permissions_of_interest)} permissions found")
	
except Exception as e:
	print(f"Error: Failed to analyze APK - {e}")
	sys.exit(1)