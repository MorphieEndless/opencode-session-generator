#!/usr/bin/env python3
"""
OpenCode Session Header 批量生成工具
支持生成：
1. 标准 UUID 格式（推荐，通用性最广）
2. 官方 CLI 风格前缀（ses_xxx）
3. 完整请求头键值对
4. JSON 格式
"""

import uuid
import secrets
import string
import argparse
import json

def gen_uuid():
    return str(uuid.uuid4())

def gen_ses_prefix(length=26):
    chars = string.ascii_lowercase + string.digits
    rand_str = ''.join(secrets.choice(chars) for _ in range(length))
    return f"ses_{rand_str}"

def main():
    parser = argparse.ArgumentParser(description="OpenCode Session Header 批量生成器")
    parser.add_argument("-n", "--count", type=int, default=5, help="生成数量（默认 5）")
    parser.add_argument("-t", "--type", choices=["uuid", "ses", "header", "json"], default="uuid", 
                        help="生成类型: uuid(默认标准UUID), ses(ses_前缀), header(键值对), json(JSON格式)")
    args = parser.parse_args()

    results = []
    for _ in range(args.count):
        if args.type == "ses":
            val = gen_ses_prefix()
        else:
            val = gen_uuid()

        if args.type == "header":
            results.append(f"x-opencode-session: {val}")
        elif args.type == "json":
            results.append({"x-opencode-session": val})
        else:
            results.append(val)

    if args.type == "json":
        print(json.dumps(results, indent=2))
    else:
        for item in results:
            print(item)

if __name__ == "__main__":
    main()
