# Chapter 8: Draw Efficiently on a Canvas with Skia

## Core Principles

- Canvas is the last native element in view tree; serves as root for Skia drawing
- Declarative API uses own React renderer behind the scenes
- Full pixel-level control over rendering pipeline
- Native-side path interpolation avoids JS thread blocking
- Transparent canvas by default enables overlay patterns
- Group operations (paint, transform, clip, bitmap) apply to children hierarchically

## Hard Rules

### MUST

- Use `collapsable={false}` on View refs passed to `makeImageFromView`
- Ensure interpolated paths have identical command count and types
- Account for PixelRatio when using image snapshots (divide dimensions by `PixelRatio.get()`)
- Plan snapshot-based effects in advance (requires ref to underlying view)
- Use `makeImageFromView` when blur/effects must affect underlying layers beyond canvas

### MUST NOT

- Assume transform origin is center (it's top-left in Skia, unlike React Native)
- Apply blur effects expecting underlying non-canvas views to be affected (blur only sees canvas elements)
- Interpolate paths with mismatched command structure (crashes app)
- Use Skia for simple cases solvable with Rive/reanimated (overkill)
- Skip snapshot capture when blur needs to affect underlying native views

## Performance Invariants

- Path interpolation calculations execute on native side (C++), not JS thread
- Native-side interpolation keeps UI responsive during path animations
- Canvas rendering bypasses React Native's standard rendering pipeline
- Group `layer` property creates bitmap drawing of children (performance cost for effects)

## Failure Modes & Anti-Patterns

- Blur effect only around canvas elements, underlying View remains sharp → use `makeImageFromView` snapshot
- Path interpolation crashes → mismatched path command structure
- Transform animations behave incorrectly → forgot top-left origin (not center)
- Overlay effects don't affect underlying content → missing snapshot capture
- Using Skia for simple animations → Rive/reanimated more appropriate
- Shadow/blur limitations in Rive → Skia provides full control
- Cross-platform shadow/masking inconsistencies → Skia unified rendering

## Decision Heuristics

- Choose Skia when: maximum rendering control needed, design requires effects beyond Rive constraints, graphics-heavy dashboards, performant image transitions, cross-platform rendering consistency required
- Choose Rive/reanimated when: simpler animations, no need for pixel-level control, file-based animations sufficient
- Snapshot strategy: required when effects must affect non-canvas views; plan refs early
- Path interpolation: use when animating between path states (graphs, morphing); ensure path structure compatibility

## React Native–Specific Implications

### JS Thread

- Canvas accepts Reanimated values directly as props (no JS thread work for value passing)
- Path interpolation calculations offloaded to native (no JS thread blocking)
- `makeImageFromView` returns Promise (async snapshot capture)
- Reanimated integration seamless (shared values work directly)

### Rendering

- Canvas uses own React renderer (separate from RN renderer)
- Canvas is transparent by default (overlay pattern)
- Group `layer` property creates bitmap (performance cost for complex effects)
- Rendering happens on UI thread (native Skia engine)

### Layout

- Canvas dimensions must be explicitly set (style width/height)
- Transform origin is top-left (not center like React Native)
- Clipping via `clip` property (invert with `invertClip`)
- Image snapshots require PixelRatio adjustment for correct display

### Architecture

- Canvas is last native element in view tree
- Child components are declarative API, not standard RN components
- Integration with react-native-gesture-handler and react-native-reanimated supported
- Native Skia engine (C++) handles heavy computations
- Bitmap effects require layer creation (memory/performance trade-off)

## Trade-Offs

- Full control vs complexity → Skia for precise requirements, simpler tools for standard cases
- Native performance vs bundle size → Skia adds native dependency
- Snapshot overhead vs effect quality → snapshot needed for blur affecting underlying views
- Path structure constraints vs interpolation performance → must match structure for native interpolation
- Bitmap layer creation vs effect capabilities → `layer` property enables effects but costs performance

## Constraints

- Path interpolation requires identical command structure (count and types)
- Blur/shadow effects limited to canvas elements without snapshot
- Transform origin difference (top-left vs center) requires mental model shift
- Snapshot-based effects require advance planning (ref availability)
- Canvas dimensions must be explicit (no flex-based sizing without explicit values)
- Rive limitations (blur, glow, shadow, path effects) → Skia fills gap
- Cross-platform rendering differences (shadows, masking, blur) → Skia provides consistency

