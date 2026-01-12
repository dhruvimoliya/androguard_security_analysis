# Android Security Analysis Tools

Python-based static analysis tools for Android APK security assessment using the Androguard framework. These tools automate the extraction and analysis of security-relevant features from Android applications.

## Overview

This repository contains two security analysis tools developed for automated APK assessment:

1. **APK Static Information Extractor** - Comprehensive metadata and security feature extraction
2. **Permission Risk Analyzer** - Privacy-focused permission analysis tool

## Features

### APK Static Information Extractor
- **Package Information**: Extract app package name and basic metadata
- **Component Analysis**: Identify all activities, services, providers, and receivers
- **Permission Analysis**: List all permissions requested by the application
- **Class Structure**: Extract all class names present in the APK
- **Intent Filter Detection**: Identify and count intent-filters
- **Security Indicators**:
  - Crypto code detection
  - Dynamic code loading detection
  - Reflection usage detection
- **Risk Assessment**: Calculate Androguard risk score
- **Error Handling**: Comprehensive error checking for APK decompilation issues

### Permission Risk Analyzer
Analyzes applications for privacy-sensitive permissions including:
- SMS permissions (SEND_SMS, READ_SMS, RECEIVE_SMS)
- Contact access (READ_CONTACTS, WRITE_CONTACTS)
- Location tracking (ACCESS_FINE_LOCATION)
- Audio recording (RECORD_AUDIO)
- Phone state access (READ_PHONE_STATE)
- Network access (INTERNET)

## Requirements

```bash
pip install androguard
```

**Dependencies:**
- Python 3.x
- Androguard library (`androguard.misc`, `androguard.core.analysis.analysis`)

## Installation

```bash
# Clone the repository
git clone https://github.com/dhruvimoliya/android-security-analysis.git
cd android-security-analysis

# Install dependencies
pip install androguard
```

## Usage

### Static Information Extraction

```bash
python androguardscript.py <path_to_apk_file>
```

**Example:**
```bash
python androguardscript.py .\samples\allreflection.apk
```

**Output includes:**
```
Package Name: com.example.sms
Total Activities: 3
Total Services: 0
Total Providers: 0
Total Receivers: 0
Total Permissions: 3
Total Classes: 476
Total Intent Filters: 2
Has crypto code: No
Has dynamic code: No
Has reflection code: Yes
Risk Score: 16
```

### Permission Analysis

```bash
python permission_checker.py <path_to_apk_file>
```

**Example:**
```bash
python permission_checker.py .\samples\allreflection.apk
```

**Output:**
```
Analyzing: .\samples\allreflection.apk
========================================
 ✓ SEND_SMS
 ✓ READ_PHONE_STATE
========================================
Total: 2 out of 9 permissions found
```

## Technical Details

**Static Analysis Approach:**
- Uses Androguard's `AnalyzeAPK` for APK decompilation and analysis
- Extracts information from Android Manifest and DEX files
- Performs bytecode analysis for security feature detection
- No dynamic execution or runtime analysis

**Security Features Detected:**
1. **Crypto Code**: Identifies usage of cryptographic libraries
2. **Dynamic Code**: Detects runtime code loading (potential security risk)
3. **Reflection**: Identifies Java reflection usage (can indicate obfuscation)

## Error Handling

Both tools include comprehensive error handling for:
- Invalid APK files
- Corrupted or malformed APKs
- Missing required components
- Decompilation failures

## Use Cases

- **Security Research**: Analyze malicious or suspicious APKs
- **Privacy Assessment**: Identify over-permissioned applications
- **App Vetting**: Screen applications before deployment
- **Educational**: Learn Android security model and static analysis
- **Penetration Testing**: Initial reconnaissance for mobile app assessments

## Limitations

- **Static Analysis Only**: Cannot detect runtime behaviors
- **Obfuscation**: May have difficulty with heavily obfuscated code
- **No Dynamic Analysis**: Does not execute the application
- **Androguard Dependency**: Analysis quality depends on Androguard's capabilities

## Future Enhancements

- [ ] Support for batch APK analysis
- [ ] JSON/CSV export for automated reporting
- [ ] Integration with VirusTotal API for malware detection
- [ ] Visualization of app components and permissions
- [ ] Advanced obfuscation detection
- [ ] Network security configuration analysis

## Learning Outcomes

This project demonstrates:
- Understanding of Android security model and permission system
- Static analysis techniques for mobile applications
- Python scripting for security automation
- Security risk assessment methodologies
- Mobile application security fundamentals

## Legal Disclaimer

⚠️ **Important**: These tools are for educational and authorized security research purposes only.

- Only analyze applications you own or have explicit permission to test
- Respect privacy and intellectual property rights
- Comply with applicable laws and regulations in your jurisdiction
- The author is not responsible for misuse of these tools

## References

- [Androguard Documentation](https://androguard.readthedocs.io/)
- [Android Security Overview](https://source.android.com/security)
- [OWASP Mobile Security Project](https://owasp.org/www-project-mobile-security/)

## Author

**Dhruvi Moliya**
- GitHub: [@dhruvimoliya](https://github.com/dhruvimoliya)
- LinkedIn: [dhruvi-moliya](https://linkedin.com/in/dhruvi-moliya-)
- Medium: [@Mirage43](https://medium.com/@Mirage43)

## License

This project is open source and available for educational purposes.

---

**Note**: Developed as part of mobile security research coursework at Gujarat University.