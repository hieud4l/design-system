#!/usr/bin/env python3
"""
Design Token Converter
Converts CSS custom properties to Style Dictionary JSON format.

Usage:
    python token_converter.py --input tokens.css --output tokens.json
"""

import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional


class TokenConverter:
    """Converts CSS custom properties to Style Dictionary JSON tokens."""
    
    # Token type detection patterns
    COLOR_PATTERN = re.compile(r'^#[0-9A-Fa-f]{3,8}$|^rgb|^hsl|^var\(--color')
    DIMENSION_PATTERN = re.compile(r'^\d+(\.\d+)?(px|rem|em|%|vh|vw)$')
    FONT_FAMILY_PATTERN = re.compile(r'[a-zA-Z\s,\-]+')
    FONT_WEIGHT_PATTERN = re.compile(r'^\d{3}$|^(normal|bold|lighter|bolder)$')
    SHADOW_PATTERN = re.compile(r'^\d+.*\d+.*#[0-9A-Fa-f]')
    
    def __init__(self):
        self.tokens = {}
        
    def parse_css_file(self, file_path: str) -> Dict[str, Any]:
        """Parse CSS file and extract custom properties."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract CSS custom properties
        # Pattern: --property-name: value;
        pattern = r'--([a-zA-Z0-9\-]+)\s*:\s*([^;]+);'
        matches = re.findall(pattern, content)
        
        css_tokens = {}
        for name, value in matches:
            css_tokens[name] = value.strip()
        
        return css_tokens
    
    def detect_token_type(self, value: str) -> str:
        """Detect the type of token based on its value."""
        value = value.strip()
        
        # Check for color
        if self.COLOR_PATTERN.match(value):
            return "color"
        
        # Check for dimension (size, spacing, etc.)
        if self.DIMENSION_PATTERN.match(value):
            return "dimension"
        
        # Check for font weight
        if self.FONT_WEIGHT_PATTERN.match(value):
            return "fontWeight"
        
        # Check for shadow
        if self.SHADOW_PATTERN.match(value):
            return "shadow"
        
        # Check for font family (contains letters and spaces)
        if ',' in value or 'sans' in value or 'serif' in value or 'mono' in value:
            return "fontFamily"
        
        # Default to string
        return "string"
    
    def parse_token_name(self, name: str) -> List[str]:
        """Parse token name into hierarchy.
        
        Example: 'color-brand-primary' -> ['color', 'brand', 'primary']
        """
        return name.split('-')
    
    def build_token_hierarchy(self, css_tokens: Dict[str, str]) -> Dict[str, Any]:
        """Build hierarchical token structure from flat CSS tokens."""
        tokens = {}
        
        for name, value in css_tokens.items():
            parts = self.parse_token_name(name)
            token_type = self.detect_token_type(value)
            
            # Navigate/create nested structure
            current = tokens
            for i, part in enumerate(parts[:-1]):
                if part not in current:
                    current[part] = {}
                current = current[part]
            
            # Add the final token with value and type
            final_key = parts[-1]
            current[final_key] = {
                "value": value,
                "type": token_type
            }
        
        return tokens
    
    def convert_reference(self, value: str) -> str:
        """Convert CSS var() references to Style Dictionary references.
        
        Example: var(--color-primary) -> {color.primary}
        """
        if 'var(--' in value:
            # Extract variable name
            match = re.search(r'var\(--([a-zA-Z0-9\-]+)\)', value)
            if match:
                var_name = match.group(1)
                # Convert to Style Dictionary reference
                ref_path = var_name.replace('-', '.')
                return f"{{{ref_path}}}"
        return value
    
    def process_references(self, tokens: Dict[str, Any]) -> Dict[str, Any]:
        """Process all token values to convert CSS references to SD references."""
        def process_value(obj):
            if isinstance(obj, dict):
                if 'value' in obj:
                    obj['value'] = self.convert_reference(obj['value'])
                for key, value in obj.items():
                    obj[key] = process_value(value)
            return obj
        
        return process_value(tokens)
    
    def convert(self, input_file: str, validate: bool = False) -> Dict[str, Any]:
        """Convert CSS file to Style Dictionary JSON format."""
        # Parse CSS file
        css_tokens = self.parse_css_file(input_file)
        
        if not css_tokens:
            raise ValueError(f"No CSS custom properties found in {input_file}")
        
        # Build hierarchical structure
        tokens = self.build_token_hierarchy(css_tokens)
        
        # Process references
        tokens = self.process_references(tokens)
        
        # Validate if requested
        if validate:
            self.validate_tokens(tokens)
        
        return tokens
    
    def validate_tokens(self, tokens: Dict[str, Any]) -> None:
        """Basic validation of token structure."""
        def validate_node(node, path=""):
            if isinstance(node, dict):
                if 'value' in node and 'type' in node:
                    # This is a token leaf node
                    if not node['value']:
                        raise ValueError(f"Empty value at {path}")
                    if not node['type']:
                        raise ValueError(f"Empty type at {path}")
                else:
                    # This is a category node
                    for key, value in node.items():
                        new_path = f"{path}.{key}" if path else key
                        validate_node(value, new_path)
        
        validate_node(tokens)
    
    def save_json(self, tokens: Dict[str, Any], output_file: str, pretty: bool = True) -> None:
        """Save tokens to JSON file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            if pretty:
                json.dump(tokens, f, indent=2, ensure_ascii=False)
            else:
                json.dump(tokens, f, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(
        description='Convert CSS custom properties to Style Dictionary JSON format'
    )
    parser.add_argument(
        '--input',
        required=True,
        help='Input CSS file path'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='Output JSON file path'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate tokens after conversion'
    )
    parser.add_argument(
        '--format',
        choices=['pretty', 'compact'],
        default='pretty',
        help='Output format (default: pretty)'
    )
    
    args = parser.parse_args()
    
    # Check input file exists
    if not Path(args.input).exists():
        print(f"Error: Input file '{args.input}' not found")
        return 1
    
    try:
        # Convert tokens
        converter = TokenConverter()
        tokens = converter.convert(args.input, validate=args.validate)
        
        # Save to file
        pretty = args.format == 'pretty'
        converter.save_json(tokens, args.output, pretty=pretty)
        
        print(f"✓ Successfully converted {args.input} to {args.output}")
        print(f"  Found {len(tokens)} token categories")
        
        if args.validate:
            print("✓ Validation passed")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
