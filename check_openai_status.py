#!/usr/bin/env python3
"""
OpenAI Status Checker

This script helps diagnose OpenAI API issues including quota problems.
"""

import os
from dotenv import load_dotenv
from rsearch_module import check_openai_status

def main():
    """Main function to check OpenAI API status and provide guidance."""

    print("🔍 OpenAI API Status Checker")
    print("=" * 40)

    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")

    # Check if API key is configured
    if not api_key:
        print("❌ OPENAI_API_KEY not found in environment variables")
        print("💡 Please add OPENAI_API_KEY to your .env file")
        return
    
    # Mask the API key for security
    masked_key = f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else "***"
    print(f"🔑 API Key Found: {masked_key}")
    
    # Check API status
    print("\n🌐 Checking OpenAI API status...")
    status = check_openai_status()
    
    print(f"📊 Status: {status['status'].upper()}")
    print(f"📝 Message: {status['message']}")
    
    if status['status'] == 'quota_exceeded':
        print("\n🚨 QUOTA EXCEEDED - Action Required:")
        print("   1. Visit your OpenAI billing dashboard:")
        print(f"      {status.get('action_url', 'https://platform.openai.com/settings/organization/billing')}")
        print("   2. Check your current usage and limits")
        print("   3. Add credits or upgrade your plan")
        print("   4. Verify your payment method is valid")
        print("\n💡 Temporary Solutions:")
        print("   - Use cached responses if available")
        print("   - Wait for quota reset (if on free plan)")
        print("   - Switch to a different OpenAI account temporarily")
        
    elif status['status'] == 'rate_limited':
        print("\n⏰ RATE LIMITED - Temporary Issue:")
        print("   - Wait a few minutes before trying again")
        print("   - The script will automatically retry with backoff")
        
    elif status['status'] == 'auth_error':
        print("\n🔐 AUTHENTICATION ERROR:")
        print("   1. Check your .env file has the correct OPENAI_API_KEY")
        print("   2. Verify the API key is valid at: https://platform.openai.com/api-keys")
        print("   3. Make sure the key hasn't expired")
        
    elif status['status'] == 'ok':
        print("\n✅ OpenAI API is working correctly!")
        print("   You can proceed with your semantic search operations.")
        
    else:
        print(f"\n❓ Unknown status: {status}")
    
    print("\n" + "=" * 40)
    print("🔗 Useful Links:")
    print("   • OpenAI Dashboard: https://platform.openai.com/")
    print("   • Usage & Billing: https://platform.openai.com/settings/organization/billing")
    print("   • API Keys: https://platform.openai.com/api-keys")
    print("   • Error Codes Guide: https://platform.openai.com/docs/guides/error-codes")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error running status check: {e}")
        print("💡 Make sure your .env file is properly configured")
