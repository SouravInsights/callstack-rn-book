# React Native Performance Principles

- Profile before optimizing—use React DevTools Profiler, Flipper, or why-did-you-render
- Measure before/after when applying any optimization technique—use release mode for accurate metrics (dev mode performance is misleading)
- Prefer bottom-up/atomic state management over top-down cascading patterns
- Use memoized selectors (`createSelector`) when deriving data from global state
- Normalize entity state in Redux using `createEntityAdapter` for O(1) access
- Optimization must be data-driven: measure first, optimize second
- React Native owns the rendering lifecycle; you control composition, not repaints
- Performance problems manifest as UI flicker and FPS drops, especially on low-end devices
- Use `useSelector` hooks over `connect` for simpler usage patterns
- Premature optimization can increase memory usage without measurable benefit
- Bundle size directly impacts TTI: All imported code is loaded, parsed, and executed; Metro doesn't tree-shake
- Layout measurement is the bottleneck: Measuring layout dominates list rendering cost
- Virtualization is mandatory for large lists: FlatList/FlashList only render visible items + buffer

