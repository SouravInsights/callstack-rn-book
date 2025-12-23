# Chapter 2: Durable Engineering Knowledge

## Core Principles

- **Specialized components abstract performance-critical logic**: Higher-order components encapsulate heuristics and calculations that maintain 60FPS
- **Layout measurement is the bottleneck**: Measuring layout dominates list rendering cost
- **Bundle size directly impacts TTI**: All imported code is loaded, parsed, and executed; Metro doesn't tree-shake
- **Memory overhead compounds with data growth**: Components that keep elements in memory degrade as datasets scale

## Hard Rules

### MUST

- **MUST use FlatList (or FlashList) for any scrollable list of items**
- **MUST provide `keyExtractor` as a stable callback** (use `useCallback` with empty deps)
- **MUST provide `renderItem` as a stable callback** (use `useCallback` with empty deps)
- **MUST provide `estimatedItemSize` for FlashList** (or use `overrideItemLayout` if sizes are known)
- **MUST analyze bundle size before adding dependencies** (use react-native-bundle-visualizer or Bundlephobia)
- **MUST import specific lodash functions** (`lodash/map` not `lodash`)
- **MUST measure performance in release mode** (dev mode performance is misleading for FlashList)

### MUST NOT

- **MUST NOT use ScrollView + View.map() for lists** (renders all items, no virtualization)
- **MUST NOT add items to state arrays with `.concat()` or spread** (causes full re-render of all items)
- **MUST NOT use complex libraries when smaller alternatives exist** (e.g., moment.js → dayjs)
- **MUST NOT import entire utility libraries** (import specific functions/modules)
- **MUST NOT rely on dev mode performance metrics** (FlashList windowSize is smaller in dev)

## Performance Invariants

- **FlatList maintains 60FPS by not rendering off-screen elements**: Virtualization is the mechanism
- **FlashList recycles views outside viewport**: Uses RecyclerListView's recycling capability
- **Layout measurement blocks scroll**: FlatList waits for item height measurement before rendering next batch
- **JS thread busy time correlates with scroll lag**: 60FPS requires JS thread availability
- **Bundle size = TTI cost**: Larger bundles increase Time to Interactive
- **Hermes pages bytecode on-demand**: Only necessary bytecode loaded into memory (mitigates bundle size impact)

## Failure Modes & Anti-Patterns

### Lists

- **ScrollView + map() pattern**: Renders all items, no virtualization, memory grows linearly
- **Unstable callbacks**: `keyExtractor`/`renderItem` recreated on each render → unnecessary re-renders
- **Missing `getItemHeight()` for constant-height items**: Forces layout measurement on every scroll
- **Complex list items with side effects**: Breaks FlashList recycling, degrades performance
- **Adding items to beginning of array**: `.concat()` or spread causes full list re-render

### Libraries

- **Choosing by GitHub stars alone**: Ignores bundle size, dependencies, feature bloat
- **Assuming web constraints apply**: Mobile has different performance characteristics
- **Not checking bundle impact**: Large libraries directly increase TTI
- **Importing entire lodash**: Pulls unused code into bundle (Metro doesn't tree-shake)

## Decision Heuristics

### When to use FlatList vs FlashList

- **Use FlatList when**: Simple lists, constant item heights, standard use cases
- **Use FlashList when**: Need 60FPS guarantee, complex lists, dynamic heights, production-scale data
- **FlashList trade-off**: Smaller windowSize in dev mode (appears slower), requires `estimatedItemSize`

### Library selection

- **Check bundle size first**: Use Bundlephobia or import-cost extension
- **Prefer smaller specialized libraries**: dayjs (2KB) over moment.js (67KB) for date operations
- **Import granularly**: `lodash/map` not `lodash`; check if library supports modular imports
- **Evaluate necessity**: Can you import a smaller subset? Do you need all features?

### List item height

- **Constant height**: Use `getItemHeight()` or `overrideItemLayout` (FlashList) to avoid measurement
- **Dynamic height**: Calculate based on text lines + layout constraints; use `react-native-text-size` for batch calculation
- **Complex items**: Average sizes for `estimatedItemSize` if items vary

## React Native–Specific Implications

### JS Thread

- **FlatList keeps JS thread busy**: Heuristics and calculations run on JS thread during scroll
- **FlashList reduces JS thread load**: Recycling reduces render work, improves FPS
- **60FPS requires JS thread availability**: Blocking JS thread causes scroll lag

### Rendering

- **Virtualization is mandatory for large lists**: FlatList/FlashList only render visible items + buffer
- **Recycling reduces memory pressure**: FlashList reuses views, reducing allocation overhead
- **Blank spaces indicate render lag**: FlashList fails to render items fast enough when JS thread is blocked

### Layout

- **Layout measurement is synchronous**: Blocks scroll until measurement completes
- **Pre-calculated heights eliminate measurement**: `getItemHeight()` or `overrideItemLayout` bypasses layout pass
- **Text height calculation**: Use `react-native-text-size` to batch-calculate all item heights upfront

### Architecture

- **Bundle size = startup cost**: All code loaded before app becomes interactive
- **Metro bundler limitation**: No tree-shaking means all imported code included
- **Hermes mitigates bundle impact**: On-demand bytecode paging reduces memory footprint
- **Release mode required for accurate metrics**: Dev mode has different performance characteristics

## Constraints & Trade-offs

### FlatList

- **Trade-off**: Abstraction overhead vs manual optimization
- **Constraint**: Must measure layout for dynamic heights (blocks scroll)
- **Constraint**: Keeps items in memory (overhead grows with data)

### FlashList

- **Trade-off**: Better performance vs more configuration (`estimatedItemSize` required)
- **Constraint**: Smaller windowSize in dev mode (misleading performance)
- **Constraint**: Items must be lightweight (side effects break recycling)
- **Benefit**: Recycles views, reduces memory pressure

### Library Selection

- **Trade-off**: Feature richness vs bundle size
- **Constraint**: Metro doesn't tree-shake (all imports included)
- **Constraint**: Bundle size directly impacts TTI
- **Mitigation**: Hermes pages bytecode on-demand

## Things Expensive to Get Wrong

- **Using ScrollView for lists**: Performance degrades exponentially with data size; difficult to retrofit
- **Missing `estimatedItemSize` in FlashList**: Causes layout thrashing, blank spaces, poor UX
- **Unstable list callbacks**: Causes unnecessary re-renders, breaks memoization, degrades scroll performance
- **Large utility libraries**: Increases TTI permanently; hard to remove once integrated
- **Not measuring bundle impact**: Technical debt accumulates; startup time degrades over time
- **Complex list items with side effects**: Breaks FlashList recycling; requires architectural changes to fix

