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
- Optimizing prematurely without dropped frames or performance symptoms, or measuring performance in dev mode instead of release mode
- Applying optimizations without measuring before/after impact

## List Patterns
- Using `ScrollView + View.map()` for lists (renders all items, no virtualization, memory grows linearly)
- Missing `estimatedItemSize` for FlashList (causes layout thrashing, blank spaces)
- Unstable list callbacks (`keyExtractor`/`renderItem` recreated on each render)
- Missing `getItemHeight()` for constant-height items (forces layout measurement on every scroll)
- Complex list items with side effects (breaks FlashList recycling)
- Adding items to beginning of array with `.concat()` or spread (causes full list re-render)

## Library Selection
- Choosing libraries by GitHub stars alone (ignores bundle size, dependencies, feature bloat)
- Not checking bundle impact before adding dependencies (large libraries directly increase TTI)
- Importing entire utility libraries like `lodash` (Metro doesn't tree-shake, pulls unused code)

