# Chapter 4: Use Mobile-Specific Libraries

## Core Principles

- React Native is not a web environment; it has distinct constraints and optimization requirements
- Mobile devices operate under resource constraints (battery, CPU, memory) that web environments don't share
- Web libraries assume browser capabilities and constraints, leading to suboptimal mobile performance
- Platform-specific SDKs provide native-level performance and stability

## Hard Rules

### MUST NOT
- Use web libraries for networking-heavy features (e.g., real-time messaging)
- Use web libraries for advanced graphics rendering (3D structures, diagrams)
- Assume web library performance translates to mobile

### MUST
- Use mobile-specific SDKs for performance-critical features
- Prefer native SDK wrappers (e.g., `@react-native-firebase/*`) over web equivalents
- Consider battery consumption impact in library selection

## Performance Invariants

- Web libraries cause extraneous CPU and memory consumption on mobile
- OS (iOS) continuously monitors resource consumption and may throttle background activities
- Background activity intervals can be reduced by OS if resource usage is excessive
- Mobile SDKs deliver performance equivalent to native applications
- Battery drain from non-optimized libraries affects both foreground and background execution

## Failure Modes & Anti-Patterns

- Using web Firebase SDK (`firebase/database`) instead of `@react-native-firebase/database`
- Using web libraries for real-time communication features
- Using web graphics libraries for complex visualizations
- Assuming web library API compatibility implies performance parity
- Ignoring OS resource monitoring and throttling behavior

## Decision Heuristics

- **Use mobile SDK if:**
  - Library depends heavily on networking
  - Library renders advanced graphics
  - Feature requires native-level performance
  - Battery consumption is a concern

- **Web library acceptable if:**
  - Feature is straightforward and low-resource
  - Maximum code reusability is prioritized over performance
  - Use case doesn't involve networking or graphics

## React Native-Specific Implications

### JS Thread
- Web libraries may introduce unnecessary JS thread overhead
- Mobile SDKs leverage native threads, reducing JS thread load

### Battery & Resource Management
- OS monitors foreground and background resource consumption
- Excessive resource usage triggers OS throttling mechanisms
- Background activity frequency can be reduced by OS based on resource consumption

### Architecture
- Native SDK wrappers provide escape hatch for performance-critical paths
- Thin wrapper layers maintain API familiarity while delivering native performance
- Platform-specific implementations enable enterprise-grade performance without compromising UX

## Trade-offs

- **Web libraries:** Lower effort, code reuse, but suboptimal performance and battery impact
- **Mobile SDKs:** Higher setup complexity, but native-level performance and battery efficiency
- **Hybrid approach:** Use web libraries for simple features, mobile SDKs for advanced use cases

