#!/usr/bin/env python3
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NVIDIA_API_KEY')
BASE_URL = "https://integrate.api.nvidia.com/v1"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

print("\n" + "="*60)
print("   NVIDIA API INTEGRATION TEST SUITE")
print("="*60 + "\n")

# Test 1: List models
print("TEST 1: Fetching Available Models...")
r = requests.get(f"{BASE_URL}/models", headers=HEADERS, timeout=10)
models = r.json()['data']
print(f"   Found {len(models)} models available\n")

# Test 2: DeepSeek models
print("TEST 2: Finding DeepSeek Models...")
deepseek = [m for m in models if 'deepseek' in m['id'].lower()]
print(f"   Found {len(deepseek)} DeepSeek models:")
for m in deepseek:
    print(f"      - {m['id']}")
print()

# Test 3: Model details
print("TEST 3: DeepSeek V4 Flash Details...")
r = requests.get(f"{BASE_URL}/models/deepseek-ai/deepseek-v4-flash", headers=HEADERS, timeout=10)
info = r.json()
print(f"   Model: {info['id']}")
print(f"      Owner: {info['owned_by']}\n")

# Test 4: Live inference
print("TEST 4: Live Inference Test...")
payload = {
    "model": "deepseek-ai/deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Say 'Hello from Nvidia!' in one sentence"}],
    "max_tokens": 50
}
r = requests.post(f"{BASE_URL}/chat/completions", 
    headers={**HEADERS, "Content-Type": "application/json"}, 
    json=payload, timeout=30)
msg = r.json()['choices'][0]['message']['content']
print(f'   Response: "{msg}"\n')

print("="*60)
print("   ALL TESTS PASSED!")
print("="*60 + "\n")
