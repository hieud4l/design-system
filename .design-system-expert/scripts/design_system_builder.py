#!/usr/bin/env python3
"""
Design System Builder
Generates a complete design system structure with tokens, config, and documentation.

Usage:
    python design_system_builder.py --name "My Design System" --brand-color "#3B82F6" --output design-system/
"""

import json
import argparse
from pathlib import Path
from typing import Dict, Any, List


class DesignSystemBuilder:
    """Builds a complete design system structure."""
    
    def __init__(self, name: str, brand_color: str = "#3B82F6"):
        self.name = name
        self.brand_color = brand_color
        
    def create_directory_structure(self, output_dir: Path) -> None:
        """Create the design system directory structure."""
        directories = [
            output_dir,
            output_dir / "tokens",
            output_dir / "build",
            output_dir / "build" / "css",
            output_dir / "build" / "scss",
            output_dir / "docs",
            output_dir / "components"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def generate_color_tokens(self) -> Dict[str, Any]:
        """Generate color tokens based on brand color."""
        return {
            "color": {
                "brand": {
                    "primary": {"value": self.brand_color, "type": "color"},
                    "secondary": {"value": "#8B5CF6", "type": "color"}
                },
                "semantic": {
                    "success": {"value": "#10B981", "type": "color"},
                    "warning": {"value": "#F59E0B", "type": "color"},
                    "error": {"value": "#EF4444", "type": "color"},
                    "info": {"value": "#3B82F6", "type": "color"}
                },
                "neutral": {
                    "50": {"value": "#F9FAFB", "type": "color"},
                    "100": {"value": "#F3F4F6", "type": "color"},
                    "200": {"value": "#E5E7EB", "type": "color"},
                    "300": {"value": "#D1D5DB", "type": "color"},
                    "400": {"value": "#9CA3AF", "type": "color"},
                    "500": {"value": "#6B7280", "type": "color"},
                    "600": {"value": "#4B5563", "type": "color"},
                    "700": {"value": "#374151", "type": "color"},
                    "800": {"value": "#1F2937", "type": "color"},
                    "900": {"value": "#111827", "type": "color"}
                },
                "background": {
                    "primary": {"value": "#FFFFFF", "type": "color"},
                    "secondary": {"value": "{color.neutral.50}", "type": "color"}
                },
                "text": {
                    "primary": {"value": "{color.neutral.900}", "type": "color"},
                    "secondary": {"value": "{color.neutral.600}", "type": "color"},
                    "tertiary": {"value": "{color.neutral.400}", "type": "color"}
                }
            }
        }
    
    def generate_typography_tokens(self) -> Dict[str, Any]:
        """Generate typography tokens."""
        return {
            "font": {
                "family": {
                    "sans": {"value": "Inter, system-ui, -apple-system, sans-serif", "type": "fontFamily"},
                    "mono": {"value": "Fira Code, Consolas, monospace", "type": "fontFamily"}
                },
                "size": {
                    "xs": {"value": "0.75rem", "type": "dimension"},
                    "sm": {"value": "0.875rem", "type": "dimension"},
                    "base": {"value": "1rem", "type": "dimension"},
                    "lg": {"value": "1.125rem", "type": "dimension"},
                    "xl": {"value": "1.25rem", "type": "dimension"},
                    "2xl": {"value": "1.5rem", "type": "dimension"},
                    "3xl": {"value": "1.875rem", "type": "dimension"},
                    "4xl": {"value": "2.25rem", "type": "dimension"}
                },
                "weight": {
                    "normal": {"value": "400", "type": "fontWeight"},
                    "medium": {"value": "500", "type": "fontWeight"},
                    "semibold": {"value": "600", "type": "fontWeight"},
                    "bold": {"value": "700", "type": "fontWeight"}
                },
                "lineHeight": {
                    "tight": {"value": "1.25", "type": "number"},
                    "normal": {"value": "1.5", "type": "number"},
                    "relaxed": {"value": "1.75", "type": "number"}
                }
            }
        }
    
    def generate_spacing_tokens(self) -> Dict[str, Any]:
        """Generate spacing tokens."""
        return {
            "spacing": {
                "0": {"value": "0", "type": "dimension"},
                "1": {"value": "0.25rem", "type": "dimension"},
                "2": {"value": "0.5rem", "type": "dimension"},
                "3": {"value": "0.75rem", "type": "dimension"},
                "4": {"value": "1rem", "type": "dimension"},
                "5": {"value": "1.25rem", "type": "dimension"},
                "6": {"value": "1.5rem", "type": "dimension"},
                "8": {"value": "2rem", "type": "dimension"},
                "10": {"value": "2.5rem", "type": "dimension"},
                "12": {"value": "3rem", "type": "dimension"},
                "16": {"value": "4rem", "type": "dimension"},
                "20": {"value": "5rem", "type": "dimension"},
                "24": {"value": "6rem", "type": "dimension"}
            }
        }
    
    def generate_shadow_tokens(self) -> Dict[str, Any]:
        """Generate shadow tokens."""
        return {
            "shadow": {
                "sm": {"value": "0 1px 2px 0 rgba(0, 0, 0, 0.05)", "type": "shadow"},
                "base": {"value": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)", "type": "shadow"},
                "md": {"value": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)", "type": "shadow"},
                "lg": {"value": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)", "type": "shadow"},
                "xl": {"value": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)", "type": "shadow"}
            }
        }
    
    def generate_border_tokens(self) -> Dict[str, Any]:
        """Generate border tokens."""
        return {
            "border": {
                "radius": {
                    "none": {"value": "0", "type": "dimension"},
                    "sm": {"value": "0.125rem", "type": "dimension"},
                    "base": {"value": "0.25rem", "type": "dimension"},
                    "md": {"value": "0.375rem", "type": "dimension"},
                    "lg": {"value": "0.5rem", "type": "dimension"},
                    "xl": {"value": "0.75rem", "type": "dimension"},
                    "full": {"value": "9999px", "type": "dimension"}
                },
                "width": {
                    "none": {"value": "0", "type": "dimension"},
                    "thin": {"value": "1px", "type": "dimension"},
                    "base": {"value": "2px", "type": "dimension"},
                    "thick": {"value": "4px", "type": "dimension"}
                }
            }
        }
    
    def generate_style_dictionary_config(self) -> Dict[str, Any]:
        """Generate Style Dictionary configuration."""
        return {
            "source": ["tokens/**/*.json"],
            "platforms": {
                "css": {
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
                }
            }
        }
    
    def generate_package_json(self) -> Dict[str, Any]:
        """Generate package.json for npm scripts."""
        return {
            "name": self.name.lower().replace(" ", "-"),
            "version": "1.0.0",
            "description": f"{self.name} design system",
            "scripts": {
                "build": "style-dictionary build",
                "clean": "rm -rf build"
            },
            "devDependencies": {
                "style-dictionary": "^3.8.0"
            }
        }
    
    def generate_readme(self) -> str:
        """Generate README.md content."""
        return f"""# {self.name}

A comprehensive design system with design tokens and Style Dictionary integration.

## Getting Started

### Installation

```bash
npm install
```

### Build Tokens

```bash
npm run build
```

This will generate CSS and SCSS variables in the `build/` directory.

## Structure

```
{self.name.lower().replace(" ", "-")}/
├── tokens/           # Design tokens (JSON)
├── build/            # Generated files
│   ├── css/         # CSS variables
│   └── scss/        # SCSS variables
├── components/       # Component specifications
├── docs/            # Documentation
├── config.json      # Style Dictionary config
└── package.json     # npm configuration
```

## Tokens

Design tokens are organized by category:

- **colors.json**: Color palette and semantic colors
- **typography.json**: Font families, sizes, weights, line heights
- **spacing.json**: Spacing scale
- **shadows.json**: Shadow definitions
- **borders.json**: Border radius and width

## Usage

### CSS

```css
@import 'build/css/variables.css';

.button {{
  background: var(--color-brand-primary);
  padding: var(--spacing-4);
  border-radius: var(--border-radius-md);
}}
```

### SCSS

```scss
@import 'build/scss/variables';

.button {{
  background: $color-brand-primary;
  padding: $spacing-4;
  border-radius: $border-radius-md;
}}
```

## Documentation

See the `docs/` directory for detailed documentation.

## License

MIT
"""
    
    def generate_getting_started_doc(self) -> str:
        """Generate getting started documentation."""
        return f"""# Getting Started with {self.name}

## Overview

{self.name} is a design system built with design tokens and Style Dictionary.

## Installation

1. Clone or download this design system
2. Install dependencies:
   ```bash
   npm install
   ```

## Building Tokens

To generate CSS and SCSS variables from design tokens:

```bash
npm run build
```

This will create:
- `build/css/variables.css` - CSS custom properties
- `build/scss/_variables.scss` - SCSS variables

## Using Tokens

### In CSS

```css
@import 'build/css/variables.css';

.my-component {{
  color: var(--color-text-primary);
  background: var(--color-background-primary);
  padding: var(--spacing-4);
}}
```

### In SCSS

```scss
@import 'build/scss/variables';

.my-component {{
  color: $color-text-primary;
  background: $color-background-primary;
  padding: $spacing-4;
}}
```

## Modifying Tokens

1. Edit token files in `tokens/` directory
2. Run `npm run build` to regenerate variables
3. Use the updated variables in your styles

## Next Steps

- Explore token categories in `tokens/`
- Read component documentation in `components/`
- Review design principles in `docs/`
"""
    
    def build(self, output_dir: str, include_examples: bool = True) -> None:
        """Build the complete design system."""
        output_path = Path(output_dir)
        
        print(f"Creating design system: {self.name}")
        print(f"Output directory: {output_path}")
        
        # Create directory structure
        print("Creating directory structure...")
        self.create_directory_structure(output_path)
        
        # Generate and save tokens
        print("Generating tokens...")
        tokens = {
            "colors": self.generate_color_tokens(),
            "typography": self.generate_typography_tokens(),
            "spacing": self.generate_spacing_tokens(),
            "shadows": self.generate_shadow_tokens(),
            "borders": self.generate_border_tokens()
        }
        
        for name, token_data in tokens.items():
            token_file = output_path / "tokens" / f"{name}.json"
            with open(token_file, 'w', encoding='utf-8') as f:
                json.dump(token_data, f, indent=2)
            print(f"  ✓ Created {name}.json")
        
        # Generate Style Dictionary config
        print("Generating Style Dictionary config...")
        config = self.generate_style_dictionary_config()
        config_file = output_path / "config.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        print("  ✓ Created config.json")
        
        # Generate package.json
        print("Generating package.json...")
        package = self.generate_package_json()
        package_file = output_path / "package.json"
        with open(package_file, 'w', encoding='utf-8') as f:
            json.dump(package, f, indent=2)
        print("  ✓ Created package.json")
        
        # Generate README
        print("Generating documentation...")
        readme = self.generate_readme()
        readme_file = output_path / "README.md"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme)
        print("  ✓ Created README.md")
        
        # Generate getting started doc
        getting_started = self.generate_getting_started_doc()
        docs_file = output_path / "docs" / "getting-started.md"
        with open(docs_file, 'w', encoding='utf-8') as f:
            f.write(getting_started)
        print("  ✓ Created docs/getting-started.md")
        
        print(f"\n✅ Design system created successfully!")
        print(f"\nNext steps:")
        print(f"  1. cd {output_path}")
        print(f"  2. npm install")
        print(f"  3. npm run build")


def main():
    parser = argparse.ArgumentParser(
        description='Generate a complete design system structure'
    )
    parser.add_argument(
        '--name',
        required=True,
        help='Design system name'
    )
    parser.add_argument(
        '--brand-color',
        default='#3B82F6',
        help='Primary brand color (hex) (default: #3B82F6)'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='Output directory path'
    )
    parser.add_argument(
        '--include-examples',
        action='store_true',
        help='Include example components'
    )
    
    args = parser.parse_args()
    
    try:
        # Build design system
        builder = DesignSystemBuilder(args.name, args.brand_color)
        builder.build(args.output, args.include_examples)
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
