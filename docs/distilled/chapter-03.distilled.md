# Chapter 3: Distilled Engineering Knowledge

## Continuous Deployment

### Core Principles
- Manual deployment doesn't scale; automation is non-negotiable for teams >1
- Short feedback loops require automated build pipelines
- Standardize deployment process to enforce company-wide performance practices
- React Native requires separate iOS and Android build configurations

### Hard Rules
- MUST automate iOS and Android builds separately (React Native is two apps at low level)
- MUST NOT commit signing credentials; use environment variables or secure storage
- MUST use `match` for iOS certificate management in team environments
- MUST run builds on CI with proper executor (macOS for iOS, Docker for Android)
- MUST generate changelogs automatically as part of deployment pipeline

### React Native Implications
- iOS signing complexity requires `match` action; Android uses Gradle directly
- Fastlane lanes must be defined in both `ios/fastlane/Fastfile` and `android/fastlane/Fastfile`
- EAS Build handles signing automatically; EAS Submit requires separate configuration for Google Play service account

### Failure Modes
- Manual deployment creates bottlenecks and inconsistent releases
- Missing environment variables for keystore passwords break Android builds
- Incorrect certificate/provisioning profile setup causes iOS build failures
- CI configuration without proper executor type fails platform-specific builds

### Decision Heuristics
- Use Fastlane + AppCenter for full control over build process
- Use EAS Build + EAS Submit for managed infrastructure (Expo projects or bare RN with Expo setup)
- Prefer graphical interfaces (AppCenter) over CLI for initial store configuration

---

## OTA Updates

### Core Principles
- JavaScript bundle updates bypass App Store review; native changes cannot
- OTA is an escape hatch for critical bugs, not a replacement for proper releases
- Update strategy must be explicit: check frequency, install mode, rollback capability

### Hard Rules
- MUST NOT use OTA for native code changes (requires new binary)
- MUST implement rollback mechanism before production OTA deployment
- MUST test OTA updates on same build profile as production
- MUST handle update failures gracefully (app must work without update)
- MUST NOT ship breaking API changes via OTA without versioning

### Performance Invariants
- OTA updates download and apply on JS thread; large bundles block UI
- Update checks on app resume add latency to foreground transitions
- Failed updates must not crash or degrade app functionality

### React Native Implications
- OTA updates only affect JavaScript bundle; native modules unchanged
- CodePush wraps root component; EAS Update uses `expo-updates` with hooks
- Update checks happen on JS thread; synchronous checks block rendering
- Branch-based updates require matching build profile (preview/production)

### Failure Modes
- Shipping OTA update with incompatible native module API breaks app
- Missing error handling causes crashes when update download fails
- Update strategy that checks on every foreground blocks user interactions
- Deploying to wrong branch/profile delivers updates to incorrect user segments

### Decision Heuristics
- Use CodePush for bare React Native with App Center integration
- Use EAS Update for Expo projects or bare RN with Expo setup
- Prefer incremental rollouts (percentage-based) over all-or-nothing
- Check for updates on app resume, not on every render or navigation

### Trade-offs
- Immediate updates vs. user experience (check frequency overhead)
- Automatic install vs. user control (forced updates may interrupt workflows)
- Branch-based targeting vs. complexity (multiple update tracks to manage)

---

## Performance Process (DMAIC)

### Core Principles
- Performance optimization is data-driven, not intuition-based
- Small incremental improvements compound; avoid big-bang optimizations
- Performance regressions are inevitable without automated monitoring
- Customer feedback defines what "fast" means; measurable CTQ required

### Hard Rules
- MUST measure before optimizing (baseline required)
- MUST NOT optimize without profiling data
- MUST prioritize based on user paths and business impact
- MUST establish control plan with acceptable ranges and monitoring frequency
- MUST automate regression detection; manual testing doesn't scale

### Performance Invariants
- Render duration and render count are primary React Native performance metrics
- Statistical significance required to validate improvements (environment variation exists)
- Profiling must account for measurement variation (same device, different runs differ)

### React Native Implications
- Most performance issues originate from JS thread; profile JavaScript first
- React Profiler measures render time and count; identifies unnecessary rerenders
- Native profiling (Xcode/Android Studio) required when JS profiling insufficient
- Flipper bridges JS and native profiling; Hermes Debugger provides JS context

### Failure Modes
- Optimizing wrong metrics (measuring wrong thing)
- Ignoring measurement variation leads to false positives/negatives
- No control phase = performance degrades over time
- Manual regression testing = regressions caught by users, not developers

### Decision Heuristics
- Profile JS first (React Profiler, react-native-performance); native if JS clean
- Use Reassure for automated regression testing in CI
- Real-time monitoring (Firebase, Sentry) for production; automated tests for development
- Cause-and-effect diagrams for root cause analysis; hypothesis testing before implementation

### Trade-offs
- Comprehensive profiling vs. development speed (profiling overhead)
- Automated testing vs. false positives (statistical thresholds)
- Real-time monitoring vs. cost (data collection and storage)

---

## iOS Profiling

### Core Principles
- Time Profiler shows native thread activity; JS context requires Flipper/Hermes Debugger
- View Hierarchy reveals layout issues and unnecessary view nesting
- Prewarming (iOS 15+) distorts startup measurements; must detect and account for it

### Hard Rules
- MUST use Time Profiler for native thread bottlenecks
- MUST combine with Hermes Debugger (Flipper) for JS context
- MUST detect prewarming before measuring startup time (ProcessInfo environment variable)
- MUST NOT profile in development mode (use production JS bundle)

### Performance Invariants
- CPU spikes during touch events are expected; sustained high CPU indicates problem
- Memory should stabilize after navigation; continuous growth indicates leak
- Hermes function names appear in Time Profiler; symbol resolution requires JS profiling

### React Native Implications
- Time Profiler shows Hermes execution but not function names (memory addresses only)
- Flipper Hermes Debugger provides JS function names and call stacks
- View Hierarchy shows RCTView nesting; can identify unflattened view trees
- Prewarming executes initializers hours before actual launch; distorts metrics

### Failure Modes
- Profiling in dev mode gives false performance characteristics
- Using only Time Profiler without JS context = can't identify JS bottlenecks
- Ignoring prewarming = inflated startup time measurements
- Not profiling on affected devices = missing device-specific issues

### Decision Heuristics
- Start with Xcode CPU/Memory monitors for quick overview
- Use Time Profiler + Hermes Debugger for detailed JS bottleneck analysis
- Use View Hierarchy for layout optimization opportunities
- Profile on lower-end devices for worst-case scenarios

### Trade-offs
- Profiling overhead vs. accuracy (more detailed = more overhead)
- Real device vs. simulator (simulator faster but less accurate)

---

## Android Profiling

### Core Principles
- Android Profiler provides real-time CPU, memory, network, energy metrics
- System Tracing reveals thread-level execution; identifies which thread is bottleneck
- Lower-end devices expose performance issues not visible on high-end hardware
- JS thread (mqt_js) is primary bottleneck for React Native apps

### Hard Rules
- MUST profile on real device, preferably lower-end or most common model
- MUST disable JS Dev Mode (use production bundle, not Metro server)
- MUST use System Tracing for thread-level analysis
- MUST NOT profile in debuggable mode (timing data deviates significantly)

### Performance Invariants
- CPU usage correlates with energy consumption
- Memory should drop when GC runs; continuous growth = leak
- mqt_js thread saturation indicates JS thread bottleneck
- UI thread blocking causes dropped frames and jank

### React Native Implications
- mqt_js thread = JavaScript execution; high usage = JS bottleneck
- UI thread = native rendering; blocking causes frame drops
- Native module thread = bridge communication; can be optimized with JSI
- Render thread (Android only) = separate rendering pipeline

### Failure Modes
- Profiling in dev mode = false performance characteristics
- Profiling on high-end device only = missing issues on lower-end devices
- Not using System Tracing = can't identify which thread is bottleneck
- Ignoring energy metrics = battery drain issues go unnoticed

### Decision Heuristics
- Start with Android Profiler overview (CPU, memory, energy)
- Use System Tracing to identify thread bottlenecks
- If mqt_js saturated: optimize JS, consider JSI, move work to native
- If UI thread blocked: optimize native rendering, reduce view complexity
- Use Flipper android-performance-profiler for automated experiments and comparisons

### Trade-offs
- Profiling detail vs. overhead (System Tracing more detailed but heavier)
- Real device vs. emulator (emulator convenient but less accurate)
- Automated profiling vs. manual (automation scales but requires setup)

---

## Cross-Platform Profiling Strategy

### Core Principles
- Profile JS first (most React Native issues are JS-side)
- Native profiling required when JS profiling shows no issues
- Automated regression testing prevents performance degradation
- Real user monitoring catches issues not visible in development

### Hard Rules
- MUST profile in production mode (not dev mode)
- MUST profile on affected devices (lower-end or most common)
- MUST combine JS and native profiling for complete picture
- MUST automate regression detection (Reassure or similar)

### Decision Heuristics
- JS bottleneck → React Profiler, react-native-performance, Flipper Hermes Debugger
- Native bottleneck → Xcode Instruments (iOS), Android Profiler (Android)
- Layout issues → View Hierarchy (iOS), Layout Inspector (Android)
- Regression prevention → Reassure in CI, real-time monitoring in production

