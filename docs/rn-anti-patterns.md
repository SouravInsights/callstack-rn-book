# React Native Performance Anti-patterns

## State Management
- Using React Context for global state without proper memoization
- Placing all state at top level (causes cascading re-renders)
- Using `connect` instead of `useSelector` hooks
- Deriving data from global state without memoized selectors
- Not normalizing entity state in Redux (missing O(1) access benefits)

## Component Patterns
- Using controlled `TextInput` (`value` prop) when you don't need to alter user input
- Memoizing components (`React.memo`, `useMemo`, `useCallback`) before profiling identifies bottlenecks

## Optimization Practices
- Optimizing prematurely without dropped frames or performance symptoms
- Applying optimizations without measuring before/after impact

