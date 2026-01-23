# Design System Expert Skill

A comprehensive skill for creating, managing, and scaling design systems with design tokens, Style Dictionary integration, and component generation.

## Overview

This skill provides tools and workflows for:
- **Design Token Management**: Create, convert, and validate design tokens
- **Style Dictionary Integration**: Set up and configure token transformation
- **CSS Architecture**: Organize scalable CSS with best practices
- **Component Generation**: Generate component specs and implementation code
- **Design System Documentation**: Create comprehensive design system docs

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 14+ (for Style Dictionary)
- Basic understanding of CSS and design tokens

### Installation

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Style Dictionary (optional, for token transformation)
npm install -g style-dictionary
```

## Directory Structure

```
design-system-expert/
├── SKILL.md                    # Main skill instructions
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── scripts/                    # Helper scripts
│   ├── token_converter.py      # Convert CSS to JSON tokens
│   ├── token_validator.py      # Validate token structure
│   ├── design_system_builder.py # Generate design system
│   ├── component_generator.py  # Create component specs
│   └── style_dictionary_config_generator.py # Generate SD config
├── resources/                  # Reference documentation
│   ├── design_token_standards.md
│   ├── css_architecture_guide.md
│   ├── component_patterns.md
│   └── naming_conventions.md
└── examples/                   # Sample files
    ├── sample_tokens.json
    ├── sample_component.md
    ├── sample_style_dictionary_config.json
    └── sample_design_system.md
```

## Common Use Cases

### 1. Create a New Design System

```bash
python scripts/design_system_builder.py \
  --name "My Design System" \
  --brand-color "#3B82F6" \
  --output my-design-system/
```

### 2. Convert CSS Variables to JSON Tokens

```bash
python scripts/token_converter.py \
  --input styles/variables.css \
  --output tokens.json \
  --validate
```

### 3. Validate Design Tokens

```bash
python scripts/token_validator.py \
  --input tokens.json \
  --check-all \
  --output validation_report.md
```

### 4. Generate Components

```bash
python scripts/component_generator.py \
  --components button,input,card \
  --tokens tokens.json \
  --output components/
```

### 5. Generate Style Dictionary Config

```bash
python scripts/style_dictionary_config_generator.py \
  --platforms web,scss,ios \
  --output config.json
```

## Key Features

### Token Conversion
- Convert CSS custom properties to Style Dictionary JSON format
- Support for colors, typography, spacing, shadows, and more
- Handle light/dark mode variants
- Automatic type detection

### Token Validation
- Check naming conventions
- Validate token values (colors, dimensions, etc.)
- Verify token references
- Detect circular dependencies
- Generate validation reports

### Design System Builder
- Generate complete design system structure
- Create token files organized by category
- Set up Style Dictionary configuration
- Include documentation templates
- Add build scripts

### Component Generation
- Create component documentation
- Generate CSS/SCSS implementation
- Include accessibility guidelines
- Add usage examples
- Support multiple variants and states

### Style Dictionary Integration
- Generate configuration files
- Support multiple platforms (web, iOS, Android)
- Configure transforms and formats
- Custom transform support

## Workflows

### New Design System from Scratch

1. Generate design system structure
2. Customize tokens
3. Build with Style Dictionary
4. Generate components
5. Document the system

### Migrate from CSS to Tokens

1. Convert existing CSS variables
2. Validate converted tokens
3. Set up Style Dictionary
4. Build and test outputs
5. Update components to use tokens

### Add New Components

1. Define component requirements
2. Generate component specs
3. Implement using design tokens
4. Document usage
5. Add to component library

## Best Practices

- **Use semantic naming**: `color-primary` not `color-blue`
- **Organize hierarchically**: Global → Alias → Component tokens
- **Keep it DRY**: Use token references to avoid duplication
- **Version control**: Track all changes to tokens and components
- **Document decisions**: Explain the "why" behind design choices
- **Validate regularly**: Run validation before building
- **Test outputs**: Verify generated files work as expected

## Resources

- **SKILL.md**: Complete instructions and workflows
- **resources/**: Best practices and standards documentation
- **examples/**: Sample tokens, components, and configurations

## Getting Help

1. Read `SKILL.md` for detailed instructions
2. Check `resources/` for standards and guidelines
3. Review `examples/` for reference implementations
4. Run scripts with `--help` flag for usage information

## Contributing

When adding new features:
- Follow existing code style
- Add documentation to SKILL.md
- Include examples
- Update this README if needed

## License

Part of the Skills Master collection.
