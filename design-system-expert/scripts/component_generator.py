#!/usr/bin/env python3
"""
Component Generator
Generates component specifications and implementation code.

Usage:
    python component_generator.py --components button,input,card --tokens tokens.json --output components/
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Any


class ComponentGenerator:
    """Generates component documentation and code."""
    
    COMPONENT_TEMPLATES = {
        "button": {
            "purpose": "Trigger actions and events with clear visual hierarchy",
            "variants": ["primary", "secondary", "tertiary", "danger"],
            "states": ["default", "hover", "active", "disabled", "loading"],
            "props": {
                "size": ["sm", "md", "lg"],
                "variant": ["primary", "secondary", "tertiary", "danger"],
                "disabled": "boolean",
                "loading": "boolean",
                "icon": "optional icon component"
            }
        },
        "input": {
            "purpose": "Accept user text input",
            "variants": ["text", "email", "password", "number"],
            "states": ["default", "focus", "error", "disabled"],
            "props": {
                "type": ["text", "email", "password", "number"],
                "placeholder": "string",
                "disabled": "boolean",
                "error": "boolean",
                "helperText": "string"
            }
        },
        "card": {
            "purpose": "Group related content in a contained format",
            "variants": ["default", "elevated", "outlined"],
            "states": ["default", "hover", "active"],
            "props": {
                "variant": ["default", "elevated", "outlined"],
                "padding": ["sm", "md", "lg"],
                "clickable": "boolean"
            }
        },
        "modal": {
            "purpose": "Display content in a layer above the main interface",
            "variants": ["default", "fullscreen"],
            "states": ["open", "closed", "opening", "closing"],
            "props": {
                "open": "boolean",
                "onClose": "function",
                "size": ["sm", "md", "lg", "fullscreen"],
                "closeOnOverlayClick": "boolean"
            }
        },
        "dropdown": {
            "purpose": "Display a list of options when triggered",
            "variants": ["default", "multi-select"],
            "states": ["closed", "open", "disabled"],
            "props": {
                "options": "array",
                "value": "any",
                "onChange": "function",
                "placeholder": "string",
                "disabled": "boolean"
            }
        },
        "tooltip": {
            "purpose": "Provide contextual information on hover or focus",
            "variants": ["default", "info", "warning", "error"],
            "states": ["hidden", "visible"],
            "props": {
                "content": "string",
                "position": ["top", "right", "bottom", "left"],
                "variant": ["default", "info", "warning", "error"]
            }
        },
        "badge": {
            "purpose": "Display small count or status indicators",
            "variants": ["default", "success", "warning", "error"],
            "states": ["default"],
            "props": {
                "variant": ["default", "success", "warning", "error"],
                "count": "number",
                "max": "number"
            }
        }
    }
    
    def __init__(self, tokens_file: str = None):
        self.tokens = {}
        if tokens_file and Path(tokens_file).exists():
            with open(tokens_file, 'r', encoding='utf-8') as f:
                self.tokens = json.load(f)
    
    def generate_component_doc(self, component_name: str) -> str:
        """Generate component documentation."""
        if component_name not in self.COMPONENT_TEMPLATES:
            raise ValueError(f"Unknown component: {component_name}")
        
        template = self.COMPONENT_TEMPLATES[component_name]
        
        doc = f"""# {component_name.capitalize()} Component

## Purpose

{template['purpose']}

## Variants

"""
        for variant in template['variants']:
            doc += f"- **{variant}**: {variant.capitalize()} style\n"
        
        doc += "\n## States\n\n"
        for state in template['states']:
            doc += f"- {state.capitalize()}\n"
        
        doc += "\n## Props/Attributes\n\n"
        for prop, prop_type in template['props'].items():
            if isinstance(prop_type, list):
                doc += f"- **{prop}**: {' | '.join(prop_type)}\n"
            else:
                doc += f"- **{prop}**: {prop_type}\n"
        
        doc += """
## Accessibility

- Use semantic HTML elements
- Include ARIA labels where appropriate
- Ensure keyboard navigation support
- Maintain minimum 44x44px touch target
- Provide visible focus indicators
- Support screen readers

## Usage Examples

### Basic Usage

```html
<{component_name} variant="primary">
  Click me
</{component_name}>
```

### With Props

```html
<{component_name} 
  variant="primary"
  size="lg"
  disabled="false">
  Click me
</{component_name}>
```

## Best Practices

- Use appropriate variant for the context
- Provide clear labels or content
- Handle loading and error states
- Ensure accessibility compliance
- Test on multiple devices and browsers
"""
        
        return doc.replace("{component_name}", component_name)
    
    def generate_component_css(self, component_name: str) -> str:
        """Generate component CSS implementation."""
        if component_name not in self.COMPONENT_TEMPLATES:
            raise ValueError(f"Unknown component: {component_name}")
        
        template = self.COMPONENT_TEMPLATES[component_name]
        
        css = f"""/* {component_name.capitalize()} Component Styles */

.{component_name} {{
  /* Base styles */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-family-sans, sans-serif);
  font-size: var(--font-size-base, 1rem);
  font-weight: var(--font-weight-medium, 500);
  line-height: var(--font-lineHeight-normal, 1.5);
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  
  /* Default spacing */
  padding: var(--spacing-3, 0.75rem) var(--spacing-4, 1rem);
  border-radius: var(--border-radius-md, 0.375rem);
}}

/* Variants */
"""
        
        for variant in template['variants']:
            css += f""".{component_name}--{variant} {{
  background: var(--color-{variant}, #3B82F6);
  color: var(--color-white, #FFFFFF);
}}

.{component_name}--{variant}:hover {{
  opacity: 0.9;
}}

"""
        
        css += "/* States */\n"
        for state in template['states']:
            if state == 'disabled':
                css += f""".{component_name}:disabled,
.{component_name}--disabled {{
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}}

"""
            elif state == 'hover':
                css += f""".{component_name}:hover {{
  transform: translateY(-1px);
  box-shadow: var(--shadow-md, 0 4px 6px rgba(0,0,0,0.1));
}}

"""
            elif state == 'active':
                css += f""".{component_name}:active {{
  transform: translateY(0);
}}

"""
        
        # Add size variants if applicable
        if 'size' in template['props']:
            css += "/* Sizes */\n"
            sizes = {
                'sm': ('--spacing-2', '--spacing-3', '--font-size-sm'),
                'md': ('--spacing-3', '--spacing-4', '--font-size-base'),
                'lg': ('--spacing-4', '--spacing-6', '--font-size-lg')
            }
            for size, (pad_y, pad_x, font) in sizes.items():
                css += f""".{component_name}--{size} {{
  padding: var({pad_y}, 0.5rem) var({pad_x}, 1rem);
  font-size: var({font}, 1rem);
}}

"""
        
        return css
    
    def generate_component(self, component_name: str, output_dir: Path, include_css: bool = True) -> None:
        """Generate component documentation and optionally CSS."""
        # Generate documentation
        doc = self.generate_component_doc(component_name)
        doc_file = output_dir / f"{component_name}.md"
        with open(doc_file, 'w', encoding='utf-8') as f:
            f.write(doc)
        print(f"  ✓ Created {component_name}.md")
        
        # Generate CSS if requested
        if include_css:
            css = self.generate_component_css(component_name)
            css_file = output_dir / f"{component_name}.css"
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(css)
            print(f"  ✓ Created {component_name}.css")


def main():
    parser = argparse.ArgumentParser(
        description='Generate component specifications and code'
    )
    parser.add_argument(
        '--components',
        required=True,
        help='Comma-separated list of components to generate (e.g., button,input,card)'
    )
    parser.add_argument(
        '--tokens',
        help='Path to tokens JSON file (optional)'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='Output directory path'
    )
    parser.add_argument(
        '--include-docs',
        action='store_true',
        default=True,
        help='Include component documentation (default: true)'
    )
    parser.add_argument(
        '--include-css',
        action='store_true',
        default=True,
        help='Include CSS implementation (default: true)'
    )
    
    args = parser.parse_args()
    
    # Parse components list
    components = [c.strip() for c in args.components.split(',')]
    
    # Create output directory
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)
    
    try:
        # Initialize generator
        generator = ComponentGenerator(args.tokens)
        
        print(f"Generating {len(components)} component(s)...")
        
        # Generate each component
        for component in components:
            if component not in ComponentGenerator.COMPONENT_TEMPLATES:
                print(f"⚠️  Unknown component: {component} (skipping)")
                continue
            
            generator.generate_component(
                component,
                output_path,
                include_css=args.include_css
            )
        
        print(f"\n✅ Components generated successfully in {output_path}")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
