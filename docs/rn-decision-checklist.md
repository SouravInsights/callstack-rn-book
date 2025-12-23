# React Native Performance Decision Checklist

## Before Optimizing
- Have we profiled the code path using React DevTools Profiler, Flipper, or why-did-you-render?
- Are we seeing actual performance symptoms (dropped frames, UI flicker, FPS drops)?
- Have we measured before/after when applying memoization techniques?

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

