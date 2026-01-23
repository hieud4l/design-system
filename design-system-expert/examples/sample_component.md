# Button Component

## Purpose

Trigger actions and events with clear visual hierarchy.

## Variants

- **primary**: Main call-to-action
- **secondary**: Less prominent actions
- **tertiary**: Minimal emphasis
- **danger**: Destructive actions

## States

- Default
- Hover
- Active
- Disabled
- Loading

## Props/Attributes

- **size**: sm | md | lg
- **variant**: primary | secondary | tertiary | danger
- **disabled**: boolean
- **loading**: boolean
- **icon**: optional icon component

## Accessibility

- Use semantic HTML `<button>` element
- Include ARIA labels where appropriate
- Ensure keyboard navigation support
- Maintain minimum 44x44px touch target
- Provide visible focus indicators
- Support screen readers

## Usage Examples

### Basic Usage

```html
<button class="button button--primary">
  Click me
</button>
```

### With Size

```html
<button class="button button--primary button--lg">
  Large Button
</button>
```

### Disabled State

```html
<button class="button button--primary" disabled>
  Disabled Button
</button>
```

### Loading State

```html
<button class="button button--primary is-loading">
  Loading...
</button>
```

## CSS Implementation

```css
/* Base button styles */
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-3) var(--spacing-4);
  font-family: var(--font-family-sans);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  border: none;
  border-radius: var(--border-radius-md);
  cursor: pointer;
  transition: all 0.2s ease;
}

/* Variants */
.button--primary {
  background: var(--color-brand-primary);
  color: white;
}

.button--primary:hover {
  opacity: 0.9;
}

.button--secondary {
  background: var(--color-brand-secondary);
  color: white;
}

.button--tertiary {
  background: transparent;
  color: var(--color-brand-primary);
}

.button--danger {
  background: var(--color-semantic-error);
  color: white;
}

/* Sizes */
.button--sm {
  padding: var(--spacing-2) var(--spacing-3);
  font-size: var(--font-size-sm);
}

.button--lg {
  padding: var(--spacing-4) var(--spacing-6);
  font-size: var(--font-size-lg);
}

/* States */
.button:disabled,
.button--disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

.button.is-loading {
  position: relative;
  color: transparent;
  pointer-events: none;
}

.button.is-loading::after {
  content: "";
  position: absolute;
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-top-color: transparent;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

## Best Practices

- Use appropriate variant for the context
- Provide clear labels or content
- Handle loading and error states
- Ensure accessibility compliance
- Test on multiple devices and browsers
- Use primary sparingly (one per section)
- Provide feedback on interaction
