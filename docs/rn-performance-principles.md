# React Native Performance Principles

- Profile before optimizing—most performance issues originate from JS thread; profile JavaScript first using React DevTools Profiler, Flipper, or why-did-you-render
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
- MUST prioritize based on user paths and business impact
- MUST establish control plan with acceptable ranges and monitoring frequency
- MUST automate regression detection; manual testing doesn't scale
- Render duration and render count are primary React Native performance metrics
- Statistical significance required to validate improvements (environment variation exists)
- Profiling must account for measurement variation (same device, different runs differ)
- MUST detect prewarming before measuring startup time (iOS 15+ ProcessInfo environment variable)
- MUST use System Tracing for thread-level analysis (Android); mqt_js thread saturation indicates JS thread bottleneck
- Consider battery consumption impact in library selection (web libraries cause extraneous CPU/memory consumption; battery drain affects both foreground and background execution)
- OS (iOS) continuously monitors resource consumption and may throttle background activities; background activity intervals can be reduced by OS if resource usage is excessive
- Mobile SDKs deliver performance equivalent to native applications; web libraries assume browser capabilities and constraints, leading to suboptimal mobile performance

