#!/usr/bin/env python3
"""
Convert CSS custom properties from token.md to Style Dictionary JSON format
"""

import json
import re
from pathlib import Path

def parse_css_value(value):
    """Parse CSS value and convert to appropriate format"""
    value = value.strip().rstrip(';')
    
    # Handle rgb() format
    if 'rgb(' in value:
        # Convert rgb(255 255 255) to #ffffff
        match = re.search(r'rgb\((\d+)\s+(\d+)\s+(\d+)(?:\s*/\s*[\d.]+)?\)', value)
        if match:
            r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
            return f"#{r:02x}{g:02x}{b:02x}"
        # Handle rgba format
        match = re.search(r'rgba?\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)', value)
        if match:
            r, g, b, a = int(match.group(1)), int(match.group(2)), int(match.group(3)), float(match.group(4))
            if a == 0:
                return "rgba(0, 0, 0, 0)"
            return value
    
    # Handle var() references - keep as is for now
    if value.startswith('var('):
        return value
    
    # Handle calc() - keep as is
    if 'calc(' in value:
        return value
    
    return value

def parse_token_name(css_var):
    """Convert CSS variable name to nested JSON structure"""
    # Remove -- prefix
    name = css_var.replace('--', '')
    
    # Split by - and handle special cases
    parts = name.split('-')
    
    return parts, name

def create_nested_dict(parts, value, token_type):
    """Create nested dictionary structure from parts list"""
    result = {}
    current = result
    
    for i, part in enumerate(parts[:-1]):
        if part not in current:
            current[part] = {}
        current = current[part]
    
    # Set the final value
    current[parts[-1]] = {
        "value": value,
        "type": token_type
    }
    
    return result

def merge_dicts(dict1, dict2):
    """Deep merge two dictionaries"""
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            merge_dicts(dict1[key], value)
        else:
            dict1[key] = value
    return dict1

def determine_token_type(name, value):
    """Determine the token type based on name and value"""
    name_lower = name.lower()
    
    if 'color' in name_lower or 'bg' in name_lower or 'fg' in name_lower or 'border' in name_lower or 'text' in name_lower:
        return 'color'
    elif 'shadow' in name_lower:
        return 'boxShadow'
    elif 'radius' in name_lower:
        return 'borderRadius'
    elif 'font-family' in name_lower or 'font' in name_lower and ('inter' in value.lower() or 'mono' in value.lower()):
        return 'fontFamily'
    elif 'spacing' in name_lower or 'width' in name_lower or 'height' in name_lower or 'breakpoint' in name_lower:
        return 'dimension'
    elif 'line-height' in name_lower:
        return 'lineHeight'
    elif 'letter-spacing' in name_lower:
        return 'letterSpacing'
    elif 'text-' in name_lower and ('xs' in name_lower or 'sm' in name_lower or 'md' in name_lower or 'lg' in name_lower or 'xl' in name_lower or 'display' in name_lower):
        return 'fontSize'
    elif 'animate' in name_lower:
        return 'animation'
    else:
        return 'other'

def parse_css_tokens(css_content):
    """Parse CSS custom properties and convert to JSON structure"""
    tokens = {}
    
    # Find all CSS custom property declarations
    pattern = r'--([a-zA-Z0-9_-]+):\s*([^;]+);'
    matches = re.findall(pattern, css_content)
    
    for var_name, value in matches:
        full_name = f"--{var_name}"
        parsed_value = parse_css_value(value)
        token_type = determine_token_type(var_name, parsed_value)
        
        parts, original_name = parse_token_name(full_name)
        
        # Create nested structure
        nested = create_nested_dict(parts, parsed_value, token_type)
        
        # Merge into main tokens dict
        tokens = merge_dicts(tokens, nested)
    
    return tokens

def main():
    # Read the token.md file
    token_file = Path('/Users/tatrunghieu/Desktop/Vibe_coding/design system/token.md')
    
    with open(token_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Parse tokens
    tokens = parse_css_tokens(css_content)
    
    # Write to JSON file
    output_file = Path('/Users/tatrunghieu/Desktop/Vibe_coding/design system/tokens.json')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(tokens, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Successfully converted {len(tokens)} token categories to {output_file}")
    print(f"📊 Token categories: {', '.join(sorted(tokens.keys()))}")

if __name__ == '__main__':
    main()
