# Chapter 7: Replace Lottie with Rive

## Core Principles

- State machines are the correct abstraction for interactive animations
- Single animation file with triggers > multiple animation files
- FPS > memory consumption (when trade-off required)
- File size directly impacts bundle size and user retention
- Designer-driven state machines eliminate developer rework cycles

## Hard Rules

### MUST

- Target 60 FPS on both JS and UI threads for animations
- Use state machines for interactive animations (triggers, inputs)
- Disable DEV mode when benchmarking animation performance
- Prefer web editor customization over requiring Adobe AE expertise
- Measure memory across Java, Native, and Graphics segments

### MUST NOT

- Use GIFs for high-fidelity or full-screen animations (file size bloat)
- Implement interactivity logic in code when state machines exist
- Use multiple animation files for state-based sequences
- Accept < 60 FPS for user-facing animations
- Bundle animations without considering storage impact

## Performance Invariants

- 60 FPS is the minimum threshold for perceived smoothness
- Rive: ~60 FPS, Lottie: ~17 FPS (same animation)
- Rive: lower Java/Native memory, higher Graphics memory
- Rive file size: ~2 KB vs Lottie: ~24 KB (same animation)
- Dropped frames: Rive ~105, Lottie ~1711 (7:30 duration)

## Failure Modes & Anti-Patterns

- Multiple animation files for onboarding steps → use single file with state machine
- Code-based animation state management → use state machine inputs/triggers
- GIFs for quality animations → 4x larger than JSON alternatives
- Lottie for performance-critical animations → 3.5x lower FPS
- Re-exporting animations for customization changes → use web editor
- Ignoring Graphics memory segment → total memory analysis incomplete

## Decision Heuristics

- Choose animation library: FPS > file size > memory (Graphics memory acceptable if FPS target met)
- Interactive animations: state machines required
- Customization needs: web editor > Adobe AE dependency
- Bundle optimization: single file with triggers > multiple files
- Performance testing: disable DEV mode, measure both threads

## React Native–Specific Implications

### JS Thread

- Animation libraries must maintain 60 FPS on JS thread
- State machine inputs/triggers execute on JS thread
- Imperative methods (play, setInputState, fireState) are JS thread operations

### UI Thread

- Rendering must maintain 60 FPS on UI thread
- Frame drops visible in Perf monitor indicate UI thread issues
- Graphics memory segment reflects UI thread rendering buffers

### Memory Architecture

- Java: Lottie ~23 MB, Rive ~12 MB
- Native: Lottie ~49 MB, Rive ~25 MB
- Graphics: Lottie ~123 MB, Rive ~184 MB
- Total: Graphics memory can be higher if FPS target achieved

### Performance Measurement

- Use React Native Perf monitor for FPS tracking
- Measure dropped frames and stutters (4+ frame drops)
- Profile both JS and UI thread FPS independently
- Memory profiling: Java, Native, Graphics segments

## Trade-Offs

- Graphics memory (Rive higher) vs FPS (Rive 3.5x better) → choose FPS
- File size (Rive smaller) vs customization (Rive web editor) → both win
- State machine complexity vs code complexity → state machine wins (designer-driven)
- Single file maintenance vs multiple file management → single file wins

## Constraints

- 18.7% app uninstalls due to storage issues → file size is critical
- 60 FPS is user expectation, not optional
- State machine inputs/triggers must be documented by animator/designer
- Web editor customization limited vs Adobe AE full control

