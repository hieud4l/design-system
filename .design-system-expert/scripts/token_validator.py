#!/usr/bin/env python3
"""
Design Token Validator
Validates design token structure, naming, and values.

Usage:
    python token_validator.py --input tokens.json --check-all --output report.md
"""

import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional


class TokenValidator:
    """Validates design tokens for correctness and best practices."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate_file(self, file_path: str, checks: Dict[str, bool]) -> Tuple[bool, str]:
        """Validate a token file and return results."""
        # Load tokens
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tokens = json.load(f)
        except json.JSONDecodeError as e:
            return False, f"Invalid JSON: {e}"
        except Exception as e:
            return False, f"Error reading file: {e}"
        
        # Run checks
        if checks.get('naming', False):
            self.check_naming_conventions(tokens)
        
        if checks.get('values', False):
            self.check_token_values(tokens)
        
        if checks.get('references', False):
            self.check_references(tokens)
        
        if checks.get('duplicates', False):
            self.check_duplicates(tokens)
        
        # Determine overall result
        has_errors = len(self.errors) > 0
        
        return not has_errors, self.generate_report()
    
    def check_naming_conventions(self, tokens: Dict[str, Any], path: str = "") -> None:
        """Check that token names follow conventions."""
        for key, value in tokens.items():
            current_path = f"{path}.{key}" if path else key
            
            # Check key naming (should be lowercase, kebab-case or camelCase)
            if not re.match(r'^[a-z][a-z0-9\-]*$', key):
                self.warnings.append(
                    f"Non-standard naming at '{current_path}': '{key}' "
                    f"(should be lowercase kebab-case)"
                )
            
            # Check for abbreviations (potential issue)
            if len(key) <= 2 and key not in ['xs', 'sm', 'md', 'lg', 'xl']:
                self.warnings.append(
                    f"Possible abbreviation at '{current_path}': '{key}' "
                    f"(consider using full words)"
                )
            
            # Recurse if not a leaf node
            if isinstance(value, dict) and 'value' not in value:
                self.check_naming_conventions(value, current_path)
    
    def check_token_values(self, tokens: Dict[str, Any], path: str = "") -> None:
        """Validate token values are correct for their type."""
        for key, value in tokens.items():
            current_path = f"{path}.{key}" if path else key
            
            if isinstance(value, dict):
                if 'value' in value and 'type' in value:
                    # This is a token leaf node
                    self.validate_token_value(current_path, value)
                else:
                    # Recurse
                    self.check_token_values(value, current_path)
    
    def validate_token_value(self, path: str, token: Dict[str, Any]) -> None:
        """Validate a single token's value matches its type."""
        value = token.get('value', '')
        token_type = token.get('type', '')
        
        # Skip references
        if isinstance(value, str) and value.startswith('{') and value.endswith('}'):
            return
        
        # Validate based on type
        if token_type == 'color':
            self.validate_color(path, value)
        elif token_type == 'dimension':
            self.validate_dimension(path, value)
        elif token_type == 'fontWeight':
            self.validate_font_weight(path, value)
        elif token_type == 'fontFamily':
            self.validate_font_family(path, value)
        elif token_type == 'shadow':
            self.validate_shadow(path, value)
    
    def validate_color(self, path: str, value: str) -> None:
        """Validate color value."""
        # Hex color
        if re.match(r'^#[0-9A-Fa-f]{3}$|^#[0-9A-Fa-f]{6}$|^#[0-9A-Fa-f]{8}$', value):
            return
        
        # RGB/RGBA
        if re.match(r'^rgba?\(', value):
            return
        
        # HSL/HSLA
        if re.match(r'^hsla?\(', value):
            return
        
        self.errors.append(
            f"Invalid color value at '{path}': '{value}' "
            f"(should be hex, rgb, or hsl)"
        )
    
    def validate_dimension(self, path: str, value: str) -> None:
        """Validate dimension value."""
        if not re.match(r'^\d+(\.\d+)?(px|rem|em|%|vh|vw|pt)$', str(value)):
            self.errors.append(
                f"Invalid dimension value at '{path}': '{value}' "
                f"(should be number with unit: px, rem, em, %, vh, vw, pt)"
            )
    
    def validate_font_weight(self, path: str, value: str) -> None:
        """Validate font weight value."""
        valid_weights = ['100', '200', '300', '400', '500', '600', '700', '800', '900']
        valid_keywords = ['normal', 'bold', 'lighter', 'bolder']
        
        if str(value) not in valid_weights and value not in valid_keywords:
            self.errors.append(
                f"Invalid font weight at '{path}': '{value}' "
                f"(should be 100-900 or normal/bold/lighter/bolder)"
            )
    
    def validate_font_family(self, path: str, value: str) -> None:
        """Validate font family value."""
        if not value or not isinstance(value, str):
            self.errors.append(
                f"Invalid font family at '{path}': '{value}' "
                f"(should be a non-empty string)"
            )
    
    def validate_shadow(self, path: str, value: str) -> None:
        """Validate shadow value."""
        # Basic check for shadow format (offset-x offset-y blur spread color)
        if not re.search(r'\d+.*\d+', value):
            self.warnings.append(
                f"Possibly invalid shadow at '{path}': '{value}' "
                f"(should contain offset and blur values)"
            )
    
    def check_references(self, tokens: Dict[str, Any]) -> None:
        """Check that all token references resolve correctly."""
        # Collect all token paths
        all_paths = set()
        
        def collect_paths(obj, path=""):
            if isinstance(obj, dict):
                if 'value' in obj:
                    all_paths.add(path)
                else:
                    for key, value in obj.items():
                        new_path = f"{path}.{key}" if path else key
                        collect_paths(value, new_path)
        
        collect_paths(tokens)
        
        # Check all references
        def check_refs(obj, path=""):
            if isinstance(obj, dict):
                if 'value' in obj:
                    value = obj['value']
                    if isinstance(value, str) and value.startswith('{') and value.endswith('}'):
                        # This is a reference
                        ref = value[1:-1]  # Remove { }
                        if ref not in all_paths:
                            self.errors.append(
                                f"Unresolved reference at '{path}': '{value}' "
                                f"(token '{ref}' does not exist)"
                            )
                else:
                    for key, value in obj.items():
                        new_path = f"{path}.{key}" if path else key
                        check_refs(value, new_path)
        
        check_refs(tokens)
    
    def check_duplicates(self, tokens: Dict[str, Any]) -> None:
        """Check for duplicate token values."""
        values_map = {}
        
        def collect_values(obj, path=""):
            if isinstance(obj, dict):
                if 'value' in obj:
                    value = obj['value']
                    # Skip references
                    if not (isinstance(value, str) and value.startswith('{') and value.endswith('}')):
                        if value not in values_map:
                            values_map[value] = []
                        values_map[value].append(path)
                else:
                    for key, val in obj.items():
                        new_path = f"{path}.{key}" if path else key
                        collect_values(val, new_path)
        
        collect_values(tokens)
        
        # Report duplicates
        for value, paths in values_map.items():
            if len(paths) > 1:
                self.info.append(
                    f"Duplicate value '{value}' found in: {', '.join(paths)} "
                    f"(consider using references)"
                )
    
    def generate_report(self) -> str:
        """Generate validation report."""
        report = []
        report.append("# Design Token Validation Report\n")
        
        # Summary
        report.append("## Summary\n")
        report.append(f"- Errors: {len(self.errors)}")
        report.append(f"- Warnings: {len(self.warnings)}")
        report.append(f"- Info: {len(self.info)}\n")
        
        # Errors
        if self.errors:
            report.append("## Errors\n")
            for error in self.errors:
                report.append(f"❌ {error}")
            report.append("")
        
        # Warnings
        if self.warnings:
            report.append("## Warnings\n")
            for warning in self.warnings:
                report.append(f"⚠️  {warning}")
            report.append("")
        
        # Info
        if self.info:
            report.append("## Information\n")
            for info in self.info:
                report.append(f"ℹ️  {info}")
            report.append("")
        
        # Conclusion
        if not self.errors:
            report.append("## Conclusion\n")
            report.append("✅ Validation passed! No errors found.")
        else:
            report.append("## Conclusion\n")
            report.append(f"❌ Validation failed with {len(self.errors)} error(s).")
        
        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description='Validate design tokens'
    )
    parser.add_argument(
        '--input',
        required=True,
        help='Input JSON token file path'
    )
    parser.add_argument(
        '--check-naming',
        action='store_true',
        help='Check naming conventions'
    )
    parser.add_argument(
        '--check-values',
        action='store_true',
        help='Validate token values'
    )
    parser.add_argument(
        '--check-references',
        action='store_true',
        help='Check token references'
    )
    parser.add_argument(
        '--check-duplicates',
        action='store_true',
        help='Check for duplicate values'
    )
    parser.add_argument(
        '--check-all',
        action='store_true',
        help='Run all checks'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )
    parser.add_argument(
        '--output',
        help='Output report file path (optional)'
    )
    
    args = parser.parse_args()
    
    # Check input file exists
    if not Path(args.input).exists():
        print(f"Error: Input file '{args.input}' not found")
        return 1
    
    # Determine which checks to run
    checks = {
        'naming': args.check_naming or args.check_all,
        'values': args.check_values or args.check_all,
        'references': args.check_references or args.check_all,
        'duplicates': args.check_duplicates or args.check_all
    }
    
    if not any(checks.values()):
        print("Error: No checks specified. Use --check-all or specific --check-* flags")
        return 1
    
    try:
        # Validate tokens
        validator = TokenValidator()
        success, report = validator.validate_file(args.input, checks)
        
        # Print report
        print(report)
        
        # Save report if output specified
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\n✓ Report saved to {args.output}")
        
        # Check strict mode
        if args.strict and validator.warnings:
            print("\n❌ Strict mode: Treating warnings as errors")
            return 1
        
        return 0 if success else 1
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
