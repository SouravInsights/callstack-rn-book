# Chapter 9: Optimize Your App's JavaScript Bundle

## Core Principles

- Bundle size directly impacts TTI (Time To Interactive) and app startup performance
- Autolinking links all native dependencies in package.json regardless of actual usage
- Hermes uses AOT bytecode compilation; JSC uses JIT compilation
- Tree shaking requires ESM (import/export) and side-effect-free packages
- Bundle size reduction compounds: smaller bundle → faster parse → faster execution → better TTI
- Native dependency linking happens at build time; unused deps still increase binary size and TTI
- ProGuard dead code elimination works on native code; tree shaking works on JavaScript
- App Bundle format enables architecture-specific APKs (35% average size reduction)

## Hard Rules

### MUST

- Enable Hermes for production builds (default since RN 0.70)
- Use App Bundle format (`bundleRelease`) for Android production, not APK
- Enable ProGuard for Android release builds (`enableProguardInReleaseBuilds = true`)
- Remove unused native dependencies (use `depcheck` to identify)
- Keep React Native version current to access performance improvements
- Test release builds after enabling ProGuard (may require custom rules)
- Use ESM imports/exports for tree-shaking eligibility
- Mark packages as side-effect-free (`sideEffects: false` in package.json) for tree shaking
- Measure TTI on release builds, not debug builds
- Rebuild native projects after toggling Hermes flag

### MUST NOT

- Ship APK with all CPU architectures (use App Bundle instead)
- Leave ProGuard disabled in release builds
- Keep unused native dependencies in package.json
- Use CommonJS requires if tree shaking is required
- Assume Metro provides tree shaking (it doesn't by default)
- Use Chrome Remote Debugger for performance profiling (executes in V8, not JSC/Hermes)
- Ship with Flipper in production (deprecated in RN 0.73+)
- Skip dependency alignment checks when upgrading React Native
- Assume all bundlers support Hermes (react-native-esbuild doesn't)
- Use code splitting with Hermes expecting large gains (memory mapping reduces benefit)

## Performance Invariants

- Hermes bytecode is generated at build time, not runtime (faster startup)
- Hermes uses memory mapping for lazy loading (only needed parts loaded from RAM)
- JIT engines require warm-up time; AOT engines don't
- Native dependency linking increases binary size and TTI linearly
- Bundle size reduction: 0-20% typical with tree shaking, can exceed 20% in rare cases
- App Bundle reduces APK size by ~35% on average (architecture-specific delivery)
- ProGuard reduces native code size (typically 700KB+ on medium apps)
- Autolinking crawls package.json and node_modules; no usage analysis
- Hermes bundle size: ~2MB overhead
- Code splitting benefits diminish with Hermes due to memory mapping

## Failure Modes & Anti-Patterns

- Large bundle size → slower parse → slower execution → poor TTI → user abandonment
- Unused native deps in package.json → autolinking includes them → larger binary → slower startup
- Shipping APK with all architectures → users download incompatible code → wasted bandwidth
- ProGuard disabled → unused native code shipped → larger APK → slower TTI
- Using Chrome Remote Debugger for profiling → V8 execution differs from JSC/Hermes → misleading metrics
- CommonJS requires → no tree shaking → dead code in bundle
- Missing `sideEffects: false` → bundler assumes side effects → tree shaking disabled
- Upgrading React Native without dependency alignment → incompatible versions → build failures or runtime crashes
- Using react-native-esbuild with Hermes → incompatible (esbuild doesn't support Hermes)
- Code splitting with Hermes expecting large gains → memory mapping already optimizes → minimal benefit
- Fast Refresh limitations with Re.Pack → full reloads more frequent → slower DX
- Module Federation with Re.Pack → HMR only works for host, remotes require full reload

## Decision Heuristics

### Bundler Selection

- Use Metro when: default setup sufficient, no code splitting needed, Fast Refresh critical, minimal configuration desired
- Use Re.Pack when: Webpack ecosystem needed, code splitting required, Module Federation needed, OTA updates planned, extensive customization required
- Use react-native-esbuild when: build speed critical, tree shaking needed, Hermes not required, TypeScript support needed, Fast Refresh not critical
- Use rnx-kit when: Metro with tree shaking needed, symlink support required, TypeScript type-checking in build, duplicate/cyclic dependency detection needed

### Tree Shaking

- Works with: Webpack (Re.Pack), ESBuild (rnx-kit, react-native-esbuild)
- Requires: ESM syntax (import/export), `sideEffects: false` in package.json
- Expected reduction: 0-20% bundle size, can exceed 20% in rare cases
- Test both bundlers if using tree shaking (implementation differs)

### Code Splitting

- Use with JSC: significant TTI improvement (load chunks on-demand)
- Use with Hermes: minimal benefit (memory mapping already optimizes)
- Use for OTA updates: load remote chunks from CDN/server
- Use for Module Federation: share chunks between independent apps

### Native Dependencies

- Remove unused deps: use `depcheck` to identify
- Impact: ~17% TTI improvement observed, 3.9MB size reduction in example
- Dev dependencies: check for native code (may still link into production)
- Autolinking: no usage analysis, links everything in package.json

### Hermes Configuration

- Android: set `enableHermes: true` in `android/app/build.gradle`
- iOS: set `hermes_enabled => true` in `ios/Podfile`
- Rebuild required: native projects must be rebuilt after toggling flag
- Default since RN 0.70: already enabled in new projects

### Android Size Optimization

- App Bundle: use `bundleRelease` instead of `assembleRelease` (35% size reduction)
- ProGuard: enable `enableProguardInReleaseBuilds = true` (700KB+ reduction typical)
- Architecture splitting: App Bundle handles automatically
- Resource optimization: compress PNG, optimize SVG

## React Native-Specific Implications

### JS Thread

- Bundle size directly impacts JS parse time (blocks JS thread)
- Hermes bytecode precompilation reduces parse time (AOT vs JIT)
- Tree shaking reduces bundle size → faster parse → less JS thread blocking
- Code splitting with JSC: chunks load asynchronously, reducing initial JS thread load

### Rendering

- TTI includes: native init → JS load/parse → React render → UIManager execution
- Bundle size affects first two phases (native init + JS load/parse)
- Smaller bundle → faster React component loading → faster first render
- Native dependency count affects native initialization phase

### Layout

- Not directly affected by bundle optimization
- Indirectly improved via faster TTI (user sees UI sooner)

### Architecture

- Autolinking: crawls package.json → links all native deps (no usage analysis)
- New Architecture: auto-linking supports Fabric components and Turbo Modules
- Hermes bundled with RN: version compatibility guaranteed (no NPM confusion)
- Lean Core: some modules extracted to react-native-community (requires separate install)

## Trade-offs

- Re.Pack: more customization vs slower builds, limited Fast Refresh
- react-native-esbuild: faster builds vs no Hermes support, no Fast Refresh/HMR
- rnx-kit: Metro compatibility + tree shaking vs beta status
- Code splitting: TTI improvement with JSC vs minimal benefit with Hermes
- ProGuard: size reduction vs potential crashes (requires testing and custom rules)
- App Bundle: size reduction vs single artifact delivery (Google Play requirement)
- Tree shaking: bundle reduction vs ESM requirement, side-effect marking
- Hermes: better TTI vs no JIT optimizations (CPU-intensive benchmarks may underperform)
- Upgrading RN: latest features vs migration effort, third-party compatibility risk

## Constraints

- Tree shaking: requires ESM syntax (no CommonJS)
- Tree shaking: requires `sideEffects: false` declaration
- Code splitting: limited value with Hermes (memory mapping already optimizes)
- react-native-esbuild: incompatible with Hermes
- Re.Pack: slower builds than Metro (Webpack overhead)
- ProGuard: may break reflection-based code (requires keep rules)
- App Bundle: Google Play requirement for new apps
- Autolinking: no way to opt-out specific packages (must remove from package.json)
- Flipper: deprecated in RN 0.73+, removed in 0.74+
- New debugger: experimental, Hermes-only (RN 0.73+)

