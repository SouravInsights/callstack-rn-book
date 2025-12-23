## CHAPTER 5

### FIND THE BALANCE BETWEEN NATIVE AND JAVASCRIPT

### SEEK THE HARMONY BETWEEN NATIVE AND JAVASCRIPT TO BUILD FAST-WORKING AND LOW-MAINTENANCE APPS.

#### ISSUE: WHILE WORKING ON NATIVE MODULES, YOU DRAW THE LINE IN THE WRONG PLACE BETWEEN NATIVE AND JAVASCRIPT ABSTRACTIONS

When working with React Native, you're going to be developing JavaScript most of the time. However, there are situations when you need to write a bit of native code. For example, you're working with a third-party SDK that doesn't have official React Native support yet. In that case, you need to create a native module that wraps the underlying native methods and exports them to the React Native realm.

All native methods need real-world arguments to work. React Native builds on top of an abstraction called a bridge, which provides bidirectional communication between JavaScript and native worlds.

Note: There's an ongoing effort to move away from asynchronous bridge communication to a synchronous one. You can read more about it in the New Architecture chapter.

As a result, JavaScript can execute native APIs and pass the necessary context to receive the desired return value. The communication itself is asynchronous – it means that while the caller is waiting for the results to arrive from the native side, the JavaScript is still running and may already be up for another task.

The number of JavaScript calls that arrive over the bridge is not deterministic and can vary over time, depending on the number of interactions that you do within your application. Additionally, each call takes time, as the JavaScript arguments need to be stringified into JSON, which is the established format that can be understood by these two realms.

For example, when the bridge is busy processing the data, another call will have to block and wait. If that interaction was related to gestures and animations, it is very likely that you have a dropped frame – the operation wasn't performed causing jitters in the UI.

# Performance Optimization in React Native

Certain libraries, such as Animated provide special workarounds. In this case, use NativeDriver, which serializes the animation, passes it once upfront to the native thread, and doesn't cross the bridge while the animation is running – preventing it from being subject to accidental frame drops while other work is happening.

That's why it is important to keep the bridge communication efficient and fast.

### MORE TRAFFIC FLOWING OVER THE BRIDGE MEANS LESS SPACE FOR OTHER THINGS

Passing more traffic over the bridge means that there is less space for other important things that React Native may want to transfer at that time. As a result, your application may become unresponsive to gestures or other interactions while you're performing native calls.

If you are seeing a degraded UI performance while executing certain native calls over the bridge or seeing substantial CPU consumption, you should take a closer look at what you are doing with the external libraries. It is very likely that there is more being transferred than should be.

#### SOLUTION: USE THE RIGHT AMOUNT OF ABSTRACTION ON THE JS SIDE – VALIDATE AND CHECK THE TYPES AHEAD OF TIME.

When building a native module, it is tempting to proxy the call immediately to the native side and let it do the rest. However, there are cases, such as invalid arguments, that end up causing an unnecessary round-trip over the bridge only to learn that we didn't provide the correct set of arguments.

# Bypassing arguments to the native module

Let's take a JavaScript module that proxies the call straight to the underlying native module.

import { NativeModules } from 'react-native';
const { ToastExample } = NativeModules;

export const show = (message, duration) => {
ToastExample.show(message, duration);
};
In the case of an incorrect or missing parameter, the native module is likely to throw an exception. The current version of React Native doesn't provide an abstraction for ensuring the JavaScript parameters and the ones needed by your native code are in sync. Your call will be serialized to JSON, transferred to the native side, and executed.

That operation will perform without any issues, even though we haven't passed the complete list of arguments needed for it to work. The error will arrive when the native side processes the call and receives an exception from the native module.

In such a scenario, you have lost some time waiting for the exception that you could've checked for beforehand.

import { NativeModules } from 'react-native';
const { ToastExample } = NativeModules;

export const show = (message, duration) => {
if (typeof message !== 'string' || message.length > 100) {
throw new Error('Invalid Toast content');
}

if (!Number.isInteger(duration) || duration > 20000) {
throw new Error('Invalid Toast duration');
}

ToastExample.show(message, duration);
};

# Using the native module with arguments validation

The above is not only tied to the native modules themselves. It is worth keeping in mind that every React Native primitive component has its native equivalent and component props are passed over the bridge every time there's a rendering happening – or is it? It's not always the case when a component re-renders. React Native renderer is smart enough to diff the parts of our JS React component hierarchy and only send enough information through the bridge, so that the native view hierarchy is updated.

This is the case when styling components like e.g. View or Text using the style prop. Let's take a look at the following example using inline styles.

import React from 'react';
import { View } from 'react-native';

const App = () => {
return (
&#x3C;View
style={{
flex: 1,
justifyContent: 'center',
alignItems: 'center',
}}>
&#x3C;View
style={{
backgroundColor: 'coral',
width: 200,
height: 200,
}}>
&#x3C;/View>
&#x3C;/View>
);
};

export default App;

Read more: https://snack.expo.dev/@callstack-snack/inline-styled-view

Even though the style prop is passed as an inline object, it doesn't cause us any performance issues. Neither when we dynamically change the styles based on props, nor when we re-render the App component. View passes its props almost directly to the underlying native representation. And thanks to the React Native renderer, no matter how often we re-render this component on the JS side, only the smallest amount of data necessary to update the style prop will be passed through the bridge.

In React Native we have nicer ways to deal with styling and it's through StyleSheet API – a dedicated abstraction similar to CSS StyleSheets. Although it provides no performance benefits, it's worth calling it out for the ease of development and maintenance. When we develop our app in TypeScript or Flow, StyleSheet is well typed and makes it possible for our code editors to auto-complete.

### BENEFITS: THE CODEBASE IS FASTER AND EASIER TO MAINTAIN

Whether you're facing any performance challenges right now, it is smart to implement a set of best practices around native modules as the benefits are not just about the speed but also the user experience. Sure, keeping the right amount of the traffic flowing over the bridge will eventually contribute to your application performing better and working smoothly. As you can see, certain techniques mentioned in this section are already being actively used inside React Native to provide you a satisfactory performance out of the box. Being aware of them will help you create applications that perform better under a heavy load.

### HOWEVER, ONE ADDITIONAL BENEFIT THAT IS WORTH POINTING OUT IS THE MAINTENANCE.

Keeping the heavy and advanced abstractions, such as validation, on the JavaScript side will result in a very thin native layer that is nothing more but just a wrapper around an underlying native SDK. In other words, the native part of your module is going to look more like a copy-paste from the documentation – comprehensible and specific.

Mastering this approach to the development of native modules is why a lot of JavaScript developers can easily extend their applications with additional functionality without specializing in Objective-C or Java.

# PART 1

# | CHAPTER 6

### ANIMATE AT 60FPS – NO MATTER WHAT

### USE NATIVE SOLUTIONS TO ACHIEVE SMOOTH ANIMATIONS AND A GESTURE-DRIVEN INTERFACE AT 60FPS.

ISSUE: JS-DRIVEN ANIMATIONS ARE OCCUPYING THE BRIDGE TRAFFIC AND SLOWING DOWN THE APPLICATION.

Mobile users are used to smooth and well-designed interfaces that quickly respond to their interactions and provide prompt visual feedback. As a result, applications have to register a lot of animations in many places that will have to run while other work is happening.

As we know from the previous section, the amount of information that can be passed over the bridge is limited. There's currently no built-in priority queue. In other words, it is on you to structure and design your application in a way that both the business logic and animations can function without any disruptions. This is different from the way we are used to performing animations. For example, on iOS, the built-in APIs offer unprecedented performance and are always scheduled with the appropriate priority. Long story short – we don't have to worry too much about ensuring they're running at 60FPS.

With React Native, this story is a bit different. If you do not think about your animations top-down beforehand and choose the right tools to tackle this challenge, you're on track to run into dropped frames sooner or later.

### JANKY OR SLOW ANIMATIONS AFFECT THE PERCEPTION OF THE APP, MAKING IT LOOK SLOW AND UNFINISHED

In today's sea of applications, providing a smooth and interactive UI might be one of your only ways to win over customers who are looking to choose the app to go.

If your application fails to provide a responsive interface that works well with the user interactions (such as gestures), not only may it affect new customers, but also decrease the ROI and user sentiment.

Mobile users like the interfaces that follow them along and that look top-notch and ensure the animations are always running smoothly is a fundamental part that builds such an experience.

#### SOLUTION: IF IT'S POSSIBLE, USE NATIVE AND CORRECT ANIMATIONS.

# One-off animations

Enabling the usage of the native driver is the easiest way of quickly improving your animations' performance. However, the subset of style props that can be used together with the native driver is limited. You can use it with non-layout properties like transforms and opacity. It will not work with colors, height, and others. Those are enough to implement most of the animations in your app because you usually want to show/hide something or change its position.

const fadeAnim = useRef(new Animated.Value(0)).current;

const fadeIn = () => {
Animated.timing(fadeAnim, {
toValue: 1,
duration: 1000,
useNativeDriver: true, // enables native driver
}).start();
};

// [...]

<animated class="view" style="{{" opacity:="" fadeanim="" }}="">
</animated>
Enabling the native driver for opacity animation

For more complex use cases, you can use the React Native Reanimated library. Its API is compatible with the basic Animated library and introduces a set of fine-grained controls for your animations with a modern hooks-based interface. More importantly, it introduces the possibility to animate all possible style props with the native driver. So animating height or color will no longer be an issue. However, transform and opacity animations will still be slightly faster since they are GPU-accelerated. You can play with different combinations in this reanimated playground.

### GESTURE-DRIVEN ANIMATIONS

The most desired effect that can be achieved with animations is being able to control animation with a gesture. For your customers, this is the most enjoyable part of the interface. It builds a strong sentiment and makes the app feel very smooth and responsive. Plain React Native is very limited when it comes to combining gestures with native driven animations. You can utilize ScrollView scroll events to build things like a smooth collapsible header.

For more sophisticated use cases, there is an awesome library – React Native Gesture Handler – which allows you to handle different gestures natively and interpolate those into animations. You can build a swipeable element by combining it with Animated. While it will still require JS callbacks, there is a remedy for that!

The most powerful pair of tools for gesture-driven animations is using Gesture Handler combined with Reanimated. They were designed to work together and give the possibility to build complex gesture-driven animations that are fully calculated on the native side.

Reanimated API supports synchronous JavaScript execution on the UI thread using the concept of worklets. The library's runtime spawns a secondary JS context on the UI thread that is then able to run JavaScript functions in the form of said worklets. Now using your imagination and leveraging Reanimated, you can create wonderful animations at full available speeds.

import React from 'react';
import { StyleSheet, View } from 'react-native';
import { PanGestureHandler } from 'react-native-gesture-handler';
import Animated, {
useAnimatedGestureHandler,
useAnimatedStyle,
useSharedValue,
withSpring,
} from 'react-native-reanimated';

const Snappable = (props) => {
const startingPosition = 0;
const x = useSharedValue(startingPosition);
const y = useSharedValue(startingPosition);

const animatedStyle = useAnimatedStyle(() => {
return {
transform: [{ translateX: x.value }, { translateY: y.value }],
};
});

const eventHandler = useAnimatedGestureHandler({
onStart: (event, ctx) => {
ctx.startX = x.value;
ctx.startY = y.value;
},
onActive: (event, ctx) => {
x.value = ctx.startX + event.translationX;
y.value = ctx.startY + event.translationY;
},
onEnd: (event, ctx) => {
x.value = withSpring(startingPosition);
y.value = withSpring(startingPosition);
},
});

return (

<animated class="view" style="{animatedStyle}">{props.children}</animated>
</pangesturehandler>
);
};

const Example = () => {
return (
<view style="{styles.container}">
<snappable>
<view style="{styles.box}">
</view></snappable>
</view>
);
};

export default Example;

# Low-level handling of gestures

Low-level handling of gestures might not be a piece of cake, but fortunately, there are third-party libraries that utilize the mentioned tools and expose the prop callbackNode. It's an Animated.Value that's derived from specific gesture behavior. Its value range is usually from 0 to 1, which follows the progress of the gesture. You can interpolate the values to animated elements on the screen. A great example of the libraries that expose CallbackNode are reanimated-bottom-sheet and react-native-tab-view.

import \* as React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Animated from 'react-native-reanimated';
import BottomSheet from 'reanimated-bottom-sheet';
import Lorem from './Lorem';

const { Value, interpolateNode: interpolate } = Animated;

const Example = () => {
const gestureCallbackNode = new Value(0);

const renderHeader = () => (
<view style="{styles.headerContainer}">
<text style="{styles.headerTitle}">Drag me</text>
</view>
);

const renderInner = () => (
<view style="{styles.innerContainer}">
<animated class="view" style="{{" opacity:="" interpolate(gesturecallbacknode,="" {="" &#x3C;="" code=""></animated></view>
| const BOX_SIZE | = 100; |
| --------------- | ------ |

const styles = StyleSheet.create({
container: {
flex: 1,
justifyContent: 'center',
alignItems: 'center',
backgroundColor: '#F5FCFF',
},
box: {
width: BOX_SIZE,
height: BOX_SIZE,
borderColor: '#F5FCFF',
alignSelf: 'center',
backgroundColor: 'plum',
margin: BOX_SIZE / 2,
},
});

Read more: https://snack.expo.dev/@callstack-snack/gesture-with-animation

<view style="{styles.container}">
<bottomsheet callbacknode="{gestureCallbackNode}" snappoints="{[50," 400]}="" initialsnap="{1}" renderheader="{renderHeader}" rendercontent="{renderInner}">
</bottomsheet></view>
<animated class="view" style="{{" transform:="" [="" {="" translatey:="" interpolate(gesturecallbacknode,="" inputrange:="" [0,="" 1],="" outputrange:="" 100],="" }),="" },="" ],="" }}="">
<lorem>
<lorem>
</lorem></lorem></animated>
<view style="{styles.container}">
<bottomsheet callbacknode="{gestureCallbackNode}" snappoints="{[50," 400]}="" initialsnap="{1}" renderheader="{renderHeader}" rendercontent="{renderInner}">
</bottomsheet></view>

const styles = StyleSheet.create({
container: {
flex: 1,
},
headerContainer: {
width: '100%',
backgroundColor: 'lightgrey',
height: 40,
borderWidth: 2,
},
headerTitle: {
textAlign: 'center',
fontSize: 20,
padding: 5,
},
innerContainer: {
backgroundColor: 'lightblue',
},
});

Read more: https://snack.expo.dev/@callstack-snack/interpolation

### GIVING YOUR JS OPERATIONS A LOWER PRIORITY

It is not always possible to fully control the way animations are implemented. For example, React Navigation uses a combination of React Native Gesture Handler and Animated which still needs JavaScript to control the animation runtime. As a result, your animation may start flickering if the screen you are navigating to loads a heavy UI. Fortunately, you can postpone the execution of such actions using InteractionManager. This handy helper allows long-running work to be scheduled after any interactions/animations have completed. In particular, this allows JavaScript animations to run smoother.

Note: In the near future, you'll be able to achieve similar behavior with React itself on a renderer level (with Fabric) using the startTransition API. Read more about it in the New Architecture chapter.

import React, { useState, useRef } from 'react';
import {
Text,
View,
StyleSheet,
Button,
Animated,
InteractionManager,
Platform,
} from 'react-native';
import Constants from 'expo-constants';

const ExpensiveTaskStates = {
notStared: 'not started',
scheduled: 'scheduled',
done: 'done',
};

const App = () => {
const animationValue = useRef(new Animated.Value(100));
const [animationState, setAnimationState] = useState(false);
const [expensiveTaskState, setExpensiveTaskState] = useSta-
te(
ExpensiveTaskStates.notStared,
);

const startAnimationAndScheduleExpensiveTask = () => {
Animated.timing(animationValue.current, {
duration: 2000,
toValue: animationState ? 100 : 300,

❗InteractionManager works only on native platforms. Open example on ❗ iOS or Android

Start animation and schedule expensive task

Animated box

Expensive task status: {expensiveTaskState}

In practice, you can show a placeholder, wait for the anima-

tion to finish, and then render the actual UI. It would help your

JavaScript animations to run smoother and avoid interruptions

by other operations. It's usually smooth enough to provide a great

experience.

Remember, that using JS-driven animations is bound to have sig-

nificantly worse performance than native run on UI thread. Making

it hard to achieve max FPS available for the device. Strive for plat-

form-native animations whenever possible. And treat APIs such

as InteractionManager for cases, where heavy UI updates may in-

terfere with gestures or animations. They may fight for the same

resource – native UI thread.

### BENEFITS: ENJOY SMOOTH ANIMATIONS AND A GESTURE-DRIVEN INTERFACE AT 60FPS.

There's no one single right way of doing animations in React Native.

The ecosystem is full of different libraries and approaches to han-

dling interactions. The ideas suggested in this section are just rec-

ommendations to encourage you to not take the smooth interface

for granted.

What is more important is painting that top-down picture in

your head of all interactions within the application and choosing

the right ways of handling them. There are cases where JavaScript-

driven animations will work just fine. At the same time, there are

interactions where native animation (or an entirely native view)

will be your only way to make it smooth.

With such an approach, the application you create will be smoother

and snappy. It will not only be pleasant for your users to use but

also for you to debug and have fun with it while developing.

„By adding delightful animations to your app, users tend to be much more forgiving. If done carefully, animations in React Native can perform great and improve the perceived performance of the app to the user.”

William Candillon – Chief Technology Officer at 28msec

# PART 1
