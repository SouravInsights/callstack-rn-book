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

