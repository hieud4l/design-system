# Sample Design System

A comprehensive design system example demonstrating best practices.

## Overview

This design system provides a foundation for building consistent, accessible user interfaces.

## Design Principles

1. **Clarity**: Every element has a clear purpose
2. **Consistency**: Patterns repeat across the product
3. **Efficiency**: Minimize user effort
4. **Accessibility**: Usable by everyone
5. **Delight**: Thoughtful micro-interactions

## Color System

### Brand Colors

- **Primary**: `#3B82F6` - Main brand color for primary actions
- **Secondary**: `#8B5CF6` - Supporting brand color

### Semantic Colors

- **Success**: `#10B981` - Positive actions and feedback
- **Warning**: `#F59E0B` - Cautionary messages
- **Error**: `#EF4444` - Errors and destructive actions
- **Info**: `#3B82F6` - Informational messages

### Neutral Scale

A 10-step gray scale from 50 (lightest) to 900 (darkest):
- 50, 100, 200, 300, 400, 500, 600, 700, 800, 900

## Typography

### Font Families

- **Sans**: Inter, system-ui, -apple-system, sans-serif
- **Mono**: Fira Code, Consolas, monospace

### Type Scale

- **xs**: 0.75rem (12px)
- **sm**: 0.875rem (14px)
- **base**: 1rem (16px)
- **lg**: 1.125rem (18px)
- **xl**: 1.25rem (20px)
- **2xl**: 1.5rem (24px)
- **3xl**: 1.875rem (30px)
- **4xl**: 2.25rem (36px)

### Font Weights

- **Normal**: 400
- **Medium**: 500
- **Semibold**: 600
- **Bold**: 700

## Spacing

Based on a 4px scale:

- **0**: 0
- **1**: 0.25rem (4px)
- **2**: 0.5rem (8px)
- **3**: 0.75rem (12px)
- **4**: 1rem (16px)
- **5**: 1.25rem (20px)
- **6**: 1.5rem (24px)
- **8**: 2rem (32px)
- **10**: 2.5rem (40px)
- **12**: 3rem (48px)
- **16**: 4rem (64px)

## Shadows

Elevation levels for depth:

- **sm**: Subtle shadow for slight elevation
- **base**: Default shadow for cards
- **md**: Medium elevation for dropdowns
- **lg**: High elevation for modals
- **xl**: Maximum elevation for popovers

## Border Radius

- **none**: 0
- **sm**: 0.125rem (2px)
- **base**: 0.25rem (4px)
- **md**: 0.375rem (6px)
- **lg**: 0.5rem (8px)
- **xl**: 0.75rem (12px)
- **full**: 9999px (pill shape)

## Components

### Button

Primary interactive element for actions.

**Variants**: primary, secondary, tertiary, danger
**Sizes**: sm, md, lg
**States**: default, hover, active, disabled, loading

### Input

Text input field for user data entry.

**Types**: text, email, password, number
**States**: default, focus, error, disabled

### Card

Container for grouping related content.

**Variants**: default, elevated, outlined
**States**: default, hover, active

## Usage Guidelines

### Accessibility

- Maintain WCAG 2.1 AA compliance
- Minimum 4.5:1 contrast for text
- 44x44px minimum touch targets
- Keyboard navigation support
- Screen reader compatibility

### Responsive Design

- Mobile-first approach
- Breakpoints: 640px, 768px, 1024px, 1280px
- Fluid typography and spacing
- Touch-friendly interactions

### Performance

- Optimize asset loading
- Minimize CSS size
- Use efficient selectors
- Leverage browser caching

## Getting Started

1. Install dependencies: `npm install`
2. Build tokens: `npm run build`
3. Import variables: `@import 'build/css/variables.css'`
4. Use tokens: `var(--color-brand-primary)`

## Resources

- [Design Token Standards](../resources/design_token_standards.md)
- [CSS Architecture Guide](../resources/css_architecture_guide.md)
- [Component Patterns](../resources/component_patterns.md)
- [Naming Conventions](../resources/naming_conventions.md)
