# Chapter 6: New Architecture & Development Infrastructure

## Core Principles

- New Architecture replaces asynchronous bridge with synchronous JSI communication
- Fabric unifies render logic in C++ for cross-platform consistency
- TurboModules enable lazy loading and synchronous native-JS communication
- Codegen ensures type safety and eliminates manual boilerplate
- Bridgeless mode removes bridge overhead entirely (RN 0.73+)
- Performance is neutral in most cases; foundation for future capabilities, not immediate speed gains
- React 18 concurrent features require New Architecture
- Testing must focus on business-critical paths, not implementation details
- CI must run before code merges to catch regressions early

## Hard Rules

### MUST
- Upgrade to latest React Native version before enabling New Architecture
- Test in both debug and release modes after migration
- Use Interop Layer (`unstable_reactLegacyComponentNames`) for incompatible components
- Write integration tests for business-critical features
- Run CI checks on every PR before merge
- Use React Native Testing Library for component tests (avoids implementation details)
- Test urgent vs non-urgent updates separately when using `startTransition`
- Build native apps in CI, not just run JS tests
- Use E2E smoke tests to catch app crashes before distribution

### MUST NOT
- Enable New Architecture without testing for incompatible components
- Assume New Architecture provides immediate performance gains
- Write tests that depend on component implementation details
- Skip CI for "small" changes
- Rely solely on manual testing as team scales
- Use snapshot tests without size limits or focused assertions
- Build production apps without CI validation
- Ignore red box warnings for unimplemented components

## Performance Invariants

- JSI enables synchronous calls; eliminates bridge serialization overhead
- Fabric lazily initializes Host Components (View, Text) → faster startup
- TurboModules lazy-load → reduced startup time
- Bridge remains single-threaded; JS thread saturation still blocks UI
- New Architecture uses more RAM but less CPU for large view counts (10K views benchmark)
- Old Architecture faster for 2K Text components (heavier UI thread consumption)
- Meta's production benchmarks show neutral performance across all surfaces
- Bridgeless mode removes bridge initialization overhead
- `startTransition` defers non-urgent updates; keeps urgent updates responsive
- Concurrent rendering allows showing old UI while preparing new UI

## Failure Modes & Anti-Patterns

- **Enabling New Architecture without testing**: Red boxes for unimplemented components in production
- **Expecting immediate performance gains**: New Architecture is foundation, not speed boost
- **Testing implementation details**: Tests break on refactors, provide false confidence
- **100% test coverage obsession**: Wastes time on non-critical paths
- **No CI or unstable CI**: Long feedback loops, regressions reach production
- **Manual PR testing only**: Doesn't scale, different environments cause inconsistencies
- **Flaky E2E tests**: Lowers confidence in test suite, wastes debugging time
- **Large snapshot tests**: Hard to maintain, catch too many irrelevant changes
- **Missing smoke tests**: Ship broken apps that crash on launch
- **Not using Interop Layer**: Block migration due to incompatible legacy components
- **Ignoring React Native version support policy**: Tech debt accumulates, security vulnerabilities

## Decision Heuristics

### New Architecture Migration
- Latest RN version → Enable New Architecture
- Red boxes appear → Use Interop Layer for legacy components
- Interop Layer inconsistencies → Wait for component migration or contribute fix
- Performance critical path → Benchmark before/after; expect neutral results

### Testing Strategy
- Business-critical feature → Integration test required
- Utility function → Unit test with Jest
- React component → React Native Testing Library (avoid implementation details)
- App launch → E2E smoke test
- Payment/login flows → E2E test
- Structured data that changes slightly → Snapshot test (with size limits)
- Multiple similar elements → Use `testID` with index suffix

### CI/CD Setup
- Generic CI needs → CircleCI or GitHub Actions
- React Native specialized → EAS Build
- Need iOS builds on non-Mac → EAS Build
- Want dependency caching → EAS Build (automatic)
- Need build signing automation → EAS Build CLI
- Multiple build profiles → Configure in `eas.json` (development, preview, production)

### React 18 Concurrent Features
- Urgent update (button click) → Direct `setState`
- Non-urgent update (heavy UI recalculation) → Wrap in `startTransition`
- Need pending state indicator → Use `isPending` from `useTransition`
- Heavy rendering during interaction → Use `startTransition` to defer

## React Native-Specific Implications

### JS Thread
- New Architecture doesn't eliminate JS thread saturation risk
- `startTransition` helps prioritize urgent updates on JS thread
- Concurrent rendering allows JS thread to prepare updates without blocking UI

### Rendering
- Fabric renders in C++; unified logic across platforms
- Host Components lazy-initialized → faster first render
- Concurrent rendering shows old UI while preparing new UI
- `startTransition` creates separate "universe" that merges when ready

### Layout
- Fabric handles layout in C++; better cross-platform consistency
- No bridge serialization for layout calculations
- Synchronous JSI calls for layout-related native modules

### Architecture
- Bridge → JSI: Asynchronous → Synchronous communication
- Bridge → Bridgeless: Removes bridge entirely (RN 0.73+)
- Legacy modules → TurboModules: Lazy loading, type safety via Codegen
- Legacy renderer → Fabric: C++ unified rendering, React 18 support
- Old Architecture → New Architecture: One-way migration path

## Trade-offs

- **New Architecture adoption**: Future-ready vs current compatibility risk
- **Performance**: Neutral now, foundation for future optimizations
- **Migration effort**: Interop Layer helps, but not 100% compatible
- **Test coverage**: 100% coverage impractical vs focused critical path testing
- **CI complexity**: Generic CI flexible vs EAS specialized for RN
- **E2E tests**: Catch real issues vs flakiness and slow feedback
- **Snapshot tests**: Quick coverage vs maintenance burden
- **`startTransition`**: Better UX for heavy updates vs added complexity

## Constraints

- New Architecture requires RN 0.68+ (experimental until stable)
- React 18 concurrent features require New Architecture
- Interop Layer not fully compatible with old rendering/event system
- E2E tests harder to set up, more flaky than JS tests
- CI must support Docker containers for native builds
- EAS requires Expo account and CLI setup
- Build signing required for device builds (EAS automates this)
- React Native supports 3 latest versions only

