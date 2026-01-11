**Step 1**: Paste your Figma design link here:

## Task
Create an interactive filter chip component that matches the Figma design with these behaviors:

### Core Functionality
- **Two states**: "All" state (unfiltered) and "Selected" state (filtered)
- **State switching**: Component changes appearance/content between states
- **Interactive dropdown**: Click chip to open selection interface
- **Dynamic content**: Shows different text/icons based on current state
- **Remove action**: Way to delete/clear the filter entirely

### Required Interactions
1. **Default state**: Component shows initial appearance from Figma
2. **Click chip**: Opens dropdown/modal for user selections
3. **Make selections**: User can choose/unchoose options
4. **Apply changes**: Component updates to show selections
5. **Clear/remove**: User can reset or delete the filter

### Technical Requirements
- **Framework**: Use what fits your project (React, Vue, vanilla JS, etc.)
- **Styling**: Match Figma specs exactly (colors, fonts, spacing, borders)
- **Icons**: Implement icon switching between states as shown in design
- **Responsive**: Ensure mobile-friendly touch targets
- **Accessible**: Keyboard navigation + screen reader support
- **Events**: Emit changes so parent components can respond

### Implementation Guide
1. **Analyze Figma**: Identify the two states and their visual differences
2. **Extract tokens**: Colors, typography, spacing, border radius from design
3. **Plan interactions**: Map user actions to state changes
4. **Build component**: Start with static states, add interactivity
5. **Test thoroughly**: Verify all interactions work across devices

### Success Criteria
✅ Visual design matches Figma exactly
✅ State transitions work smoothly
✅ Dropdown/selection interface functions correctly
✅ Component integrates with parent application
✅ Accessible via keyboard and screen readers
✅ Works on mobile and desktop

**Deliverable**: Functional filter component that replicates Figma design with full interactivity.