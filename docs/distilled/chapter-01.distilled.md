# Chapter 1: UI Re-renders - Distilled Engineering Knowledge

## Core Performance Principles

- React Native owns the rendering lifecycle; you control component composition, not when/how repaints occur
- Components re-render when parent re-renders OR props change (even if props didn't actually change—acceptable tradeoff to avoid prop comparison overhead)
- Performance problems manifest as UI flicker and FPS drops, especially on low-end devices
- Optimization must be data-driven: measure first, optimize second
- Premature optimization can increase memory usage and provide marginal benefit

## Hard Rules

### MUST
- Profile before optimizing (use React DevTools Profiler, Flipper, why-did-you-render)
- Use memoized selectors (`createSelector`) when deriving data from global state
- Normalize entity state in Redux (use `createEntityAdapter` for O(1) access)
- Prefer bottom-up/atomic state management over top-down
- Measure before/after when applying memoization techniques
- Use `useSelector` hooks over `connect` for simpler usage

### MUST NOT
- Optimize prematurely (wait for dropped frames or performance symptoms)
- Use React Context for global state without proper memoization
- Place all state at top level (causes cascading re-renders)
- Use controlled `TextInput` when you don't need to alter user input

## Performance Invariants

- Controlled `TextInput` creates bidirectional sync: JS state → Native → JS state
- Fast typing + slow devices + controlled input = flickering (race condition in async sync)
- Global state changes propagate renders to all subscribers
- State normalization enables O(1) entity access, fast CRUD operations
- Bottom-up state management prevents parent re-renders from cascading to children
- Manual memoization (`React.memo`, `useMemo`, `useCallback`) increases memory usage

## Failure Modes & Anti-patterns

### Controlled TextInput Race Condition
- **Symptom**: Input flickers when typing fast on slow devices
- **Root cause**: `onChangeText` updates arrive before React Native syncs previous updates back to native
- **Fix**: Use `defaultValue` instead of `value` when you don't need to alter input

### Global State Re-render Cascade
- **Symptom**: Single control (TextInput, CheckBox) update causes whole app re-render
- **Root cause**: Bad global state design—components subscribe to entire store
- **Fix**: Use memoized selectors that only update when specific data subset changes

### Context Without Memoization
- **Symptom**: Performance degradation as app grows
- **Root cause**: Custom Context implementation replaces state library without memoization
- **Fix**: Use proper state management library (Redux, Zustand, Jotai) or implement memoized selectors

### Top-Down State Management
- **Symptom**: Parent state update causes unnecessary child re-renders
- **Root cause**: State placed at top level, passed down via props
- **Fix**: Use atomic/bottom-up approach—state local to component, shared via state manager

### Premature Memoization
- **Symptom**: Increased memory usage without measurable performance gain
- **Root cause**: Memoizing before profiling identifies actual bottlenecks
- **Fix**: Profile first, memoize only when data shows benefit

## Decision Heuristics

### TextInput: Controlled vs Uncontrolled
- **Use uncontrolled** (`defaultValue`) when: you don't need validation, masking, or input alteration
- **Use controlled** (`value`) when: you need to validate, mask, or modify user input as they type

### State Management Library Selection
- **Redux Toolkit**: When you need normalized entities, complex state shape, team familiarity
- **Zustand**: When you want simplicity, atomic state, less boilerplate
- **Jotai**: When you want built-in bottom-up approach, atomic design pattern
- **React Context**: Only for truly local state or when properly memoized

### When to Memoize
- **Use `React.memo`**: When Profiler shows component re-renders unnecessarily
- **Use `useMemo`**: When expensive computation runs on every render
- **Use `useCallback`**: When function identity matters for child memoization
- **Don't memoize**: Before profiling shows it's needed

### State Normalization
- **Normalize when**: Working with entities (User, Post, Todo) that have unique IDs
- **Use `createEntityAdapter`**: For CRUD operations on normalized entities
- **Benefit**: O(1) access, fast updates, efficient selectors

## React Native–Specific Implications

### Rendering & Reconciliation
- React Native's reconciliation compares component trees and performs minimal updates
- Prop comparison overhead avoided by default—components may re-render even if props unchanged
- JS thread performance directly impacts rendering—too many operations cause frame drops

### TextInput Synchronization
- Native input → `onChangeText` → JS state → Native input (bidirectional)
- Async nature means updates can arrive out of order
- Fast typing creates race conditions where native value temporarily reverts

### JS Thread Bottleneck
- All React logic runs on single JS thread
- Excessive state operations block thread, causing UI stutter
- Memoization reduces work but increases memory pressure

### New Architecture Considerations
- Fabric (new renderer) improves performance but same principles apply
- State management patterns remain valid regardless of architecture

## Atomic State Pattern

- **Principle**: Build from atoms (smallest components) upward, not top-down
- **Benefit**: State local to component, shared via state manager—prevents cascading re-renders
- **Implementation**: Use Zustand or Jotai for atomic stores, avoid monolithic Redux store
- **Tradeoff**: More granular state management, but better performance characteristics

## React Forget (Future)

- Auto-memoizing compiler—eliminates need for manual `memo()`, `useCallback()`, `useMemo()`
- Memoizes both computed values and React element objects
- Still experimental—don't rely on it yet, but understand it will change optimization approach