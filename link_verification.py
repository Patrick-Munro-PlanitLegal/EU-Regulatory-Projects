#!/usr/bin/env python3
"""
EU Regulatory Tracker - Link Verification Script

This script verifies all external links in the EU regulatory tracker
to ensure they are working and accessible.

Author: AI Assistant
Date: August 13, 2025
"""

import requests
import json
import time
from urllib.parse import urlparse
from datetime import datetime
import sys

class LinkVerifier:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.results = {
            'total_links': 0,
            'working_links': 0,
            'broken_links': 0,
            'timeout_links': 0,
            'details': []
        }
    
    def verify_link(self, url, description, timeout=10):
        """Verify if a single link is working"""
        try:
            response = self.session.get(url, timeout=timeout, allow_redirects=True)
            status = response.status_code
            
            if 200 <= status < 400:
                return True, f"✅ Working (Status: {status})"
            else:
                return False, f"❌ Broken (Status: {status})"
                
        except requests.exceptions.Timeout:
            return False, "⏰ Timeout"
        except requests.exceptions.ConnectionError:
            return False, "🔌 Connection Error"
        except requests.exceptions.RequestException as e:
            return False, f"❌ Error: {str(e)}"
        except Exception as e:
            return False, f"❌ Unexpected Error: {str(e)}"
    
    def verify_regulation_links(self, regulation_data):
        """Verify all links for a single regulation"""
        regulation_name = regulation_data['name']
        print(f"\n🔍 Verifying links for: {regulation_name}")
        
        links_to_check = [
            (regulation_data['eurLexUrl'], 'EUR-Lex Document'),
            (regulation_data['germanImplementation']['url'], 'German Authority')
        ]
        
        for url, description in links_to_check:
            if url and url != 'TBD':
                print(f"  Checking {description}: {url}")
                is_working, status = self.verify_link(url, description)
                
                self.results['total_links'] += 1
                if is_working:
                    self.results['working_links'] += 1
                else:
                    self.results['broken_links'] += 1
                
                self.results['details'].append({
                    'regulation': regulation_name,
                    'url': url,
                    'description': description,
                    'status': status,
                    'working': is_working
                })
                
                print(f"    {status}")
                time.sleep(1)  # Be respectful to servers
    
    def verify_all_links(self, database_file):
        """Verify all links in the regulatory database"""
        print("🇪🇺 EU Regulatory Tracker - Link Verification")
        print("=" * 60)
        
        try:
            with open(database_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"📊 Found {len(data['regulations'])} regulations to verify")
            
            for regulation in data['regulations']:
                self.verify_regulation_links(regulation)
            
        except FileNotFoundError:
            print(f"❌ Error: Database file '{database_file}' not found")
            return False
        except json.JSONDecodeError:
            print(f"❌ Error: Invalid JSON in '{database_file}'")
            return False
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False
        
        return True
    
    def generate_report(self):
        """Generate a comprehensive verification report"""
        print("\n" + "=" * 60)
        print("📋 LINK VERIFICATION REPORT")
        print("=" * 60)
        
        # Summary statistics
        print(f"📊 SUMMARY:")
        print(f"   Total Links Checked: {self.results['total_links']}")
        print(f"   ✅ Working Links: {self.results['working_links']}")
        print(f"   ❌ Broken Links: {self.results['broken_links']}")
        print(f"   ⏰ Timeout Links: {self.results['timeout_links']}")
        
        success_rate = (self.results['working_links'] / self.results['total_links'] * 100) if self.results['total_links'] > 0 else 0
        print(f"   📈 Success Rate: {success_rate:.1f}%")
        
        # Detailed results
        if self.results['broken_links'] > 0:
            print(f"\n❌ BROKEN LINKS FOUND:")
            for detail in self.results['details']:
                if not detail['working']:
                    print(f"   • {detail['regulation']} - {detail['description']}")
                    print(f"     URL: {detail['url']}")
                    print(f"     Status: {detail['status']}")
                    print()
        
        # Working links summary
        print(f"✅ WORKING LINKS:")
        for detail in self.results['details']:
            if detail['working']:
                print(f"   • {detail['regulation']} - {detail['description']}")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS:")
        if self.results['broken_links'] == 0:
            print("   🎉 All links are working! No action needed.")
        else:
            print(f"   🔧 Fix {self.results['broken_links']} broken links")
            print("   📝 Update broken URLs in the database")
            print("   🔍 Investigate timeout issues")
        
        # Save detailed report
        report_file = f"link_verification_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'summary': {
                    'total_links': self.results['total_links'],
                    'working_links': self.results['working_links'],
                    'broken_links': self.results['broken_links'],
                    'success_rate': success_rate
                },
                'details': self.results['details']
            }, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Detailed report saved to: {report_file}")
        
        return self.results['broken_links'] == 0

def main():
    """Main function"""
    verifier = LinkVerifier()
    
    # Check if database file exists
    database_file = "eu_regulations_database.json"
    
    if not verifier.verify_all_links(database_file):
        sys.exit(1)
    
    # Generate and display report
    all_working = verifier.generate_report()
    
    # Exit with appropriate code
    sys.exit(0 if all_working else 1)

if __name__ == "__main__":
    main()
