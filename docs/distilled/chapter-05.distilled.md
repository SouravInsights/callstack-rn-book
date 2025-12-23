# Chapter 5: Native-JavaScript Balance

## Core Principles

- Bridge communication is asynchronous, non-deterministic, and capacity-limited
- Each bridge call requires JSON serialization/deserialization overhead
- Bridge traffic competes with gestures, animations, and UI updates
- Native modules must be thin wrappers; heavy abstractions belong on JS side
- Validation and type checking must occur before bridge calls

## Hard Rules

### MUST
- Validate all arguments on JS side before native module calls
- Use `useNativeDriver: true` for transform/opacity animations
- Use Reanimated for animations requiring layout properties (height, color, etc.)
- Use Gesture Handler + Reanimated for gesture-driven animations
- Defer heavy UI work during animations using `InteractionManager`
- Keep native layer as thin wrapper around underlying SDKs

### MUST NOT
- Proxy calls directly to native without JS-side validation
- Use JS-driven animations for gesture interactions
- Block bridge with unnecessary traffic during animations
- Put validation or complex abstractions in native code
- Assume bridge calls are fast or predictable

## Performance Invariants

- Bridge has no built-in priority queue; all traffic competes equally
- Busy bridge during gestures/animations causes dropped frames
- React Native renderer diffs props and only sends minimal updates over bridge
- NativeDriver serializes animation once upfront; no bridge traffic during execution
- Reanimated worklets run JavaScript synchronously on UI thread
- Gesture Handler processes gestures natively, avoiding JS thread

## Failure Modes & Anti-Patterns

- **Unvalidated native calls**: Round-trip to native only to discover invalid args
- **JS-driven gesture animations**: Bridge saturation causes jank
- **Heavy native abstractions**: Makes maintenance harder, violates separation
- **Missing InteractionManager**: Heavy UI updates interrupt animations
- **Inline style objects**: Not a performance issue (renderer optimizes), but StyleSheet preferred for DX
- **Assuming bridge is fast**: Treat every bridge call as potentially expensive

## Decision Heuristics

### Animation Strategy
- Transform/opacity → `Animated` with `useNativeDriver: true`
- Layout properties (height, color) → Reanimated
- Gesture-driven → Gesture Handler + Reanimated
- Simple one-offs → NativeDriver sufficient
- Complex interactions → Full native stack (Gesture Handler + Reanimated)

### Native Module Design
- JS layer: validation, type checking, business logic
- Native layer: thin wrapper, direct SDK calls, minimal logic
- Error handling: catch on JS side before bridge call

### Performance Optimization
- Minimize bridge traffic during active animations
- Defer heavy work until animations complete
- Prefer native solutions over JS-driven alternatives
- Profile bridge traffic when seeing UI jank

## React Native-Specific Implications

### Bridge Architecture
- Asynchronous communication; no synchronous guarantees
- JSON serialization overhead for all data transfer
- No priority system; all calls compete for bandwidth
- Bridge saturation blocks gestures, animations, and interactions

### Rendering
- React Native renderer performs prop diffing
- Only changed props sent over bridge on re-render
- Inline style objects don't cause performance issues (renderer optimizes)
- StyleSheet provides DX benefits (typing, autocomplete) but no performance gain

### Animation Threading
- NativeDriver: animation serialized upfront, runs on native thread
- Reanimated: worklets execute JS on UI thread synchronously
- Gesture Handler: gesture recognition on native thread
- JS-driven animations: compete with other JS work, subject to frame drops

### Trade-offs
- NativeDriver: fast but limited to transform/opacity
- Reanimated: full property support but slightly slower than GPU-accelerated transforms
- JS-driven: flexible but worst performance, requires InteractionManager for smoothness
- Native views: best performance but least flexible

## Constraints

- Bridge capacity is finite and shared
- No built-in priority queue for bridge traffic
- NativeDriver limited to non-layout properties
- JS-driven animations cannot achieve consistent 60FPS
- Heavy abstractions in native code hurt maintainability

## Critical Paths

- Gesture recognition → must be native (Gesture Handler)
- Animation execution → prefer native thread (NativeDriver/Reanimated)
- Argument validation → must be JS-side (avoid unnecessary bridge calls)
- Heavy UI updates → defer until animations complete (InteractionManager)

