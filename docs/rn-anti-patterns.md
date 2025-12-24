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
- Ignoring stutter threshold (4+ dropped frames indicates UI thread issues; measure dropped frames and stutters separately)
- Applying optimizations without measuring before/after impact

## Profiling Practices
- Profiling in debuggable mode (Android timing data deviates significantly)
- Not detecting prewarming before measuring startup time (iOS 15+ distorts metrics)
- Using only Time Profiler without JS context (can't identify JS bottlenecks)
- Profiling on high-end device only (missing issues on lower-end devices)
- Not using System Tracing (can't identify which thread is bottleneck)
- Profiling animations in DEV mode (DEV mode performance is misleading; disable DEV mode for animation benchmarking)
- Measuring memory without Graphics segment (Java, Native, Graphics segments all contribute to total memory; Graphics memory reflects UI thread rendering buffers)

## List Patterns
- Using `ScrollView + View.map()` for lists (renders all items, no virtualization, memory grows linearly)
- Missing `estimatedItemSize` for FlashList (causes layout thrashing, blank spaces)
- Unstable list callbacks (`keyExtractor`/`renderItem` recreated on each render)
- Missing `getItemHeight()` for constant-height items (forces layout measurement on every scroll)
- Complex list items with side effects (breaks FlashList recycling)
- Adding items to beginning of array with `.concat()` or spread (causes full list re-render)

## Library Selection
- Choosing libraries by GitHub stars alone (ignores bundle size, dependencies, feature bloat, web vs mobile compatibility)
- Not checking bundle impact before adding dependencies (large libraries directly increase TTI)
- Importing entire utility libraries like `lodash` (Metro doesn't tree-shake, pulls unused code)
- Using web libraries for networking-heavy features (e.g., real-time messaging) instead of mobile-specific SDKs
- Using web libraries for advanced graphics rendering (3D structures, diagrams) instead of native solutions
- Using web Firebase SDK (`firebase/database`) instead of `@react-native-firebase/database` (web SDK causes extraneous CPU/memory consumption)
- Assuming web library API compatibility implies performance parity on mobile
- Ignoring OS resource monitoring and throttling behavior (iOS throttles background activities based on resource consumption)

## Bridge & Animation Patterns
- Proxying calls directly to native without JS-side validation (causes unnecessary round-trips)
- Using JS-driven animations for gesture interactions (bridge saturation causes jank)
- Blocking bridge with unnecessary traffic during animations (causes dropped frames)
- Assuming bridge calls are fast or predictable (bridge is asynchronous and capacity-limited)
- Putting validation or complex abstractions in native code (violates separation, hurts maintainability)
- Missing InteractionManager deferral for heavy UI work during animations (interrupts smooth animations)

## Skia/Canvas Patterns
- Using Skia for simple cases solvable with Rive/reanimated (overkill, adds unnecessary native dependency)
- Assuming transform origin is center in Skia (it's top-left, unlike React Native; causes incorrect transform animations)
- Interpolating paths with mismatched command structure (crashes app; paths must have identical command count and types)
- Applying blur effects expecting underlying non-canvas views to be affected without snapshot (blur only sees canvas elements; use `makeImageFromView` snapshot)

## Testing Practices
- Writing tests that depend on component implementation details (tests break on refactors, provide false confidence)
- 100% test coverage obsession (wastes time on non-critical paths)
- No CI or unstable CI (long feedback loops, regressions reach production)
- Manual PR testing only (doesn't scale, different environments cause inconsistencies)
- Flaky E2E tests (lowers confidence in test suite, wastes debugging time)
- Large snapshot tests without size limits or focused assertions (hard to maintain, catch too many irrelevant changes)
- Missing smoke tests (ship broken apps that crash on launch)
- Skipping CI for "small" changes (regressions reach production)
- Building production apps without CI validation (ship broken builds)
- Enabling New Architecture without testing for incompatible components (red boxes for unimplemented components in production)
- Not using Interop Layer for incompatible legacy components (blocks migration unnecessarily)

