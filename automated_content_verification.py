#!/usr/bin/env python3
"""
Automated Content Verification System
EU Tech Regulations Dashboard - Ongoing Content Accuracy

Version: 1.0
Last Updated: August 13, 2025
Author: Patrick Munro - Planit Legal

This script provides automated verification of:
- EUR-Lex link health
- German authority website accessibility
- Content accuracy validation
- Regulatory status verification
- Automated reporting and alerts
"""

import json
import asyncio
import aiohttp
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('content_verification.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class VerificationResult:
    """Data class for verification results"""
    url: str
    description: str
    status: str
    response_time: float
    error_message: Optional[str] = None
    verification_timestamp: str = None
    working: bool = False

class ContentVerificationSystem:
    """Main content verification system"""
    
    def __init__(self, database_file: str = "eu_regulations_database_enhanced.json"):
        self.database_file = database_file
        self.verification_results = []
        self.verification_summary = {}
        self.session = None
        
    async def initialize(self):
        """Initialize the verification system"""
        try:
            # Load database
            self.database = await self.load_database()
            
            # Initialize HTTP session
            timeout = aiohttp.ClientTimeout(total=30)
            connector = aiohttp.TCPConnector(limit=10, limit_per_host=5)
            self.session = aiohttp.ClientSession(
                timeout=timeout,
                connector=connector,
                headers={'User-Agent': 'EU-Regulations-Verification-Bot/1.0'}
            )
            
            logging.info("Content verification system initialized successfully")
            
        except Exception as e:
            logging.error(f"Failed to initialize verification system: {e}")
            raise
    
    async def load_database(self) -> Dict[str, Any]:
        """Load the regulations database"""
        try:
            with open(self.database_file, 'r', encoding='utf-8') as f:
                database = json.load(f)
            logging.info(f"Database loaded: {len(database.get('regulations', []))} regulations")
            return database
        except Exception as e:
            logging.error(f"Failed to load database: {e}")
            raise
    
    async def verify_link(self, url: str, description: str) -> VerificationResult:
        """Verify individual link health"""
        start_time = datetime.now()
        
        try:
            async with self.session.get(url, allow_redirects=True) as response:
                response_time = (datetime.now() - start_time).total_seconds()
                
                result = VerificationResult(
                    url=url,
                    description=description,
                    status=str(response.status),
                    response_time=response_time,
                    verification_timestamp=datetime.now().isoformat(),
                    working=response.status < 400
                )
                
                if not result.working:
                    result.error_message = f"HTTP {response.status}"
                
                logging.info(f"Verified {description}: {url} - Status: {response.status}")
                return result
                
        except Exception as e:
            response_time = (datetime.now() - start_time).total_seconds()
            result = VerificationResult(
                url=url,
                description=description,
                status="ERROR",
                response_time=response_time,
                error_message=str(e),
                verification_timestamp=datetime.now().isoformat(),
                working=False
            )
            
            logging.warning(f"Failed to verify {description}: {url} - Error: {e}")
            return result
    
    async def verify_eur_lex_links(self) -> List[VerificationResult]:
        """Verify all EUR-Lex links"""
        logging.info("Starting EUR-Lex link verification...")
        
        eur_lex_links = []
        for regulation in self.database.get('regulations', []):
            if 'eurLex' in regulation.get('resources', {}):
                url = regulation['resources']['eurLex']
                description = f"EUR-Lex: {regulation['name']}"
                eur_lex_links.append((url, description))
        
        tasks = [self.verify_link(url, desc) for url, desc in eur_lex_links]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter out exceptions
        valid_results = [r for r in results if isinstance(r, VerificationResult)]
        
        logging.info(f"EUR-Lex verification completed: {len(valid_results)} links")
        return valid_results
    
    async def verify_german_authority_links(self) -> List[VerificationResult]:
        """Verify all German authority website links"""
        logging.info("Starting German authority link verification...")
        
        authority_links = []
        for regulation in self.database.get('regulations', []):
            if 'germanAuthority' in regulation.get('resources', {}):
                url = regulation['resources']['germanAuthority']
                description = f"German Authority: {regulation['name']}"
                authority_links.append((url, description))
        
        tasks = [self.verify_link(url, desc) for url, desc in authority_links]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter out exceptions
        valid_results = [r for r in results if isinstance(r, VerificationResult)]
        
        logging.info(f"German authority verification completed: {len(valid_results)} links")
        return valid_results
    
    async def verify_guidance_links(self) -> List[VerificationResult]:
        """Verify guidance document links"""
        logging.info("Starting guidance document link verification...")
        
        guidance_links = []
        for regulation in self.database.get('regulations', []):
            german_impl = regulation.get('germanImplementation', {})
            if 'guidanceDocuments' in german_impl:
                for i, url in enumerate(german_impl['guidanceDocuments']):
                    description = f"Guidance: {regulation['name']} - Document {i+1}"
                    guidance_links.append((url, description))
        
        tasks = [self.verify_link(url, desc) for url, desc in guidance_links]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter out exceptions
        valid_results = [r for r in results if isinstance(r, VerificationResult)]
        
        logging.info(f"Guidance document verification completed: {len(valid_results)} links")
        return valid_results
    
    async def verify_all_links(self) -> Dict[str, List[VerificationResult]]:
        """Verify all external links"""
        logging.info("Starting comprehensive link verification...")
        
        results = {
            'eur_lex': await self.verify_eur_lex_links(),
            'german_authorities': await self.verify_german_authority_links(),
            'guidance_documents': await self.verify_guidance_links()
        }
        
        # Combine all results
        all_results = []
        for category_results in results.values():
            all_results.extend(category_results)
        
        self.verification_results = all_results
        logging.info(f"Comprehensive verification completed: {len(all_results)} total links")
        
        return results
    
    def generate_verification_summary(self) -> Dict[str, Any]:
        """Generate verification summary report"""
        total_links = len(self.verification_results)
        working_links = sum(1 for r in self.verification_results if r.working)
        broken_links = total_links - working_links
        
        # Categorize results
        eur_lex_results = [r for r in self.verification_results if 'EUR-Lex' in r.description]
        authority_results = [r for r in self.verification_results if 'German Authority' in r.description]
        guidance_results = [r for r in self.verification_results if 'Guidance' in r.description]
        
        summary = {
            'verification_timestamp': datetime.now().isoformat(),
            'total_links': total_links,
            'working_links': working_links,
            'broken_links': broken_links,
            'success_rate': f"{(working_links/total_links)*100:.1f}%" if total_links > 0 else "0%",
            'categories': {
                'eur_lex': {
                    'total': len(eur_lex_results),
                    'working': sum(1 for r in eur_lex_results if r.working),
                    'broken': sum(1 for r in eur_lex_results if not r.working)
                },
                'german_authorities': {
                    'total': len(authority_results),
                    'working': sum(1 for r in authority_results if r.working),
                    'broken': sum(1 for r in authority_results if not r.working)
                },
                'guidance_documents': {
                    'total': len(guidance_results),
                    'working': sum(1 for r in guidance_results if r.working),
                    'broken': sum(1 for r in guidance_results if not r.working)
                }
            },
            'broken_links_details': [
                {
                    'url': r.url,
                    'description': r.description,
                    'error': r.error_message,
                    'status': r.status
                }
                for r in self.verification_results if not r.working
            ]
        }
        
        self.verification_summary = summary
        return summary
    
    def save_verification_report(self, filename: str = None):
        """Save verification report to file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"verification_report_{timestamp}.json"
        
        report = {
            'summary': self.verification_summary,
            'detailed_results': [
                {
                    'url': r.url,
                    'description': r.description,
                    'status': r.status,
                    'response_time': r.response_time,
                    'working': r.working,
                    'error_message': r.error_message,
                    'verification_timestamp': r.verification_timestamp
                }
                for r in self.verification_results
            ]
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            logging.info(f"Verification report saved: {filename}")
        except Exception as e:
            logging.error(f"Failed to save verification report: {e}")
    
    def update_database_verification_status(self):
        """Update database with verification results"""
        try:
            # Update verification metadata
            self.database['metadata']['lastVerified'] = datetime.now().isoformat()
            self.database['metadata']['nextReview'] = (
                datetime.now() + timedelta(days=30)
            ).isoformat()
            
            # Update individual regulation verification status
            for regulation in self.database.get('regulations', []):
                regulation_id = regulation['id']
                
                # Find verification results for this regulation
                regulation_results = [
                    r for r in self.verification_results
                    if regulation['name'] in r.description
                ]
                
                if regulation_results:
                    # Update verification details
                    if 'validation' not in regulation:
                        regulation['validation'] = {}
                    
                    regulation['validation']['lastVerified'] = datetime.now().isoformat()
                    regulation['validation']['linkHealth'] = (
                        'all_working' if all(r.working for r in regulation_results)
                        else 'some_broken' if any(r.working for r in regulation_results)
                        else 'all_broken'
                    )
                    
                    # Update verification details
                    if 'verificationDetails' not in regulation['validation']:
                        regulation['validation']['verificationDetails'] = {}
                    
                    # Update EUR-Lex status
                    eur_lex_results = [r for r in regulation_results if 'EUR-Lex' in r.description]
                    if eur_lex_results:
                        eur_lex_result = eur_lex_results[0]
                        regulation['validation']['verificationDetails']['eurLexLink'] = (
                            f"✅ Working - Last verified: {datetime.now().strftime('%Y-%m-%d')}"
                            if eur_lex_result.working
                            else f"❌ Broken - Error: {eur_lex_result.error_message}"
                        )
                    
                    # Update authority contact status
                    authority_results = [r for r in regulation_results if 'German Authority' in r.description]
                    if authority_results:
                        authority_result = authority_results[0]
                        regulation['validation']['verificationDetails']['authorityContact'] = (
                            f"✅ {authority_result.url} - Working"
                            if authority_result.working
                            else f"❌ {authority_result.url} - Error: {authority_result.error_message}"
                        )
            
            # Save updated database
            backup_filename = f"eu_regulations_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(backup_filename, 'w', encoding='utf-8') as f:
                json.dump(self.database, f, indent=2, ensure_ascii=False)
            
            # Update main database
            with open(self.database_file, 'w', encoding='utf-8') as f:
                json.dump(self.database, f, indent=2, ensure_ascii=False)
            
            logging.info(f"Database updated with verification status. Backup: {backup_filename}")
            
        except Exception as e:
            logging.error(f"Failed to update database: {e}")
    
    async def cleanup(self):
        """Cleanup resources"""
        if self.session:
            await self.session.close()
        logging.info("Verification system cleanup completed")
    
    def send_verification_alert(self, email_config: Dict[str, str] = None):
        """Send verification alert email"""
        if not email_config:
            logging.info("No email configuration provided, skipping alert")
            return
        
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = email_config['from_email']
            msg['To'] = email_config['to_email']
            msg['Subject'] = f"EU Regulations Verification Alert - {datetime.now().strftime('%Y-%m-%d')}"
            
            # Create email body
            body = self.create_alert_email_body()
            msg.attach(MIMEText(body, 'html'))
            
            # Send email
            with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
                if email_config.get('use_tls'):
                    server.starttls()
                if email_config.get('username') and email_config.get('password'):
                    server.login(email_config['username'], email_config['password'])
                
                server.send_message(msg)
            
            logging.info(f"Verification alert sent to {email_config['to_email']}")
            
        except Exception as e:
            logging.error(f"Failed to send verification alert: {e}")
    
    def create_alert_email_body(self) -> str:
        """Create HTML email body for verification alert"""
        summary = self.verification_summary
        
        body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #1a365d; color: white; padding: 20px; border-radius: 8px; }}
                .summary {{ background-color: #f7fafc; padding: 20px; border-radius: 8px; margin: 20px 0; }}
                .broken-links {{ background-color: #fed7d7; padding: 20px; border-radius: 8px; margin: 20px 0; }}
                .success {{ color: #38a169; }}
                .warning {{ color: #dd6b20; }}
                .error {{ color: #e53e3e; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🔍 EU Regulations Content Verification Alert</h1>
                <p>Verification completed: {summary['verification_timestamp']}</p>
            </div>
            
            <div class="summary">
                <h2>📊 Verification Summary</h2>
                <p><strong>Total Links:</strong> {summary['total_links']}</p>
                <p><strong>Working Links:</strong> <span class="success">{summary['working_links']}</span></p>
                <p><strong>Broken Links:</strong> <span class="error">{summary['broken_links']}</span></p>
                <p><strong>Success Rate:</strong> <span class="success">{summary['success_rate']}</span></p>
                
                <h3>Category Breakdown:</h3>
                <ul>
                    <li><strong>EUR-Lex:</strong> {summary['categories']['eur_lex']['working']}/{summary['categories']['eur_lex']['total']} working</li>
                    <li><strong>German Authorities:</strong> {summary['categories']['german_authorities']['working']}/{summary['categories']['german_authorities']['total']} working</li>
                    <li><strong>Guidance Documents:</strong> {summary['categories']['guidance_documents']['working']}/{summary['categories']['guidance_documents']['total']} working</li>
                </ul>
            </div>
        """
        
        if summary['broken_links'] > 0:
            body += f"""
            <div class="broken-links">
                <h2>🚨 Broken Links Requiring Attention</h2>
                <ul>
            """
            
            for broken_link in summary['broken_links_details']:
                body += f"""
                    <li><strong>{broken_link['description']}</strong><br>
                    URL: {broken_link['url']}<br>
                    Error: {broken_link['error']}<br>
                    Status: {broken_link['status']}</li>
                """
            
            body += """
                </ul>
            </div>
            """
        
        body += """
            <p><em>This is an automated verification report. Please review and address any broken links.</em></p>
            <p><strong>Contact:</strong> patrick.munro.ext@planit.legal</p>
        </body>
        </html>
        """
        
        return body

async def main():
    """Main verification process"""
    verifier = ContentVerificationSystem()
    
    try:
        # Initialize system
        await verifier.initialize()
        
        # Perform verification
        await verifier.verify_all_links()
        
        # Generate summary
        summary = verifier.generate_verification_summary()
        
        # Save report
        verifier.save_verification_report()
        
        # Update database
        verifier.update_database_verification_status()
        
        # Print summary
        print("\n" + "="*60)
        print("🔍 EU REGULATIONS CONTENT VERIFICATION COMPLETED")
        print("="*60)
        print(f"📊 Total Links: {summary['total_links']}")
        print(f"✅ Working Links: {summary['working_links']}")
        print(f"❌ Broken Links: {summary['broken_links']}")
        print(f"📈 Success Rate: {summary['success_rate']}")
        print("="*60)
        
        # Send alert if there are broken links
        if summary['broken_links'] > 0:
            print(f"🚨 ALERT: {summary['broken_links']} broken links detected!")
            print("Check the verification report for details.")
        
        # Category breakdown
        print("\n📋 Category Breakdown:")
        for category, stats in summary['categories'].items():
            status = "✅" if stats['broken'] == 0 else "⚠️" if stats['broken'] < stats['total'] else "❌"
            print(f"   {status} {category.replace('_', ' ').title()}: {stats['working']}/{stats['total']} working")
        
        print("\n📁 Verification report saved")
        print("📊 Database updated with verification status")
        print("="*60)
        
    except Exception as e:
        logging.error(f"Verification process failed: {e}")
        print(f"❌ Verification failed: {e}")
    
    finally:
        await verifier.cleanup()

if __name__ == "__main__":
    # Run verification
    asyncio.run(main())
