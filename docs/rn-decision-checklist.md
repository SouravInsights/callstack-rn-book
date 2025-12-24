# React Native Performance Decision Checklist

## Before Optimizing
- Have we profiled the code path using React DevTools Profiler, Flipper, or why-did-you-render?
- Are we seeing actual performance symptoms (dropped frames, UI flicker, FPS drops)?
- Have we measured before/after when applying memoization techniques?

## Before Profiling
- Are we profiling in production mode (not dev/debuggable)?
- Are we profiling on affected devices (lower-end or most common)?
- Are we combining JS and native profiling for complete picture?

## TextInput Decision
- Do we need to validate, mask, or modify user input as they type?
  - **Yes**: Use controlled `TextInput` (`value` prop)
  - **No**: Use uncontrolled `TextInput` (`defaultValue` prop)

## State Management Decision
- Is this state truly global or can it be local to the component?
- Are we using memoized selectors (`createSelector`) when deriving data from global state?
- If using Redux with entities (User, Post, Todo), is the state normalized with `createEntityAdapter`?
- Are we using `useSelector` hooks instead of `connect`?

## Memoization Decision
- Does the Profiler show this component re-rendering unnecessarily?
- Is there an expensive computation running on every render?
- Does function identity matter for child memoization?
- If none of the above: don't memoize yet

## List Implementation Decision
- Are we rendering a scrollable list of items?
  - **Yes**: Use FlatList or FlashList (never ScrollView + map)
- Do we need 60FPS guarantee or have complex/dynamic-height items?
  - **Yes**: Use FlashList (requires `estimatedItemSize`)
  - **No**: Use FlatList
- Are list item heights constant?
  - **Yes**: Provide `getItemHeight()` or `overrideItemLayout` to avoid measurement
- Are `keyExtractor` and `renderItem` stable callbacks? (use `useCallback` with empty deps)

## Library Selection Decision
- Have we checked bundle size impact? (use Bundlephobia or react-native-bundle-visualizer)
- Can we import specific functions instead of entire library? (e.g., `lodash/map` not `lodash`)
- Is there a smaller alternative? (e.g., dayjs vs moment.js)
- Does this library depend heavily on networking, render advanced graphics, or require native-level performance?
  - **Yes**: Use mobile-specific SDK (e.g., `@react-native-firebase/*` not `firebase/database`)
- Is battery consumption a concern for this feature?
  - **Yes**: Prefer mobile SDK over web library (web libraries cause extraneous CPU/memory consumption)
- Is this a straightforward, low-resource feature where code reusability outweighs performance?
  - **Yes**: Web library acceptable (but still check bundle size)

## Profiling Strategy Decision
- JS bottleneck → React Profiler, react-native-performance, Flipper Hermes Debugger
- Native bottleneck → Xcode Instruments (iOS), Android Profiler (Android)
- Layout issues → View Hierarchy (iOS), Layout Inspector (Android)
- Regression prevention → Reassure in CI, real-time monitoring in production

## iOS Profiling Decision
- Are we detecting prewarming before measuring startup time?
- Are we combining Time Profiler with Hermes Debugger for JS context?

## Android Profiling Decision
- Are we using System Tracing for thread-level analysis?
- Are we checking mqt_js thread saturation?

## Animation Strategy Decision
- What properties need animation?
  - **Transform/opacity only**: Use `Animated` with `useNativeDriver: true`
  - **Layout properties (height, color, etc.)**: Use Reanimated
- Is this gesture-driven?
  - **Yes**: Use Gesture Handler + Reanimated
  - **No**: NativeDriver (transform/opacity) or Reanimated (layout properties) sufficient
- Are we deferring heavy UI work during animations using `InteractionManager`?

## Native Module Design Decision
- Are we validating all arguments on JS side before native module calls?
- Is the native layer a thin wrapper (not heavy abstraction)?
- Is error handling catching issues on JS side before bridge call?
- Are we profiling bridge traffic when seeing UI jank?

## Bridge Traffic Decision
- Are we minimizing bridge traffic during active animations?
- Are we deferring heavy work until animations complete?
- When seeing UI jank, have we profiled bridge traffic?

## New Architecture Migration Decision
- Are we on the latest React Native version?
  - **Yes**: Enable New Architecture
- Do red boxes appear for unimplemented components?
  - **Yes**: Use Interop Layer (`unstable_reactLegacyComponentNames`) for legacy components
- Are there Interop Layer inconsistencies?
  - **Yes**: Wait for component migration or contribute fix
- Is this a performance-critical path?
  - **Yes**: Benchmark before/after; expect neutral results
- Note: Must test in both debug and release modes after migration

## Testing Strategy Decision
- Is this a business-critical feature?
  - **Yes**: Integration test required
- Is this a utility function?
  - **Yes**: Unit test with Jest
- Is this a React component?
  - **Yes**: Use React Native Testing Library (avoids implementation details)
- Do we need to test app launch?
  - **Yes**: E2E smoke test
- Do we need to test payment/login flows?
  - **Yes**: E2E test
- Do we have structured data that changes slightly?
  - **Yes**: Snapshot test (with size limits)
- Are we testing multiple similar elements?
  - **Yes**: Use `testID` with index suffix
- Are we using `startTransition`?
  - **Yes**: Test urgent vs non-urgent updates separately

## CI/CD Setup Decision
- Do we need generic CI capabilities?
  - **Yes**: Use CircleCI or GitHub Actions
- Do we need React Native specialized builds?
  - **Yes**: Use EAS Build
- Do we need iOS builds on non-Mac machines?
  - **Yes**: Use EAS Build
- Do we want automatic dependency caching?
  - **Yes**: Use EAS Build (automatic)
- Do we need build signing automation?
  - **Yes**: Use EAS Build CLI
- Do we need multiple build profiles (development, preview, production)?
  - **Yes**: Configure in `eas.json`

## React 18 Concurrent Features Decision
- Is this an urgent update (e.g., button click)?
  - **Yes**: Direct `setState`
- Is this a non-urgent update (e.g., heavy UI recalculation)?
  - **Yes**: Wrap in `startTransition`
- Do we need a pending state indicator?
  - **Yes**: Use `isPending` from `useTransition`
- Is heavy rendering happening during user interaction?
  - **Yes**: Use `startTransition` to defer
- Note: React 18 concurrent features require New Architecture

