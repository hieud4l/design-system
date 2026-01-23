# Design Token Standards

A comprehensive guide to design tokens, their categories, naming conventions, and best practices.

## What are Design Tokens?

Design tokens are the atomic design decisions that make up your design system. They are platform-agnostic values that can be transformed into platform-specific formats (CSS, SCSS, iOS, Android, etc.).

## Token Categories

### 1. Color Tokens

Color tokens define the color palette for your design system.

**Structure**:
```json
{
  "color": {
    "brand": {
      "primary": { "value": "#3B82F6", "type": "color" },
      "secondary": { "value": "#8B5CF6", "type": "color" }
    },
    "semantic": {
      "success": { "value": "#10B981", "type": "color" },
      "warning": { "value": "#F59E0B", "type": "color" },
      "error": { "value": "#EF4444", "type": "color" }
    }
  }
}
```

**Best Practices**:
- Use semantic names (success, error) not descriptive names (green, red)
- Create neutral scales (50-900) for grays
- Define light and dark mode variants
- Limit primary palette to 5-7 colors

### 2. Typography Tokens

Typography tokens define font families, sizes, weights, and line heights.

**Structure**:
```json
{
  "font": {
    "family": {
      "sans": { "value": "Inter, sans-serif", "type": "fontFamily" }
    },
    "size": {
      "base": { "value": "1rem", "type": "dimension" }
    },
    "weight": {
      "normal": { "value": "400", "type": "fontWeight" }
    },
    "lineHeight": {
      "normal": { "value": "1.5", "type": "number" }
    }
  }
}
```

**Best Practices**:
- Use a type scale (1.25 or 1.333 ratio)
- Limit to 2 font families maximum
- Define clear weight hierarchy
- Set appropriate line heights (1.5 for body, 1.2 for headings)

### 3. Spacing Tokens

Spacing tokens define the spacing scale for margins, padding, and gaps.

**Structure**:
```json
{
  "spacing": {
    "0": { "value": "0", "type": "dimension" },
    "1": { "value": "0.25rem", "type": "dimension" },
    "2": { "value": "0.5rem", "type": "dimension" },
    "4": { "value": "1rem", "type": "dimension" }
  }
}
```

**Best Practices**:
- Use a consistent scale (4px, 8px, 16px, etc.)
- Base on multiples of 4 or 8
- Include 0 for no spacing
- Use rem units for accessibility

### 4. Shadow Tokens

Shadow tokens define elevation and depth.

**Structure**:
```json
{
  "shadow": {
    "sm": { "value": "0 1px 2px 0 rgba(0, 0, 0, 0.05)", "type": "shadow" },
    "md": { "value": "0 4px 6px -1px rgba(0, 0, 0, 0.1)", "type": "shadow" }
  }
}
```

**Best Practices**:
- Create 3-5 elevation levels
- Use subtle shadows for depth
- Consider light and dark mode variants
- Test on different backgrounds

### 5. Border Tokens

Border tokens define border radius and width.

**Structure**:
```json
{
  "border": {
    "radius": {
      "sm": { "value": "0.125rem", "type": "dimension" },
      "md": { "value": "0.25rem", "type": "dimension" }
    },
    "width": {
      "thin": { "value": "1px", "type": "dimension" }
    }
  }
}
```

## Token Hierarchy

Organize tokens in three levels:

### 1. Global Tokens (Base Values)

Foundation values that rarely change:
```json
{
  "color": {
    "blue": {
      "500": { "value": "#3B82F6", "type": "color" }
    }
  }
}
```

### 2. Alias Tokens (Semantic References)

Semantic references to global tokens:
```json
{
  "color": {
    "primary": { "value": "{color.blue.500}", "type": "color" }
  }
}
```

### 3. Component Tokens (Component-Specific)

Component-specific values:
```json
{
  "button": {
    "background": { "value": "{color.primary}", "type": "color" }
  }
}
```

## Naming Conventions

### Pattern

```
{category}-{property}-{variant}-{state}
```

### Examples

**Good**:
- `color-background-primary`
- `color-text-secondary`
- `font-size-heading-lg`
- `spacing-component-md`
- `shadow-elevation-high`

**Bad**:
- `blue` (not semantic)
- `bg-1` (unclear meaning)
- `s-md` (too abbreviated)
- `buttonColor` (camelCase instead of kebab-case)

### Rules

1. **Use kebab-case**: `color-primary` not `colorPrimary`
2. **Be descriptive**: `button-padding-large` not `btn-pd-lg`
3. **Use semantic names**: `color-success` not `color-green`
4. **Follow hierarchy**: category → property → variant → state
5. **Avoid abbreviations**: Write full words for clarity

## Token Types

Style Dictionary supports these token types:

- `color`: Color values (hex, rgb, hsl)
- `dimension`: Size values with units (px, rem, em)
- `fontFamily`: Font family names
- `fontWeight`: Font weight values
- `number`: Unitless numbers
- `shadow`: Box shadow values
- `string`: Text strings

## Token References

Reference other tokens using curly braces:

```json
{
  "color": {
    "blue": { "value": "#3B82F6", "type": "color" },
    "primary": { "value": "{color.blue}", "type": "color" }
  }
}
```

**Benefits**:
- Single source of truth
- Easy updates
- Maintain relationships
- Reduce duplication

## Light/Dark Mode

Support multiple modes using `$extensions`:

```json
{
  "color": {
    "background": {
      "primary": {
        "value": "#FFFFFF",
        "type": "color",
        "$extensions": {
          "mode": {
            "light": "#FFFFFF",
            "dark": "#1F2937"
          }
        }
      }
    }
  }
}
```

## File Organization

Organize tokens by category:

```
tokens/
├── colors.json
├── typography.json
├── spacing.json
├── shadows.json
├── borders.json
└── components/
    ├── button.json
    └── input.json
```

## Validation Checklist

- [ ] All tokens have `value` and `type`
- [ ] Names follow kebab-case convention
- [ ] Semantic naming used
- [ ] No circular references
- [ ] Values match their types
- [ ] References resolve correctly
- [ ] Organized by category
- [ ] Documented with comments

## Common Mistakes

1. **Using descriptive names**: `color-blue` instead of `color-primary`
2. **Inconsistent naming**: Mixing camelCase and kebab-case
3. **Too many tokens**: Creating tokens for every value
4. **Circular references**: Token A references B which references A
5. **Wrong types**: Color value with dimension type
6. **Deep nesting**: More than 4 levels deep
7. **No documentation**: Tokens without context

## Best Practices

1. **Start small**: Begin with essential tokens
2. **Use references**: Avoid hardcoded duplicates
3. **Document decisions**: Explain why tokens exist
4. **Version control**: Track changes over time
5. **Validate regularly**: Check for errors
6. **Test outputs**: Verify generated files
7. **Keep it DRY**: Don't repeat yourself
8. **Think semantically**: Name by purpose, not appearance
