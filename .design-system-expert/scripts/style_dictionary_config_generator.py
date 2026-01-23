#!/usr/bin/env python3
"""
Style Dictionary Config Generator
Generates Style Dictionary configuration files.

Usage:
    python style_dictionary_config_generator.py --platforms web,ios,android --output config.json
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Any


class StyleDictionaryConfigGenerator:
    """Generates Style Dictionary configuration."""
    
    PLATFORM_CONFIGS = {
        "web": {
            "transformGroup": "css",
            "buildPath": "build/css/",
            "files": [{
                "destination": "variables.css",
                "format": "css/variables"
            }]
        },
        "scss": {
            "transformGroup": "scss",
            "buildPath": "build/scss/",
            "files": [{
                "destination": "_variables.scss",
                "format": "scss/variables"
            }]
        },
        "ios": {
            "transformGroup": "ios",
            "buildPath": "build/ios/",
            "files": [{
                "destination": "StyleDictionary.h",
                "format": "ios/macros"
            }, {
                "destination": "StyleDictionary.m",
                "format": "ios/strings"
            }]
        },
        "android": {
            "transformGroup": "android",
            "buildPath": "build/android/",
            "files": [{
                "destination": "colors.xml",
                "format": "android/colors"
            }, {
                "destination": "dimens.xml",
                "format": "android/dimens"
            }]
        },
        "json": {
            "transformGroup": "js",
            "buildPath": "build/json/",
            "files": [{
                "destination": "tokens.json",
                "format": "json/flat"
            }]
        }
    }
    
    def __init__(self):
        self.config = {
            "source": ["tokens/**/*.json"],
            "platforms": {}
        }
    
    def add_platform(self, platform_name: str) -> None:
        """Add a platform configuration."""
        if platform_name not in self.PLATFORM_CONFIGS:
            raise ValueError(f"Unknown platform: {platform_name}")
        
        self.config["platforms"][platform_name] = self.PLATFORM_CONFIGS[platform_name]
    
    def add_custom_transform(self, name: str, transform_type: str, transformer: str) -> None:
        """Add a custom transform to the configuration."""
        if "transform" not in self.config:
            self.config["transform"] = {}
        
        self.config["transform"][name] = {
            "type": transform_type,
            "transformer": transformer
        }
    
    def set_source(self, source_patterns: List[str]) -> None:
        """Set source file patterns."""
        self.config["source"] = source_patterns
    
    def generate(self) -> Dict[str, Any]:
        """Generate the complete configuration."""
        return self.config
    
    def save(self, output_file: str, pretty: bool = True) -> None:
        """Save configuration to file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            if pretty:
                json.dump(self.config, f, indent=2)
            else:
                json.dump(self.config, f)


def main():
    parser = argparse.ArgumentParser(
        description='Generate Style Dictionary configuration'
    )
    parser.add_argument(
        '--platforms',
        required=True,
        help='Comma-separated list of platforms (web, scss, ios, android, json)'
    )
    parser.add_argument(
        '--source',
        default='tokens/**/*.json',
        help='Source file pattern (default: tokens/**/*.json)'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='Output configuration file path'
    )
    parser.add_argument(
        '--format',
        choices=['pretty', 'compact'],
        default='pretty',
        help='Output format (default: pretty)'
    )
    
    args = parser.parse_args()
    
    # Parse platforms
    platforms = [p.strip() for p in args.platforms.split(',')]
    
    try:
        # Generate configuration
        generator = StyleDictionaryConfigGenerator()
        
        # Set source if provided
        if args.source:
            generator.set_source([args.source])
        
        # Add platforms
        for platform in platforms:
            if platform not in StyleDictionaryConfigGenerator.PLATFORM_CONFIGS:
                print(f"⚠️  Unknown platform: {platform} (skipping)")
                continue
            generator.add_platform(platform)
        
        if not generator.config["platforms"]:
            print("Error: No valid platforms specified")
            return 1
        
        # Save configuration
        pretty = args.format == 'pretty'
        generator.save(args.output, pretty=pretty)
        
        print(f"✓ Style Dictionary configuration created: {args.output}")
        print(f"  Platforms: {', '.join(generator.config['platforms'].keys())}")
        print(f"\nNext steps:")
        print(f"  1. Install Style Dictionary: npm install -g style-dictionary")
        print(f"  2. Build tokens: style-dictionary build --config {args.output}")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
