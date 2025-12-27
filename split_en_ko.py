#!/usr/bin/env python3
"""
Split bilingual EN/KO markdown files into separate language versions.

Usage: python3 split_en_ko.py <pillar_directory>
Example: python3 split_en_ko.py 01-DHARMIC
"""

import os
import re
import sys
from pathlib import Path


def split_content_section(content):
    """
    Split a content section into English and Korean parts.
    Returns (en_content, ko_content)
    """
    # Pattern: **English:** ... **한국어:** ...
    en_pattern = r'\*\*English:\*\*\s*\n(.*?)(?=\*\*한국어:\*\*|\n##|\Z)'
    ko_pattern = r'\*\*한국어:\*\*\s*\n(.*?)(?=\n##|\*\*English:\*\*|\Z)'

    en_match = re.search(en_pattern, content, re.DOTALL)
    ko_match = re.search(ko_pattern, content, re.DOTALL)

    en_content = en_match.group(1).strip() if en_match else ''
    ko_content = ko_match.group(1).strip() if ko_match else ''

    return en_content, ko_content


def should_keep_in_both(line, context_lines, idx):
    """
    Determine if a line should be kept in both EN and KO versions.
    """
    line_strip = line.strip()

    # Bilingual headers (with |)
    if '|' in line and line.startswith('#'):
        return True

    # Horizontal rules
    if line_strip == '---':
        return True

    # Section headers
    if line.startswith('##'):
        return True

    # Tables
    if line_strip.startswith('|'):
        return True

    # Footer content
    if any(marker in line for marker in ['弘益人間', 'WIA-Wisdom', 'Benefit All Humanity']):
        return True

    if line_strip.startswith('*This document') or line_strip.startswith('*이 문서'):
        return True

    # Cross-references, Sources sections (usually no language markers)
    if idx > 0:
        # Check previous lines for section headers
        for i in range(max(0, idx - 5), idx):
            prev_line = context_lines[i].strip()
            if prev_line.startswith('##') and any(keyword in prev_line for keyword in
                ['Cross-Reference', '상호 참조', 'Sources', '출처', 'Primary Sources', '1차 자료', 'References', '참고']):
                return True

    return False


def split_markdown_file(content):
    """
    Split a bilingual markdown file into English and Korean versions.
    Returns (en_version, ko_version)
    """
    lines = content.split('\n')
    en_lines = []
    ko_lines = []

    i = 0
    in_english_block = False
    in_korean_block = False

    while i < len(lines):
        line = lines[i]
        line_strip = line.strip()

        # Check if this line should be in both versions
        if should_keep_in_both(line, lines, i):
            en_lines.append(line)
            ko_lines.append(line)
            i += 1
            continue

        # Summary lines (> at the start)
        if line.startswith('>'):
            # First summary is English, second is Korean
            if i + 1 < len(lines) and lines[i + 1].startswith('>'):
                en_lines.append(line)
                ko_lines.append(lines[i + 1])
                i += 2
            else:
                en_lines.append(line)
                ko_lines.append(line)
                i += 1
            continue

        # Detect language block markers
        if line_strip == '**English:**':
            in_english_block = True
            in_korean_block = False
            i += 1
            continue

        if line_strip == '**한국어:**':
            in_korean_block = True
            in_english_block = False
            i += 1
            continue

        # If in English block
        if in_english_block:
            # Stop at Korean marker or section boundary
            if line_strip == '**한국어:**' or line.startswith('##') or line_strip == '---':
                in_english_block = False
                if line.startswith('##') or line_strip == '---':
                    # Process this line in next iteration
                    continue
                else:
                    i += 1
                    in_korean_block = True
                    continue
            en_lines.append(line)
            i += 1
            continue

        # If in Korean block
        if in_korean_block:
            # Stop at English marker or section boundary
            if line_strip == '**English:**' or line.startswith('##') or line_strip == '---':
                in_korean_block = False
                if line.startswith('##') or line_strip == '---':
                    # Process this line in next iteration
                    continue
                else:
                    i += 1
                    in_english_block = True
                    continue
            ko_lines.append(line)
            i += 1
            continue

        # Empty lines - add to current context
        if not line_strip:
            if in_english_block:
                en_lines.append(line)
            elif in_korean_block:
                ko_lines.append(line)
            else:
                # Add to both when outside language blocks
                en_lines.append(line)
                ko_lines.append(line)
            i += 1
            continue

        # Default: likely shared content
        i += 1

    # Clean up excessive blank lines
    def clean_lines(lines):
        result = []
        prev_blank = False
        for line in lines:
            if not line.strip():
                if not prev_blank:
                    result.append(line)
                    prev_blank = True
            else:
                result.append(line)
                prev_blank = False
        # Remove trailing blank lines
        while result and not result[-1].strip():
            result.pop()
        return result

    en_lines = clean_lines(en_lines)
    ko_lines = clean_lines(ko_lines)

    return '\n'.join(en_lines), '\n'.join(ko_lines)


def process_file(file_path, pillar_dir):
    """
    Process a single markdown file: split and save EN/KO versions.
    """
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content
    en_content, ko_content = split_markdown_file(content)

    # Determine relative path from pillar directory
    rel_path = os.path.relpath(file_path, pillar_dir)

    # Create EN version path
    en_path = os.path.join(pillar_dir, 'en', rel_path)
    os.makedirs(os.path.dirname(en_path), exist_ok=True)

    # Create KO version path
    ko_path = os.path.join(pillar_dir, 'ko', rel_path)
    os.makedirs(os.path.dirname(ko_path), exist_ok=True)

    # Write EN version
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(en_content)

    # Write KO version
    with open(ko_path, 'w', encoding='utf-8') as f:
        f.write(ko_content)

    print(f"  → EN: {en_path}")
    print(f"  → KO: {ko_path}")

    # Remove original file
    os.remove(file_path)
    print(f"  ✓ Removed: {file_path}")


def process_pillar(pillar_dir):
    """
    Process all markdown files in a pillar directory.
    """
    pillar_path = Path(pillar_dir)

    if not pillar_path.exists():
        print(f"Error: Directory {pillar_dir} not found")
        return

    # Find all .md files (excluding en/ and ko/ subdirectories if they exist)
    md_files = []
    for root, dirs, files in os.walk(pillar_dir):
        # Skip en/ and ko/ subdirectories
        if '/en/' in root or '/ko/' in root:
            continue

        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    print(f"\nFound {len(md_files)} markdown files in {pillar_dir}\n")

    for md_file in sorted(md_files):
        process_file(md_file, pillar_dir)

    print(f"\n✓ Completed processing {pillar_dir}")
    print(f"  Total files split: {len(md_files)}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 split_en_ko.py <pillar_directory>")
        print("Example: python3 split_en_ko.py 01-DHARMIC")
        sys.exit(1)

    pillar_dir = sys.argv[1]
    process_pillar(pillar_dir)
