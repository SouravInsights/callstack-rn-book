# THE ULTIMATE GUIDE TO REACT NATIVE OPTIMIZATION

# 2024 Edition

# TABLE OF CONTENTS

- How This Guide Is Organized 3
- Introduction to React Native Optimization 6
- It’s all about TTI and FPS? 7

# PART 1

- Pay attention to UI re-renders 12
- Use dedicated components for certain layouts 35
- Think twice before you pick an external library 45
- Always remember to use libraries dedicated to the mobile platform 51
- Find the balance between native and JavaScript 57
- Animate at 60FPS – no matter what 64
- Replace Lottie with Rive 75
- Draw efficiently on a canvas with Skia 83
- Optimize your app’s JavaScript bundle 95

# PART 2

- Always run the latest React Native version to access the new features 102
- How to debug faster and better with Flipper 118
- Avoid unused native dependencies 124
- Optimize your application startup time with Hermes 131
- Optimize your Android application’s size with these Gradle settings 139
- Experiment with the New Architecture of React Native 146

# PART 3

- Run tests for key pieces of your app 158
- Have a working Continuous Integration (CI) in place 168
- Don’t be afraid to ship fast with Continuous Deployment 179
- Ship OTA (Over-The-Air) when in an emergency 192
- Make your app consistently fast 201
- Know how to profile iOS 214
- Know how to profile Android 223

Thank you 233

About Callstack 238

# HOW THIS GUIDE IS ORGANIZED

Optimizing the React Native app is a complex process where you need to take various aspects into account – from implementation through using the latest React Native features to testing and continuous deployment.

This guide is a comprehensive source of tactics, tricks, tips, tools, and best practices to help you deliver an optimized React Native app that delights your users.

We not only focus on the technological aspects of React Native optimization; we also underline the impact of each technological aspect on business continuity.

# This guide contains best practices for optimizing:

- Stability
- Performance
- Resource usage
- User experience
- Maintenance costs
- Time-to-market

All these aforementioned aspects have a particular impact on the revenue-generating effectiveness of your apps. Each element – stability, performance, and resource usage – are directly related to improving user engagement with (and therefore the ROI) of your products because of their positive impact on the user experience.

With a faster time-to-market, you can stay ahead of your competitors, and a streamlined maintenance process will help you reduce your spending on that particular process.

# WHAT THIS GUIDE LOOKS LIKE AND THE TOPICS IT COVERS

THIS GUIDE IS DIVIDED INTO THREE PARTS:

The first part is about improving performance through understanding the React Native implementation details and knowing how to maximize them. This part covers the following topics:

1. Pay attention to UI re-renders
2. Use dedicated components for certain layouts
3. Think twice before you pick an external library
4. Always remember to use libraries dedicated to the mobile platform
5. Find the balance between native and JavaScript
6. Animate at 60FPS – no matter what
7. Replace Lottie with Rive
8. Optimize your app’s JavaScript bundle

The second part is about improving performance by using the latest React Native features or turning some of them on. This part describes the following topics:

Always run the latest React Native version to access the latest features

1. How to debug faster and better with Flipper
2. Avoid unused native dependencies
3. Optimize your Android application startup time with Hermes
4. Optimize your Android application’s size with Gradle settings
5. Experiment with the New Architecture of React Native

# The third part is about enhancing the stability of the application by investing in testing and continuous deployment. This part tackles the following topics:

1. Run tests for key pieces of your app
2. Have a working Continuous Integration (CI) in place
3. Don’t be afraid to ship fast with Continuous Deployment
4. Ship OTA (Over-the-Air) in an emergency
5. Make your app consistently fast
6. Know how to profile iOS
7. Know how to profile Android

# THE STRUCTURE OF EACH SECTION LOOKS LIKE THIS:

# Issue

This part describes the main problem with React Native performance.

# Solution

This part outlines how that problem may affect your business and what the best practices are to solve it.

# Benefits

This part focuses on the business benefits of our proposed solution.

# INTRODUCTION TO REACT NATIVE OPTIMIZATION

# IT’S ALL ABOUT TTI AND FPS?

Wait a minute, what are these weird acronyms even?! When thinking about optimizing a mobile React Native app, we need to acknowledge the two most important metrics—apart from the value proposition and engagement—that our users will base their feeling of how fast and snappy our app is, are the Time To Interactive (TTI) and Frames Per Second (FPS).

The former is a measure of how quickly a user can start using (or interacting with) your app. TTI is about boot-time performance. Opening a new app should be fast, period. The latter is a measure of how snappy your app’s interface is to the user interactions. FPS is about runtime performance. Using the app should be as smooth as riding a bike. Maybe unless you turn on that energy saver feature. The best apps out there, combine great boot-time and runtime performance to provide the best end-to-end experience for the users.

Almost every piece of advice you’ll find in this guide will be about directly or indirectly impacting one of these metrics. And since React Native gives us the tools to build native Android and iOS apps sprinkled with some JavaScript on top, there will be lots of opportunities to impact these metrics from many different angles!

Thankfully, most of the heavy-lifting is done for us on the framework level so any React Native developer can start with a good baseline performance today. However the more complex your app gets, the more challenging it may be to keep a good baseline of healthy TTI and FPS metrics.

And frankly, it’s not all about these two metrics. After all, if your app crashes at runtime, can you measure FPS for the interaction you go after? Optimization is a complex and ongoing process that needs to happen continuously and on many different grounds for every successful product. As you progress through this guide, you’ll gain a better grasp on what affects your users’ experience, what matters for delivering and perceiving a better performance, why it matters, and how to solve the challenges that prevent your beloved users from enjoying the best experience when using your React Native app.

# REACT NATIVE TAKES CARE OF THE RENDERING. BUT PERFORMANCE IS STILL KEY.

With React Native, you create components that describe how your interface should look like. During the runtime, React Native turns them into platform-specific native components. Rather than talking directly to the underlying APIs, you focus on the user experience of your application.

However, that doesn’t mean all the applications developed with React Native are equally fast and offer the same level of user experience.

# EVERY DECLARATIVE APPROACH (INCLUDING REACT NATIVE) IS BUILT UPON IMPERATIVE APIS, WHICH REQUIRES GREAT CARE.

When you’re building your application the imperative way, you carefully analyze every callsite to the external APIs. For example, when working in a multi-threaded environment, you safely write your code in a thread, being aware of the context and resources that the code is looking for.

Despite all the differences between the declarative and imperative ways of doing things, they have a lot in common. Every declarative abstraction can be broken down into a number of imperative calls. For example, React Native uses the same APIs to render your application on iOS as native developers would use themselves.

# REACT NATIVE UNIFIES PERFORMANCE, BUT IT ISN’T A GUARANTEE!

While you don’t have to worry about the performance of the underlying iOS and Android APIs calls, how you compose the components can make all the difference. All your components will offer the same level of performance and responsiveness.

# BUT IS “SAME” A SYNONYM FOR “BEST”? IT’S NOT.

That’s when our checklist comes into play. Use React Native to its full potential. As discussed before, React Native is a declarative framework and takes care of rendering the application for you. In other words, you don’t dictate how the application will be rendered.

Your job is to define the UI components and forget about the rest. However, that doesn’t mean that you should take the performance of your application for granted. In order to create fast and responsive applications, you have to think the React Native way. You have to understand how the framework interacts with the underlying platform APIs.

# IF YOU NEED HELP WITH PERFORMANCE, STABILITY, USER EXPERIENCE, OR OTHER COMPLEX ISSUES – CONTACT US!

As React Native Core Contributors and leaders of the community, we will be happy to help.

# PART 1

# IMPROVE PERFORMANCE BY UNDERSTANDING THE IMPLEMENTATION DETAILS OF REACT NATIVE.

In this section, we will dive deeper into the most popular performance bottlenecks and the React Native implementation details that contribute to them. This will not only be a smooth introduction to some of the advanced React Native concepts, but it will also let you improve the stability and performance of your application by performing small tweaks and changes.

The following part is focused on the first point from the checklist of performance optimization tactics: UI re-renders. It’s a very important part of the React Native optimization process because it allows for the reduction of the device’s battery usage which translates into a better user experience for your app.

# PART 1

# CHAPTER 1

# PAY ATTENTION TO

# UI RE-RENDERS

# OPTIMIZE THE NUMBER OF STATE OPERATIONS AND REMEMBER ABOUT MEMOIZED COMPONENTS TO MAKE YOUR APP WORK FASTER WITH FEWER RESOURCES.

# ISSUE: INCORRECT STATE UPDATES CAUSE EXTRANEOUS RENDERING CYCLES OR THE DEVICE IS JUST TOO SLOW.

As discussed briefly, React Native takes care of rendering the application for you. You have to define all the components you need and compose the final interface out of these smaller building blocks. In that approach, you don’t control the application rendering lifecycle.

In other words, when and how to repaint things on screen is purely React Native’s responsibility. React looks out for the changes you have done to your components, compares them, and, by design, only performs the required and smallest number of actual updates.

By default, a component can re-render if its parent is re-rendering or the props are different. This means that your component’s render method can sometimes run, even if their props didn’t change. This is an acceptable tradeoff in most scenarios, as comparing the two objects (the previous and current props) would take longer.

# NEGATIVE IMPACT ON PERFORMANCE, UI FLICKER, AND FPS DECREASE

While the above heuristics are correct most of the time, performing too many operations can cause performance problems, especially on low-end mobile devices.

As a result, you may observe your UI flickering (when the updates are performed) or frames dropping (while there’s an animation happening and an update is coming along).

Note: Performing premature optimizations may have the opposite of the intended effect. Try looking at performance issues as soon as you spot dropped frames or undesired performance within your app.

As soon as you see any of these symptoms, it is the right time to look a bit deeper into your application lifecycle and look for extraneous operations that you would not expect to happen.

# HOW DO WE KNOW WHAT TO OPTIMIZE?

When it comes to performance optimization, we want to make decisions based on data. The data comes from measuring performance using specialized tools. The process is often referred to as profiling. There are many tools available that can help us with profiling our React Native apps: react-devtools, why-did-you-render, Profiler, and others.

For this exercise, we’ll use Flipper, a platform for debugging iOS, Android, and React Native apps. It has React DevTools Profiler integrated as a plugin that can produce a flame graph of the React rendering pipeline as a result of profiling. We can leverage this

# Flipper (0.176.0)

# APP INSPECT

# DevTools 4.24.3-46a98cff2

# Components

# Profiler

MyForkedApp

React Native

Flamegraph

Ranked Timeline

Plugins

- Device
- Crash Reporter
- Headless-demo
- Logs
- React Native
- Headless-demo
- No profiling data has been recorded.
- Click the record button to start recording.
- Logs
- React DevTools
- Disabled
- Unavailable plugins

# Here is the code we’re about to profile:

import React, { useEffect, useState } from 'react';
import { View } from 'react-native';

const App = () => {
const [value, setValue] = useState('');
const backgroundStyle = {
backgroundColor: '#fff',
flex: 1,
marginTop: 80,
};

useEffect(() => {
setTimeout(() => {
setValue('update 1');
}, 3000);
setTimeout(() => {
setValue('update 2');
}, 5000);
}, []);

return (
<view style="{backgroundStyle}">
<coloredview>
</coloredview></view>
);
};
const ColoredView = () => {
const style = { backgroundColor: 'red', padding: 10 };
return <view style="{style}">;
};

export default App;
</view>

# In the Flipper app, make sure the ''Record why each component rendered while profiling'' option is enabled in the settings icon and hit the round blue button to start profiling.

After around 5 seconds, hit the round red button to stop profiling. Your profile will look something like this:

|                                   | Components  | Profiler             |                      |     |
| --------------------------------- | ----------- | -------------------- | -------------------- | --- |
| 0 +                               | 4           | Timeline             | ColoredView          | X   |
| RootComponent (MyforkedApp)       |             | Why did this render? | The parent component |     |
| PerformanceLoggerContext.Provider |             | 1.6s for 4.4ms       |                      |     |
| AppContainer                      |             |                      |                      |     |
| RootTagContext.Provider           |             | 3.6s for 0.5ms       |                      |     |
| View (ForwardRef)                 |             |                      |                      |     |
| TextAncestorContext.Provider      |             |                      |                      |     |
| View (ForwardRef) key="1"         |             | App (4.1ms of 4.4ms) |                      |     |
| View (ForwardRef)                 |             | (0.1ms of 0.3ms)     |                      |     |
| TextAncestorContext.Provider      |             |                      |                      |     |
|                                   | ColoredView |                      | (0.1ms of 0.2ms)     |     |

This profile shows us how much time a certain component took to render, how many times it re-rendered, and what was the cause of it. In our case, ColoredView rendered 2 times due to the parent component being re-rendered. This might give us a hint that there’s an unexpected performance implication of the code associated with ColoredView. Using this knowledge, we can apply tailored solutions to avoid the extra re-renders.

Taking a look at the performance flame graph for the first time may be slightly intimidating. To understand React DevTools more in-depth, this video from Ben Awad is good at explaining it. Don’t forget to watch this talk by Alex at React Native EU, which explains how we can use flame graph to identify and fix the issues. Also, visit the official react website for detailed information on React Profiler.

# SOLUTION: OPTIMIZE THE NUMBER OF STATE OPERATIONS AND REMEMBER TO USE MEMOIZED COMPONENTS WHEN NEEDED.

There’re a lot of ways your application can turn into unnecessary rendering cycles and that point itself is worth a separate article. Here, we will focus on two common scenarios – using a controlled component, such as TextInput and global state.

# CONTROLLED VS UNCONTROLLED COMPONENTS

Let’s start with the first one. Almost every React Native application contains at least one TextInput that is controlled by the component state as per the following snippet:

import React, { useState } from 'react';
import { TextInput, StyleSheet } from 'react-native';

const UselessTextInput = () => {
const [value, setValue] = useState('Text');

const onChangeText = (text) => {
setValue(text);
};

return (
<textinput accessibilitylabel="" text="" input="" field&#x27;&#x27;="" style="{styles.textInput}" onchangetext="{onChangeText}" value="{value}">
);
};

const styles = StyleSheet.create({
textInput: {
height: 40,
borderColor: 'gray’,
borderWidth: 1,
},
});

export default UselessTextInput;</textinput>
Read more: https://snack.expo.dev/@callstack-snack/textinput-example

The above code sample will work in most cases. However, on slow devices, and in situations where the user is typing really fast, it may cause a problem with the view updates.

This problem is caused by React Native’s asynchronous nature. To better understand what is going on here, let’s first take a look at the order of standard operations that occur while the user is typing and populating your &#x3C;TextInput /> with new characters.

# Diagram that shows what happens while typing TEST

As soon as the user starts inputting a new character into the native input, an update is sent to React Native via the onChangeText prop (operation 1 on the above diagram). React processes that information and updates its state accordingly by calling setState. Next, a controlled component synchronizes its JavaScript value with the native component value (operation 2 on the above diagram).

There are benefits to such an approach. React is a source of truth that dictates the value of your inputs. This technique lets you alter the user input as it happens, by e.g. performing a validation, masking it, or completely modifying it.

Unfortunately, the aforementioned approach, while ultimately cleaner and more compliant with the way React works, has one downside and it is most noticeable when there are limited resources available and/or the user is typing at a very high rate.

# Diagram that shows what happens while typing TEST too fast

When the updates via onChangeText arrive before React Native synchronized each of them back, the interface will start flickering. The first update (operation 1 and operation 2) performs without issues as the user starts typing T.

Next, operation 3 arrives, followed by operation 4. The user typed E &#x26; S while React Native was busy doing something else, delaying the synchronization of the letter E (operation 5). As a result, the native input will temporarily change its value back from TES to TE.

Now, the user was typing fast enough to actually enter another character when the value of the text input was set to TE for a second. As a result, another update arrived (operation 6), with the value of TET. This wasn’t intentional – the user wasn’t expecting the value of its input to change from TES to TE.

Finally, operation 7 synchronized the input back to the correct input received from the user a few characters before (operation 4 informed us about TES). Unfortunately, it was quickly overwritten by another update (operation 8), which synchronized the value to TET – the final value of the input.

The root cause of this situation lies in the order of operations. If operation 5 was executed before operation 4, things would have run smoothly. Also, if the user didn’t type T when the value was TE instead of TES, the interface would flicker but the input value would remain correct.

One of the solutions for the synchronization problem is to remove the value prop from TextInput entirely. As a result, the data will flow only one way, from the native to the JavaScript side, eliminating the synchronization issues that were described earlier.

import React, { useState } from 'react';
import { Text, TextInput, View, StyleSheet } from 'react-native';

const PizzaTranslator = () => {
const [value, setValue] = useState('');

const onChangeText = (text) => {
setValue(text);
};

return (
<view style="{styles.container}">
<textinput accessibilitylabel="Text input field" placeholder="Type  here to translate!" onchangetext="{onChangeText}" defaultvalue="{value}" style="{styles.textInput}">
<text style="{styles.label}">
{value
.split(' ') 🍕
.map((word) => word &#x26;&#x26; ' ’)
.join(' ')}
</text>
</textinput></view>
);
};

export default PizzaTranslator;

const styles = StyleSheet.create({
container: {
padding: 10,
},
textInput: {
height: 40,
},
label: {
padding: 10,
fontSize: 42,
},
});

Read more: https://snack.expo.dev/@callstack-snack/handling-text-input

However, as pointed out by @nparashuram in his YouTube video (which is a great resource to learn more about React Native performance), that workaround alone isn’t enough in some cases. For example, when performing an input validation or masking, you still need to control the data that the user is typing and alter what ends up being displayed within TextInput.

GLOBAL STATE

Another common reason for performance issues is how components are dependent on the application’s global state. The worst case scenario is when the state change of a single control like TextInput or CheckBox propagates the render of the whole application. The reason for this is a bad global state management design.

First, your state management library should take care of updating components only when a defined subset of data has changed – here comes the useSelector hooks (use them in favor of connect function, as they are simpler to use).

Second, if your component uses data in a different shape than what is stored in your state, it may re-render, even if there is no real data change. To avoid this situation, you can implement a selector that would memorize the result of the derivation until the set of passed dependencies changes. In Redux Toolkit you have createSelector which is meant for creating memoized selectors.

import { createSelector } from '@reduxjs/toolkit';

const selectVisibilityFilter = (state) => state.visibilityFilter;
const selectAllTodos = (state) => state.todos;
const selectVisibleTodos = createSelector(
[selectVisibilityFilter, selectAllTodos],
(filter, todos) => {
switch (filter) {
case 'SHOW_COMPLETED':
return todos.filter((t) => t.completed);
case 'SHOW_UNCOMPLETED':
return todos.filter((t) => !t.completed);
default:
return todos;
}
},
);

# const TodoList = () => {

const todos = useSelector(selectVisibleTodos);

return (

&#x3C;FlatList
data={todos}
renderItem={({ item }) => (
&#x3C;TodoItem name={item.name} completed={item.completed}/>
)}
keyExtractor={(item) => item.id}
/>
);

# A typical example of memoized selectors with Redux Toolkit

A common bad performance practice is the belief that a state management library can be replaced by using a custom implementation based on React Context. It may be handy at the beginning because it reduces the boilerplate code that state management libraries introduce. But using it without proper memoization will lead to huge performance drawbacks. You will probably end up refactoring state management to Redux, because it will turn out that it is easier than the implementation of custom selectors to your current solution.

You can also optimize your application on a single component level. Using React.memo or React.useMemo will likely save you a lot of re-renders – the React Profiler can tell you precisely how many. Try not to implement these techniques in advance, because it may be premature optimization. In rare cases, memoization can lead to the app being less performant due to increased memory usage. Which is impossible to measure with JS tooling. Always make sure to profile the 'before' and 'after' of your changes to have certainty it makes the app faster.

# STATE NORMALIZATION (REDUX TOOLKIT):

In app development, it is common to work with entities, which are collections of data where each unique record has a unique ID value.

in a specific field, such as User, Post, Todo, Comment. State normalization is a recommended approach to managing entities in a standardized and organized manner in a Redux store. It significantly helps with CRUD (create, read, update, delete) operations, while maintaining high performance. It involves treating a portion of the store as if it were a database and keeping that data in a normalized form.

Imagine you have a stack of important documents on your desk. If you take the time to sort them, put them into binders, tag each binder with an ID, and prepare the list of IDs in order how you put the binders on the shelf, you will be able to find the document you need much more quickly in the future. This is much more efficient than digging through an unorganized stack every time you need to find something but requires some time for preparation.

Similarly we can organize an array of blog posts – we need to transform the array into a mapped record of entities addressed by their IDs (the binders with IDs) and an array of IDs which is used to indicate ordering (list of binders on the shelf).

const blogPosts = [
{
id: ''post1'',
author: { username: ''user1'', name: ''User 1'' },
body: ''......'',
comments: [
{
id: ''comment1'',
author: { username: ''user2'', name: ''User 2'' },
comment: ''.....'',
},
{
id: ''comment2'',
author: { username: ''user3'', name: ''User 3'' },
comment: ''.....'',
},
],
},
{
id: ''post2'',
author: { username: ''user2'', name: ''User 2'' },

# Blog Posts

# Post 1

......

# Comments

User 1: .....

User 2: .....

# Post 2

......

# Comments

User 3: .....

User 1: .....

User 3: .....

# Comments

| Comment ID | Author | Comment |
| ---------- | ------ | ------- |
| comment1   | User 2 | .....   |
| comment2   | User 3 | .....   |
| comment3   | User 3 | .....   |
| comment4   | User 1 | .....   |
| comment5   | User 3 | .....   |

# Managing Big Amounts of Data with Redux Toolkit

Thanks to immediate access to each individual entity by its ID, we have a fast method of managing big amounts of data. Not only selecting is fast, but also adding, upserting, updating and deleting.

In the Redux Toolkit we have a createEntityAdapter method which handles this mechanism automatically and returns a dedicated set of tools: CRUD functions, selectors and sorting helpers.

import {
createEntityAdapter,
createSlice,
PayloadAction,
nanoid,
} from '@reduxjs/toolkit';
import { RootState } from '../../store';

export interface Todo {
id: string;
name: string;
completed: boolean;
}

const todoEntity = createEntityAdapter<todo>();

export const todoSlice = createSlice({
name: 'todo',
initialState: todoEntity.getInitialState(),
reducers: {
addTodo(state, { payload: { name } }: PayloadAction&#x3C;{
name: string }>) {
todoEntity.addOne(state, {
name,
id: nanoid(),
completed: false,
});
},
removeTodo(state, { payload }: PayloadAction<string>) {
todoEntity.removeOne(state, payload);
},
updateValue(state, action: PayloadAction<todo>) {
todoEntity.upsertOne(state, action);
},
updateBy(state, { payload: { id } }: PayloadAction&#x3C;{ id: string }>) {
const previousValue = state.entities[id]?.completed;
</todo></string></todo>

if (typeof previousValue === 'boolean') {
todoEntity.updateOne(state, {
id,
changes: { completed: !previousValue },
});
}
},
},
});

export const todoActions = todoSlice.actions;

export type TodoSlice = {
[todoSlice.name]: ReturnType&#x3C;(typeof todoSlice)['reducer']>;
};

const globalizedTodoSelector = (state: RootState) => state[todoSlice.name];

const entitySelectors = todoEntity.getSelectors<rootstate>((state) =>
globalizedTodoSelector(state),
);

export const todoSelectors = {
...entitySelectors,

The primary content of an entity adapter is a set of generated reducer functions for adding, updating, and removing entity instances from an entity state object:

const todoEntity = createEntityAdapter<todo>()

The entity adapter contains a getSelectors() function that returns a set of selectors that know how to read the contents of an entity state object:

const entitySelectors = todoEntity.getSelectors<rootstate>((state) =>
state[todoSlice.name])
</rootstate></todo></rootstate>

# ATOMIC STATE

The pattern of a single store – a top-down mental model – as initially promoted by Redux is moving towards a more atomic design.

# Why is it moving away from a single store?

- It’s often overkill for some apps.
- It’s too verbose.
- You end up using memoization techniques to avoid re-renders.
- Top-down is straightforward but leads to poor performance.
- More states are needed when the app grows, and each has its own problems and sub-states, such as handling local UI states (loadings, errors, messages, etc).

If you don’t pay attention to the Redux store, it tends to absorb all the states, leading to a monolithic structure that’s quite hard to reason with. The top-down build places most of the states at the top of the component; because of this, a state update from a parent component could produce re-renders to its children. Ideally, if possible, the state should be local to the component so it can be reused – this means building from the bottom-up.

To start thinking about this bottom-up pattern, we want to build from the smaller components, often called atoms. We don’t build the component starting from the parent (or "root" container element), we need to look at all the elements that make up the component. We then have to start from the atom and add the right state action, if needed.

Let’s say we have a TODO list with some filters: "show all", "just the active ones", or "just the completed ones". We identify the top component, the TodoList, but we don’t start here. We first identify the children and start building those smaller components, so that later we can mix them and build a complex element. We need to make some data visible in one component which will be managed by another one. To avoid a parent state and passing down the data and actions (top-down), we are going to use a state manager. This state manager will be in charge of storing the data, making it accessible, and providing actions/modifiers, because we

# Bottom-Up Approach with Zustand

We are moving to a bottom-up approach. We are going to use some libraries that will help us.

# Zustand

Zustand is often used as a top-down pattern but given the simplicity and unopinionated library, we can use it to build a component bottom-up.

# Store

We create the obj where the filter will be and the modifiers will be exposed:

export const useHomeStore = create((set) => ({
filter: filterType.all,
showAll: () => set({ filter: filterType.all }),
showOnlyCompleted: () => set({ filter: filterType.completed }),
showOnlyActive: () => set({ filter: filterType.active }),
}));

# Show all filter button

Here we update the ticket and this item so any children won’t suffer a re-render:

const ShowAllItem = () => {
const showAll = useHomeStore((state) => state.showAll);
return ;
};

# Todo item

Here because we are looking at a filter, TodoItemList will only re-render when it changes.

export const TodoItemList = ({ item }) => {
const filter = useHomeStore((state) => state.filter);
if (!shouldBeShown(filter, item.done)) {
return null;
}

return (
<view>
<text>{item.title}</text>
<text>{item.description}</text>
</view>
);
};

# Jotai

Jotai was built with this bottom-up approach in mind, so its syntax is minimal and simple. Using the concept of atom as a ''store'' then you use different hooks to make the atom readonly or mutable.

# Store

We use useAtomValue to read the filter value and useSetAtom to set a new value. This is especially useful when performance is a concern.

const filter = atom(filterType.all);

export const useCurrentFilter = () => useAtomValue(filter);
export const useUpdateFilter = () => useSetAtom(filter);

# FilterMenuItem

const FilterMenuItem = ({ title, filterType }) => {
const setUpdateFilter = useUpdateFilter();
const handleShowAll = () => setUpdateFilter(filterType);

return ;
};

# TodoItem

export const TodoItemList = ({ item }) => {
const filter = useCurrentFilter();

if (!shouldBeShown(filter, item.done)) {
return null;
}

return (
<view>
<text>{item.title}</text>
<text>{item.description}</text>
</view>
);
};

Using this bottom-up approach, we can prevent state changes on the parent component, and produce re-renders to its children. In addition, it often leads to less overuse of memoization.

# FUTURE WITH REACT FORGET

Manual memory management is not fun to most of the builders out there – whether it’s about deallocating memory with C or manually memoizing components and values with React. We usually dive into languages or use smart compilers to handle that for us.

React Forget is an "auto-memoizing compiler" for React which promises to enhance component re-rendering and might even eliminate the need for using memo(), useCallback() and useMemo() altogether. The compiler memoizes not only the calculation of useMemo() results but also the resulting React element objects returned by the component.

The name React Forget comes from the principle with which this tool is supposed to work. The component level optimisations and memoization will be taken care of by the compiler, so you can "forget" about all the overhead and extra boilerplate that came with doing this by hand.

# React Forget and Todo List Example

Note: It’s worth mentioning that as of the time of writing this chapter, React Forget is still under development and has not been released yet to the wider public. There’s a great video from React Conf 2021, where @Huxpro describes how React Forget will work underneath the hood. And in 2023, we received an update from Joe Savona and Mofei Zhang from Meta at React Advanced 2023 on the state of development and experimentation at instagram.com website.

Let’s take a look at the example code for todo list application from the previous chapter about atomic state and see how it can be simplified with the future Forget compiler.

We have a TodoListItem, which we would like to use in a TodoList component. In order for not having multiple unnecessary rerenders when adding todos, changing the visibility or themeSettings we would need to wrap it with React.memo. We need to also remember about all the functions inside the component which will be recreated with every render such as handleChange. There are a lot of things there to memoize and remember about handling manually. That can quickly get really annoying.

const MemoizedTodo = React.memo(TodoListItem);

const TodoList = ({ visibility, themeSettings }) => {
const [todos, setTodos] = useState(initialTodos);

const handleChange = useCallback((todo) => {
setTodos((todos) => getUpdated(todos, todo));
}, []);

const doneTodosNumber = useMemo(getDoneTodos(todos, visibility), []);

return (
<view>
<flatlist data="{todos}" renderitem="{MemoizedTodo}">
<text>Done: {doneTodosNumber}</text>
<touchableopacity onpress="{handleChange}">
<text>Change</text>
</touchableopacity>
</flatlist></view>
);
};

# React Forget

React Forget aims to resolve that issue forever. The promise is that the code for the aforementioned example will look like follows:

const TodoList = ({ visibility, themeSettings }) => {
const [todos, setTodos] = useState(initialTodos);

const handleChange = setTodos((todos) => getUpdated(todos, todo));

const doneTodosNumber = getDoneTodos(todos, visibility);
return (
<view>
<flatlist data="{todos}" renderitem="{TodoListItem}">
<text>Done: {doneTodosNumber}</text>
<touchableopacity onpress="{handleChange}">
<text>Change</text>
</touchableopacity>
</flatlist></view>
);
};
and it will behave exactly the same as the previous example with manual memoization.

There will be no need for using useCallback or memo and the code will be optimized by the compiler. Very neat.

As authors of this book, we’re all excited for React Forget and can’t wait when it ships. Hopefully we’ll be able to remove most of the topics related to manual memory memoization management.

# BENEFITS: FEWER RESOURCES NEEDED AND A FASTER APPLICATION.

You should always keep the performance of your app in the back of your head. Beware of optimizing too fast. Some say that premature optimization is the root of all evil. They’re not entirely correct, but also not entirely wrong. Premature memoization may lead to more memory usage and provide only a fraction of improvement compared to the effort taken. That’s why measuring and identifying impactful problems to tackle is so important.

Most hard-to-solve performance issues are caused by bad architectural decisions around state management. Different libraries juggle different sets of tradeoffs. Make sure you and your team

understand them and pick the tool you’re most productive with.

For some, it may be the verbosity of Redux. But others may pre-

fer the ease of Zustand that avoids having to think about extra re-renders.

With all these steps in mind, your application should perform few-

er operations and need smaller resources to complete its job. As

a result, this should lead to lower battery usage and more satis-

faction from interacting with the interface.

# PART 1

# CHAPTER 2

# USE DEDICATED COMPONENTS FOR CERTAIN LAYOUTS

9

# FIND OUT HOW TO USE DEDICATED HIGHER-ORDERED REACT NATIVE COMPONENTS TO IMPROVE THE USER EXPERIENCE AND THE PERFORMANCE OF YOUR APPS

ISSUE: YOU ARE UNAWARE OF THE HIGHER-ORDER COMPONENTS THAT ARE PROVIDED WITH REACT NATIVE.

In a React Native application, everything is a component. At the end of the component hierarchy, there are so-called primitive components, such as Text, View, or TextInput. These components are implemented by React Native and provided by the platform you are targeting to support the most basic user interactions.

When we're building our application, we compose it out of smaller building blocks. To do so, we use primitive components. For example, in order to create a login screen, we would use a series of TextInput components to register user details and a Touchable component to handle user interaction. This approach is true from the very first component that we create within our application and holds true through the final stage of its development.

On top of primitive components, React Native ships with a set of higher-order components that are designed and optimized to serve a certain purpose. Being unaware of them or not using them can potentially affect your application performance, especially as you populate your state with real production data. A bad performance of your app may seriously harm the user experience. In consequence, it can make your clients unsatisfied with your product and turn them towards your competitors.

# NOT USING SPECIALIZED COMPONENTS WILL AFFECT YOUR PERFORMANCE AND UX AS YOUR DATA GROWS.

If you're not using specialized components, you are opting out of performance improvements and risking a degraded user experience when your application enters production. It is worth noting that certain issues remain unnoticed while the application is developed, as mocked data is usually small and doesn't reflect the size of a production database. Specialized components are more comprehensive and have a broader API to cover than the vast majority of mobile scenarios.

# SOLUTION: ALWAYS USE A SPECIALIZED COMPONENT, E.G. FLATLIST FOR LISTS.

Let's take long lists as an example. Every application contains a list at some point. The fastest and dirtiest way to create a list of elements would be to combine ScrollView and View primitive components.

However, such an example would quickly become problematic when the data grows. Dealing with large data-sets, infinite scrolling, and memory management was the motivation behind FlatList – a dedicated component in React Native for displaying and working with data structures like this.

# Compare the performance of adding a new list element based on ScrollView

import React, { useCallback, useState } from 'react';
import { ScrollView, View, Text, Button, StyleSheet } from 'react-native';

const objects = [
['avocado', '🥑'],
['apple', '🍏'],
['orange', '🍊'],
['cactus', '🌵'],
['eggplant', '🍆'],
['strawberry', '🍓'],
['coconut', '🥥'],

# List Component

const getRandomItem = () => {
const item = objects[~~(Math.random() * objects.length)];

return {
name: item[0],
icon: item[1],
id: Date.now() + Math.random(),
};
};

const \_items = Array.from(new Array(5000)).map(getRandomItem);

const List = () => {
const [items, setItems] = useState(\_items);

const addItem = useCallback(() => {
setItems([getRandomItem()].concat(items));
}, [items]);

return (
<view style="{styles.container}">

<scrollview>
{items.map(({ name, icon, id }) => (
<view style="{styles.itemContainer}" key="{id}">
<text style="{styles.name}">{name}</text>
<text style="{styles.icon}">{icon}</text>
</view>
))}
</scrollview>

);
};

const styles = StyleSheet.create({
container: {
marginTop: 30,
},
itemContainer: {
borderWidth: 1,
margin: 3,
padding: 5,
flexDirection: 'row',
},
name: {
fontSize: 20,
width: 150,
},
icon: {
fontSize: 20,
},
});

export default List;
</view>
Read more: https://snack.expo.dev/@callstack-snack/scrollview-example

# React Native Example

import React, { useCallback, useState } from 'react';
import { View, Text, Button, FlatList, StyleSheet } from 'react-native';

const objects = [
'avocado 🥑',
'apple 🍏',
'orange 🍊',
'cactus 🌵',
'eggplant 🍆',
'strawberry 🍓',
'coconut 🥥',
];

const getRandomItem = () => {
const item = objects[~~(Math.random() * objects.length)].split(' ');

return {
name: item[0],
icon: item[1],
id: Date.now() + Math.random(),
};
};

const \_items = Array.from(new Array(5000)).map(getRandomItem);

const List = () => {
const [items, setItems] = useState(\_items);

const addItem = useCallback(() => {
setItems([getRandomItem()].concat(items));
}, [items]);

const keyExtractor = useCallback(({ id }) => id.toString(), []);

const renderItem = useCallback(
({ item: { name, icon } }) => (
<view style="{styles.itemContainer}">
<text style="{styles.name}">{name}</text>
<text style="{styles.icon}">{icon}</text>
</view>
),
[],
);

return (
<view style="{styles.container}">

<flatlist data="{items}" keyextractor="{keyExtractor}" renderitem="{renderItem}">

);
};
</flatlist></view>

# FlatList Performance

const styles = StyleSheet.create({

- container: { marginTop: 30, },
- itemContainer: { borderWidth: 1, margin: 3, padding: 5, flexDirection: 'row', },
- name: { fontSize: 20, width: 150, },
- icon: { fontSize: 20, },

});

export default List;

Read more: https://snack.expo.dev/@callstack-snack/flatlist-example

The difference is significant, isn't it? In the provided example of 5000 list items, the ScrollView version does not even scroll smoothly.

At the end of the day, FlatList uses ScrollView and View components as well. What's the deal then?

Well, the key lies in the logic that is abstracted away within the FlatList component. It contains a lot of heuristics and advanced JavaScript calculations to reduce the amount of extraneous renderings that happen while you're displaying the data on screen and to make the scrolling experience always run at 60FPS. Just using FlatList may not be enough in some cases. FlatList performance optimizations rely on not rendering elements that are currently not displayed on the screen.

The most costly part of the process is layout measuring. FlatList has to measure your layout to determine how much space in the scroll area should be reserved for upcoming elements.

For complex list elements, it may slow down the interaction with FlatList significantly. Every time FlatList approaches

# FLASHLIST AS A SUCCESSOR TO FLATLIST

to render the next batch of data, it will have to wait for all the new items to render to measure their height.

However, you can implement getItemHeight() to define the element height up-front without the need for measurement. It is not straightforward for items without a constant height. You can calculate the value based on the number of lines of text and other layout constraints.

We recommend using the react-native-text-size library to calculate the height of the displayed text for all list items at once. In our case, it significantly improved the responsiveness for scroll events of FlatList on Android.

# FLASHLIST AS A SUCCESSOR TO FLATLIST

As already discussed, FlatList drastically improves the performance of a huge list compared to ScrollView. Despite proving itself as a performant solution, it has some caveats.

There are popular cases where developers or users have encountered, for instance, blank spaces while scrolling, laggy scrolling, and a list not being snappy, almost on a daily basis. FlatList is designed to keep certain elements in memory, which adds overhead on the device and eventually slows the list down, and blank areas happen when FlatList fails to render the items fast enough.

We can, however, minimize these problems to some extent by following the tips here, but still, in most cases, we want more smoothness and snappy lists. With FlatList, the JS thread is busy most of the time and we always fancy having that 60FPS tag associated with our JS thread when we're scrolling the list.

So how should we approach such issues? If not FlatList, then what? Luckily for us, the folks at Shopify developed a pretty good drop-in replacement for FlatList, known as FlashList. The library works on top of RecyclerListView, leveraging its recycling capability and fixing common pain points such as

complicated API, using cells with dynamic heights, or first render layout inconsistencies.

FlashList recycles the views that are outside of the viewport and re-uses them for other items. If the list has different items, FlashList uses a recycle pool to use the item based on its type. It's crucial to keep the list items as light as possible, without any side effects, otherwise, it will hurt the performance of the list.

There are a couple of props that are quite important with FlashList. First is estimatedItemSize, the approximate size of the list item. It helps FlashList to decide how many items to render before the initial load and while scrolling. If we have different-sized items, we can average them. We can get this value in a warning by the list, if we do not supply it on the first render and then use it forward. The other way is to use the element inspector from the dev support in the React Native app.

The second prop is overrideItemLayout, which is prioritized over estimatedItemSize. If we have different-sized items and we know their sizes, it's better to use them here instead of averaging them.

Let's talk about measuring FlashList. Remember to turn on release mode for the JS bundle beforehand. FlashList can appear to be slower than FlatList in dev mode. The primary reason is a much smaller and fixed windowSize equivalent. We can leverage FlashList's built-in callback functions to measure the blank area onBlankArea and list load time onLoad. You can read more about available helpers in the Metrics section of the documentation.

We can also use Bamlab's Flashlight, which gives us the results for FPS on the release builds in the form of a performance report. It also creates a nice-looking graph of CPU usage over the period of profiling, so we can verify how certain actions affect this metric. For now, Flashlight supports Android only, but the team is working on supporting iOS.

# Performance report from Bamlab's Flashlight

| Flatlist             | FLASH-list |                      |          |
| -------------------- | ---------- | -------------------- | -------- |
| 25                   | 68         |                      |          |
| Average Test Runtime | 35483 ms   | Average Test Runtime | 29318 ms |
| Average FPS          | 53.2 FPS   | Average FPS          | 56.4 FPS |
| Average CPU usage    | 216 %      | Average CPU usage    | 141.1%   |
| High CPU Usage       | 14.8 s     | High CPU Usage       | 4.3 s    |
| Average RAM usage    | 202.9 MB   | Average RAM usage    | 168.3 MB |

# Frame rate (FPS)

| 4600 | 9200 |     | 13800 | 18400 | 23000 |
| ---- | ---- | --- | ----- | ----- | ----- |

With Flashlight there is no need to install anything in your app, making this tool even easier to use. It can also measure performance of production apps and generate very handsome looking web reports which include: Total CPU usage, CPU usage per thread and RAM utilization.

There are 2 ways of using Flashlight – you can run it locally:

- curl https://get.flashlight.dev
- bash

or in the cloud with flashlight.dev

Thanks to using specialized components, your application will always run as fast as possible. You can automatically opt-in to all the performance optimizations performed by React Native and subscribe for further updates. At the same time, you also save

yourself a lot of time reimplementing the most common UI patterns from the ground up, sticky section headers, pull to refresh – you name it. These are already supported by default if you choose to go with FlashList.

# PART 1

# | CHAPTER 3

# THINK TWICE BEFORE YOU PICK AN EXTERNAL LIBRARY

# HOW WORKING WITH THE RIGHT JAVASCRIPT LIBRARIES CAN HELP YOU BOOST THE SPEED AND PERFORMANCE OF YOUR APPS.

# ISSUE: YOU ARE CHOOSING LIBRARIES WITHOUT CHECKING WHAT IS INSIDE

JavaScript development is like assembling applications out of smaller blocks. To a certain degree, it is very similar to building React Native apps. Instead of creating React components from scratch, you are on the hunt for the JavaScript libraries that will help you achieve what you had in mind. The JavaScript ecosystem promotes such an approach to development and encourages structuring applications around small and reusable modules.

This type of ecosystem has many advantages, but also some serious drawbacks. One of them is that developers can find it hard to choose from multiple libraries supporting the same use case.

When picking the one to use in the next project, they often research the indicators that tell them if the library is healthy and well maintained, such as GitHub stars, the number of issues, contributors, and PRs.

What they tend to overlook is the library's size, number of supported features, and external dependencies. They assume that since React Native is all about JavaScript and embracing the existing toolchain, they will work with the same constraints and best practices they know from making web applications.

Truth is, they won't, as mobile development is fundamentally different and has its own set of rules. For example, while the size of the assets is crucial in the case of web applications, it is not

# COMPLEX LIBRARIES HAMPER THE SPEED OF YOUR APPS

as equally important in React Native, where assets are located in the filesystem.

The key difference lies in the performance of the mobile devices and the tooling used for bundling and compiling the application.

Although you will not be able to do much about the device limitations, you can control your JavaScript code. In general, less code means faster opening time. And one of the most important factors affecting the overall size of your code is libraries.

Unlike a fully native application, a React Native app contains a JavaScript bundle that needs to be loaded into memory. Then it is parsed and executed by the JavaScript VM. The overall size of the JavaScript code is an important factor.

While that happens, the application remains in the loading state. We often describe this process as TTI – Time to Interactive. It is a time expressed in (well, hopefully) the milliseconds between when the icon gets selected from the application drawer and when it becomes fully interactive.

Unfortunately, Metro – the default React Native bundler – currently doesn't support tree shaking. If you're not familiar with this notion, read this article.

This means that all the code that you pull from NPM and import to your project will be present in your production JS bundle, loaded into memory, and parsed. That can have a negative impact on the total startup time of your application.

What's worth pointing out is that it's not the case with Hermes engine, which automatically pages only necessary bytecode into memory. Read more in the Hermes chapter.

# HOW DO WE ANALYZE BUNDLE SIZE

Keeping tabs on your bundle size is very important. We can make use of the react-native-bundle-visualizer to analyze the bundle with the help of GUI. We can get the details of any added library in the bundle; hence deciding if it's worth keeping or removing that library. This package produces output using the app bundle in the following form:

| /                            | 3 MB              | 100.0%    |
| ---------------------------- | ----------------- | --------- |
| node_modules                 | 1.65 MB           | 54.8%     |
| react-native                 | 574.3 KB          | 19.1%     |
| react-native-firebase        | 162.11 KB         | 5.4%      |
| Rendener                     | 171.57 KB         | 5.7%      |
| Components                   | 82.44 KB          |           |
| Lists                        | 56.8 KB           |           |
| Animated                     | modules           | 144.09 KB |
| oss                          | 170.44 KB         | 5.7%      |
| Touchable                    |                   |           |
| ReactNativeRenderer          | 23.06 KB          | 0.8%      |
| prod js                      | 86.72 KB          | 2.9%      |
| ReactFabric-prod             | 83.73 KB          | 2.8%      |
| Teadtinput                   | WebView           |           |
| vendor                       | 23.91 KB          |           |
| Utilities                    | 15.6 KB           |           |
| Network                      | Experimepolyfills |           |
| @react-navigation            | 69.76 KB          |           |
| react-navigation-stack       | moment            | 55.56 KB  |
| react-native-calendars       | mobx              | 52.49 KB  |
| react-native-reanimated      | core              | 43.94 KB  |
| lib                          | 34.8 KB           |           |
| module                       | 34.8 KB           | 0.9%      |
| react-native-svg             | 47.26 KB          |           |
| react-native-gesture-handler | react-native-maps |           |
| react-native-tab             | htmlparser2       | lodash    |
| react-navigation             | buffer            | 20.45 KB  |
| tinycolor2                   | react             |           |
| moba-react                   | lodash            | isequal   |
| src                          | 319.63 KB         | 10.6%     |
| screens                      | 172.07 KB         | 5.7%      |
| store                        | 66.1 KB           | 2.2%      |
| components                   | 62.67 KB          | 2.1%      |
| search                       | 30.92 KB          | 1.0%      |
| vehicle                      | 20.38 KB          | 1.0%      |

# SOLUTION: BE MORE SELECTIVE AND USE SMALLER SPECIALIZED LIBRARIES.

The easiest way to overcome this issue is to employ the right strategy for architecturing the project upfront.

If you are about to pull a complex library, check if there are smaller alternatives that have the functionality you're looking for.

Here's an example: One of the most common operations is manipulating dates. Let's imagine you are about to calculate an elapsed

# Parsing a date with moment.js

import moment from 'moment';

const date = moment('12-25-1995', 'MM-DD-YYYY');

# Parsing a date with day.js

import dayjs from 'dayjs';

const date = dayjs('12-25-1995', 'MM-DD-YYYY');
If there are no alternatives, a good rule of thumb is to check if you can import a smaller part of the library.

For instance, many libraries such as lodash have already split themselves into smaller utility sets and support environments where dead code elimination is unavailable.

Let's say you want to use lodash map. Instead of importing the whole library, (as presented here),

import { map } from 'lodash';

const square = (x) => x \* x;
map([4, 8], square);
Using lodash map by importing the whole library

# Using lodash map by importing only single function

import map from 'lodash/map';

const square = (x) => x \* x;
map([4, 8], square);

As a result, you can benefit from the utilities that are a part of the lodash package without pulling them all into the application bundle.

If you'd like to have constant insight into your dependencies' size impact, we highly recommend the import-cost VSCode extension or using the Bundlephobia website.

# BENEFITS: YOUR APP HAS A SMALLER FOOTPRINT AND LOADS FASTER.

Mobile is an extremely competitive environment, with lots of applications designed to serve similar purposes and fight over the same customers. Faster startup time, smoother interactions, and the overall look and feel might be your only way to stand out from the crowd.

You shouldn't downplay the importance of choosing the right set of libraries. Being more selective with third-party dependencies may seem irrelevant at first. But all the saved milliseconds will add up to significant gains over time.

# PART 1

# CHAPTER 4

ALWAYS REMEMBER TO USE

LIBRARIES DEDICATED TO

THE MOBILE PLATFORM

# USE LIBRARIES DEDICATED TO MOBILE

AND BUILD FEATURES FASTER ON MANY PLATFORMS AT ONCE, WITHOUT COMPROMISING ON THE PERFORMANCE AND USER EXPERIENCE.

# ISSUE: YOU USE WEB LIBRARIES THAT ARE NOT OPTIMIZED FOR MOBILE.

As discussed earlier, one of the best things about React Native is that you can write the mobile application with JavaScript, reuse some of your React components, and do business logic with your favorite state management library.

While React Native provides web-like functionality for compatibility with the web, it is important to understand that it is not the same environment. It has its own set of best practices, quick wins, and constraints.

For example, while working on a web application, we don’t have to worry too much about the overall CPU resources needed by our application. After all, most of the websites run on devices that are either plugged into the network or have large batteries.

It is not hard to imagine that mobile is different. There’s a wide range of devices with different architectures and resources available. Most of the time, they run on a battery and the drain caused by the application can be a deciding factor for many developers.

In other words – how you optimize the battery consumption both in the foreground and background can make all the difference.

# NOT OPTIMIZED LIBRARIES CAUSE BATTERY DRAIN AND SLOW DOWN

THE APP. THE OS MAY LIMIT YOUR APPLICATION/S CAPABILITIES.

While React Native makes it possible to run the same JavaScript on mobile as in the browser, that doesn’t mean you should be doing this every time. As with every rule, there are exceptions.

If the library depends heavily on networking, such as real-time messaging or offers the ability to render advanced graphics (3D structures, diagrams), it is very likely that you’re better off going with a dedicated mobile library.

Mobile libraries were developed within the web environment in the first place, assuming the capabilities and constraints of the browser. It is very likely that the result of using a web version of a popular SDK will result in extraneous CPU and memory consumption.

Certain OSs, such as iOS, are known to be constantly analyzing the resources consumed by the application in order to optimize the battery life. If your application is registered to perform background activities and these activities take too much of the resources, the interval for your application may get adjusted, lowering the frequency of the background updates that you initially signed up for.

# SOLUTION: USE A DEDICATED, PLATFORM-SPECIFIC VERSION OF THE LIBRARY.

Let’s take Firebase as an example. Firebase is a mobile platform from Google that lets you build your apps faster. It is a collection of tools and libraries that enable certain features instantly within your app.

Firebase contains SDKs for the web and mobile – iOS and Android respectively. Each SDK contains support for Realtime Database.

# Thanks to React Native, you can run the web version of it without major problems:

import { getDatabase, onValue, ref } from /firebase/database/;

const database = getDatabase();

onValue(ref(database, //users/123/), (snapshot) => {
console.log(snapshot.val());
});

# An example reading from Firebase Realtime Database in RN

However, this is not what you should be doing. While the above example works without issues, it does not offer the same performance as the mobile equivalent. The SDK itself also contains fewer features – no surprises here, as web is different and there’s no reason Firebase.js should provide support for mobile features.

In this particular example, it is better to use a dedicated Firebase library that provides a thin layer on top of dedicated native SDKs and offers the same performance and stability as any other native application out there.

Here s how the above example would look like:

import database from '@react-native-firebase/database';

database().ref('/users/123').on('value', (snapshot) => {
console.log(snapshot.val());
});

An example reading from Firebase Realtime Database in RN

As you can see, the difference is minimal. In this case, the library
authors did a great job mimicking the API to reduce the potential
confusion while switching back and forth between the web and
mobile context.

# BENEFITS: PROVIDE THE FASTEST AND MOST PERFORMANT SUPPORT WITH NO HARM TO THE BATTERY LIFE.

React Native is all about giving you control and freedom to choose
how you want to build your application.

For straightforward aspects and maximum reusability, you can
choose to go with the web version of the library. This will give

you access to the same features as in the browser with relatively low effort.

For advanced use cases, you can easily extend React Native with a native functionality and talk directly to the mobile SDKs. Such an escape hatch is what makes React Native extremely versatile and enterprise-ready. It allows you to build features faster on many platforms at once, without compromising on the performance and user experience – something other hybrid frameworks cannot claim.

# PART 1

# CHAPTER 5

# FIND THE BALANCE BETWEEN NATIVE AND JAVASCRIPT

# SEEK THE HARMONY BETWEEN NATIVE AND JAVASCRIPT TO BUILD FAST-WORKING AND LOW-MAINTENANCE APPS.

# ISSUE: WHILE WORKING ON NATIVE MODULES, YOU DRAW THE LINE IN THE WRONG PLACE BETWEEN NATIVE AND JAVASCRIPT ABSTRACTIONS

When working with React Native, you're going to be developing JavaScript most of the time. However, there are situations when you need to write a bit of native code. For example, you're working with a third-party SDK that doesn't have official React Native support yet. In that case, you need to create a native module that wraps the underlying native methods and exports them to the React Native realm.

All native methods need real-world arguments to work. React Native builds on top of an abstraction called a bridge, which provides bidirectional communication between JavaScript and native worlds.

Note: There's an ongoing effort to move away from asynchronous bridge communication to a synchronous one. You can read more about it in the New Architecture chapter.

As a result, JavaScript can execute native APIs and pass the necessary context to receive the desired return value. The communication itself is asynchronous – it means that while the caller is waiting for the results to arrive from the native side, the JavaScript is still running and may already be up for another task.

The number of JavaScript calls that arrive over the bridge is not deterministic and can vary over time, depending on the number of interactions that you do within your application. Additionally, each call takes time, as the JavaScript arguments need to be stringified into JSON, which is the established format that can be understood by these two realms.

For example, when the bridge is busy processing the data, another call will have to block and wait. If that interaction was related to gestures and animations, it is very likely that you have a dropped frame – the operation wasn't performed causing jitters in the UI.

# Performance Optimization in React Native

Certain libraries, such as Animated provide special workarounds. In this case, use NativeDriver, which serializes the animation, passes it once upfront to the native thread, and doesn't cross the bridge while the animation is running – preventing it from being subject to accidental frame drops while other work is happening.

That's why it is important to keep the bridge communication efficient and fast.

# MORE TRAFFIC FLOWING OVER THE BRIDGE MEANS LESS SPACE FOR OTHER THINGS

Passing more traffic over the bridge means that there is less space for other important things that React Native may want to transfer at that time. As a result, your application may become unresponsive to gestures or other interactions while you're performing native calls.

If you are seeing a degraded UI performance while executing certain native calls over the bridge or seeing substantial CPU consumption, you should take a closer look at what you are doing with the external libraries. It is very likely that there is more being transferred than should be.

# SOLUTION: USE THE RIGHT AMOUNT OF ABSTRACTION ON THE JS SIDE – VALIDATE AND CHECK THE TYPES AHEAD OF TIME.

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

# BENEFITS: THE CODEBASE IS FASTER AND EASIER TO MAINTAIN

Whether you're facing any performance challenges right now, it is smart to implement a set of best practices around native modules as the benefits are not just about the speed but also the user experience. Sure, keeping the right amount of the traffic flowing over the bridge will eventually contribute to your application performing better and working smoothly. As you can see, certain techniques mentioned in this section are already being actively used inside React Native to provide you a satisfactory performance out of the box. Being aware of them will help you create applications that perform better under a heavy load.

# HOWEVER, ONE ADDITIONAL BENEFIT THAT IS WORTH POINTING OUT IS THE MAINTENANCE.

Keeping the heavy and advanced abstractions, such as validation, on the JavaScript side will result in a very thin native layer that is nothing more but just a wrapper around an underlying native SDK. In other words, the native part of your module is going to look more like a copy-paste from the documentation – comprehensible and specific.

Mastering this approach to the development of native modules is why a lot of JavaScript developers can easily extend their applications with additional functionality without specializing in Objective-C or Java.

# PART 1

# | CHAPTER 6

# ANIMATE AT 60FPS – NO MATTER WHAT

# USE NATIVE SOLUTIONS TO ACHIEVE SMOOTH ANIMATIONS AND A GESTURE-DRIVEN INTERFACE AT 60FPS.

ISSUE: JS-DRIVEN ANIMATIONS ARE OCCUPYING THE BRIDGE TRAFFIC AND SLOWING DOWN THE APPLICATION.

Mobile users are used to smooth and well-designed interfaces that quickly respond to their interactions and provide prompt visual feedback. As a result, applications have to register a lot of animations in many places that will have to run while other work is happening.

As we know from the previous section, the amount of information that can be passed over the bridge is limited. There's currently no built-in priority queue. In other words, it is on you to structure and design your application in a way that both the business logic and animations can function without any disruptions. This is different from the way we are used to performing animations. For example, on iOS, the built-in APIs offer unprecedented performance and are always scheduled with the appropriate priority. Long story short – we don't have to worry too much about ensuring they're running at 60FPS.

With React Native, this story is a bit different. If you do not think about your animations top-down beforehand and choose the right tools to tackle this challenge, you're on track to run into dropped frames sooner or later.

# JANKY OR SLOW ANIMATIONS AFFECT THE PERCEPTION OF THE APP, MAKING IT LOOK SLOW AND UNFINISHED

In today's sea of applications, providing a smooth and interactive UI might be one of your only ways to win over customers who are looking to choose the app to go.

If your application fails to provide a responsive interface that works well with the user interactions (such as gestures), not only may it affect new customers, but also decrease the ROI and user sentiment.

Mobile users like the interfaces that follow them along and that look top-notch and ensure the animations are always running smoothly is a fundamental part that builds such an experience.

# SOLUTION: IF IT'S POSSIBLE, USE NATIVE AND CORRECT ANIMATIONS.

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

# GESTURE-DRIVEN ANIMATIONS

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

# GIVING YOUR JS OPERATIONS A LOWER PRIORITY

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

# BENEFITS: ENJOY SMOOTH ANIMATIONS AND A GESTURE-DRIVEN INTERFACE AT 60FPS.

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

# CHAPTER 7

REPLACE LOTTIE WITH RIVE

# LEVERAGE STATE MACHINES TO PROVIDE ROBUST INTERACTIVE ANIMATIONS AT 60FPS

# ISSUE: REAL-TIME ANIMATIONS SUFFERING FROM LOW FPS, FILE SIZE, AND NOT BEING ROBUST

When we talk about interactive mobile apps, we often think there'll be using certain user driven animations. For example, we can think of getting a nice order placed animation when we complete a checkout. A more complex example would be onboarding steps where the user has to tap on various buttons to move forward and, in most cases, each step shows a nice animation. So how can developers implement such behavior? One approach is using GIFs. If we have 3 onboarding steps, then we will want to have 3 GIFs. And often this solution is good enough performance – and UX-wise. But what if we need more fidelity in our animations? Or when it needs to be high quality, maybe on a full screen? GIFs can quickly add a few megabytes to our app's bundle.

So what other options do we have? Let's talk about Lottie. A mobile client for Android and iOS, which was created by the developers at Airbnb to leverage LottieFiles, which is JSON-based animation exported using the plugin BodyMoving from Adobe AfterEffects. They have a pretty good community with lots of free-to-use animations. Check it out here.

If we look at the React Native Lottie library, it is pretty popular and well-received by the community. We can control the animation using the progress prop or use imperative methods such as play. There are other useful props that we can use to suit our needs. Let's compare the size of a Lottie JSON animation and a corresponding GIF.

# Optimizing Animation Formats

Lottie JSON: 46.2 KB

Optimized Lottie JSON: 38.1 KB

18% smaller than Lottie JSON

dotLottie: 13.9 KB

ZIP Archive: 13.9 KB

GIF: 164.5 KB

Customize GIF: 0

MP4: 164.5 KB

Upload to My Workspace

Source: https://lottiefiles.com/128635-letter-d

If we compare, JSON is 46.2 KB and the GIF is 164.5 KB, which is almost 4 times as much as JSON. We can further reduce the size of JSON using the Optimized Lottie JSON but that's a paid solution. Now if we recall the above approach of having separate GIFs for each onboarding step, we can now use Lottie instead of GIFs since it's smaller. We can also use the remote resources of Lottie JSON instead of having it in a bundle but an extra effort will be required to keep it available for offline purposes.

We can still do better, but how good will that be if we use a single animation and control it using triggers? For example, if we tap on a button, the state of the animation changes for the next step. Let's say we want to change the size or do other customizations, we can't do it in the editor provided by LottieFiles. Instead, we will have to import that in Adobe AE and then do the adjustments and re-export it as JSON. We can, however, customize the color for layers in the web editor. Not everyone has expertise in using Adobe AE and has an animator to consult, e.g. if we're working on our pet project, we will want to adjust any animation in the web editor.

# SOLUTION: LEVERAGE DEVELOPER-FRIENDLY TOOLS WHICH OFFER BETTER FPS WITH LESS FILE SIZE.

There's a new tool in town called Rive. It aims to be an alternative to Lottie by providing everything Lottie does and then some. It also ships a web editor to customize real-time animations on the go. The editor allows the user to build interactive animations which have the capability to interact based on the inputs provided by the user. Having trigger-based animations is a great win, especially for mobile platforms.

Remember the approach we took for the onboarding steps animations? Now if we use Rive animations, we can leverage its state machine, triggers, and user inputs to use a single animation file for our onboarding steps. It really helps in improving the developer experience and the cherry on top: the size of the animation file is very small compared to Lottie JSON. We also don't have to keep different files for each onboarding step; hence saving some KBs for the bundle as well.

import React, { useRef } from 'react';
import { Button, SafeAreaView, StyleSheet } from 'react-native';
import Rive, { RiveRef } from 'rive-react-native';

const stateMachineOne = 'State Machine 1';

const App = () => {
const riveRef = useRef<riveref>(null);
const isRunning = useRef(false);

const onIsRunning = () => {
isRunning.current = !isRunning.current;
riveRef.current?.setInputState(
stateMachineOne,
'isRunning',
isRunning.current,
);
};</riveref>

const onSideKick = () => {
riveRef.current?.fireState(stateMachineOne, 'sideKick');
};

return (
<safeareaview>
<rive ref="{riveRef}" resourcename="" character&#x27;&#x27;="" style="{styles.character}" statemachinename="{stateMachineOne}" autoplay>

);
};

export default App;

const styles = StyleSheet.create({
character: {
width: 400,
height: 400,
},
});
</rive></safeareaview>
As we see, adding complex animation is developer-friendly. We can also add triggers or input-based animations quickly. All we need is the information regarding the state machine, inputs, and triggers. If we have an animator who built a beautiful animation for our project on Rive Editor, we can ask them to pass along the info. Otherwise, we can always look up this info in the web editor ourselves.

Now let's talk about performance in terms of FPS, CPU, and memory consumption. We will do a comparison of an animation that is built for Lottie with the same animation built for Rive. This tweet shows benchmarks done for the web platform. We'll extend this by using the same animations for Rive and Lottie on our React Native app.

Lottie

# Performance Metrics

# Lottie

Time: 7:31

Progress: 0100%

UI: 16.8 fps

JS: 16.8 fps

Dropped frames: 1711

Stutters: 3 (4+)

| Others    | 17.2 MB  |
| --------- | -------- |
| Code      | 33.8 MB  |
| Stack     | 0.05 MB  |
| Graphics  | 122.8 MB |
| Native    | 49.3 MB  |
| Java      | 23.1 MB  |
| Allocated | N/A      |
| Total     | 246.3 MB |

Lottie playing our animation at roughly 17 FPS both on JS and UI threads

# Rive

Time: 7:30

Progress: a0 100%

UI: 59.9 fps

JS: 59.9 fps

Dropped frames: 105

Stutters: 1 (4+)

| Others    | 17.9 MB  |
| --------- | -------- |
| Code      | 36.1 MB  |
| Stack     | 0.08 MB  |
| Graphics  | 184.1 MB |
| Native    | 25.6 MB  |
| Java      | 12.3 MB  |
| Allocated | N/A      |
| Total     | 276 MB   |

Rive playing our animation at roughly 60 FPS both on JS and UI threads

We benchmarked this on a Sony Xperia Z3 model using an Android profiler and Perf monitor that is shipped with the React Native app. We disabled the DEV mode so that our JS thread doesn't throttle because of it.

Both images show a tiny window right above the rocket with details of FPS on both the UI and JS thread. The results show

that the Rive animation runs almost at 60FPS whereas Lottie runs at 17FPS.

Now let's focus on the right part of both images, which is the Memory consumption detailed view. If we look closely, there are mainly three portions: Java, Native, and Graphics. Java represents the memory allocated for Java or Kotlin code. The Native represents the memory allocated from C or C++ code. The graphics represent the memory used for the graphics buffer queues to display pixels on the screen. In Java, Lottie uses almost 23 MB and Rive uses almost 12 MB of RAM. In Native, Lottie uses 49 MB and Rive uses 25 MB of RAM. In Graphics, Lottie consumes 123 MB, whereas Rive uses 184 MB of RAM. The total memory consumption of Lottie is 246 MB and Rive is 276 MB.

The results show that Rive outperforms Lottie in all departments except Graphics. The end user expects the app to run at 60FPS to enjoy a smooth user experience. If one has to do a trade-off between memory consumption and FPS, they might go with FPS as most of the devices have enough memory to exercise the app's needs.

# BENEFITS: A REDUCED REGRESSION CYCLE WHILE DEVELOPING A FEATURE AND A HAPPY USER BASE

If we opt-in to a world without state machines, the developers will be implementing the logic in their code. And each time there is a change in the interactivity of the animation, devs will be required to re-work their code. This is not a good developer experience.

Rive's state machines give designers the power to think as if they were coding and structure the state machine for an animation.

that will interact after being given a certain input. Now the developer can use that animation and implement the interactivity firing the inputs on the animation and be done with it. If this animation needs to be changed with the same inputs, the dev only needs to replace the animation source and that's it. More info here.

Almost 18.7% of people uninstall the app due to storage issues. This hurts the company's ROI. Developers should always pay attention to reducing the bundle size and the storage utilized by their app. In a tweet by Rive's CEO, the Lottie file was around 24.37 KB and the same Rive file was around 2 KB. At the end of the day, each KB saved adds up to a reduced app size. We always want to choose a library that best fulfills our needs by providing a better developer experience, ease of API, and a smooth experience for the end user.

# PART 1

# CHAPTER 8

# DRAW EFFICIENTLY ON A CANVAS WITH SKIA

ISSUE: CORE APPLICATION DESIGN

IDEA IS DIFFICULT TO IMPLEMENT WITH THE TRADITIONAL APPROACHES

PO or design team may have the uncompromised vision of the product design or have in mind some specific features that may be difficult to build with Rive/react-native-reanimated without sacrificing performance or cross platform issues. Maybe there's an idea to adopt some design trend? Maybe the app will be graphs-heavy or will have a graphic-rich dashboard? Or maybe there's a plan to have a screen with performant and beautiful image transitions?

Component's shadow rendering approach is different in iOS and android, masking may be rather slow on android, limited blur support on android.

While being easy to use and performant tool, Rive also has some constraints like limited Blur, Glow, Shadow support and limited path effects.

So at the time this kind of issue is encountered you will most likely have in mind an exact picture you want to see in your app. And with the requirements that precise you will require the tool that can give you maximum control over the rendering pipeline.

# SOLUTION: MAYBE IT'S TIME TO CHECKOUT SKIA

Skia is an open source 2D graphics library which provides common APIs that work across a variety of hardware and software platforms. It serves as the graphics engine for Google Chrome and ChromeOS, Android, Flutter, Mozilla Firefox and Firefox OS, and many other products.

Thanks to Shopify, React Native developers have access to declarative Skia drawing capabilities using the @shopify/react-native-skia library. With it we can get full control over the rendering, down to

the pixels. It's a powerful instrument to cover almost any case you can imagine with the great performance overall.

# React Native Skia

React Native Skia's API uses the &#x3C;Canvas /> element that will be the last native element in the app's view tree and will serve as a root of your Skia drawing. All react-native-skia child components that will be put into it will serve as a declarative api for the library. Behind the scenes it'll use its own React renderer.

Here's an example of how @shopify/react-native-skia can be used, rendering two circles on the fixed size Canvas and blend them together.

import React from 'react';
import { useWindowDimensions } from 'react-native';
import { Canvas, Circle, Group, vec } from '@shopify/react-native-skia';

const App = () => {
const {width, height} = useWindowDimensions();
const c = vec(width / 2, height / 2);
const r = width \* 0.33;
return (
&#x3C;Canvas style={{ width, height }}>
&#x3C;Group blendMode='multiply'>
&#x3C;Circle cx={r} cy={c.y} r={r} color='cyan' />
&#x3C;Circle cx={width - r} cy={c.y} r={r} color='magenta' />
&#x3C;/Group>
&#x3C;/Canvas>
);
};

From this example we also can see one of the core elements of the API – the &#x3C;Group /> component. Groups can be deeply nested and can apply operations to their children:

- Paint properties – pretty similar to svg the properties applied to the group (ex. style, color) will be inherited by the child elements.
- Transformations – almost identical to React Native transform property with one significant difference: in React Native, the origin of transformation is the center of the object, whereas it is the top-left position of the object in Skia.
- Clipping – clip property provides the region in which children elements will be shown while outside region's part will be hidden. It can be reverted by the invertClip property.
- Bitmap effects – layer property will create bitmap drawing of the children which you can for example use to build effects that need to be applied to the group of elements.

To make one of the circles move we can use Reanimated:

import React from 'react';
import { useWindowDimensions } from 'react-native';
import { Canvas, Circle, Group, vec } from '@shopify/react-native-skia';
import {
Easing,
cancelAnimation,
useSharedValue,
withRepeat,
withTiming,
} from 'react-native-reanimated';

export const useLoop = ({ duration }) => {
const progress = useSharedValue(0);
useEffect(() => {
progress.value = withRepeat(
withTiming(1, { duration, easing: Easing.inOut(Easing.ease) }),
-1,
true
);
return () => {
cancelAnimation(progress);
};
}, [duration, progress]);
return progress;
};

const App = () => {
const ANIMATION_OFFSET = 50;
const {width, height} = useWindowDimensions();
const c = vec(width / 2, height / 2);
const r = width \* 0.33;
const progress = useLoop({duration: 2000});
const circleTranslate = useDerivedValue(
() => mix(progress.value, c.y + ANIMATION_OFFSET, c.y - ANIMATION_OFFSET),
[progress],
);
return (

<group>
</group>

# React Native Skia Integration

As you might have noticed, React Native Skia can directly accept Reanimated values as props, making it seamless to integrate canvas drawings with animations that delight your users.

One major thing to notice is that &#x3C;Canvas /> is transparent by default so it will be a nice baseline to use it for some fancy looking custom components. Here we'll add a &#x3C;View /> with the red square in the middle which will be rendered underneath the &#x3C;Canvas />.

const App = () => {
const ANIMATION_OFFSET = 50;
const {width, height} = useWindowDimensions();
const c = vec(width / 2, height / 2);
const r = width \* 0.33;
const progress = useLoop({duration: 2000});
const circleTranslate = useDerivedValue(
() => mix(progress.value, c.y + ANIMATION_OFFSET, c.y -
ANIMATION_OFFSET),
[progress],
);
return (
&#x3C;>
&#x3C;View
style={{
alignItems: 'center',
justifyContent: 'center',
...StyleSheet.absoluteFill,
}}>
&#x3C;View style={{height:      300, width:  300,
backgroundColor:    'red'}} />
&#x3C;/View>
&#x3C;Canvas style={{flex: 1}}>

# Current Page

<group>
<circle cx="{r}" cy="{c.y}" r="{r}" color="cyan">
<circle cx="{width" -="" r}="" cy="{circleTranslate}" r="{r}" color="magenta">
</circle></circle></group>

The thing to remember is that if you are using the to apply the effect that will need to affect the underlying layer these changes will only be applied to the elements. Things like <shadow> will be rendered correctly but <blur> will only have the data about the elements that are used inside canvas. You will need to somehow capture the snapshot of the layer.
</blur></shadow>

For that the makeImageFromView function exists. You can call it with the ref to the <view> you want the snapshot of and it will return you a Promise with the image data that you can use as a canvas layer for transformation.
</view>

So if we add a blurred card to our component you will see the blur only around the circles and the red square we've added in the last example will look as sharp as always. To fix that we'll take a snapshot of the underlying view and refer it as an image on the .

const pd = PixelRatio.get();

const App = () => {
const {width, height} = useWindowDimensions();
const c = vec(width / 2, height / 2);
const r = width _ 0.33;
const CARD_WIDTH = width - 60;
const CARD_HEIGHT = CARD_WIDTH _ 0.5;
const ANIMATION_OFFSET = 50;
const clip = useMemo(
() => rrect(rect(0, 0, CARD_WIDTH, CARD_HEIGHT), 20, 20),
[CARD_HEIGHT, CARD_WIDTH],
);
const ref = useRef<view>(null);
};
</view>

const progress = useLoop({ duration: 2000 });
const x = useSharedValue((width - CARD_WIDTH) / 2);
const y = useSharedValue((height - CARD_HEIGHT) / 2);
const transform = useDerivedValue(() => [
{ translateY: y.value },
{ translateX: x.value },
]);
const circleTranslate = useDerivedValue(
() => mix(progress.value, c.y + ANIMATION_OFFSET, c.y - ANIMATION_OFFSET),
[progress],
);
const [image, setImage] = useState<SkImage | null>(null);

useEffect(() => {
makeImageFromView(ref).then(snapshot => setImage(snapshot));
}, []);

return (
<>
<View
ref={ref}
collapsable={false}
style={{
alignItems: 'center',
justifyContent: 'center',
...StyleSheet.absoluteFill,
}}>
<View style={{ height: 300, width: 300, backgroundColor: 'red' }} />
</View>

<Image
image={image}
x={0}
y={0}
height={(image?.height() ?? 0) / pd}
width={(image?.width() ?? 0) / pd}
/>
<Group>
<Circle cx={r} cy={c.y} r={r} color='cyan' />
<Circle cx={width - r} cy={circleTranslate} r={r} color='magenta' />
</Group>

</>
);

This approach can help you to create nicely looking cross-platform overlays on top of your main application content but need to be planned in advance since you need to have a ref to the underlying view.

Another thing react-native-skia is great at is path interpolation. The calculations are performed on the native side with C++ so it's blazingly fast, does not lock the JS thread, and hence will keep the UI responsive to user actions.

# In this simple example we'll use the d3 library to generate two curved paths from the data that we'll then render on the canvas and animate the switch between them.

import React, {useEffect} from 'react';
import {useSharedValue, withRepeat, withTiming} from 'react-native-reanimated';
import {
Skia,
usePathInterpolation,
Canvas,
Path,
} from '@shopify/react-native-skia';
import {curveBasis, line, scaleLinear, scaleTime} from 'd3';
const GRAPH_HEIGHT = 500;
const GRAPH_WIDTH = 350;
export const data1 = [
{date: '2023-12-01T00:00:00.000Z', value: 110},
…
{date: '2023-12-15T00:00:00.000Z', value: 700},
];
export const data2 = [
{date: '2023-12-01T00:00:00.000Z', value: 700},
…
{date: '2023-12-15T00:00:00.000Z', value: 400},
];
const makeGraph = data => {
const max = Math.max(...data.map(val => val.value));
const y = scaleLinear().domain([0, max]).range([GRAPH_HEIGHT, 35]);
const x = scaleTime()
.domain([new Date(2023, 12, 1), new Date(2023, 12, 15)])
.range([10, GRAPH_WIDTH - 10]);
const curvedPath = line()
.x(d => x(new Date(d.date)))
.y(d => y(d.value))
.curve(curveBasis)(data);
return Skia.Path.MakeFromSVGString(curvedPath!);
};
const App = () => {
const progress = useSharedValue(0);
const graphData = [makeGraph(data1), makeGraph(data2)];
useEffect(() => {
progress.value = withRepeat(withTiming(1, {duration:

1000}), -1, true);

}, [progress]);

const path = usePathInterpolation(

progress,

[0, 1],

[graphData[0], graphData[1]],

);

return (

&#x3C;Canvas style={{flex: 1}}>

&#x3C;Path

path={path}

style='stroke'

strokeWidth={5}

strokeCap='round'

strokeJoin='round'

/>

&#x3C;/Canvas>

);

Myn

The usePathInterpolation hook will take care of the correct

interpolation of the path value when switching the graphs. For

the animation to look smooth, the path needs to be interpolatable

and contain the same number and types of commands or the interpolation may potentially look incorrect or can cause the crash of your app.

# BENEFITS: ACCESS TO THE POWERFUL TOOL THAT WILL HELP YOU CREATE UNIQUE AND PERFORMANT UI

Close to native performance, high customizability and great API will help you a lot if your goal is to create something creative and fast. Add to that good integration with the current generation of tools like react-native-gesture-handler and react-native-reanimated and you'll get yourself a fantastic instrument to have when a new UI design trend pops up.

We only covered a fraction of things react-native-skia can do. Things like image processing filters, masking, rich text render and all powerful shaders are out of our scope of this guide.

The best places to learn more about React Native Skia and possible applications will be the official documentation, William Candillon's YouTube channel, and Daniel Friyia's YouTube channel.

”In 2023, we made a strategic decision to rely completely on Reanimated for animations. This move has brought several benefits. Firstly, it's the React Native animation system that people are already proficient with, which streamlines the learning curve. It enables us to animate native views and Skia drawings simultaneously and integrates seamlessly with react-native-gesture-handler. Now, we're taking our integration with Reanimated further by providing new APIs. These APIs allow for the creation of textures directly on the UI thread and enable the animation of large scenes based on these textures.”

William Candillon

# PART 1

# CHAPTER 9

# OPTIMIZE YOUR APP’S JAVASCRIPT BUNDLE

# ISSUE: METRO, THE DEFAULT JS BUNDLER FOR REACT NATIVE, PRODUCES A BUNDLE THAT’S TOO LARGE.

React Native application’s logic is mostly located in the JavaScript code which runs in the JavaScript engine (JavaScriptCore or Hermes). But before loading JavaScript code into the app, it should be bundled, usually into a single JS file or sometimes to multiple files. React Native provides a built-in tool for JavaScript code bundling called Metro.

# SOLUTION: USE EXTERNAL PLUGINS OR SWAP IT WITH THIRD-PARTY BUNDLERS.

Like any bundler, Metro takes in an entry file and various options and gives you back a single JavaScript file that includes all your code and its dependencies, also known as a JavaScript bundle. According to official docs, Metro speeds up builds using a local cache of transformed modules out of the box. Metro trades configurability for performance, whereas other bundlers like Webpack are the other way around. So when your project needs custom loaders or the extensive Webpack configurability for bundling JavaScript code and splitting app logic, there are a few alternative bundlers that could be used in React Native apps and provide more configuration features. Each of them have some benefits and limitations.

# Re.Pack

Re.Pack is a Webpack-based toolkit to build your React Native application with full support of the Webpack ecosystem of loaders, plugins, and support for various features like symlinks, aliases, code splitting, etc. Re.Pack is the successor to Haul, which served a similar purpose but balanced a different set of tradeoffs and developer experience.

The ecosystem part of Webpack is crucial for many developers, since it’s the most popular bundler of the web, making the community behind loaders and plugins its key advantage. Thanks to that pluggability, it provides ways to improve the build process and Webpack’s overall performance. At least for the parts that are not connected to the internal module graph building and processing. Such parts would be, e.g. JavaScript and TypeScript transpilation or code minification. You can replace Babel transpiler and Terser minifier with faster alternatives like ESBuild thanks to the esbuild-loader or swc with swc-loader.

Another Webpack feature that helps our apps achieve better performance is reducing the amount of code in the final bundle with tree shaking. Tree shaking is a dead code elimination technique done by analyzing the import and export statements in the source code and determining which code is actually used by the application. Webpack will then remove any unused code from the final bundle, resulting in a smaller and more efficient application. The code that’s eligible for tree shaking needs to be written in ECMAScript modules (import and export statements) and mark itself as side-effect free through package.json sideEffects: false clause.

Webpack has support for symlinks but since React Native 0.72, Metro offers that as well in an experimental form. And since v0.73 it’s turned on by default. Symlinks prove useful inside of monorepos, where node modules can be optimally shared between different workspaces.

Re.Pack also offers the ability to use asynchronous chunks to split your bundle into multiple files and load them on-demand, which can improve initial loading times if you’re using the JavaScriptCore engine. However, it won’t provide that much value when used with Hermes, which leverages the memory mapping technique for dynamic reading only the necessary parts of the bundle’s bytecode directly from the RAM. It might make a slight difference when your app’s bundle is really big, and you are targeting low-end Android devices. But there’s a twist to that! Webpack doesn’t really care whether you load the dynamic chunk from the filesystem or remote. Hence it allows for dynamic loading code that’s never been there in the app bundle in the first place – either directly from

a remote server or a CDN. Now this can help you with reducing not only the initial load time, but also the precious app size. It also opens up a way to Over-The-Air (OTA) updates that target only a small part of your app.

On top of that, Webpack 5 introduced support for the concept of Module Federation. It’s a functionality that allows for code-splitting and sharing the split code parts (or chunks) between independent applications. It also helps distributed and independent teams to ship large applications faster. Giving them the freedom to choose any UI framework they like and deploy independently, while still sharing the same build infrastructure. Re.Pack 3 supports this functionality out-of-the-box and provides you with a lot of utilities that prove useful in such scenarios e.g. CodeSigningPlugin can help you with integrity verification of remotely loaded bundles.

All these configurations and flexibility affect the build process. The build speed is a little bit longer than the default Metro bundler due to customization options. When switching from Metro, it might require you to solve some resolution errors, as the algorithms differ between the two bundlers. Also, the Fast Refresh functionality is limited compared to the Metro bundler. The Hot Module Replacement (HMR) and React Refresh features might sometimes require the full application reload with Webpack and Re.Pack. When working with Module Federation, the HMR functionality is also limited to refreshing parts of the app originating from the host. For the remote modules a full reload is required.

If you don’t need the huge customization that the Webpack ecosystem offers or don’t plan to split your app code, then you may as well keep the default Metro bundler.

# react-native-esbuild

One of the main benefits of react-native-esbuild is fast builds. It uses the ESBuild bundler under the hood which has huge improvements in bundling performance even without caching. It also provides some features like tree shaking and is much more configurable compared to the Metro bundler. ESBuild has its own ecosystem with plugins, custom transformers, and env variables. This loader is enabled by default for .ts , .tsx , .mts , and

.cts files, which means ESBuild has built-in support for parsing TypeScript syntax and discarding the type annotations. However, ESBuild does not do any type checking so you will still need to run type check in parallel with ESBuild to check types. This is not something ESBuild does itself.

Unfortunately, react-native-esbuild has some tradeoffs, so it is very important to select the right bundler by paying attention to them as well.

It doesn’t support Hermes, which is now the default engine for React Native. And it does not have Fast Refresh or Hot Module Replacement, but this library supports live reload instead.

# rnx-kit

An interesting extension to Metro is Microsoft’s rnx-kit. It is a package with a huge variety of React Native development tools. Historically, it enabled the use of symlinks with Metro, before it was officially supported. Another benefit compared to Metro is the tree shaking functionality out-of-the-box, through the use of ESBuild for bundling.

Metro supports TypeScript source files, but it only transpiles them to JavaScript. Metro does not do any type-checking. rnx-kit solves this problem. Through the configuration, you can enable type-checking. Warnings and errors from TypeScript appear in the console.

Also, rnx-kit provides duplicate dependencies and cyclic dependencies detection out-of-the-box. This could be very useful to reduce the size of the bundle which leads to better performance and prevents cyclic dependencies issues. Note that you will have to solve these issues yourself, but thankfully rnx-kit documentation provides some insights on how to deal with them.

# BENEFITS: SHIP LESS JAVASCRIPT TO YOUR USERS.

# SAVE DEVELOPERS’ TIME WHEN BUNDLING.

The choice of a bundle tool depends on the specific case. It is impossible to select only one bundler for all the apps.

# Tree-Shaking in React Native

As you can see, tree-shaking in React Native can be achieved through use of Webpack (via Re.Pack) or ESBuild (via rnx-kit or react-native-esbuild). Tree-shaking implementation differs between bundlers, so it might be feasible to check the results of both and determine what’s best for your app. Note that tree-shaking through rnx-kit is still in beta, but the results are optimistic so far. It’s reasonable to expect the bundle size difference between 0% and 20%, and in rare cases, even more than that.

Should you feel a need for customization options provided by the Webpack ecosystem or plan to split your app code, then we would suggest using Re.Pack for its widely customizable configuration, a huge amount of loaders, plugins maintained by the community. If the Webpack ecosystem feels like an overhead, then it is better to stay with the default Metro bundler or try to use other bundler options like react-native-esbuild and rnx-kit which also provides some benefits like decreased build time, using esbuild under the hood, symlinks, and typescript support out-of-the-box. But be careful and always pay attention to the tradeoffs that come with a new bundling system.

# IF YOU NEED HELP WITH PERFORMANCE, STABILITY, USER EXPERIENCE, OR OTHER COMPLEX ISSUES – CONTACT US!

As React Native Core Contributors and leaders of the community, we will be happy to help.

# PART 2

# IMPROVE PERFORMANCE BY USING THE LATEST REACT NATIVE FEATURES.

React Native is growing fast and so is the number of features.

Last year, developers contributed more than 3670 commits to the React Native core. The number may seem impressive, but, in fact, it's even larger, since it doesn't include the smaller contributions made under the React Native Community organization (9678 commits).

All that proves that React Native is developing at a really healthy pace. Contributions made by both the community and Meta enable more and more advanced use cases of the framework. A great example of that is Hermes – an entirely new JavaScript engine built and designed specifically for React Native and Android. Hermes aims to replace the JavaScriptCore, previously used on both Android and iOS. It also brings a lot of enterprise-grade optimizations by improving your Android application's performance, start-up time, and overall size reduction.

In this section, we will show you some of the features you can turn on right now to start your optimization process. We also encourage you to keep track of all the new React Native features to make sure you use the framework to its full potential.

# PART 2

# | CHAPTER 1

ALWAYS RUN THE LATEST REACT NATIVE VERSION TO ACCESS THE NEW FEATURES

# UPGRADE YOUR APP TO THE LATEST VERSION TO GET MORE FEATURES AND BETTER SUPPORT.

ISSUE: YOU ARE RUNNING AN OLD AND UNSUPPORTED VERSION OF REACT NATIVE AND DEPRIVING YOURSELF OF NEW IMPROVEMENTS AND FEATURES

Keeping your application up to speed with the frameworks you use is crucial. That is why you should subscribe to the latest features, performance improvements, and security fixes.

The JavaScript ecosystem is particularly interesting in this aspect, as it moves really quickly. If you don't update your app regularly, chances are your code will end up being so far behind that upgrading it will become painful and risky.

Every day, developers from all around the world introduce new features, critical bug fixes, and security patches. On average, each release includes around 500 commits.

Over the years, React Native has grown significantly, thanks to open-source contributors and Meta's dedication to improving the ecosystem. Here are some highlighted crucial features that have been introduced to React Native over the course of its releases.

# FAST REFRESH

To improve the developer experience and velocity, the React team introduced a feature called Fast Refresh to React Native. This lets you quickly reflect the code on the device, whenever you save the file instead of building or reloading the app. It is smart enough

# to decide when to do a reload after we fix an error or just render otherwise.

A tip here: the local state of functional components and hooks is preserved by default. We can override this by adding a comment to that file: // @refresh reset. Whereas, class components are remounted without preserving the state.

# AUTO-LINKING

Whenever we add native code to our React Native app as a dependency, it needs to be linked. Previously linking was done manually or using react-native link dep-name. React Native CLI introduced auto-linking so the devs didn't need to link a library themselves. After a couple of years, when the re-architecture of React Native was released to the community, a need arose to auto link fabric components and turbo modules, which was handled gracefully by the CLI team. They released an update to the community to help the developer experience and velocity.

# FLIPPER

Important note: Debugging React Native apps with Flipper is deprecated in React Native 0.73. The out-of-the box support will eventually be removed for JS debugging via Flipper in 0.74.

It is one of the ways of debugging React Native apps. It is loaded with awesome tools such as ReactDevtools, Network Inspector, Native Layout Inspector, and plugins for e.g. to measure the performance of the React Native apps. We can also view the Metro and Device logs right in Flipper.

# NEW DEBUGGING EXPERIENCE

In v0.73, React Native introduced a new debugger natively supported by Hermes and supporting Chrome Debugging Protocol (CDP). The dev menu is now updated with one-click action to the complete new first party debugger which replaces Flipper. This workflow is zero install and works if you have Google Chrome.

# DevTools (React Native)

# Welcome to debugging in React Native

Microsoft Edge or any Chromium-based browser installed on your system. The new debugger can be also triggered from React Native CLI by using the “J” hotkey. The frontend of the new debugging system in RN is based on Chrome Dev Tools and features a customized UI with panels and menus that match debugging features that React Native supports today, nothing more than that, so what you see works. Since the debugger is based on Chrome Dev tools it has future capability to support rich and comprehensive debugging features offered by the web ecosystem.

# Technology Preview

React Native JS Inspector

Debugging.doca What's new

Note: Please be aware that at the time of writing, the feature is still in the experimental phase. The React Native team is ironing out the bugs and making sure that, when the debugger launches fully, it will work more completely than the current debugging methods.

You can opt-in to the new debugger using the start's command --experimental-debugger flag:

npx react-native start --experimental-debugger

# Welcome to Metro v0.80.2

# Fast - Scalable - Integrated

info Dev server ready

- L - run on iOS
- a - run on Android
- open Dev Menu
- open debugger (experimental, Hermes only)
- r - reload app

Now it's just a case of hitting the j key and this will launch the new debugger using Google Chrome or Microsoft Edge.

# EXPO DEV TOOLS PLUGINS

For apps using Expo tools, you can already use and write plugins that leverage the Chrome Debugging Protocol introduced in React Native 0.73. Expo's Dev tool plugins are an extensible way of debugging your Expo and React Native apps. These plugins are available as small dependencies that can be installed in your app. They allow developers to inspect various aspects of their app, trigger test behaviors, and much more, all in real time.

Dev tools plugins are snippets that create a bridge between your app and Chrome window. These bridges open up a world of possibilities for app inspection and debugging, making the process both simpler and more efficient.

# Available plugins

While this is a relatively new feature, Expo already has some built-in dev tool plugins that are already available to use:

- React Navigation Plugin: Ideal for apps utilizing React Navigation or Expo Router, allows rewinding navigation history and even sending deep links.
- Apollo Client Plugin: Useful for apps using Apollo Client, providing insights into query and mutation history, and cache management.

# Integrating a plugin

Integrating a plugin into your Expo or React Native app is straightforward. For example, let's assume you use a navigation library in your app, such as Expo Router or React Navigation. You can use @dev-plugins/react-navigation to see the history of React Navigation actions and state. It also allows rewinding to a previous point in the navigation history and even test sending deep links to your app.

To use this plugin, install the package:

npx expo install @dev-plugins/react-navigation
After installation, add the necessary code snippet to your app's root component. This setup ensures seamless two-way communication between your app and the plugin, enriching your development and debugging process.

In this example, we'll pass the navigation root to the plugin in our app's entry point when running in development mode when using React Navigation:

import { NavigationContainer, useNavigationContainerRef } from '@react-navigation/native';
import { useReactNavigationDevTools } from '@dev-plugins/react-navigation';

export default function App() {
const navigationRef = useNavigationContainerRef();

# Plugins

- React Query Plugin: Useful for apps using TanStack Query to explore data and queries, check cache status, and manage queries.
- TinyBase Plugin: Connects the TinyBase Store Inspector to your app, allowing for real-time store content viewing and updating.

More dev tools plugins are expected to be added over time. To see a complete list, see this GitHub repository.

useReactNavigationDevTools(navigationRef);

return (
<navigationcontainer ref="{navigationRef}">{/_ ... _/}
);
}

You can also use the same plugin when you navigate with Expo
Router since it also uses React Navigation under the hood. However,
the setup is slightly different:

import { useRef } from 'react';
import { useNavigationContainerRef, Slot } from 'expo-router';
import { useReactNavigationDevTools } from '@dev-plugins/
react-navigation';

export default Layout() {
const navigationRef = useNavigationContainerRef();
useReactNavigationDevTools(navigationRef);

return ;
}

Once these code changes are applied, open your terminal, run
npx expo start, press shift + m to open the list of dev tools, and
then select the React Navigation plugin. This will open the plugin's
web interface, showing your navigation history as you navigate
through your app.
</navigationcontainer>

# React Native Updates

00D @dev-plugins/hreact-navigatx + 0OO iPhone 15 P1o n @ b

- o Not Secure 192.168.0.106:8081/\_expo/plugins/@dev-plugins/react-navigation \* D 0810

Logs Linking 19:40

# NAVIGATE

Reset to this Action Tab One

"root" : ( 3 items

NAVIGATE Reset to his "type" : string "NAVIGATe"

"payload" : { 2 items

NAVIGATE Hosst to t "name" : string "index

"merge" : boot true

}

"target": string "tab- Tab One

52rvuIDhaHeMQA1dsdYtY

}

State Open up the code for this screen:

"root" : { 6 items "state" ; soul false "type : striny"stack

@dev-pluginsgreact-navigat× + Not Secure 192.168.0.106:8081/\_expo/plugins/@dev-plugins/react-navigation \* D - Tap here if your app doesn't automatically update after making changes

Logs Linking

Type a path to display porund scremns, x.a, /users/evergll Action

"root" : { 2 itens

Custom configuration (Advanced)

(tabs) index

"type" : string "NAVIGATE"

"payload" : { 2 itoms

"name": striny"(tabs)"

params" : { 3 itens

initial" : oul true

screen": trang"ind

If you haven't found a plugin to fit your use case yet, you can also build your own.

# LOGBOX

React Native redesigned its error and warning handling system. They had to do a ground-up redesign of its logging system and the developer experience is much better because of it. Developers can easily trace the cause of an error using code frames and component stacks. Syntax error formatting helps to understand the issue more quickly with the aid of syntax highlighting. Log Notifications show warnings and logs at the bottom of the screen instead of covering the whole screen.

# HERMES

A new JS engine created by Meta to improve the performance of React Native apps in terms of CPU usage, memory consumption, app size, and Time To Interactive (TTI). Initial support was launched for Android devices, but after two years, support was extended to iOS as well. After a couple of months, the previously used garbage collector for Hermes GenGC was replaced with a new one called Hades – a concurrent garbage collector. The Meta team saw improvements of CPU-intensive workloads by 20-50%. Later on, the team decided to ship a bundled Hermes.

instead of downloading it from NPM. This was done to avoid con-

fusion between what version of Hermes is compatible with React

Native. Also, both Hermes and React Native use the same JSI

code which makes it hard to maintain. Now whenever a version

of React Native is released, a version of Hermes can be released

as well, making sure that both are fully compatible.

# NEW ARCHITECTURE

This one has its own chapter.

In the React Native ecosystem, it's common that libraries are not

backward – compatible. New features often use goodies not avail-

able in the previous versions of the framework. This means that if

your application runs on an older version of React Native, you are

eventually going to start missing out on the latest improvements.

That's why keeping up with the newest React Native upgrades is

the only way to go.

Unfortunately, there is some serious work associated with upgrading your React Native code with every new release. Its amount will depend on the number of underlying changes to the native functionalities and core pieces. Most of the time, you have to carefully analyze and compare your project against the latest version and make the adjustments on your own. This task is easier if you're already comfortable with moving around the native environment. But if you're like most of us, it might be a bit more challenging.

For instance, it may turn out that the modules and components you used in your code are no longer part of the react-native core.

It would be because of the changes introduced by Meta during a process called the LEAN CORE link. The goals of the effort were to:

- Make the react-native package smaller, more flexible, and easier to maintain by extracting some parts of the core and moving them to the react-native-community repository,
- Transfer the maintenance of the extracted modules to the community.

The process accelerated the growth of particular modules and made the whole ecosystem better organized. But it also had some negative effects on the react-native upgrading experience. Now, you have to install the extracted packages as an additional dependency, and until you do, your app will not compile or crash at runtime.

However, from a developer's perspective, the migration to community packages is usually nothing more than introducing a new dependency and rewriting imports.

Another important issue is the support of third-parties. Your code usually relies on external libraries and there's a risk that they might also be incompatible with the latest React Native version.

There are at least two ways to solve this problem:

- Wait for the project maintainers to perform the necessary adjustments before you upgrade.

• Look for alternatives or patch the modules yourself – by using a handy utility called patch-package or creating a temporary fork with the necessary fixes.

# RUNNING ON AN OLD VERSION MEANS SHIPPING WITH ISSUES THAT MAY DISCOURAGE YOUR USERS

If you are running on an older version, it is likely that you are lagging behind your competition that uses the latest versions of the framework.

The number of fixes, improvements, and advancements in the React Native framework is really impressive. If you're playing a game of catch up, you are opting out of a lot of updates that would make your life a lot easier. The workload and the cost involved in making regular upgrades are always offset by the immediate DX enhancements.

In this section, we present some of the well-established practices to make upgrading React Native to the newer version easier.

# SOLUTION: UPGRADE TO THE LATEST VERSION OF REACT NATIVE (WE'LL SHOW YOU HOW).

Upgrading React Native might not be the easiest thing in the world. But there are tools that can simplify the process and take most of the problems away.

The actual amount of work will depend on the number of changes and your base version. However, the steps presented in this section can be applied to every upgrade, regardless of the state of your application.

# PREPARING FOR THE UPGRADE

React Native Upgrade Helper is a good place to start. On a high level, it gives you an overview of the changes that have happened to React Native since the last time you upgraded your local version.

React Native Upgrade Helper\*star 2.7

# What's your current react-native version?

# To which version would you like to upgrade?

| 0.69.0                  | V 0.70.0 |
| ----------------------- | -------- |
| Show me how to upgrade! |          |

# Useful content for upgrading

| Binaries              | Split                                        | Unified   |
| --------------------- | -------------------------------------------- | --------- |
| package.json MODIFIED |                                              | View file |
| #e -10.8 +10,8 #e     |                                              |           |
| 10                    | Lint; "eslint."                              | 10        |
| 11                    | )                                            | 11        |
| 12                    | "dependencies": (                            | 12        |
| 13                    | "react": "18.6.0",                           | 13        |
| 34                    | react-native": "0.69.0"                      | 13        |
| 13                    | )                                            |           |
| 16                    | "devDependencies": (                         | 16        |
| 17                    | "@babel/core": "\~7.12.9"                    | 17        |
| 20                    | "babel-jest": "\*26.6.3",                    | 20        |
| 21                    | "eslint": "\*7.32.8",                        | 21        |
| 22                    | "jest": "\*26.6.3".                          | 22        |
| 23                    | "metro-react-native-babel-preset": "0.70.3". | 23        |
| 24                    | "react-test-renderer": "18.0.0"              | 24        |
| 25                    | )                                            | 25        |
| 26                    | jest:                                        | 26        |
| 27                    | "preset": "react-native"                     | 27        |

To do so, the helper compares bare React Native projects created by running npx react-native init with your version and the one you're upgrading to. Next, it shows the differences between the projects, making you aware of every little modification that took place in the meantime. Some changes may be additionally annotated with special information that will give more context on why something has happened.

# Additional explanation of the more interesting changes to user files

Having a better overview of the changes will help you move faster and act with more confidence.

Note: Having more context is really important as there is no automation in place when it comes to upgrading – you will have to apply the changes yourself.

# v ios/Podfile

ADDED ! View file

@@ -0,0 +1,47 @@
1 platform :ios, '9.0'
2 require_relative '../node_modules/@react-native-community/cli-platform-ios/native_modules'
3
4 target 'RnDiffApp' do
5 # Pods for RnDiffApp
6 pod 'React', :path => '../node_modules/react-native/'

All these libraries below have been removed from the Xcode project file and now live in the Podfile. Cocoapods handles the linking now. Here you can add more libraries with native modules.

React Native Upgrade Helper also suggests useful content to read while upgrading. In most cases that includes a dedicated blog post published on the React Native blog as well as the raw changelog.

# Useful content for upgrading

You can use the following command to kick off the upgrade: npx @rnx-kit/align-deps - requirements react-native@[major.minor]

align-deps is an OSS tool from Microsoft that automates dependency management. It knows which packages\* versions are compatible with your specific version of RN, and it uses that knowledge to align dependencies, keeping your app healthy and up-to-date\*\*. Find out more here.

- - Not all packages are supported out-of-the-box.
- \*\* You still need to do the other changes below and verify the changelogs of the libraries that got upgraded.

Check out Upgrade Support if you are experiencing issues related to React Native during the upgrading process.

Keep in mind that RnDiffApp and rndiffapp are placeholders. When upgrading, you should replace them with your actual project's name. You can also provide your app name by clicking the settings icon on the top right.

# Useful content to read while upgrading React Native to a newer version

We advise you to read the recommended resources to get a better grip on the upcoming release and learn about its highlights.

Thanks to that, you will not only be aware of the changes, but you will also understand the reasoning behind them. And you will be ready to open up your project and start working on it.

# APPLYING THE JAVASCRIPT CHANGES

The process of upgrading the JavaScript part of React Native is similar to upgrading other JavaScript frameworks. Our recommendation here is to perform upgrades step-by-step – bumping one library at a time. As a rule of thumb, once you have upgraded a library, save your work at that point in a commit and then move on to the next library. In our opinion, this approach is better than upgrading everything at once as it gives you more control and makes catching regressions much easier.

# UPGRADING REACT NATIVE

The first step is to bump the React and React Native dependencies to the desired versions and perform the necessary changes (including breaking changes). To do so, you can look up the suggestions provided by React Native Upgrade Helper and apply them manually. Once it's completed, make sure to reinstall your node_modules.

Note: When performing the upgrade, you may see a lot of changes coming from iOS project files (everything inside .xcodeproj, including .pbxproj). These are files generated by Xcode as you work with your iOS part of React Native application. Instead of modifying the source file, it is better to perform the changes via the Xcode UI. This was the case with upgrading to React Native 0.60 and the appropriate operations were described in this issue.

Finally, you should try running the application. If everything is working – perfect. The upgrade was smooth and you can call it a day! On a more serious note though – now you should check if there are newer versions of other dependencies you use! They may be shipping important performance improvements.

Unfortunately, there's also another more pessimistic scenario. Your app may not build at all or may instantly crash with a red screen. In that case, it is very likely that some of your third-party dependencies are not working properly, as in some cases the dependencies include native code which supports new OS features, so you need to make them compatible with your React Native version.

Note: If you have a problem with your upgrades, you can check the Upgrade Support project. It is a repository where developers share their experience and help each other solve some of the most challenging operations related to upgrading.

# UPGRADING THIRD-PARTY LIBRARIES

In most cases, it's your React Native dependencies that you should look at first. Unlike regular JavaScript/React packages, they often depend on native build systems and more advanced React Native.

APIs. This exposes them to potential errors as the framework matures into a more stable API.

If the error occurs during the build time, bumping the dependency to its latest version usually makes it work. But it may not always be the case. To make sure the version of React Native you're upgrading to is compatible with your dependencies, use the align-deps project by Microsoft developers. It allows you to keep your dependencies on the right version based on the requirements and by leveraging the presets of rules. It also has a CLI, so you can wire it up to your CI and ensure that no one in your repo or monorepo will inadvertently introduce incompatible versions of packages and break the app.

Once your application builds, you are ready to check the changelog and make yourself familiar with the JavaScript changes that happened to the public API. If you overlook this step, it can result in runtime exceptions. Using Flow or TypeScript should help you ensure that the changes were applied properly.

As you can see, there is no magic trick that would fix all the errors and upgrade the dependencies automatically. This is mostly manual work that has to be done with patience and attention. It also requires a lot of testing to ensure that you didn't break any features along the way. Fortunately, there are tools like align-deps that help you avoid at least some of the manual work, improving the upgrading experience significantly.

# BENEFITS: YOU'RE RUNNING THE LATEST VERSIONS WHICH TRANSLATES TO MORE FEATURES AND BETTER SUPPORT.

Upgrading to the latest React Native version shouldn't be different from keeping your other frameworks and libraries up to date. Apart from critical performance and security improvements, new React Native releases also address the latest underlying changes to iOS and Android. That includes the breaking changes that apply to mobile phones, such as when certain APIs get deprecated.

Here is an example: In 2019, Google announced that all Android applications submitted to Google Play after August 1, 2019 had to

be 64-bit. In order to continue developing their applications and shipping new features, developers had to upgrade to React Native 0.59 and perform the necessary adjustments.

Similar situation happened in 2023, when Google announced a new target API level requirement, which required developers to either manually update their targetSdkVersion to 33 or upgrade their React Native apps to v0.71 or higher.

Upgrades like this are really critical to keeping your users satisfied. After all, they would be disappointed if the app started to crash with the newer version of the operating system or disappeared from the App Store. There might be some additional workload associated with every release, but staying up to date will pay back with happier users, more stable apps, and a better development experience.

# PART 2 | CHAPTER 2

# HOW TO DEBUG FASTER AND BETTER WITH FLIPPER

AE4

# ESTABLISH A BETTER FEEDBACK LOOP BY IMPLEMENTING FLIPPER AND HAVE MORE FUN WHILE WORKING ON YOUR APPS.

# ISSUE: YOU’RE USING CHROME REMOTE DEBUGGER OR SOME OTHER HACKY WAY TO DEBUG AND PROFILE YOUR REACT NATIVE APPLICATION.

Debugging is one of the more challenging parts of every developer’s daily work and finding out what is wrong can be very frustrating. We usually try to fix bugs as soon as possible, especially when they are critical and make an app unfunctional. Time is an important factor in that process and we usually have to be agile to quickly solve the issues. However, debugging React Native is not very straightforward, as the issue you are trying to solve may occur on different levels. Namely, it may be caused by:

- JavaScript – your application’s code or React Native,
- Native code – third-party libraries or React Native itself.

When it comes to debugging native code, you have to use the tools built into Android Studio and Xcode.

When it comes to debugging JavaScript code, you may encounter several difficulties. The first and most naive way to debug is to write console.logs in your code and check the logs in the terminal. This method works for solving trivial bugs only or when following the divide and conquer technique. In all other cases, you may need to use an external debugger.

By default, React Native ships with some built-in debugging utilities.

# iPhone 14 Pro

# iOS 16.2

1:47

RAM JSC Views UI JS Hermes for RN 0.70.6

| 94.40 | 0.00 | 57  | 60  | 60  |
| ----- | ---- | --- | --- | --- |
| MB    | MB   | 100 |     |     |

# Welcome to React Native

# Step One

Edit App.tsx to change this screen and then come back to see your edits.

See Your Changes

Press Cmd + R in the simulator to reload your app's code.

# Debug

Press Cmd + D in the simulator or Shake your device to open the React Native debug menu.

# Learn More

Read the docs to discover what to do next:

The Racire Explains a Hello World for

The most common one is Google Chrome Remote Debugger. It allows you to set breakpoints in your code or preview logs in a handier way than in a terminal. Unfortunately, using the Remote Debugger may lead to hard-to-spot issues. It’s because your code is executed in Chrome’s V8 engine instead of a platform-specific engine, such as JSC or Hermes.

The instructions generated in Chrome are sent via Websocket to the emulator or device. It means that you cannot really use the debugger to profile your app so it detects the performance issues. It can give you a rough idea of what might cause the issues, but you will not be able to debug the real cause due to the overhead of WebSocket message passing.

Another inconvenience is the fact that you cannot easily debug network requests with the Chrome Debugger (it needs additional setup and still has its limitations). In order to debug all possible requests, you have to open a dedicated network debugger using the emulator’s developer menu. However, its interface is very small and inconvenient due to the size of the emulator’s screen.

From the developer menu, you can access other debugging utilities, such as layout inspector or performance monitor. The latter is relatively convenient to use, as it’s displaying only a small piece of information. However, employing the former is a struggle because of the limited workspace it provides.

# SPENDING MORE TIME ON DEBUGGING AND FINDING PERFORMANCE ISSUES MEANS A WORSE DEVELOPER EXPERIENCE AND LESS SATISFACTION

Unlike native developers, the ones working with React Native have access to a wide range of debugging tools and techniques. Each originates from a different ecosystem, such as iOS, Android, or JS. While it may sound great at first, you need to remember that every tool requires a different level of expertise in the native development. That makes the choice challenging for the vast majority of JavaScript developers.

Inconvenient tooling usually decreases the velocity of the team and frustrates its members. As a result, they are not as effective as they could be, affecting the quality of the app and making the releases less frequent.

# SOLUTION: TURN ON FLIPPER AND START DEBUGGING.

Wouldn’t it be great to have one comprehensive tool to handle all of the above use cases? Of course, it would! And that’s where Flipper comes into play!

Flipper is a debugging platform for mobile apps. It also supports React Native as its first-class citizen. Launched in September

# Flipper (0.176.0)

2019, Flipper has been shipped by default with React Native since version 0.62.

# APP INSPECT

MyForkedApp

React Native

# PLUGINS

- Device
- Crash Reporter
- Headless-demo
- Logs
- React DevTools

No profiling data has been recorded.

Click the record button to start recording.

Click here to learn more about profiling.

# Source

https://fbflipper.com/docs/features/react-native

It is a desktop app with a convenient interface, which directly integrates with your application’s JS and native code. This means that you no longer have to worry about JS runtime differences and the performance caveats of using the Chrome Remote Debugger. It comes with a network inspector, React DevTools, and even a native view hierarchy tool.

What’s more, Flipper lets you preview logs from native code and track native crashes, so you don’t have to run Android Studio or Xcode to check what is happening on the native side!

Flipper is easily extensible, so there is a high chance it will be enriched with a wide range of useful plugins developed by the community. At this point, you can use Flipper for tasks such as detecting memory leaks, previewing the content of Shared Preferences, or inspecting loaded images. Additionally, Flipper for React Native is shipped with React DevTools, Hermes debugger, and Metro bundler integration.

What’s most exciting is that all the needed utilities are placed in one desktop app. This minimizes context switches. Without Flipper, a developer debugging an issue related to displaying the data fetched from the backend had to use the Chrome Debugger (to preview logs), in-emulator network requests debugger, and probably in-emulator layout inspector, or a standalone React Devtools app. With Flipper, all those tools are available as built-in plugins. They are easily accessible from a side panel and have similar UI and UX.

# BENEFITS: YOU HAVE MORE FUN WORKING WITH REACT NATIVE AND ESTABLISH A BETTER FEEDBACK LOOP.

A better debugging process makes your app development cycle faster and more predictable. As a result, your team is able to produce more reliable code and spot any kind of issues much easier.

Having all the debugging utilities in one interface is definitely ergonomic and does not disrupt any interactions with an emulator or device. The process will be less burdensome for your team and that will positively impact the velocity of the product development and bug fixing.

“Feel like a functionality is missing in Flipper? Good news! Flipper is easily extensible and has a comprehensive guide on how to write custom plugins in React. Why not build your own?”

— Alexandre Moureaux, App performance specialist at BAM

# PART 2

# | CHAPTER 3

# AVOID UNUSED NATIVE DEPENDENCIES

# IMPROVE THE TIME TO INTERACTIVE OF YOUR APP BY REMOVING THE LINKING OF UNUSED DEPENDENCIES.

# ISSUE: YOU HAVE A LOT OF DEPENDENCIES IN YOUR PROJECT BUT YOU DON’T KNOW IF YOU NEED ALL OF THEM

Every bit of native code we use in our apps has a runtime cost associated with reading, loading, and executing said code. The more native dependencies our apps have, the slower it is for apps to start, which impacts the TTI (Time to Interactive) metric, which in turn frustrates your users who wait longer to start enjoying your app.

In our React Native apps, we often rely on dependencies that load Kotlin, Java, Swift, Objective-C, JavaScript, and recently more often, even C++. Those dependencies are declared in the package.json file, which allows for a JavaScript bundler to correctly discover and, well, bundle their JS parts into the final application. It may be counterintuitive at first, but this declaration in the JavaScript toolchain influences the native side as well. And the reason for that is the “autolinking” feature of the React Native CLI.

Autolinking allows us to link native dependencies in our React Native apps automatically, without ever touching native tooling like Cocoapods, CMake, and Gradle, and just enjoy using the resulting functionality with JavaScript. If you’re not familiar with how the Android or iOS toolchains work in terms of using community packages, you might be asking “What in my app would be linking native dependencies?” While there are some React Native community packages that are pure JavaScript, many require compiling native code – sometimes different native code per platform – to convey that functionality to your application’s JavaScript. When dealing with native binaries, be it either in C++, Objective-C, or Swift, linking is a way for the native toolchain to understand where

to find the actual code that’s associated with the third-party de-

pendency we want our app to use. What’s important is that it’s

necessary and for a long time we, React Native developers, need-

ed to do this step manually. Since React Native 0.60, we have

an automated way of doing this thanks to the React Native CLI.

One important thing to know about how autolinking works is that it

crawls your package.json and then node_modules in search of

native code. The tool doesn’t know whether you’re actively using

the library that ships native code or not. It will be linked anyway.

How does that impact your application’s performance, you ask?

All the native dependencies discovered by auto-linking will be

linked and available in our app bundle. As a result, we’ll end up

with an increased application binary size (separate from, and in

addition to, the JS bundle size) and likely worse TTI, as the mobile

OS will spend more time loading the native binaries, showing your

users a splash screen a bit longer.

# SOLUTION: FIND AND REMOVE UNUSED DEPENDENCIES.

To find the unused dependencies in our project, we can use

the depcheck tool. It is very effective for analyzing the project’s

dependencies to see how each one of them is used, which de-

pendencies are superfluous, and which dependencies are

missing from package.json. To use depcheck, we need to

run npx depcheck in the root of our project. An example of

the results looks like this:

# Unused dependencies

- lottie-react-native
- react-native-gesture-handler
- react-native-maps
- react-natave-reanimated
- react-native-video
- react-native-webview

# Unused devDependencies

- @babel/core
- @babel/runtime
- @react-native-community/eslint-config
- @tsconfig/react-native
- @types/jest
- @types/react-test-renderer
- babel-jest
- jest-circus
- metro-react-native-paper-preset
- typescript

Example output of the depcheck library

Dev dependencies likely won’t end up in the JS bundle, but could still link native code into your production app if they have native code in their implementation. In this example, the dev Dependencies listed are JS-only, so there is no need to focus on them. The results show us that we have a few unused dependencies – and what’s more important, in this example, these dependencies are relying on some native code. Now we have to remove them and it’s done! In the example app, removing unused dependencies from the screenshot above occurred with the following reduction in the application size:

| app-release.aab Info   | app-release.aab Info |                        |         |
| ---------------------- | -------------------- | ---------------------- | ------- |
| app-release.aab        | 23.6 MB              | app-release.aab        | 19.7 MB |
| Modified: Today, 08:36 |                      | Modified: Today, 08:56 |         |

Comparision of bundle sizes before and after removing unused native dependencies

Possibly even more than reducing the application size, there was a noticeable improvement in the Time to Interactive on the tested Android device, which was reduced by 17% in this case.

You may be wondering how you can measure the TTI in your application. There are a few ways to do it. Whichever you choose, remember to always measure on a release version of the app when dealing with absolute numbers.

One way is to use a stopwatch and measure the time the app took to show the first screen, as shown here. It’s entirely manual, but it will often get the job done for one-off measurements. Another manual way is to use a recent phone that has a high-frame rate camera (eg 120fps), and record a video of your app launch on a real device. You can then load the video, zooming into the timeline to the exact time offsets between tapping your app icon and when the first meaningful render happens. We have used this data-driven method to accurately and repeatedly observe improvements as small as 50ms, which may sound small, but can often be the difference between an adequate experience for the user versus a magical one.

If we want to get a more detailed output, we can make use of Perfetto for Android. For iOS, we can enable Perf Monitor from the DevMenu and double-tap on the monitor window to expand. The output will look like this:

| Id                    | Time     |
| --------------------- | -------- |
| NativeModulePrepar    |          |
| NativeRieMainT        |          |
| NativeModuleSetup     | 1ms      |
| TurboModuleSetup      | 0ms      |
| JSCWrapperOpenLibrary | 0ms      |
| BridgeStartup         | 1074ms   |
| RootViewTTI           | 1267ms   |
| BundleSize            | 4748075b |
| ReactInstanceInit     | 0ms      |

Performance monitor on the iOS simulator

We can also use App launch from Xcode instruments, but you should note that this is not the same as the end-user experience on their device. You should always double-check your production application build on a retail device as to as possible to what your users have. All you need is to install a release build through profiling to your real device. Then select App Launch from the window that will appear automatically once the build is installed. Hit

# Example usage of Xcode’s App Launch tool

The record button, and once the app has launched, stop recording. You will get an output similar to this:

| ANY ATTRIBUTE            | targetINSTRuMENT  | I=Thread State Trace   | m             | Target                           | All Tracks           |
| ------------------------ | ----------------- | ---------------------- | ------------- | -------------------------------- | -------------------- |
| 00:00.000                |                   |                        |               | 00:00.050                        |                      |
| Time Profiler            | CPU Usage         | RR                     | UR            | Instrument                       |                      |
| Static Initializer Calls | Initializer Calls | libSy                  |               |                                  |                      |
| ReactNativeApp           | CPU Usage         | GB                     | ®@0 C(R       | ROO GKR (R()RTR)                 |                      |
| ProcessV 675             | App Lifecycle     | Initializing - Syste.. | Initializing. | Launching - Uikit Initialization | Launching - didFi... |
| Foreground - Active      |                   |                        |               |                                  |                      |

# App Lifecycle

| Start         | Duration  | Narrative                                          |
| ------------- | --------- | -------------------------------------------------- |
| 00:00.000.000 | 26.66 ms  | The system took 26.66 ms to create the process     |
| 00:00.026.659 | 10.21 ms  | The system frameworks took 10.21 ms to initialize. |
| 00:00.027.159 | 15.70 ms  | The system frameworks took 15.70 ms to initialize. |
| 00:00.036.869 | 5.99 ms   | Initializing - Static Runtime Initialization       |
| 00:00.042.931 | 16.97 ms  | Launching - UIKit Initialization                   |
| 00:00.059.902 | 309.71 μs | Launching - UIKit Scene Creation                   |
| 00:00.060.212 | 841.37 μs | Launching - UIKit Scene Creation                   |
| 00:00.061.053 | 8.96 ms   | Launching - didFinishLaunchingWithOptions()        |
| 00:00.070.013 | 239.17 us | Launching - UIKit Scene Creation                   |
| 00:00.070.252 | 382.00 μs | Launching - Initial Frame Rendering                |
| 00:00.073.682 | 1.14s     | Currently running in the foreground..              |

There are two phases when calculating app launch time on iOS. The first one is called pre-main time, and it’s the time before the main function of the app is executed. It’s marked with the purple area on the graph above – all the work needed to launch the app correctly, like initialization and the linking of libraries happens in this phase.

The second phase, called post-main-time, is the time between executing the app’s main function and presenting the first interactable view to the user. It’s marked with the green color on the graph above. The total app launch time is the sum of both of these metrics. If you want to learn more about testing app launch time, here’s a good read on this topic.

It’s worth mentioning that there are lots of third-party tools helping developers to gain a bunch of performance information from apps already submitted to Google Play and App Store. The most popular are Firebase Performance Monitoring, Sentry, and DataDog. The key advantage of using one of these tools is gaining

data about performance from the myriad of different devices used by your actual users.

# BENEFITS: A SMALLER BUNDLE SIZE AND FASTER TIME TO INTERACTIVE.

Removing a few unused native dependencies ended up reducing both the size of the app bundle and TTI by around 17%. Providing only resources needed by the app can improve the Time to Interactive metric, making users less likely to uninstall your app from their devices due to excessive load time.

It’s worth remembering that although autolinking is a great and powerful feature, it can be overzealous when it comes to linking code our app doesn’t really use. Make sure to keep your dependencies up to date and clean up unused ones during refactorings.

“There are so many tricky parts to making a great native app, and to lower the barrier to entry, React Native can abstract away things that you might want to come back and check on later once you’ve got your app up and running – this ebook does a solid job of helping you understand how to really get from good to great.“

Orta Therox – CocoaPods creator, TypeScript core contributor

# PART 2 | CHAPTER 4

# OPTIMIZE YOUR APPLICATION STARTUP TIME WITH HERMES

4 2

# ACHIEVE A BETTER PERFORMANCE OF YOUR APPS WITH HERMES.

ISSUE: YOU'RE LOADING A LOT OF ANDROID PACKAGES DURING THE STARTUP TIME WHICH IS UNNECESSARY. ALSO, YOU'RE USING AN ENGINE THAT IS NOT OPTIMIZED FOR MOBILE.

Users expect applications to be responsive and load fast. Apps that fail to meet these requirements can end up receiving bad ratings in the App Store or Play Store. In the most extreme situations, they can even get abandoned in favor of their competition.

There is no single definition of the startup time. It's because there are many different stages of the loading phase that can affect how “fast” or “slow” the app feels. For example, in the Lighthouse report, there are eight performance metrics used to profile your web application. One of them is Time to Interactive (TTI), which measures the time until the application is ready for the first interaction.

There are quite a few things that happen from the moment you press the application icon from the drawer for the first time.

The loading process starts with a native initialization which loads the JavaScript VM and initializes all the native modules (1 in the above diagram). It then continues to read the JavaScript from the disk and loads it into the memory, parses, and starts executing (2 in the above diagram). The details of this operation were discussed earlier in the section about choosing the right libraries for your application.

In the next step, React Native starts loading React components and sends the final set of instructions to the UIManager (3 in the above diagram). Finally, the UIManager processes the information received from JavaScript and starts executing the native instructions that will result in the final native interface (4 in the above diagram).

As you can see in the diagram below, there are two groups of operations that influence the overall startup time of your application.

The first one involves the first two operations (1 and 2 in the diagram above) and describes the time needed for React Native to bootstrap (to spin up the VM and for the VM to execute the JavaScript code). The other one includes the remaining operations (3 and 4 in the diagram above) and is associated with the business logic that you have created for your application. The length of this group is highly dependent on the number of components and the overall complexity of your application.

This section focuses on the first group – the improvements related to your configuration and not the business logic itself.

If you have not measured the overall startup time of your application or have not played around with things such as Hermes yet – keep on reading.

# LONG STARTUP TIMES AND SLOW UX CAN BE ONE OF THE REASONS YOUR APP GETS A BAD RATING AND ENDS UP BEING ABANDONED.

Creating applications that are fun to play with is extremely important, especially considering how saturated the mobile market already is. Now, all mobile apps have to be not only intuitive, they also should be pleasant to interact with.

# There is a common misconception that React Native applications come with a performance trade-off compared to their native counterparts.

The truth is that with enough attention and configuration tweaks, they can load just as fast and without any considerable difference.

# SOLUTION: TURN ON HERMES TO BENEFIT FROM A BETTER PERFORMANCE.

While a React Native application takes care of a native interface, it still requires JavaScript logic to be running at runtime. To do so, it spins off its own JavaScript virtual machine. Until recently, it used JavaScript – Core (JSC). This engine is a part of WebKit – which powers the Safari browser – and by default is only available on iOS. For a long time, it made sense for React Native to use JSC for running JavaScript on Android as well. It’s because using the V8 engine (that ships with Chrome) could potentially increase the differences between Android and iOS, and make sharing the code between the platforms way more difficult.

JavaScript engines need to perform various complicated operations. They constantly ship new heuristics to improve the overall performance, including the time needed to load the code and then execute it. To do so, they benchmark common JavaScript operations and challenge the CPU and memory needed to complete this process.

Most of the work of developers handling the JavaScript engines is being tested against the most popular websites, such as Facebook or Twitter. It is not a surprise that React Native uses JavaScript in a different way. For example, the JavaScript engine made for the web doesn’t have to worry much about the startup time. The browser will most likely already be running at the time of loading a page. Because of that, the engine can shift its attention to the overall CPU and memory consumption, as web applications can perform a lot of complex operations and computations, including 3D graphics.

As you could see on the performance diagram presented in the previous section, the JavaScript virtual machine consumes

# Hermes: A JavaScript Engine for React Native

A big chunk of the app's total loading time. Unfortunately, there is little you can do about it unless you build your own engine. That’s what the Meta team ended up doing.

Meet Hermes – a JavaScript engine made specifically with React Native in mind. It is optimized for mobile and focuses on relatively CPU-insensitive metrics, such as application size and memory consumption. Chances are you’re already using it! As of v0.70, React Native has been shipping with Hermes turned on by default, which marks an important milestone in the engine’s stability.

It’s come a long way from the bare-bones Android-only engine open-sourced in 2019, with a carefully curated set of supported JS features – due to size constraints – through finding low-size-footprint ways of adding more EcmaScript spec features, like Proxies and Intl, until making it available for macOS and iOS.

Today Hermes is still small enough (~2 MB) to provide significant improvements to apps' TTI and gives us a set of features rich enough to be used in most of the apps out there.

Before we go into the details of enabling Hermes in existing React Native applications, let’s take a look at some of its key architectural decisions.

# BYTECODE PRECOMPILATION

Typically, the traditional JavaScript VM works by parsing the JavaScript source code during the runtime and then producing the bytecode. As a result, the execution of the code is delayed until the parsing completes. It is not the same with Hermes. To reduce the time needed for the engine to execute the business logic, it generates the bytecode during the build time.

It can spend more time optimizing the bundle using various techniques to make it smaller and more efficient. For example, the generated bytecode is designed in a way so that it can be mapped in the memory without eagerly loading the entire file. Optimizing that process brings significant TTI improvements as I/O operations on mobile devices tend to increase the overall latency.

# NO JIT

The majority of modern browser engines use just-in-time (JIT) compilers. It means that the code is translated and executed line-by-line. However, the JIT compiler keeps track of warm code segments (the ones that appear a few times) and hot code segments (the ones that run many times). These frequently occurring code segments are then sent to a compiler that, depending on how many times they appear in the program, compiles them to the machine code and, optionally, performs some optimizations.

Hermes, unlike the other engines, is an AOT (ahead-of-time) engine. It means that the entire bundle is compiled to bytecode ahead of time. As a result, certain optimizations that JIT compilers would perform on hot code segments are not present.

On one hand, it makes the Hermes bundles underperform in benchmarks that are CPU-oriented. However, these benchmarks are not really comparable to a real-life mobile app experience, where TTI and application size takes priority.

On the other hand, JIT engines decrease the TTI as they need time to parse the bundle and execute it in time. They also need time to “warm up”. Namely, they have to run the code a couple of times to detect the common patterns and begin to optimize them.

If you want to start using Hermes on Android, make sure to turn the enableHermes flag in android/app/build.gradle to true:

project.ext.react = [
entryFile: ''index.js'',
enableHermes: true
]

# For iOS, turn the hermes_enabled flag to true in ios/Podfile:

use_react_native!(
:path => config[:reactNativePath],

# to enable hermes on iOS, change `false` to `true` and

then install pods
:hermes_enabled => true
)

In both cases, whenever you switch the Hermes flag, make sure to rebuild the project according to instructions provided in the native files. Once your project is rebuilt, you can now enjoy a faster app boot time and likely smaller app size.

# BENEFITS: A BETTER STARTUP TIME LEADS TO A BETTER PERFORMANCE. IT'S A NEVER-ENDING STORY.

Making your application load fast is an ongoing effort and its final result will depend on many factors. You can control some of them by tweaking both your application's configuration and the tools it uses to compile the source code.

Turning Hermes on is one of the things that you can do today to drastically improve certain performance metrics of your app, mainly the TTI.

Apart from that, you can also look into other significant improvements shipped by the Meta team. To do so, get familiar with their write-up on React Native performance. It is often a game of gradual improvements that make all the difference when applied at once. The React Native core team has created a visual report on benchmarking between stock RN and Hermes-enabled RN: see here.

As we have mentioned in the section on running the latest React Native, Hermes is one of those assets that you can leverage as long as you stay up to date with your React Native version.

Doing so will help your application stay on top of the performance game and let it run at a maximum speed.

# THE FUTURE WITH STATIC HERMES (EXPERIMENTAL)

At the React Native EU 2023 conf, the lead Hermes engineer, Tzvetan Mikov, announced an experimental tool that his team works on codenamed “Static Hermes”. It pushes what Hermes can do today with the ability to statically compile typed JavaScript code (essentially TypeScript or Flow) into native assembler instructions ahead of time. It exercises the idea that your app does not need to use Hermes or any other JavaScript engine to run, because it already has the native code inside it. That’s pretty wild.

Static Hermes is an ongoing experiment, however you can give it a try today. Read more on Hermes GitHub issue tracker: “How to try Static Hermes”

# PART 2

# | CHAPTER 5

# OPTIMIZE YOUR ANDROID APPLICATION’S SIZE WITH THESE GRADLE SETTINGS

# IMPROVE TTI AND REDUCE MEMORY USAGE

# AND THE SIZE OF YOUR APP BY ADJUSTING PROGUARD RULES TO YOUR PROJECTS.

ISSUE: YOU ARE NOT ENABLING PROGUARD FOR RELEASE BUILDS AND CREATING APK WITH CODE FOR ALL CPU ARCHITECTURES. YOU SHIP A LARGER APK.

At the beginning of each React Native project, you usually don’t care about the application size. After all, it is hard to make such predictions so early in the process. But it takes only a few additional dependencies for the application to grow from a standard 5 MB to 10, 20, or even 50 MB, depending on the codebase.

Should you really care about app size in the era of super-fast mobile internet and WiFi access everywhere? Why does a bundle size grow so rapidly? We will answer those questions in this section. But first, let’s have a look at what a typical React Native bundle is made of.

By default, a React Native application on Android consists of:

- four sets of binaries compiled for different CPU architectures,
- a directory with resources such as images, fonts, etc.,
- a JavaScript bundle with business logic and your React components,
- other files.

React Native offers some optimizations that allow you to improve the structure of the bundle and its overall size. But they are disabled by default.

If you are not using them effectively, especially when your application grows, you are unnecessarily increasing the overall size of your application in bytes. That can have a negative impact on the experience of your end users. We discuss it in the next section.

# A BIGGER APK SIZE MEANS MORE TIME NEEDED TO DOWNLOAD FROM THE APP STORE AND MORE BYTECODE TO LOAD INTO MEMORY

It’s great that you and your team operate on the latest devices and have fast and stable access to the internet. But you need to remember that not everyone has the same luxury. There are still parts of the world where network accessibility and reliability are far from perfect. Projects such as Starlink already improve that situation, but that will take time to cover the most remote areas out there.

Right now, there are still markets where every megabyte of traffic has its price. In those regions, the application’s size directly impacts the conversion, and the installation/cancellation ratio increases along with the app size.

Source: https://segment.com/blog/mobile-app-size-effect-on-downloads/

It is also a common belief that every well crafted and carefully designed application not only provides a beautiful interface but is also optimized for the end device. Well, that is not always the case. And because the Android market is so competitive, there is a big chance that a smaller alternative to those beautiful yet large apps is already gaining more traction from the community.

Another important factor is device fragmentation. The Android market is very diverse in that respect. There are more than 20 popular manufacturers, each releasing an array of devices every year. Contributing to a relatively significant share of mid to low-end devices, which account for over 60% of all smartphone sales annually. And those devices may face issues when dealing with bigger APKs.

As we have stressed already, the startup time of your application is essential. The more code the device has to execute while opening up your code, the longer it takes to launch the app and make it ready for the first interaction.

Now, let’s move to the last factor worth mentioning in this context – device storage.

Apps usually end up taking up more space after the installation. Sometimes they may even not fit into the device’s memory. In such a situation, users may decide to skip installing your product if that would mean removing other resources such as applications or images.

# SOLUTION: FLIP THE BOOLEAN FLAG

ENABLEPROGUARDINRELEASEBUILDS TO TRUE, ADJUST THE PROGUARD RULES TO YOUR NEEDS, AND TEST RELEASE BUILDS FOR CRASHES. ALSO, FLIP ENABLESEPARATEBUILDPERCPUARCHITECTURE TO TRUE.

Android is an operating system that runs on plenty of devices with different architectures, so your build must support most of them. React Native supports four: armeabi-v7a, arm64-v8a, x86, and x86_64.

While developing your application, Gradle generates the APK file that can be installed on any of the mentioned CPU architectures. In other words, your APK (the file outputted from the build process) is actually four separate applications packaged into a single file with .apk extension. This makes testing easier as the application can be distributed onto many different testing devices at once.

Unfortunately, this approach has its drawbacks. The overall size of the application is now much bigger than it should be as it contains the files required by all architectures. As a result, users will end up downloading extraneous code that is not even compatible with their phones.

Thankfully, you can optimize the distribution process by taking advantage of App Bundles when releasing a production version of your app.

# App Bundle

App Bundle is a publishing format that allows you to contain all compiled code and resources. It’s all due to the fact that Google Play Store Dynamic Delivery will later build tailored APKs depending on the end users’ devices.

To build App Bundle, you have to simply invoke a different script than usual. Instead of using ./gradlew assembleRelease, you should use ./gradlew bundleRelease, but inside React Native Community CLI there’s a command that handles everything under the hood, so all you need to run is:

npx react-native build-android

# Building a React Native app as App Bundle

The main advantage of the Android App Bundle over builds for multiple architectures per CPU is the ease of delivery. After all, you have to ship only one artifact and Dynamic Delivery will do all the magic for you. It also gives you more flexibility on supported platforms.

You don’t have to worry about which CPU architecture your end user’s device has. The average size reduction for an app is around 35%, but in some cases, it can be even cut in half, according to the Android team.

# APP STUOTOS

# PLUTO in text+ ABA

0

Source: https://medium.com/google-developer-experts/exploring-the-android-app-bundle-ca16846fa3d7

Another way of decreasing the build size is by enabling Proguard. Proguard works in a similar way to dead code elimination from JavaScript – it gets rid of the unused code from third-party SDKs and minifies the codebase.

However, Proguard may not work out-of-the-box with some projects and usually requires an additional setup to achieve optimal results. In this example, we were able to reduce the size of the mentioned 28 MB build by 700 KB. It is not much, but it is still an improvement.

def enableProguardInReleaseBuilds = true

Enabling proguard in android/app/build gradle

Another good practice is keeping your eye on resources optimization. Each application contains some svg or png graphics that can be optimized using free web tools.

# Reducing Redundant Text from SVG and Compressing PNG Images

Reducing redundant text from svg and compressing png images can save some bytes when your project has already too many of them.

# BENEFITS: A SMALLER APK, SLIGHTLY FASTER TTI, AND SLIGHTLY LESS MEMORY USED.

All the mentioned steps are worth taking when you’re struggling with a growing application size. You will achieve the most significant size reduction by building the app for different architectures. But the list of possible optimizations doesn’t stop there.

By striving for a smaller APK size, you will do your best to reduce the download cancellation rate. Also, your customers will benefit from a shorter Time To Interactive and be more inclined to use the app more often.

Finally, you will demonstrate that you care about every user, not only those with top-notch devices and fast internet connections. The bigger your platform gets, the more important it is to support those minor groups, as every percent of users translates into hundreds of thousands of actual users. If you’d like to learn more about optimizing Android, check the Android Profiling chapter.

# PART 2

# CHAPTER 6

# EXPERIMENT WITH THE NEW ARCHITECTURE OF REACT NATIVE

70

# LEVERAGE THE CAPABILITIES OF THE NEW RENDERING SYSTEM INSIDE YOUR APP.

# ISSUE: YOUR APP IS USING OLD ARCHITECTURE WITHOUT THE CONCURRENT FEATURES OF REACT 18.

Maybe it's better to say “current” architecture since it's still mostly used by production apps. This term refers to how React Native's two realms (Native and JS) communicate with each other. Both new and old architecture is based on the communication between JavaScript and the native side. Currently, this communication is handled by the bridge. Let's go over its limitations in order to easier understand the problems that the New Architecture is trying to solve.

- It is asynchronous: the JavaScript side submits data to a bridge and waits for the data to be processed by the native side.
- It's single-threaded (that's why it's important to not overload the JS thread and execute animations on the UI thread).
- It adds additional overhead when it comes to the serialization of data from JSON objects.

The bridge is still working fine for most use cases. However, when we start to send a lot of data over the bridge, it may become a bottleneck for our app. This problem can be seen when rendering a lot of components in a long list. In the case when the user scrolls fast, there will be a blank space caused by the communication between the JS and native sides being asynchronous. Essentially what happens is that we are having a “traffic jam” on our bridge with objects waiting to be serialized. The same issue with the bridge being “overloaded” can be seen in native modules sending a lot of data back and forth.

This bottleneck, together with providing a type safe way of communicating between native and JS, are the main things that the new architecture is trying to solve. However, not everything about new architecture is as good as it may seem. We will also get into the drawbacks that it brings.

# SOLUTION: MIGRATE YOUR APP TO NEW ARCHITECTURE.

# WHAT IS NEW ARCHITECTURE?

Starting from React Native v0.68 developers can leverage new capabilities of the framework. The New Architecture relies on a series of tools which are key components to the new experience, two most important ones are: Fabric and TurboModules. The first one is a new rendering system and the second one is a new way of writing native modules. We will get into details later in this section.

Codegen and JSI are two new tools improving developer experience. They are essential to understand how the new architecture works.

Codegen drastically improves DX by generating a lot of native boilerplate code and ensuring type safety. And JSI, a C++ API for interacting with any JS engine.

Note: New Architecture is still considered experimental. Always use the latest version of React Native when using it.

# Codegen

A code generation tool that makes JS source of truth by automating the compatibility between JS and native side. It allows to write statically typed JS (called JS Spec) which is then used to generate the interface files needed by Fabric native components and TurboModules. Spec consists of a set of types written in TypeScript or Flow that defines all the APIs provided by the native module. Codegen ensures type-safety as well as compile-time type safety, which means smaller code and faster execution as both realms can trust each other around validating the data every time. To find out more about it, refer to the docs.

JSI

# JSI

JSI is the foundation of the New Architecture, a C++ API for interacting with any JS engine. In contrast to the bridge which was asynchronous, JSI is synchronous which allows for invoking native functions faster. It lets JavaScript to hold references to C++ host objects and invoke methods directly on them. This removes the major overhead of asynchronous communication between JS and native by serializing objects using the bridge.

# Fabric

Fabric is React Native's new concurrent rendering system, a conceptual evolution of the legacy render system. The core principle is to unify more render logic in C++ to better leverage interoperability between platforms. Host Components like View, Text, etc. are now lazily initialized, resulting in faster startups. Fabric allows us to take advantage of the features introduced in React 18.

# TurboModules

This is a new way of writing native modules that also leverages the power of JSI, allowing for synchronous, and an order of magnitude faster data transfer from native to JS and vice versa. It is a rewrite of the communication layer between JavaScript and platform native modules like Bluetooth, Biometrics, etc. It also allows for writing native code for both platforms using C++ and introduces the lazy loading of modules to speed up your app startup time.

# Bridgeless mode

The ultimate goal of the New Architecture is to fully sunset the bridge. Starting from React Native 0.73, you can enable Bridgeless Mode which will disable the creation of the bridge entirely.

This will result in a slightly faster app startup due to removing the overhead of loading the rest of the React Native runtime: error handling, global event emitters, timers, and more.

# HOW TO TURN ON NEW ARCHITECTURE

According to official React Native core team recommendation, in order to turn on the New Architecture in your app, you need to update your app to the latest version of React Native.

To migrate your app to the New Architecture, follow these steps:

1. Upgrade your app to at least React Native version, you can use https://react-native-community.github.io/upgrade-helper/
2. [Android] Set newArchEnabled=true in gradle.properties.
3. [iOS] Run RCT_NEW_ARCH_ENABLED=1 pod install inside the iOS folder.
4. Run the app in debug and release modes. Look for Components that are not yet compatible – they will show as red boxes – Unimplemented component: &#x3C;ComponentName> – and you will likely notice them.
5. In case of unsupported components, use the Interop Layer through react-native.config.js file and the unstable_react-LegacyComponentNames option and try again. Take note that the interop layer is not fully compatible with the old rendering and event system, so inconsistencies may be expected in some cases.

# BENEFITS: YOU ARE ABLE TO LEVERAGE ALL THE LATEST FEATURES INCLUDING REACT 18, FABRIC, TURBOMODULES, AND JSI.

Now that you know the basics of how the New Architecture works, let's go over the benefits.

# Performance

Due to the synchronous nature of the new architecture, while communicating with the native side, there will be some performance improvements. The app's startup time will be significantly reduced as every native module will be lazily-loaded. Once the bridgeless mode will be available it will also remove the overhead of loading the bridge at startup. However, not every scenario proves this, in some of the benchmarks architecture performance is worse.

Meta's goal was not to make new architecture X times faster than the old one. Apart from removing major bottlenecks they wanted to create a new solid foundation which would allow for new capabilities that could not be developed using previous architecture. Migration of the Facebook app took over a year and they haven't noticed any significant performance improvements nor regressions that are perceivable by the end user. However, this doesn't mean that performance improvements won't come in the future. Now that they reworked internals they have a great foundation to build upon.

# Performance Benchmarks

Let's go over some performance benchmarks by Alexandre Moureaux from BAM. Here is the link to the source: https://github.com/reactwg/react-native-new-architecture/discussions/85

# Benchmark of rendering 10K views

In this case new architecture proves that it's more efficient than the old one. Using on average less CPU but more RAM.

| CPU Usage per thread (%) | 100.0 |
| ------------------------ | ----- |
|                          | 90.0  |
|                          | 80.0  |
|                          | 70.0  |
|                          | 60.0  |
|                          | 50.0  |
|                          | 40.0  |
|                          | 30.0  |
|                          | 20.0  |
|                          | 10.0  |
|                          | 0.0   |

3200 6400 9600 12800 1600

(fabric_bg) (10k Views - New Arch DISABLED (fabric_bg) (10k Views - New Arch ENABLED

(mqt_native_modu) (10k Views - New Arch DISABLED) (mqt_native_modu) (10k Views - New Arch ENABLED

# Benchmark of rendering 2K Text components

In this scenario, the old architecture is faster, mainly because of heavier UI thread consumption.

| (X pa Ta S M pa I(C pe T- Sx M I | 10000 | 0008 | 0009  | 2000            | 2000 | 0    |
| -------------------------------- | ----- | ---- | ----- | --------------- | ---- | ---- |
| 0°0                              | 0.01  | 2200 | 000   | 0°00            | 0'09 | 0'09 |
| 200                              | 0'08  | 0'06 | 0'001 | () pea ed ee Co |      |      |

The official response from the React Native team is that their internal benchmarks while rolling out the New Architecture to users was neutral across all React Native surfaces in the Facebook app on both Android and iOS. As stated by Samuel Susla in this discussion thread, “In the last years, we conducted dozens of tests in production on millions of devices to assure performance was neutral.”

So in most use cases, you can expect a neutral performance impact without any performance regressions. And keep in mind that the New Architecture is getting better every single day with many developers contributing to the repository, so the results may be totally different by the time you are reading this.

# FUTURE READINESS

New Architecture allows your app to leverage Concurrent React features. Which improves UI responsiveness, provides Suspense for data fetching to handle complex UI loading schemes, and ensures your app is ready for any further React innovations that will be built on top of its new concurrent engine introduced in React 18.

Let's see how we can leverage React18's startTransition API in order to prioritize between two state updates. In our example,

# Understanding Non-Urgent Updates in React

A button click can be considered an urgent update whereas the NonUrgentUI can be considered a non-urgent update. To tell React about a non-urgent update, we can wrap the setState in the startTransition API. This allows React to prepare a new UI and show the old UI until a new one is prepared. In our example, we wrapped setNonUrgentValue in startTransition and told React that nonUrgentValue is a transition and not so urgent, it may take some time. We've also added a conditional backgroundColor. When you run this example, you will see that once you click on the button, the view will retain its old UI for e.g., if we start at value 1, the UI will be green.

Once you click on the button, the Value text UI will be updated but the UI for the container will still remain green until the transition is completed and the color will change to red due to the new UI being rendered. That's the magic of React's concurrent rendering.

To understand it better, assume that wrapping an update in startTransition renders it in a different universe. We don't see that universe directly but we can get a signal from it using the isPending variable returned from the useTransition hook. Once the new UI is ready, both universes merge together to show the final UI.

import React from 'react';
import { Button, StyleSheet, Text, View } from 'react-native';

const dummyData = Array(10000).fill(1);

const NonUrgentUI = ({ value, isPending }) => {
const backgroundStyle = {
backgroundColor: value % 2 === 0 ? 'red' : 'green',
};

return (
<view>
<text>Non urgent update value: {isPending ? 'PENDING' : value}</text>
<view style="{[styles.container," backgroundstyle]}="">
{dummyData.map((\_, index) => (
<view key="{index}" style="{styles.item}">
))}
</view>
</view>
);
};</view>

# ConcurrentStartTransition

const ConcurrentStartTransition = () => {
const [value, setValue] = React.useState(1);
const [nonUrgentValue, setNonUrgentValue] = React.useState(1);
const [isPending, startTransition] = React.useTransition();

const handleClick = () => {
const newValue = value + 1;
setValue(newValue);
startTransition(() => {
setNonUrgentValue(newValue);
});
};
return (
<view>

<text>Value: {value}</text>
<nonurgentui value="{nonUrgentValue}" ispending="{isPending}">

);
};

export default ConcurrentStartTransition;

const styles = StyleSheet.create({
container: {
flexDirection: 'row',
flexWrap: 'wrap',
},
item: {
width: 10,
height: 10,
},
</nonurgentui></view>
To understand it better, let's visualize the code snippet that we just went through. The image below shows a comparison of when we use startTransition and when we don't. Looking at the image, we see that React flushes the urgent update right off, which happens due to calling setValue without wrapping it in startTransition.

Next, we see that React shows the old UI (viewed in green) for the UI that depends on the nonurgent updates, which means the updates that are wrapped in startTransition. We also see a Pending text displayed, this is a way for React18 to tell us that the new UI depending on this state is not yet ready. Once it's ready, React flushes it and we don't see the Pending text anymore, and the view color changes to red.

On the other hand, if we don't use startTransition, React tries to handle both updates as urgent and flushes once both are ready. This certainly has a few downsides, such as the app trying to render some heavy UI all at once which may cause jarring effects for the users. With React18, we can handle this by delaying the updates that are not urgent.

# Using React18's startTransition

# Not Using React18's startTransition

| 8340                       | 4                          | 8:36 | 4   |
| -------------------------- | -------------------------- | ---- | --- |
| INCREMENT VALUE            | INCREMENT VALUE            |      |     |
| Value: 1                   | Value: 1                   |      |     |
| Non urgent update value: 1 | Non urgent update value: 1 |      |     |

| 834      | A                                | 8:37            | 4                          |
| -------- | -------------------------------- | --------------- | -------------------------- |
|          | INCREMENT VALUE                  | INCREMENT VALUE |                            |
| Value: 2 | Value: 2                         |                 |                            |
|          | Non urgent update value: PENDING |                 | Non urgent update value: 2 |

8:34

INCREMENT VALUE

Value: 2

Non urgent update value: 2

There are some other noticeable features in React18 that you might want to check out by playing with the linked sandboxes from React's official website. See useDeferredValue and startTransition with Suspense.

# MAINTENANCE &#x26; SUPPORT

The React Native core team is committed to offer support for the 3 latest versions of React Native (you can check the support policy here: https://github.com/reactwg/react-native-releases#releases-support-policy). And the React core team plans new features built on the concurrent rendering engine. It's important to not stay behind, as the cost of paying the tech debt will get higher in time. It's worth calling out that React Native is no different to any other software project in this regard. Not updating dependencies may not only cause your team to spend more time on this task when

it's unavoidable. It can also expose your app to security vulnera-

bilities already patched in the upstream.

The React Native team has dedicated capacity to help the com-

munity solve their app and library problems regarding new ar-

chitecture adoption in close cooperation. Although it's not stable

yet, it's worth trying out in your app today. Especially considering

that since React Native v0.72 the Interop Layer exists which al-

lows running most of the old architecture components with apps

that enabled new architecture.

# IF YOU NEED HELP WITH

# PERFORMANCE, STABILITY, USER

# EXPERIENCE, OR OTHER COMPLEX

# ISSUES – CONTACT US!

As React Native Core Contributors and leaders of the com-

munity, we will be happy to help.

# PART 3

# HOW TO SHIP QUICKER WITH A STABLE DEVELOPMENT ENVIRONMENT

React Native is great for shipping fast and with confidence, but are you ready for that?

These days, having a stable and comfortable development setup that encourages shipping new features and doesn't slow you down is a must. You have to ship fast and be ahead of your competitors.

React Native plays really well in such environments. For example, one of its biggest selling points is that it allows you to ship updates to your applications without undergoing the App Store submission. They're called Over-the-Air (OTA) updates.

The question is: is your application ready for that? Does your development pipeline accelerate the development and shipping features with React Native?

Most of the time, you would like the answer to be simply yes. But in reality, it gets complicated.

In this section, we present some of the best practices and recommendations that allow you to ship your apps faster and with more confidence. And it's not just about turning on the Over-the-Air updates, as most articles suggest. It's about building a steady and healthy development environment where React Native shines and accelerates innovation.

And that's what this part of our guide is all about.

# PART 3

# | CHAPTER 1

# RUN TESTS FOR KEY PIECES OF YOUR APP

# FOCUS TESTING ON KEY PIECES OF THE APP TO HAVE A BETTER OVERVIEW OF NEW FEATURES AND TWEAKS.

# ISSUE: YOU DON'T WRITE TESTS AT ALL OR WRITE LOW-QUALITY TESTS WITH NO REAL COVERAGE, AND YOU ONLY RELY ON MANUAL TESTING.

Building and deploying apps with confidence is a challenging task. However, verifying if everything actually works requires a lot of time and effort – no matter if it is automated or not. Having somebody who manually verifies that the software works as expected is vital for your product.

Unfortunately, this process doesn't scale well as the amount of your app functionalities grow. It also doesn't provide direct feedback to the developers who write the code. Because of that, it increases the time needed to spot and fix a bug.

So what do the developers do to make sure their software is always production-ready and doesn't rely on human testers? They write automated tests. And React Native is no exception. You can write a variety of tests both for your JS code – which contains the business logic and UI – and the native code that is used underneath.

You can do it by utilizing end-to-end testing frameworks, spinning up simulators, emulators, or even real devices. One of the great features of React Native is that it bundles to a native app bundle, so it allows you to employ all the end-to-end testing frameworks that you love and use in your native projects.

But beware, writing a test may be a challenging task on its own, especially if you lack experience. You might end up with a test that doesn't have a good coverage of your features. Or only to test positive behavior, without handling exceptions. It's very common.

to encounter low-quality tests that don't provide too much value and hence, won't boost your confidence in shipping the code.

Whichever kind of test you're going to write, be it unit, integration, or E2E (short for end-to-end), there's a golden rule that will save you from writing the bad ones. And the rule is to “avoid testing implementation details.” Stick to it and your test will start to provide value over time. You can't move as fast as your competition, chances of regressions are high, and apps can be removed from stores when receiving bad reviews. The main goal of testing your code is to deploy it with confidence by minimizing the number of bugs you introduce in your codebase. And not shipping bugs to the users is especially important for mobile apps, which are usually published in app stores.

Because of that, they are a subject of a lengthy review process, which may take from a few hours up to a few days. And the last thing you want is to frustrate your users with an update that makes your app faulty. That could lead to lower ratings and, in extreme cases, even taking the app down from the store.

Such scenarios may seem pretty rare, but they happen. Then, your team may become so afraid of having another regression and crash that it will lose its velocity and confidence.

# SOLUTION: DON'T AIM AT 100% COVERAGE, FOCUS ON KEY PIECES OF THE APP. TEST MOSTLY INTEGRATION.

Running tests is not a question of “if” but “how”. You need to come up with a plan on how to get the best value for the time spent. It's very difficult to have 100% lines of your code and dependencies covered. Also, it's often quite impractical.

Most of the mobile apps out there don't need a full test coverage of the code they write.

The exceptions are situations in which the client requires full coverage because of the government regulations they must abide by. But in such cases, you're probably already aware of the problem.

It's crucial for you to focus your time on testing the right thing. Learning to identify business-critical features and capabilities is usually more important than writing a test itself. After all, you want to boost confidence in your code, not write a test for the sake of it. Once you do that, all you need to do is decide on how to run it. You have quite a few options to choose from.

In React Native, your app consists of multiple layers of code, some written in JS, some in Java/Kotlin, some in Objective-C/Swift, and some even in C++, which is gaining adoption in the React Native core.

# Therefore, for practical reasons, we can distinguish between:

- JavaScript testing – with the help of the Jest framework. In the context of React Native, if you think about “unit” or “integration” tests, this is the category they eventually fall into. From a practical standpoint, there is no reason for distinguishing between those two groups.
- End-to-end app testing – with the help of Detox, Appium, or another mobile testing framework you're familiar with.

Because most of your business code lives in JS, it makes sense to focus your efforts there.

Testing pyramid. Source: https://twitter.com/aaronabramov_/status/805913874704674816

# JAVASCRIPT TESTING

Writing tests for utility functions should be pretty straightforward. To do so, you can use your favorite test runner. The most popular and recommended one within the React Native community is Jest. We'll also be referring to it in the following sections.

Testing trophy. Source: https://twitter.com/kentcdodds/status/960723172591992832

# For testing React components, you need more advanced tools though.

Let's take the following component as an example:

import React, { useState } from 'react';
import {
View,
Text,
TouchableOpacity,
TextInput,
ScrollView,
} from 'react-native';

const QuestionsBoard = ({ questions, onSubmit }) => {
const [data, setData] = useState({});

return (
<scrollview>
{questions.map((q, index) => {
return (
<view key="{q}">
<text>{q}</text>
<textinput accessibilitylabel="" answer="" input&#x27;&#x27;="" onchangetext="{(text)" &#x3D;=""> {
setData((state) => ({
...state,
[index + 1]: { q, a: text },
}));
}}
/>
</textinput></view>
);
})}
<touchableopacity onpress="{()" &#x3D;=""> onSubmit(data)}>
<text>Submit</text>
</touchableopacity>
</scrollview>
);
};

export default QuestionsBoard;
It is a React component that displays a list of questions and allows for answering them. You need to make sure that its logic works by checking if the callback function is called with the set of answers provided by the user.

To do so, you can use an official react-test-renderer library from the React core team. It is a test renderer, in other words, it allows you to render your component and interact with its lifecycle.

without actually dealing with native APIs. Some people may find it intimidating and hard to work with because of the low-level API.

That's why the community around React Native came out with helper libraries, such as React Native Testing Library, providing us with a good set of helpers to productively write your high-quality tests.

A great thing about this library is that its API forces you to avoid testing the implementation details of your components, making it more resilient to internal refactors.

# A test for the QuestionsBoard component would look like this:

import { render, screen, fireEvent } from '@testing-library/react-native';
import { QuestionsBoard } from '../QuestionsBoard';

test('form submits two answers', () => {
const allQuestions = ['q1', 'q2'];
const mockFn = jest.fn();

render(<questionsboard questions="{allQuestions}" onsubmit="{mockFn}">);

const answerInputs = screen.getAllByLabelText('answer input');

fireEvent.changeText(answerInputs[0], 'a1');
fireEvent.changeText(answerInputs[1], 'a2');
fireEvent.press(screen.getByText('Submit'));

expect(mockFn).toBeCalledWith({
1: { q: 'q1', a: 'a1' },
2: { q: 'q2', a: 'a2' },
});
});
</questionsboard>

Test suite taken from the official RNTL documentation

You first render the QuestionsBoard component with your set of questions. Next, you query the tree by label text to access an array of questions, as displayed by the component. Finally, you set up the right answers and press the submit button.

If everything goes well, your assertion should pass, ensuring that the verifyQuestions function has been called with the right set of arguments.

Note: You may have also heard about a technique called “snapshot testing” for JS. It can help you in some of the testing scenarios, e.g. when working with structured data that may change slightly between tests. The technique is widely adopted in the React ecosystem because of its built-in support from Jest.

If you're into learning more about snapshot testing, check out the official documentation on the Jest website. Make sure to read it thoroughly, as toMatchSnapshot and toMatchInlineSnapshot are low-level APIs that have many gotchas.

They may help you and your team quickly add coverage to the project. And at the same time, snapshots make adding low-quality and hard-to-maintain tests too easy. Using helper tools like eslint-plugin-jest with its no-large-snapshots option, or snapshot-diff with its component snapshot comparison feature for focused assertions, is a must-have for any codebase that leverages this testing technique.

# E2E TESTS

The cherry on top of our testing pyramid is a suite of end-to-end tests. It's good to start with a so-called “smoke test” – a test ensuring that your app doesn't crash on the first run. It's crucial to have a test like this, as it will help you avoid sending a faulty app to your users. Once you're done with the basics, you should use your E2E testing framework of choice to cover the most important functionalities of your apps.

These can be, for instance, logging in (successfully or not), logging out, accepting payments, and displaying lists of data you fetch from your or third-party servers.

Note: Beware that these tests are usually a bit harder to set up than the JS ones.

Also, they are more likely to fail because of the issues related to e.g. networking, file system operations or storage or memory shortage. What's more, they provide you with little information on why they do it. This test's quality (not only the E2E ones) is called “flakiness” and should be avoided at all cost, as it lowers your confidence in the test suite. That's why it's so important to divide testing assertions into smaller groups, so it's easier to debug what went wrong.

# Detox

For the purpose of this section, we'll be looking at Detox – the most popular E2E test runner within the React Native community.

Before going any further, you have to install Detox. This process requires you to take some additional “native steps” before you're ready to run your first suite. Follow the official documentation as the steps are likely to change in the future.

Once you have successfully installed and configured Detox, you're ready to begin with your first test.

This quick snippet shown above would ensure that the first question is displayed.

Before that assertion is executed, you should reload the React Native instance to make sure that no previous state is interfering with the results.

it('should display the questions', async () => {
await devicePixelRatio.reloadReactNative();

await element(by.text(allQuestions[0])).toBeVisible();
});

Note: When you're dealing with multiple elements (e.g. in our case – a component renders multiple questions), it is a good practice to assign a suffix testID with the index of the element, to be able to query the specific one. This, as well as some other interesting techniques, is in the official Detox recommendation.

There are various matchers and expectations that can help you build your test suite the way you want to.

# BENEFITS

YOU HAVE A BETTER OVERVIEW OF THE NEW FEATURES AND TWEAKS, CAN SHIP WITH CONFIDENCE, AND WHEN THE TESTS ARE GREEN – YOU SAVE THE TIME OF OTHER PEOPLE (THE QA TEAM).

A high-quality test suite that provides enough coverage for your core features is an investment in your team's velocity. After all, you can move only as fast as your confidence allows you to. And the tests are all about making sure you're heading in the right direction.

The React Native community is working hard to make testing as easy and pleasant as possible – for both your team and the QA teams. Thanks to that, you can spend more time innovating and pleasing users with flashy new functionalities, and not squashing bugs and regressions over and over again.

“By testing key features of an app via integration testing, developers can effectively identify and eliminate potential bugs, ultimately leading to a more confident and efficient development process.”

Christoph Nakazawa – Senior Engineering Manager &#x26; Creator of Jest

# PART 3 | CHAPTER 2

# HAVE A WORKING CONTINUOUS INTEGRATION (CI) IN PLACE

# USE A CI PROVIDER TO IMPROVE THE BUILDING, TESTING, AND DISTRIBUTION OF YOUR APPS.

ISSUE A LACK OF CI OR HAVING AN UNSTABLE ONE MEANS A LONGER FEEDBACK LOOP – YOU DON’T KNOW IF YOUR CODE WORKS AND YOU COOPERATE SLOWLY WITH OTHER DEVELOPERS.

As you have already learned from the previous section, covering your code with tests can be very helpful for increasing the overall reliability of your app. However, while testing your product is vital, it is not the only prerequisite on your way to shipping faster and with more confidence.

What is equally important is how quickly you detect the potential regressions and whether finding them is a part of your daily development lifecycle. In other words – it all comes down to the feedback loop.

For better context, let’s take a look at the early days of the development process. When you’re starting out, your focus is on shipping the first iteration (MVP) as fast as possible. Because of that, you may overlook the importance of the architecture itself. When you’re done with the changes, you submit them to the repository, letting other members of your team know that the feature is ready to be reviewed.

An example of a workflow on Github, where changes are proposed in the form of a PR.

While this technique can be very useful, it is potentially dangerous on its own, especially as your team grows in size. Before you’re ready to accept a PR, you should not only examine the code but also clone it to your environment and test it thoroughly. At the very end of that process, it may turn out that the proposed changes introduce a regression that the original author hasn’t spotted.

The regression can occur because we all have different configurations, environments, and ways of working.

# IT’S HARDER TO ONBOARD NEW MEMBERS TO YOUR ORGANIZATION. YOU CAN’T SHIP AND TEST PRS AND DIFFERENT CONTRIBUTIONS AS THEY HAPPEN.

If you’re testing your changes manually, you’re not only increasing the chances of shipping regressions to production. You’re also slowing down the overall pace of the development. Thankfully, with the right set of methodologies and a bit of automation, you can overcome this challenge once and for all.

This is when Continuous Integration (CI) comes into play. CI is a development practice where proposed changes are checked-in to the upstream repository several times a day by the development team. Next, they are verified by an automated build, allowing the team to detect changes early.

The automated builds are performed by a dedicated cloud-based CI provider that usually integrates from the place where you store your code. Most of the cloud providers available these days support GitHub, which is a Microsoft-owned platform for collaborating on projects that use Git as their version control system.

CI systems pull the changes in real-time and perform a selected set of tests to give you early feedback on your results. This approach introduces a single source of truth for testing and allows developers with different environments to receive convenient and reliable information.

# Continuous Deployment with CI Services

Using a CI service, you not only test your code but also build a new version of the documentation for your project, build your app, and distribute it among testers or releases. This technique is called Continuous Deployment and focuses on the automation of releases. It has been covered in more depth in this section.

# SOLUTION: USE A CI PROVIDER SUCH AS CIRCLE CI OR EAS BUILD TO BUILD YOUR APPLICATION.

RUN ALL THE REQUIRED TESTS AND MAKE PREVIEW RELEASES IF POSSIBLE.

There are many CI providers to choose from, and you can pick the one best suited for your project needs, or even use a combination of CI tools. Circle CI and GitHub actions are generic CI providers with expansive capabilities that also span outside of mobile app development. Bitrise specializes in services used in Mobile App Development, and EAS is specialized specifically in building and deploying React Native projects.

We have selected CircleCI as our reference CI provider for the purpose of this section, as it has wide community adoption. In fact, there is actually an example project demonstrating the use of CI with React Native. You can learn more about it here. We will employ it later in this section to present different CI concepts.

After this overview, we will show you how to alternatively set up EAS on your React Native project, and use it to build your native iOS and Android bundles for development, preview and production.

Note: A rule of the thumb is to take advantage of what React Native or React Native Community projects already use. Going that route, you can ensure that it is possible to make your chosen provider work with React Native and that the most common challenges have been already solved by the Core Team.

CircleCI

As with most CI providers, it is extremely important to study their configuration files before you do anything else.

Let’s take a look at a sample configuration file for CircleCI, taken from the mentioned React Native example:

version: 2.1

jobs:
android:
working_directory: ~/CI-CD
docker:

- image: reactnativecommunity/react-native-android
  steps:
- checkout
- attach_workspace:
  at: ~/CI-CD
- run: npm i -g envinfo &#x26;&#x26; envinfo
- run: npm install
- run: cd android &#x26;&#x26; chmod +x gradlew &#x26;&#x26; ./gradlew assembleRelease

workflows:
build_and_test:
jobs:

- android

Example of .circleci/config.yml

The structure is a standard Yaml syntax for text-based configuration files. You may want to learn about its basics before proceeding any further.

Note: Many CI services, such as CircleCI or GitHub Actions, are based on Docker containers and the idea of composing different jobs into workflows. You may find many similarities between such services.

These are the three most important building blocks of a CircleCI configuration: commands, jobs, and workflows.

A command is nothing more than a shell script. It is executed within the specified environment. Also, it is what performs the actual job in the cloud. It can be anything, from a command to install your dependencies, such as yarn install (if you’re using Yarn).

to something more complex like ./gradlew assembleDebug that builds Android files.

# 1. Jobs

A job is a series of commands – described as steps – that is focused on achieving a single, defined goal. Jobs can be run in different environments, by choosing an appropriate Docker container.

For example, you may want to use a Node container if you need to run only your React unit tests. As a result, the container will be smaller, have fewer dependencies, and will install faster. If you want to build a React Native application in the cloud, you may choose a different container, e.g. with Android NDK/SDK or the one that uses OS X to build Apple platforms.

Note: To help you choose the container to use when running React Native tests, the team has prepared a Docker Android container that includes both Node and Android dependencies needed to perform the Android build and tests.

# 2. Executing Jobs

In order to execute a job, it has to be assigned to a workflow. By default, jobs will be executed parallelly within a workflow, but this can be changed by specifying the requirements for a job.

You can also modify the jobs execution schedule by adding filters, so, for instance, a deploy job will only run if the changes in the code refer to the main branch.

You can define many workflows for different purposes, e.g. one for tests that would run once a PR is opened, and the other to deploy the new version of the app. This is what React Native does to automatically release its new versions every once in a while.

Expo Application Services (EAS)

EAS is a set of deeply integrated cloud services for Expo and React Native apps, built and maintained by the team behind Expo. The three most popular services it includes are:

- EAS Build: a cloud service that helps you build React Native app bundles
- EAS Submit: a cloud service that lets you to upload your built app bundles directly to TestFlight on the Apple App Store, and your preferred track on the Android Google Play Store
- EAS Update: a service to deliver over the air (OTA) updates to React Native apps

In this section, we will focus on EAS Build. As mentioned above, EAS is highly specialized in providing the fastest and most seamless experience for building React Native apps. To provide the best developer experience, EAS Build already has the iOS and Android development environments pre-configured, and it comes with built-in support for all the more popular package managers including npm, yarn, pnpm and bun.

One benefit of using EAS to build your React Native apps, is that because it’s a cloud service, you can trigger the app builds from a Mac, Windows or even a Linux machine and download the build directly to your development device. This means you could for example develop an iOS app on a Windows machine, getting around the Apple restrictions of needing to own a Mac in order to build a native iOS app.

Another benefit of using EAS for building your React Native apps is that you get build caching for your JavaScript, Android and iOS dependencies out of the box with no configuration needed.

# Setting up EAS Build

To set up EAS Build in an existing React Native app, you’ll first want to install the EAS cli:

npm i -g eas-cli

# Creating App Builds

You’ll also need to create an Expo account if you didn’t already have one, and log in on the cli:

eas login
To create app builds that run on real devices, you will need to configure build signing: this means generating keystores for Android and Provisioning Profiles and Certificates for iOS.

One of the perks of using EAS is that it comes with a cli tool that can automatically create and update all of your build credentials for you. The CLI prompts you to do this when you configure your first build, or you can also manage the credentials without triggering a build by running the eas credentials cli command.

After installing the CLI and logging in, run the following in the root directory of your project:

eas build:configure
This will add the eas.json file to the root directory of your project:

{
''cli'': {
''version'': ''>= 6.0.0''
},
''build'': {
''development'': {
''developmentClient'': true,
''distribution'': ''internal''
},
''preview'': {
''distribution'': ''internal''
},
''production'': {}
},
''submit'': {
''production'': {}
}
}

# Configuration of eas.json File

The eas.json file will contain all the configuration needed to build your app on EAS. By default, it will come with 3 build profiles: development, preview and production:

# 1. Development

distribution: 'internal' in the development profile means that the build will be downloadable via a link, and developmentClient: true enables the dev menu, allowing the JavaScript to be bundled separately. This is the build you’d want to use for local development.

# 2. Preview

The preview build will also be downloadable via a link, but it does not include the dev client. This means that it will come with one JavaScript bundle and cannot be used for local development. It is best used to test or preview your production app before you submit it to the stores.

# 3. Production

This creates the production apps that you can upload to the Google Play and Apple App Stores.

You can always add additional profiles as needed. For example, you could add a separate build profile for creating an iOS app that can run on a Simulator:

development:simulator: {
ios: {
simulator: true
},
developmentClient: true,
distribution: 'internal'
}

As seen above, each profile can have additional platform-specific configurations, though most of the time the configuration will be shared. See the eas.json reference for all available configuration options.

# Running your build on EAS Build

Any build configured in eas.json can be triggered with a single command. For example, if you want to build the app for local development, run:

eas build –profile development
The CLI will prompt you whether you want to build the iOS app, Android app or both. The development build has ''developmentClient'': true, meaning it can be used for local development. You won’t need to rebuild it again unless you add any native code or packages. Once you’ve created a build, you can use Expo Orbit to install and run builds from EAS or local files on simulators and physical devices.

To use a different build profile, for example the preview build, you can run the same command with --profile preview:

eas build –profile preview
Once the build is complete, the CLI will print out the URL for the build, and any member of your team can download the app to their device.

# Builds92c739b9

| Android internal distribution build |             | Show Details |              |           |                        |
| ----------------------------------- | ----------- | ------------ | ------------ | --------- | ---------------------- |
| Profile                             | SDK version | Version      | Version code | Commit    | Created by             |
| preview                             | 49.0.0      | 1.0.0        | 2            | ade4887\* | Kadi Kraman (expokadi) |

# Build artifact APK

| Status   | Start time           | Wait time | Queue time | Build time | Total time | Availability |
| -------- | -------------------- | --------- | ---------- | ---------- | ---------- | ------------ |
| Finished | Jan 11, 2024 1:20 PM | None      | 49s        | 7m 31s     | 8m 21s     | 82 days      |

To automate this workflow, you could configure EAS to build from GitHub with the Expo GitHub App.

# Continuous Integration with EAS

While EAS is primarily used for building and submitting your native apps to the stores, it does also support running E2E tests as part of your workflow.

# Benefits

YOU GET EARLY FEEDBACK ON ADDED FEATURES, AND SWIFTLY SPOT THE REGRESSIONS. ALSO, YOU DON’T WASTE THE TIME OF OTHER DEVELOPERS ON TESTING THE CHANGES THAT DON’T WORK.

A properly configured and working CI provider can save you a lot of time when shipping a new version of an application.

| &0  | Some checks were not successful                                          |
| --- | ------------------------------------------------------------------------ |
|     | 2 failing and 66 successful checks                                       |
| ×   | Run Danger on PR / danger (pull_request_target) Failing after 50s        |
|     | Test Docker Android Image / Test Docker (pull_request) Successful in 48m |
| ×   | Danger — Found some issues. Don't worry, everything is fixable.          |
|     | FB Facebook CLA Check — Contributor License Agreement is valid!          |
|     | Facebook Internal - Builds & Tests — 1 passed                            |
|     | Facebook Internal - Linter — 1 passed                                    |

# Merging Status

X Merging is blocked

The base branch restricts merging to authorized users. Learn more about protected branches

Merge pull request You're not authorized to merge this pull request.

GitHub UI reporting the status of CircleCI jobs, an example taken from React Native repository

By spotting errors beforehand, you can reduce the effort needed to review the PRs and protect your product against regressions and bugs that may directly decrease your income.

# PART 3

# CHAPTER 3

# DON’T BE AFRAID TO SHIP

# FAST WITH CONTINUOUS DEPLOYMENT

# ESTABLISH A CONTINUOUS DEPLOYMENT SETUP TO SHIP NEW FEATURES AND VERIFY CRITICAL BUGS FASTER.

ISSUE: BUILDING AND DISTRIBUTING YOUR APPS MANUALLY IS A COMPLEX AND TIME-CONSUMING PROCESS.

As you have learned in the previous section, automation of the critical pieces of the development lifecycle can help you improve overall development speed and security. The shorter the feedback loop, the faster your team can iterate on the product itself.

However, testing and development are only a part of the activities that you have to perform when working on a product. Another important step is the deployment – building and distributing the application to production. Most of the time, this process is manual.

The deployment takes time to set up and is far more complex than just running tests in the cloud. For example, on iOS, Xcode configures many settings and certificates automatically. This ensures a better developer experience for someone who’s working on a native application. Developers who are used to such an approach often find it challenging to move the deployment to the cloud and set up such things as certificates manually.

The biggest downside of the manual approach is that it takes time and doesn’t scale. In consequence, teams that don’t invest in the improvements to this process end up releasing their software at a slower pace.

# Continuous Deployment

Continuous Deployment is a strategy in which software is released frequently through a set of automated scripts. It aims at building, testing, and releasing software with greater speed and frequency. The approach helps reduce the cost, time, and risk of delivering changes by allowing for more incremental updates to applications in production.

YOU ARE NOT SHIPPING NEW FEATURES AND FIXES AS QUICKLY AS YOU SHOULD.

Building and distributing your application manually slows down your development process regardless of how big your team is. Even in small product teams of around 5 people, automated build pipelines make everyone’s work easier and reduce unnecessary communication. This is especially important for remote companies.

Continuous Deployment also allows you to introduce standards and best practices focused on improving the overall performance of the application. Some of them have been previously discussed in this guide. With all the steps required for the deployment in a single place, you can ensure that all releases are done the same way and enroll company-wide standards.

# SOLUTION: ESTABLISH A CONTINUOUS DEPLOYMENT SETUP THAT MAKES THE BUILD AND GENERATES THE CHANGELOG. SHIP TO YOUR USERS INSTANTLY.

When it comes to automating the deployment of mobile applications, there are a few established ways to go.

One way is to write a set of scripts from scratch by interacting with xcode and gradle directly. Unfortunately, there are significant differences between the tooling of Android and iOS and not many developers have enough experience to handle this.

automation. On top of that, iOS is much more complicated than Android due to advanced code signing and distribution policies. And as we have said before, if you are doing it manually, even Xcode cannot help you.

Another way is to use a pre-existing tool in which the developers have handled the majority of use cases. Our favorite one is fastlane – a set of modular utilities written in Ruby that let you build your iOS and Android applications by writing a set of instructions in a configuration file.

After you have successfully built your binaries, it is time to deploy them to their destination.

Again, you can either upload the files to the desired service (e.g. App Store) manually or use a tool that will take care of that for you. For the same reasons as before, we prefer to use an existing solution – in this case, AppCenter by Microsoft.

AppCenter is a cloud service with tooling for the automation and deployment of your application. Its biggest advantage is that many of the settings can be configured from the graphical interface. It is much easier to set up the App Store and Play Store deployments this way, rather than working with uploads from the command line.

The same can be achieved with EAS by combining EAS Build to build your app bundles and EAS Submit to automatically upload them to your preferred track on the Google Play Store and TestFlight on App Store Connect.

For the purpose of this section, we will use Fastlane and AppCenter in CircleCI pipelines to fully automate the process of app delivery to the final users. Then, we will dive into the EAS Submit.

Note: Describing the ins and outs of the setup would make this section too long. That’s why we have chosen to refer only to the specific documentation. Our goal is to provide you with an overview, and not a step-by-step guide, since the final config will be different for each project.

# Setting Up Fastlane

Next, you have to run the init command within the React Native project. We will run the fastlane command twice from each native folder. This is because React Native is actually two separate apps at a low level.

As a result, this command will generate setup files in both ios and android folders. The main file in each folder would be called Fastfile and it’s where all the lanes will be configured.

cd ./ios &#x26;&#x26; fastlane init
cd ./android &#x26;&#x26; fastlane init
In the fastlane nomenclature, a lane is just like a workflow – a piece that groups low-level operations that deploy your application.

Low-level operations can be performed by calling actions – predefined fastlane operations that simplify your workflow. We will show you how they function in the next section.

# Setting Up Fastlane on Android

Now that you have successfully set up fastlane in your projects, you are ready to automate the deployment of our Android application. To do so, you can choose an Android specific action – in this case, gradle. As the name suggests, Gradle is an action that allows you to achieve similar results as with Android Gradle used standalone.

Our lane uses the gradle action to first clean the build folder, and then assemble the APK with signature based on passed params.

default_platform(:android)

project_dir = File.expand_path(''..'', Dir.pwd)

platform :android do
lane :build do |options|
if (ENV[''ANDROID_KEYSTORE_PASSWORD''] &#x26;&#x26; ENV[''ANDROID_
KEY_PASSWORD''])
properties = {
''RELEASE*STORE_PASSWORD'' => ENV[''ANDROID_KEYSTORE*
PASSWORD'']
''RELEASE*KEY_PASSWORD'' => ENV[''ANDROID_KEY*
PASSWORD'']
}
end

gradle(
task: ''clean'',
project_dir: project_dir,
properties: properties,
print_command: false
)

gradle(
task: ''assemble'',
build_type: ''Release'',
project_dir: project_dir,
properties: properties,
print_command: false
)
end

Part of the android/fastlane/Fastfile that defines Android lane, named build

You should be able to run a lane build by implementing:

cd ./android &#x26;&#x26; fastlane build

This should produce a signed Android APK.

Note: Don’t forget to set environment variables
to access keystore. These are RELEASE*STORE*
PASSWORD and RELEASE_KEY_PASSWORD and
have been set in the example presented above.

SETTING UP FASTLANE ON IOS

With the Android build being automated, you’re ready to move to iOS now. As we discussed earlier, iOS is a bit more complex due to the certification and provisioning profiles. They were designed by Apple to increase security. Fortunately, fastlane ships with a few dedicated actions that help us overcome these complexities.

You can start with the match action. It helps in managing and distributing iOS certificates and provisioning profiles among your team members. You can read about the idea behind match in the codesigning.

Simply put, match takes care of setting up your device in a way that it can successfully build an application that will be validated and accepted by the Apple servers.

Note: Before you move any further, make sure that your init match for your project. It will generate the required certificates and store them in a central repository where your team and other automation tools can fetch them.

Another action that you could use apart from match is gym. Gym is similar to the Gradle action in a way that it actually performs the build of your application. To do so, it uses the previously fetched certificates and signs settings from match.

default_platform(:ios)

ios_directory = File.expand_path('..', Dir.pwd)
base_path = File.expand_path('..', ios_directory)
ios_workspace_path = '#{ios_directory}/YOUR_WORKSPACE.xcworkspace'
ios_output_dir = File.expand_path('./output', base_path)
ios_app_id = 'com.example'
ios_app_scheme = 'MyScheme'

before_all do
if is_ci? &#x26;&#x26; FastlaneCore::Helper.mac?
setup_circle_ci
end
end

# Part of ios/fastlane/Fastfile where iOS lane is defined

platform :ios do
lane :build do |options|
match(
type: options[:type],
readonly: true,
app_identifier: ios_app_id,
)

cocoapods(podfile: ios_directory)

gym(
configuration: ''Release'',
scheme: ios_app_scheme,
export_method: ''ad-hoc'',
workspace: ios_workspace_path,
output_directory: ios_output_dir,
clean: true,
xcargs: ''-UseModernBuildSystem=NO''
)
end
end

You should be able to run lane build by running the same command as for Android:

cd ./ios &#x26;&#x26; fastlane build
This should produce an iOS application now too.

# DEPLOYING THE BINARIES

Now that you have automated the build, you are able to automate the last part of the process – the deployment itself. To do so, you could use App Center, as discussed earlier in this guide.

Note: You have to create an account in the App Center, apps for Android and iOS in the dashboard and generate access tokens for each one of them. You will also need a special Fastlane plugin that brings an appropriate action to your toolbelt. To do so, run fastlane add_plugin appcenter.

Once you are done with configuring your projects, you are ready to proceed with writing the lane that will package the produced binaries and upload them to the App Center.

# Deploying Your App

lane :deploy do
build

appcenter_upload(
api_token: ENV['APPCENTER_TOKEN'],
owner_name: 'ORGANIZATION_OR_USER_NAME',
owner_type: 'organization', # 'user' or 'organization'
app_name: 'YOUR_APP_NAME',
file: '#{ios_output_dir}/YOUR_WORKSPACE.ipa',
notify_testers: true
)

Part of ios/fastlane/Fastfile with upload lane

That’s it! Now it is time to deploy the app by executing deploy lane from your local machine.

# Integrating with CircleCI

Using all these commands, you are able to build and distribute the app locally. Now, you can configure your CI server so it does the same on every commit to main. To do so, you will use CircleCI – the provider we have been using throughout this guide.

Note: Running Fastlane on CI server usually requires some additional setup. Refer to official documentation to better understand the difference between the settings in local and CI environments.

To deploy an application from CircleCI, you can configure a dedicated workflow that will focus on building and deploying the application. It will contain a single job, called deploy_ios, that will execute our fastlane command.

# Version: 2.1

# Jobs:

# deploy_ios:

- macos:
- xcode: 14.2.0
- working_directory: ~/CI-CD
- steps:
- checkout
- attach_workspace:
- at: ~/CI-CD
- run: npm install
- run: bundle install
- run: cd ios &#x26;&#x26; bundle exec fastlane deploy

# Workflows:

# deploy:

- jobs:
- deploy_ios

Part of CircleCI configuration that executes Fastlane build lane

Pipeline for Android will look quite similar. The main difference would be the executor. Instead of a macOS one, a docker react-native-android Docker image should be used.

Note: This is a sample usage within CircleCI. In your case, it may make more sense to define filters and dependencies on other jobs, to ensure the deploy_ios is run at the right point in time.

You can modify or parametrize the presented lanes to use them for other kinds of deploys, for instance, for the platform-specific App Store. To learn the details of such advanced use cases, get familiar with the official Fastlane documentation.

# EAS Submit

EAS Submit is a hosted service for uploading and submitting your app binaries to the app stores. Unlike with CircleCI or AppCenter you don’t need to go through creating your app signing credentials and signing your builds manually. The EAS CLI eases you through this process and can do it automatically when you run eas build.

# Uploading iOS Apps to App Store Connect with EAS Submit

If needed, you can also manage your signing credentials without creating a build using eas credentials.

In order to use EAS Submit, you will first need to run eas build to create the production .ipa for Apple and .aab for Android. The EAS Build section in the previous chapter explains how to set this up.

Once you have your build .ipa either on your local machine or on EAS, open your terminal and run eas submit. The cli will ask you to either choose a build from EAS or from your local machine, you’ll be prompted to log into your Apple Developer account, and the build will be uploaded to App Store Connect. It usually takes a couple of minutes for it to finish processing and become available on App Store Connect.

~/Code/tutti git:(main)
eas submit
Select platform > iOS
? What would you like to submit? > - Use arrow-keys. Return to submit.
Select a build from EAS
Provide a URL to the app archive
Provide a path to a local app binary file
Provide a build ID to identify a build on EAS

Alternatively you can build and submit your app in one command with eas build –auto-submit.

Using eas submit to upload your app will not make it immediately available on the Apple App Store. It is not possible to upload to the App Store directly. Instead, eas submit will upload your app to TestFlight from which you can choose to either publish it to a test group on TestFlight, or create a release and submit it for App Store review. Only after the app has passed review can it be made available to users on the App Store.

Uploading Android Apps to Google Play with EAS Submit

Before you can use eas submit to automatically upload builds to Google Play, some additional configuration is required.

First you will need to create your Android app on the Google Play console and upload the first build manually. For this, you can use eas build to create the build, download it from EAS and drag and drop the .aab file to the app upload section on Google Play Console.

During this process, you’ll have to fill in all the metadata about your app including adding app screenshots, marketing descriptions, terms and conditions and security and privacy declarations. If you open Dashboard on your Google Play Console, make sure all the items under "Finish setting up your app" are checked off. Then open "Publishing Overview" and ensure all changes have been submitted for approval and approved.

Once that’s done, you’ll need to set up a Google Service account by following this guide. After completing the guide, you should have downloaded the JSON private key for your Google Service account (this is a private key so it should be stored securely and not committed to .git). Add a path to the JSON file under serviceAccountPath in your eas.json:

{
"submit": {
"production": {
"android": {
"serviceAccountPath": "../path/to/api-xyz.json",
"track": "internal"
}
}
}
}

# Automatic Submission

Now you’re all set up to do an automatic submission! For the next build you want to upload, you can run eas submit to submit it automatically, or run eas build –auto-submit to build and submit it in one go.

Google Play builds are uploaded to specific test tracks with "internal" being the lowest. You can upload to a different test track or manually promote the release up from Google Play as it passes each stage of testing.

# Benefits

A SHORT FEEDBACK LOOP ALONG WITH NIGHTLY OR WEEKLY BUILDS LETS YOU VERIFY FEATURES FASTER AND SHIP CRITICAL BUGS MORE OFTEN.

With automated deployment, you no longer waste your time on manual builds and sending the artifacts to test devices or app stores. Your stakeholders are able to verify features faster and shorten the feedback loop even further. With regular builds, you will be able to catch or ship fixes to any critical bugs with ease.

# PART 3

# | CHAPTER 4

# SHIP OTA (OVER-THE-AIR)

# WHEN IN AN EMERGENCY

# SUBMIT CRITICAL UPDATES AND FIXES INSTANTLY THROUGH OTA.

ISSUE: TRADITIONAL WAYS OF UPDATING APPS ARE TOO SLOW AND YOU LOSE YOUR PRECIOUS TIME ON THEM.

The traditional model of sending updates on mobile is fundamentally different from the one we know from writing JavaScript applications for other platforms. Unlike the web, mobile deployment is much more complex and comes with better security out-of-the-box. We have talked about that in detail in the previous section focused on the CI/CD.

# What does it mean for your business?

Every update, no matter how quickly shipped by your developers, is usually going to wait some time while the App Store and Play Store teams review your product against their policies and best practices.

This process is particularly challenging in all Apple platforms, where apps are often taken down or rejected, because of not following certain policies or meeting the required standard for the user interface. Thankfully, the risk of your app being rejected with React Native is reduced to a minimum, as you're working on the JavaScript part of the application. The React Native Core Team ensures that all the changes done to the framework have no impact on the success of your application's submission.

As a result, the submission process takes a while. And if you're about to ship a critical update, every minute counts.

Fortunately, with React Native, it is possible to dynamically ship your JavaScript changes directly to your users, skipping the App Store review process. This technique is often referred to as an over-the-air update. It lets you change the appearance of your

application immediately, for all the users, following the technique that you have selected.

# WHEN CRITICAL BUGS HAPPEN – MINUTES AND HOURS CAN BE CRITICAL. DON'T WAIT TO FIX YOUR END USERS' EXPERIENCE.

If your application is not OTA-ready, you risk it being left with a critical bug on many devices, for as long as Apple/Google reviews your product and allows it to be distributed.

Even though the review times have gotten much better over the years, it is still a good escape hatch to be able to immediately recover from an error that slipped through the testing pipeline and into production.

# SOLUTION: IMPLEMENT OTA UPDATES WITH APP CENTER/ CODEPUSH OR EAS UPDATE

As mentioned earlier, React Native is OTA-ready. It means that its architecture and design choices make such updates possible. However, it doesn't ship with the infrastructure to perform such operations. To do so, you will need to integrate a 3rd-party service that carries its own infrastructure for doing so.

These are the popular ways to implement OTA into your app:

- CodePush: A service that is part of Microsoft's App Center suite.
- EAS Update: A service that is created by Expo and is part of EAS suite.

# APP CENTER/CODEPUSH

# Configuring the native side

To integrate CodePush into your application, please follow the required steps for iOS and Android, respectively. We decided to link to the official guides instead of including the steps here as they include additional native code to apply and that is very likely to change in the coming months.

# CONFIGURING THE JAVASCRIPT SIDE

Once you set up the service on the native side, you can use the JavaScript API to enable the updates and define when they should happen. One of the ways that enable fetching updates on the app startup is to use the codePush wrapper and wrap your main component.

import React from 'react';
import { View } from 'react-native';
import codePush from 'react-native-code-push';

const MyApp = () => &#x3C;View />;

export default codePush(MyApp);

# Basic CodePush integration

That's it! If you have performed all the changes on the native side, your application is now OTA-ready.

For more advanced use cases, you can also change the default settings on when to check for updates and when to download and apply them. For example, you can force CodePush to check for updates every time the app is brought back to the foreground and install updates on the next resume.

The following diagram code snippet demonstrates such a solution:

import React from 'react';
import { View } from 'react-native';
import codePush from 'react-native-code-push';

const MyApp = () => &#x3C;View />;

export default codePush({
updateDialog: true,
checkFrequency: codePush.CheckFrequency.ON_APP_RESUME,
installMode: codePush.InstallMode.ON_NEXT_RESUME,
})(MyApp);

# Custom CodePush setup

# SHIPPING UPDATES TO THE APPLICATION

After configuring CodePush on both JavaScript and the native side of React Native, it is time to launch the update and let your new customers enjoy it. To do so, we can do this from the command line, by using the App Center CLI:

npm install -g appcenter-cli
appcenter login
And then, a release command to bundle React Native assets and files and send them to the cloud:

appcenter codepush release-react -a &#x3C;ownerName>/&#x3C;appName>
Once these steps are complete, all users running your app will receive the update using the experience you configured in the previous section.

Note: Before publishing a new CodePush release, you will have to create an application in the App Center dashboard.

That will give you the ownerName and appName that you're looking for. As said before, you can either do this via UI by visiting App Center, or by using the App Center CLI.

# EAS Update

EAS Update is an EAS service for delivering Over the Air Updates. It provides first-class support for instant updates in React Native applications and is especially user-friendly if you're already using Expo.

It serves updates from the edge with a global CDN and uses modern networking protocols like HTTP/3 for clients that support them. Furthermore, it implements the Expo Updates protocol, which is an open standard specification for instant updates.

# Using EAS Update

As with other Expo products, EAS Update provides a superior Developer Experience, making it a preferred choice for many developers. It also enhances developer workflows with features like:

- Automated Publishing: Integrate with GitHub Actions for automated update publishing.
- Incremental Rollouts: Roll out updates gradually to a selected percentage of users.
- Rollbacks: Ability to rollback any previously published update.
- Asset Selection: Choose which assets to include in an update.
- Custom Update Strategies: Utilize the useUpdates() hook to create tailored update strategies.

# To use EAS Update in your project

To use EAS Update in your project, you'll need to install the eas-cli package and log in to your Expo account using eas login.

Note: To get EAS Update working in your project with the bare React Native workflow, you need to also set up Expo in your project. See the guide to make that work correctly.

# Setting up EAS Update

Start by installing expo-updates library in your project:

npx expo install expo-updates
Next, initialize your project with EAS Update:

eas update:configure
Then, set up the configuration file for builds:

eas build:configure
After running these commands, eas.json is created at the root of your project. Inside it, you will notice that there are two different build profiles (preview and production), each with

# Creating a build

Create a build of your app using EAS Build or another tool of your choice. The new build will include the expo-updates native module, which will be responsible for downloading and launching your updates.

You can set up an internal distribution build using the preview build profile and after the build completes, install it on your device or an emulator or simulator. See Internal distribution for more information.

# Creating an update

After installing the new build on your device, you're ready to send an update to it! Make a small, visible change to the JS of the app. You can also confirm this change by running the development server with npx expo start locally on our machine.

After you've confirmed our changes, let's run the command to create and publish an update with EAS Update:

eas update --branch preview --message “Fixed a bug.”

This command creates an update. You can view this in our EAS project's dashboard:

| Updates                     | 890e0211 |                 |           |                           |                      |                      |
| --------------------------- | -------- | --------------- | --------- | ------------------------- | -------------------- | -------------------- |
| Update: Update text message |          |                 |           |                           |                      |                      |
| Group ID                    | Branch   | Runtime version | Commit    | Created by                | Created at           | Updated at           |
| 890e02f10                   | preview  | 1.0.0           | 326501b\* | Aman Mittal (amanhimself) | Jan 19, 2024 6:39 PM | Jan 19, 2024 6:39 PM |

# Platform-specific updates

| Platform | ID                                   | Actions |
| -------- | ------------------------------------ | ------- |
| Android  | be4fe266-a452-466e-b50e-9a1f5a32dbda | Preview |
| ios      | 9r666880-277e-4804-ae32-29b6eebe846d | Preview |

Each update contains details about the branch that is linked to the build profile, the commit, and information about platform-specific (Android and iOS) details. See the conceptual overview of how EAS Update works for more information.

# Running an update

After this step is completed, all users running our app will receive an update with the changes. By default, expo-updates checks for the updates in the background when the app launches. When testing with an internal distribution, to see the update in the app you'll need to force close and reopen the app up to two times to see the changes.

You can expand on the default functionality and implement your own strategy using the useUpdates() hook from expo-updates, which allows you to:

- Fetch information on available updates
- Fetch information available on currently running updates
- Check for changes manually using Updates.checkForUpdateAsync()
- Download and run updates using Updates.fetchUpdateAsync()

EAS Update can be extremely useful for deploying changes to production and is equally beneficial during the development phase. It offers a convenient and rapid method for sharing your work with team members.

# BENEFITS: SHIP CRITICAL FIXES AND SOME CONTENT INSTANTLY TO THE USERS.

With OTA updates integrated into your application, you can send your JavaScript updates to all your users in a matter of minutes. This possibility may be crucial for fixing significant bugs or sending instant patches.

For example, it may happen that your backend will stop working and it causes a crash at startup. It may be a mishandled error – you

never had a backend failure during the development and forgot to handle such edge cases.

You can fix the problem by displaying a fallback message and informing users about the problem. While the development will take you around one hour, the actual update and review process can take hours if not days. With OTA updates set up, you can react to this in minutes without risking the bad UX that will affect the majority of users.

# PART 3

# | CHAPTER 5

# MAKE YOUR APP CONSISTENTLY FAST

# USE THE DMAIC PROCESS TO HELP YOU PREVENT REGRESSING ON APP PERFORMANCE

ISSUE: EVERY ONCE IN A WHILE AFTER FIXING A PERFORMANCE ISSUE, THE APP GETS SLOW AGAIN.

Customers have very little patience for slow apps. There is so much competition on the market that customers can quickly switch to another app. According to the Unbounce report, nearly 70% of consumers admit that page speed influences their willingness to buy. Good examples here are Walmart and Amazon – both of these companies noticed an increase in revenue by up to 1% for every 100 milliseconds of load time improvement. The performance of websites and mobile apps can thus noticeably impact businesses' performance.

It's becoming increasingly important to not only fix performance issues but also make sure they don't happen again. You want your React Native app to perform well and fast at all times.

SOLUTION: USE THE DMAIC METHODOLOGY TO HELP YOU SOLVE PERFORMANCE ISSUES CONSISTENTLY.

From the technical perspective, we should begin by avoiding any guesswork and base all decisions on data. Poor assumptions lead to false results. We should also remember that improving performance is a process, so it's impossible to fix everything at once. Small steps can provide big results.

This all leads us to the fact that developing an app is a process. There are some interactions that lead to results. And, what is most important, the processes can be optimized.

# One of the most effective ways of doing that is using the DMAIC methodology.

It's very data-driven and well-structured and can be used to improve React Native apps. The acronym stands for Define, Measure, Analyze, Improve, and Control. Let's see how we can apply each phase in our apps.

# Define

In this phase, we should focus on defining the problem, what we want to achieve, opportunities for improvement, etc. It's important to listen to the customer's voice in this phase – their expectations and feedback. It helps to better understand the needs and preferences and what problems they are facing. Next, it is very important to measure it somehow. Let's say the customer wants a fast checkout. After analyzing the components, we know that to achieve this we need a swift checkout process, a short wait time, and smooth animations and transitions. All of these points can be decomposed into CTQ (Critical-to-Quality) that are measurable and can be tracked. For example, a short wait time can be decomposed into a quick server response and a low number of server errors.

Another handy tool is analyzing common user paths. With good tracking, we can analyze and understand what parts of the app are mostly used by the users.

In this phase, it's very important to choose priorities. It should end up with defining the order in which we will optimize things. Any tools and techniques for prioritizing will definitely help here.

Ultimately, we need to define where we want to go – we should define our goals and what exactly we want to achieve. Keep in mind that it all should be measurable! It's a good practice to put these goals in the project scope.

# Measure

Since we already know where we want to go, it's time to assess the starting point. It's all about collecting as much data as possible to get the actual picture of the problem. We need to ensure the measurement process is precise. It's really helpful to create

# Profiling in React Native

A data collection plan and engage the development team to build the metrics. After that, it's time to do some profiling.

When profiling in React Native, the main question is whether to do this on JavaScript or the native side. It heavily depends on the architecture of the app, but most of the time it's a mix of both.

One of the most popular tools is React Profiler, which allows us to wrap a component to measure the render time and the number of renders. It's very helpful because many performance issues come from unnecessary rerenders. Discover how to use it here:

import React, { Profiler } from 'react';
import { View } from 'react-native';

const Component = () => (
console.log(args)}>
<view>
</view></profiler>
);

export default Component;

# Using React Profiler API

It will output the data:

{
id: 'Component',
phase: 'mount',
actualDuration: 1.3352311453,
baseDuration: 0.95232323318,
...
}

# Output of the React Profiler API

The second tool is a library created by Shopify – react-native-performance. It allows you to place some markers in the code and measure the execution time. There is also a pretty nice Flipper plugin that helps to visualize the output:

# Performance Measurement in React Native

Speaking of Flipper, it has some more plugins that help us to measure the app performance and speed up the development process. We can use, e.g. React Native Performance Monitor Plugin for a Lighthouse-like experience or React Native Performance Lists Profiler Plugin.

On the native side, the most common method is using Native IDEs – Xcode and Android Studio. There are plenty of useful insights which can be analyzed and lead to some conclusions and results.

The most important aspect of this phase is measurement variation. Due to different environments, we have to be very careful when profiling. Even if the app is run on the same device, there might

| Blank spaces | 1000 |
| ------------ | ---- |
|              | 750  |
|              | 500  |
|              | 250  |
|              | 0    |

| Blank space averages | 1207 |
| -------------------- | ---- |
|                      | 90   |
|                      | 60   |
|                      | 30   |
|                      | 0    |

Twitter

TwitterFlatList

https://shopify.github.io/react-native-performance/docs/guides/flipper-react-native-performance

# Analyze

The goal of this phase is to find the root cause of our problem. It's a good idea to start with a list of things that could potentially cause the problem. A little brainstorming with a team is really helpful here.

One of the most popular tools to define a problem is called a cause and effect diagram. It looks like a fish and we should draw it from right to left. We start from the head and it should contain the problem statement – at this stage, we should already have it based on the Define phase. Then, we identify all the potential major causes of the problem and assign them to the fish bones. After that, we assign all the potential causes to each major cause. There are many things that could have an impact on performance. The list could get really long, so it's important to narrow it down. Outline the most important factors and focus on them.

Finally, it's time to test the hypothesis. For example, if the main problem is low FPS, and the potential major cause is related to list rendering, we can think of some improvements in the area of images in the list items. We need to design a test that will help us accept or reject the hypothesis – it will probably be some kind of proof of concept. Next, we interpret the results and decide if it was improved or not. Then we make a final decision.

# Cause and effect diagram example

# Improve

Now we know what our goal is and how we want to achieve it, it's time to make some improvements. This is the phase where optimization techniques start to make sense.

Before starting, it's a good idea to have the next brainstorming session and identify potential solutions. Depending on the root cause, there might be a lot of them. Based on the last example with images on the list item, we can think about implementing proper image caching and reducing unnecessary renders.

After outlining the solutions, it's time to pick the best one. Sometimes the solution that gives the best effects might be extremely costly, e.g. when it's necessary to make some architectural changes.

It's then time to implement the solution. After that, it's required to properly test it and we are done!

# Control

The last step is the control phase. We need to make sure that everything works well now. The performance will degrade if it is not under control. People tend to blame devices, the used technology, or even users when it comes to bad performance. So what do we need to do to keep our performance on a high level?

We need to make sure that we have a control plan. We can use some of our work from the previous phases to make it. We should point out focal points, some measurement characteristics, acceptable ranges for indicators, and testing frequency. Additionally, it is a good practice to write down some procedures and what to do if we spot issues.

The most important aspect of the control phase is monitoring regressions. Until recently it was quite difficult to do that in React Native, but now we have plenty of options to improve our monitoring.

# Real-time user monitoring

One way to keep the performance improvements we introduce in our apps is through real-time monitoring tools. Such as Firebase Performance Monitoring, which is a service that gives us some insights into performance issues in production. Or Sentry Performance Monitoring, which tracks application performance, collects metrics like throughput and latency, and displays the impact of errors across multiple services.

It's a great addition to any app builders that want to have insights on how the performance is distributed across all the devices that install their apps. Based on real user data.

# TESTING REGRESSIONS AS A PART OF THE DEVELOPMENT PROCESS

Another way to keep performance regressions under control is through automated testing. Profiling, measuring, and running on various devices is quite manual and time-consuming. That's why developers avoid doing it. However, it gets too easy to unintentionally introduce performance regressions that would only get caught during QA, or worse, by your users. Thankfully, we have a way to write automated performance regression tests in JavaScript for React and React Native.

Reassure allows you to automate React Native app performance regression testing on CI or a local machine. In the same way you write your integration and unit tests that automatically verify that your app is still working correctly, you can write performance tests that verify that your app is still working performantly. You can think about it as a React performance testing library. In fact, Reassure is designed to reuse as much of your React Native Testing Library tests and setup as possible. As it's designed by its maintainers and creators.

It works by measuring certain characteristics – render duration and render count – of the testing scenario you provide and comparing that to the stable version measured beforehand. It repeats the scenario multiple times to reduce the impact of random variations in render times caused by the runtime environment. Then it applies a statistical analysis to figure out whether the code

changes are statistically significant or not. As a result, it generates a human-readable report summarizing the results and displays it on CI or as a comment to your pull request.

# The simplest test you can write would look something like this:

import React from 'react';
import { View } from 'react-native';
import { measurePerformance } from 'reassure';

const Component = () => {
return &#x3C;View />;
};

test('mounts Component', async () => {
await measurePerformance(&#x3C;Component />);
});

Code: Component.perf-test.tsx

This test will measure the render times of Component during mounting and the resulting sync effects. Let's take a look at a more complex example though. Here we have a component that has a counter and a slow list component:

import React from 'react';
import { Pressable, Text, View } from 'react-native';
import { SlowList } from './SlowList';

const AsyncComponent = () => {
const [count, setCount] = React.useState(0);

const handlePress = () => {
setTimeout(() => setCount((c) => c + 1), 10);
};

return (
&#x3C;View>
&#x3C;Pressable accessibilityRole=''button'' onPress={handlePress}>
&#x3C;Text>Action&#x3C;/Text>
&#x3C;/Pressable>

&#x3C;Text>Count: {count}&#x3C;/Text>

&#x3C;SlowList count={200} />
&#x3C;/View>
);
};

And the performance test looks as follows:

import React from 'react';
import { screen, fireEvent } from '@testing-library/react-native';
import { measurePerformance } from 'reassure';
import { AsyncComponent } from '../AsyncComponent';

test('AsyncComponent', async () => {
const scenario = async () => {
const button = screen.getByText('Action');

fireEvent.press(button);
await screen.findByText('Count: 1');

fireEvent.press(button);
await screen.findByText('Count: 2');

fireEvent.press(button);
fireEvent.press(button);
fireEvent.press(button);
await screen.findByText('Count: 5');
};

await measurePerformance(<asynccomponent>, { scenario });
});
</asynccomponent>

When run through its CLI, Reassure will generate a performance comparison report. It's important to note that to get a diff of measurements, we need to run it twice. The first time with a --baseline flag, which collects the measurements under the .reassure/ directory.

Running performance tests:

Baseline: main (16b3893c0592236c55708a03302265136ba344d2)

PASS src/AsyncComponent.perf-test.tsx
AsyncComponent (2982 ms)

Test Suites: 1 passed, 1 total
Tests: 1 passed, 1 total
Snapshots: 0 total
Time: 4.769 s, estimated 5 s
Ran all test suites.

Written Baseline performance measurements to .reassure/baseline.perf

After running this command, we can start optimizing our code and see how it affects the performance of our component. Normally, we would keep the baseline measurement and wait for performance.

regressions to be caught and reported by Reassure. In this case, we'll skip that step and jump straight into optimizing, because we just noticed a nice possibility to do so. And since we have our baseline measurement for reference, we can actually verify our assumptions and whether the improvement was real or only subjective.

The possibility we noticed is that the &#x3C;SlowList/> component can be memoized, as it doesn't depend on any external variables. We can leverage useMemo for that case:

const slowList = useMemo(() => &#x3C;SlowList count={200} />, []);
Once we're done, we can run Reassure a second time. Now without the --baseline flag.

# Performance comparison results:

Current: main (16b3893c0592236c55708a03302265136ba344d2)

Baseline: main (16b3893c0592236c55708a03302265136ba344d2)

| Significant changes to render duration |                                      |
| -------------------------------------- | ------------------------------------ |
| AsyncComponent:                        | 78.4 ms → 26.3 ms (-52.1 ms, -66.5%) |
| Meaningless changes to render duration |                                      |
| Render count changes                   |                                      |
| Added scenarios                        |                                      |
| Removed scenarios                      |                                      |

# Performance comparison report from Reassure

Now that Reassure has two test runs to compare – the current and the baseline – it can prepare a performance comparison report. As you can notice, thanks to applying memoization to the SlowList component rendered by AsyncComponent, the render duration went from 78.4 ms to 26.3 ms, which is roughly a 66% performance improvement.

Test results are assigned to certain categories:

- Significant Changes To Render Duration shows a test scenario where the change is statistically significant and should be looked into as it marks a potential performance loss/improvement.

# Performance Comparison Report

Current: main (16b3893c0592236c55708a03302265136ba344d2)

Baseline: main (16b3893c0592236c55708a03302265136ba344d2)

# Significant Changes To Render Duration

There are no entries

# Meaningless Changes To Render Duration

Show entries

| Name        | Render Duration                    | Render Count |
| ----------- | ---------------------------------- | ------------ |
| Simple Test | 0.3 ms → 0.0 ms (-0.3 ms, -100.0%) | 1            |

Show details

# Changes To Render Count

There are no entries

# Added Scenarios

There are no entries

# Removed Scenarios

There are no entries

Report generated by Reassure with Danger JS

# Benefits: A Well-Structured and Organized Optimization Process

When working on an app, regardless of its size, it's important to have a clear path for reaching our goals. The main benefit of using DMAIC when optimizing React Native applications is a structured and direct approach. Without it, it may be difficult to verify what works (and why). Sometimes our experience and intuition are just enough. But that's not always the case.

Having a process like this allows us to focus on problem-solving and constantly increase productivity. Thanks to the DMAIC approach, performance optimization becomes a part of your normal development workflow. Making your app closer to being performant by default. Spotting the performance issues even before they hit your users.

No software is flawless. Bugs and performance issues will happen even if you're the most experienced developer on the team. But we can take action to mitigate those risks by using automated tools like Sentry, Firebase, or Reassure. Use them in your project and enjoy the additional confidence they bring to your projects. And the improved UX they bring to your users in turn.

“Performance regression monitoring is a critical process in the development and maintenance of mobile apps. Without it, small issues can go unnoticed and lead to significant performance degradation, negatively impacting the user experience and potentially decreasing user retention. Regular performance regression monitoring allows developers to proactively identify and fix issues before they become a problem for users, ensuring the app runs at optimal performance and providing a better experience for all users.”

Michał Chudziak – Independent Consultant @michalchudziak.dev

# PART 3

# | CHAPTER 6

# KNOW HOW TO PROFILE IOS

30

# IMPROVE YOUR APP WITH REAL-TIME METRICS

ISSUE: IT TAKES TOO MUCH TIME TO SEE THE RESULT OF AN ACTION.

Profiling is essential to understanding the runtime performance of the app, through analysis that measures the memory or time complexity, frequency, and duration of function calls, etc. Getting all this information helps you to track down and provide proper solutions to keep your app healthy and your users engaged.

Xcode provides some basic tools to do the first report. You can monitor the CPU, Memory, and Network.

| cardColorTodo PID.. | CPU  | Memory   | Disk      | Network     |
| ------------------- | ---- | -------- | --------- | ----------- |
|                     | 101% | 120,4 MB | Zero KB/s | 230 bytes/s |

CPU Monitor measures the amount of work done. Memory Monitor is for observing the use of the app. All iOS devices use SSD for permanent storage, accessing this data is slower compared to RAM. Disk Monitor is for understanding your app’s disk-writing performance. Network Monitor analyzes your iOS app’s TCP/IP and UDP/IP connections.

You can tap on each of them to find more information.

It also provides an extra monitor that isn’t shown by default but can help you inspect your UI – it’s the View Hierarchy.

When the app is running and you are on the screen you want to inspect, click on Debug View Hierarchy.

# 10

cardColorTodo

This will show your current UI in a 2D/3D model and the view tree.

| **cardColorTodo** | CPU     | 3%        |
| ----------------- | ------- | --------- |
|                   | Memory  | 128,3 MB  |
|                   | Disk    | Zero KB/s |
|                   | Network | Zero KB/s |

UWindowScene Foreground Active

- UIWindow
- UlTransitionView
- UIDropShadowView
- UIViewController
- RCTRootView
- RCTRootContentView - M Test 1 0 Test 2 0 Test 3 0
- RCTView -M M Test 1 0 Test 2 0 Test 3 0 Test 4 .
- RCTView - Test 1 0 Test 2 0 Test 30 Test 4 0.
- RNCSafeAreaProvider - Test 1 0 Test 2 0 Test..
- RCTView - Test 1 0 Test 2 0 Test 3 0 Tes.
- RCTView - MM MTest 1 0 Test 2 0 Test 3 0 T
- RCTView M Test 1 0 Test 2 0 Test 30.
- RCTView - M
- RCTView - []
- RCTVieW -
- RCTView - M
- RCTView - ]
- RCTTextView -
- RCTView - []
- RCTVieW -
- RCTViewTest 1 0 Test 2 0 Test 3 0 Te
- RCTView - Test 1 0 Test 2 0 Test 3 0
- RCTView Test 1 0 Test 2 0 Test 3 0..
- RCTView -] Test 1 0 Test 2 0 ] Test 3 0.
- RCTView Test 1 0 Test 2 0 Test 3 ..
- RCTView Test 1 0 Test 2 0 Tes.
- RCTScrollViewTest 1 0 Test 2 0..
- RCTCustomScrolIView 88
- RCTScrolContentView - [] Test 1 0. H 0
- RCTView - Test 1 0 3 8 candColorTodo Thread 1)
- RCTViewTest 2 0
- RCTView Test 3 0
- RCTView Test 4 0
- 'operationTimestamos'
- RCTView Test 4 0
- RCTView - Test 4 0
- RCTView Test 4 0
- RCTView -

This will help you to detect overlappings (you can’t see a component) or if you want to flatten your component tree. Even though RN does a view flattening it sometimes can’t do it with all of them, so here we can do some optimization focusing on specific items.

Focused

- RCTView - 7] Test 4 0
- RCTView - Test 4 0
- RCTView -Test 4 0
- RCTView -
- RCTView -
- RCTTextView - 114
- RCTTextView - Test 4
- RCTView
- RCTTextView - 0

Let’s say we have a TODO list app, and when the Add button is pressed, it adds the new item to the list. However, it takes a couple of seconds to show up on the list because there is some logic

# IOS INSTRUMENTS

Instruments is a debugging and profiling tool that comes pre-packaged with xCode, and is literally a box of tools, each of them serving a different purpose. You choose from a list of templates, and you choose any of them depending on your goal: improving performance or battery life or fixing a memory problem.

We are going to use Time Profiler. Let’s dive into it. With xCode open, we go to Open Developer Tool – > Instruments. Then, scroll down to find the Time Profiler tool.

| All              | Standard          | User         | Recent             | Filter        |
| ---------------- | ----------------- | ------------ | ------------------ | ------------- |
| 0                |                   |              |                    |               |
| Core ML          | CPU Counters      | CPU Profiler | File Activity      | Game Memory   |
| Game Performance | Leaks             | Logging      | Metal System Trace | Network       |
| SceneKit         | Swift Concurrency | SwiftUI      | System Trace       | Time Profiler |

# Time Profiler

Performs low-overhead time-based sampling of processes running on the system's CPUs.

It will open a new window. To start profiling your app, click on the dropdown menu and select your device and the app.

iPhone 14 (16.1) cardColorTodo

When the app opens, start using it normally, or in this case, add a new TODO item.

# CPU Usage

# Process 63339

| Weight  | Self Weight | Symbol Name                                 | Heaviest Stack |
| ------- | ----------- | ------------------------------------------- | -------------- |
| 15.04 s | 100.0%      | cardColorTodo (63339)                       | 15043          |
| 15.04 s | 99.9%       | >\_NSThread\_\_start_Ox188e47 +             | 15035          |
| 6.00 ms | 0.0%        | > Main Thread Ox188db5                      | 15035          |
| 2.00 ms | 0.0%        | >\_dispatch_workloop_worker_thread Ox188e44 |                |

After playing around and adding the new TODO item, we can see there is a big blue rectangle, which means there is something that is taking a lot of time to finish. Let’s take a look at the threads.

| Weight    | Self Weight | Symbol Name         |
| --------- | ----------- | ------------------- |
| 15.02 s   | 99.8%       | Ox103a0bb9c hermes  |
| 15.02 s   | 99.8%       | Ox103a0bc44 hermes  |
| 15.02 s   | 99.8%       | Ox1039ed9b4 hermes  |
| 15.02 s   | 99.8%       | Ox103abe428 hermes  |
| 15.02 s   | 99.8%       | Ox1039ec088 hermes  |
| 15.02 s   | 99.8%       | −Ox1039edcd0 hermes |
| 15.02 s   | 99.8%       | vOx103a0bb9c hermes |
| 15.02 s   | 99.8%       | vOx103a0bc44 hermes |
| 11.41 s   | 75.8%       | Ox103a0bc44 hermes  |
| 2.26 s    | 15.0%       | Ox103a1931c hermes  |
| 1.00 s    | 6.6%        | Ox103a4f5d4 hermes  |
| 342.00 ms | 2.2%        | Ox103a45078 hermes  |
| 1.00 ms   |             | Ox1039ed30c hermes  |

You can expand by pressing option+click over the chevron, which will expand to display useful information. At least for now it is showing the memory address, but we will need to find another way to find where the problem is.

# SOLUTION: COMBINING WITH A TOOL SPECIFIC FOR JS CONTEXT TRACKING.

Let’s use Flipper, the same one that we used in Pay Attention to UI re-renders, but we are going to use another monitor called Hermes Debugger (RN). With the app open and running, we go to Flipper, select the running app if not selected already, and go to Hermes Debugger (RN) –> Profiler

# APP INSPECT

Console Sources Memory Profiler

cardColorTodo

React Native

Profiles

Record JavaScript CPU Profile

CPU profiles show where the execution time is spent in your page's JavaScript functions.

Select JavaScript VM instance

PLUGINS

6.2 MB (empty)

Device 2

React Native 3

c/> Hermes Debugger (RN)

Logs

React DevTools

Disabled

Unavailable plugins 12

We click Start so the profiler begins. We do the same flow and actions as before when profiling with Time Profiler. When we Stop, we will see all the data collected.

| Profiles          | Self Time              | Total Time                                                                            | Function                                                                             |
| ----------------- | ---------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| CPU PROFILES      | 3776.3 ms 50.04 %      | 4024.5 ms 50.94 %                                                                     | doFib(http\://localhost:8081/index.bundle?platform=ios\&dev=true\&minify=false\&mod. |
| 7018.1 ms 25.49 % | 7159.9 ms 26.01 %      | doFib(http\://localhost:8081/index.bundle?platform=ios\&dev=true\&minify=false\&mo... |                                                                                      |
| Profile 1         | Save 6758.2 ms 24.55 % | 6864.5 ms 24.94 %                                                                     | doFib(http\:/localhost:8081/index.bundle?platform=ios\&dev=true\&minify=false\&mo... |
|                   | 248.1 ms 0.90 %        | 248.1 ms 0.90 %                                                                       | \[GC Young Gen]                                                                      |
|                   | 11.8 ms 0.04 %         | 11.8 ms 0.04 %                                                                        | callReactNativeMicrotasks(http\:/localhost:8081/index.bundle?platform=ios\&dev=tru.. |
|                   | 11.8 ms 0.04 %         | 11.8 ms 0.04 %                                                                        | onResponderGrant(http\:/localhost:8081/index.bundle?platform=ios\&dev=true\&minif..  |

By default the data will be sorted bottom-up with the heavy tasks at the top. We can see that a function called doFib is taking ~14 sec to complete, it is a good start, let’s go into that function and see what we can do. The fixes will vary depending on your code.

After applying a possible fix, we first check Time Profiler again. We click on the record button and start using the app, in our case let’s add a new TODO item.

| Weight    | Self Weight | Symbol Name        |
| --------- | ----------- | ------------------ |
| 161.00 ms | 84.7%       | US                 |
| 161.00 ms | 84.7%       | 0s                 |
| 160.00 ms | 84.2%       | Os 2               |
| 141.00 ms | 74.2%       | Os +               |
| 141.00 ms | 74.2%       | Os                 |
| 141.00 ms | 74.2%       | Os                 |
| 141.00 ms | 74.2%       | Ox104017c44 hermes |
| 67.00 ms  | 35.2%       | 0s                 |
| 32.00 ms  | 16.8%       | 29.00 ms           |
| 7.00 ms   | 3.6%        | Os                 |

As we can see, the fix we applied did work, we aren’t seeing the big blue rectangle like before. This is a good sign. Let’s continue with our profiling path to check how it looks in Flipper.

Start profiling the app one more time using Hermes Debugger (RN) –> Profiler.

| Heavy (Bottom Up) | ox       |            |          |                  |                                                                                                                                                                              |
| ----------------- | -------- | ---------- | -------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Profies           | 102.4 ms | Total Time | Function |                  |                                                                                                                                                                              |
| CPU PROFILES      | 85.3 ms  | 0.54 %     | 102.4 ms | 0.54 %           | FiberNodehttp/locahost:Bc81/ndex.bunde?platformicstdevtrue\&minifyfalse\&modulesOnly-falsedrunModule=truedapporg.reactjs.native.example.cardColorTodo:159..                  |
|                   | 0.45 %   | 85.3 ms    | 0.45 %   | \[Host Function] |                                                                                                                                                                              |
| IT Profile 1Save  | 68.2 ms  | 0.36%      | 68.2 ms  | 0.36 %           | >metroRequire2httpu/localhost:8o81/index.bundie?platform=ios\&dev=true\&eminify=false\&modulesOnly=false\&runModule=true\&app=org.reactjs.native.example.cardColorTodoc6...  |
|                   | 51.2 ms  | 0.27 %     | 51.2 ms  | 0.27 %           | >reconcileChiidFibersehttp\:/focalhost:Bo8t/index.bundie?platform-ios\&dev-truedminity-false\&modulesOnfly>-false\&runModule-trueBapp-org.reactjs.native.example.cardColor.. |
|                   | 34.1 ms  | 0.18 %     | 34.1 ms  | 0.18 %           | gnWorkhtp/ocaos808/index.und?platfios\&deue\&inyfasedmoduesOnlfalsednModuleuedapor.eacativ.example.cardColorTod:                                                             |
|                   | 34.1 ms  | 0.18 %     | 34.1 ms  | 0.18 %           | >mergeLanesthttpu/fiocalhost:B081/index.bundie?platform=los\&dev=true\&minity=falsedmodulesOnly=false\&runModule=truedapp=org.reactjs.native.example.cardColorTodo:54...     |
|                   | 34.1 ms  | 0.18 %     | 34.1 ms  | 0.18 %           | \[GC Young Gen]                                                                                                                                                              |
|                   | 34.1 ms  | 0.18 %     | 34.1 ms  | 0.18 %           | Wrkdnrogt/ocB0/nd.lasdasOnaMuoractexle.Co                                                                                                                                    |
|                   | 34.1 ms  | 0.18 %     | 34.1 ms  | 0.18 %           | >validatehttp/focalhost:8081/ndex.bunde?platfor-los\&dev=true\&minifyfalse\&modulesOnlyfaledirunModule-truedapp-org.reacts.natve.example.cardColorTodo98460:7)               |
|                   | 34.1 ms  | 0.18 %     | 34.1 ms  | 0.18 %           | 0/asi.C                                                                                                                                                                      |
|                   | 17.1 ms  | 0.09 %     | 17.1 ms  | 0.00 %           | >workLooeSynohmoc//local etso81/ndex.bundle?plaeformaliosBdevwtruelminifyafalselmodulesOnly=false\&runModuleutrue\&anpworg.resctis.native.example.cardiColorTodo:            |

We don’t see the doFib function anymore, only other expected RN tasks.

# Introduction to Prewarming in iOS 15

Prewarming, introduced in iOS 15, impacts the user experience by minimizing the delay before an app becomes operational. This process launches inactive application processes ahead of time, enabling the system to construct and cache vital low-level structures for a swift full launch. It transforms traditional notions of startup time measurement, as it may activate processes well before the user actually opens the app. For instance, if a user habitually starts an app every day at 8 am, iOS might preemptively initiate certain processes around 7:50 am to align with the user’s anticipated behavior.

# Early Stages of App Launch

Prior to the execution of the app’s main function and +applicationDidFinishLaunching, iOS undertakes considerable preparatory work. This involves initializing dynamic libraries (dylibs), executing +load methods, and more, a process that could extend beyond a second. Grasping this procedure is essential for developers focused on optimizing their app’s launch efficiency.

# Prewarming Mechanics

During prewarming, the app’s launch sequence remains suspended either until a complete app launch is initiated or when the system, needing to free up resources, removes the prewarmed app.

# Special Handling for iOS 15’s Prewarming

With the advent of iOS 15, initializers and other preparatory steps can be executed hours ahead of the actual app startup. Developers must, therefore, account for the interval between the commencement of the process in the pre-main initializer and the subsequent post-main period. Otherwise, they may notice a lot of very high numbers in their monitoring tools.

# Distinguishing Prewarming in Objective-C and Swift

Developers can utilize the ProcessInfo environment variable to ascertain whether prewarming has occurred. This helps tailor the app’s behavior based on the prewarming status. Following snippets enable developers to detect if the app was launched through prewarming and adjust their startup measurements accordingly.

if ([[[NSProcessInfo processInfo] environment]
[@''ActivePrewarm''] isEqual:@''1'']) {
// Handle prewarmed app launch scenario
} else {
// Handle regular app launch scenario
}
Code snippet: example in Objective-C

if ProcessInfo.processInfo.environment[''ActivePrewarm''] ==
''1'' {
// Handle prewarmed app launch scenario
} else {
// Handle regular app launch scenario
}
Code snippet: example in Swift

# BENEFITS: HAVING A FASTER AND MORE RESPONSIVE APP.

70% of the users will leave the app if the response to a given action takes too long. Profiling our apps has become one of the main steps in our development life cycle. Using specific tools like Time Profiler will help us understand if our app is responding fast or where we could find areas of improvement. Remember, users are becoming more sensitive to speed and delays, even a 0.1 sec of improvement can increase a conversion rate by 10.1%.

# PART 3

# | CHAPTER 7

# KNOW HOW TO

# PROFILE ANDROID

# GET REAL-TIME METRICS TO BETTER YOUR APP UNDERSTANDING

# ISSUE: YOU ENCOUNTER A PERFORMANCE ISSUE THAT COMES DIRECTLY FROM ANDROID RUNTIME.

In the event of any performance issues, we mostly use React Profiler to troubleshoot and resolve our problems. Since most of the performance problems originate from the JS realm, we don’t usually need to do anything beyond that. But sometimes we’ll encounter a bug or performance issue that comes directly from the Android runtime. In such a case, we’ll need a fine tool to help us gather the following metrics from the device:

- CPU
- memory
- network
- battery usage

Based on that data, we can check whether our app consumes more energy than usual or in some cases, uses more CPU power than it should. It is useful especially to check the executed code on lower-end (LE) Android devices. Some algorithms can run faster on some devices and the end user will not spot any glitches, but we have to remember, some customers can use LE devices and the algorithm or function can be too heavy for their phones. High-end devices will handle it because their hardware is powerful.

# SOLUTION: PROFILE YOUR APP WITH ANDROID PROFILER IN ANDROID STUDIO

# Android Profiler in Android Studio

Android Studio is the IDE developed by JetBrains. It is officially supported by Google and the official IDE, which can be used to develop any Android app. It is very powerful and contains lots of functionalities in one place. One of those tools is Android Profiler.

# Profiler in Android Studio

If you have not installed Android Studio yet, you can install it using this link.

To open the Profiler, choose View > Tool Windows > Profiler from the Android Studio menu bar:

View Navigate Code Refactor Build Run Tools

Tool Windows Project # 1
Appearance Favorites #2

Quick Definition Space QFind # 3
Show Siblings Run #4
Quick Debug # 5
Type Definition Problems # 6

Recent Files HE Structure # 7
Recently Changed Files Services #8
Recent Locations HE P Version Control # 9
Recent Changes TC □ Emulator

Compare with Clipboard a Profiler
AppInspection
Quick Switch Scheme.. Build

Bidi Text Base Direction Build Variants
Device File Explorer

Or click Profile in the toolbar.

app Pixel 5 API 32

Profile'app

Before you start profiling the app, please remember:

- Run the app on a real Android device that is affected, preferably a lower-end phone or emulator if you don’t have one. If your app has runtime monitoring set up, use a model that is either the most used by users or the one that’s affected by a particular issue.

# Performance

• Turn off development mode. You must be sure that the app uses a JS bundle instead of the metro server, which provides that bundle. To turn it off, please share your device, click on Settings and find JS Dev Mode:

# JS Dev Mode

Load JavaScript bundle with \__DEV_ = true for easier debugging. Disable for performance testing. Reload for the change to take effect.

After that, go to the Profiler tab and add a new profiler session:

| Profiler                                                         | com.pagerviewexample (Motorola Moto X4) |
| ---------------------------------------------------------------- | --------------------------------------- |
| SESSIONS                                                         | +                                       |
| Timing data from debuggable processes will deviate significantly |                                         |
| 12:41                                                            | Load from file...                       |
| pagerviewexample (M                                              | Motorola Moto X4                        |
| com.pagerviewexample (13925) (debuggable)                        | 26 sec                                  |
| CPU                                                              | No other debuggable processes           |
| 100 % No other profileable processes                             |                                         |

Wait for the session to attach to your app and start performing actions that could cause some performance issues, like swiping, scrolling, navigating, etc. Once you’re done, you should see some metrics like these:

# Profile

| SESSIONS                    | Timing data from debuggable processes will deviate significantly from real world performance. A profileable process may |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 12:41                       | pegervie                                                                                                                |
| MEMORY                      | 219.9 MB                                                                                                                |
| Network Profiler has moved. | ENERGY                                                                                                                  |
| 25.000                      |                                                                                                                         |

Each greenfield React Native app has only one Android Activity. If your app has more than one, it’s most likely a brownfield one. Read more about the brownfield approach here. In the above example,

we don’t see anything interesting. Everything works fine without any glitches. Let’s check each metric:

- The CPU metric is strictly correlated to energy consumption because the CPU needs more energy to do some computations.
- The memory metric is not changing while using the app, which is expected. Memory usage can grow, e.g. when opening new screens, and drop when the garbage collector (GC) releases free memory, e.g. when navigating out of a screen. When memory increases unexpectedly and keeps on growing, it may indicate a memory leak, which we want to avoid, as it can crash the app with out of memory (OOM) errors.
- The network section has been moved to a separate tool called the Network Tab. In most cases, this metric is not needed, because it is mostly related to the backend infrastructure. If you would like to profile a network connection, you can find more information here.
- The energy section gives hints on when our app’s energy usage is low, medium, or high, impacting the daily experience of using the app.

# USE ANDROID PROFILER IN ACTION

In the previous example, we could see some relations between each metric:

20000

6182100213

Su 2010an

Too B Pnss

00812:12

To see a more detailed view, we have to double-click on the tab. Now we can see more details. When the user started to do some touch action (swiping in the above example), we could see more CPU work. Each app will have its own signature of CPU spikes and lows. It’s important to build an intuition about it, by interacting with it and pairing certain activities, like touch events, with the increased usage. In other words, some spikes are expected, because the work needs to be done. The problem starts when CPU usage is very high for extended periods of time or in unexpected places.

Let’s imagine you would like to pick the best list or scroll view component for your React Native app, which has the best performance on a lower-end device. You noticed the current solutions could be

revamped or improved and you started working on this. In your experiment, you would like to check how your solution works for LE devices using the above-described solution. When you double-clicked on CPU, you could spot the below data:

| A    | Reanenuad | Reanneuad | sibw | Mceexaaemc | (TH) TA |
| ---- | --------- | --------- | ---- | ---------- | ------- |
| %00L | CPN       | MaN       |      |            |         |

Here you can see the mqt_js thread is used almost all the time and does some heavy computation because your computations are done on the JS side. You can start thinking about how to improve it. There are multiple options to check:

- Replace the bridge with JSI in terms of communication – do tests if JSI is faster than the bridge.
- Move some part of the code to the native side – on the native side you have more control over threads execution and can schedule some work to not block the JS or UI thread.
- Use a different native component – replace the native scroll view with your custom solution.
- Use shadow nodes – do some expensive calculation with C++ and pass it to the native side.

You can try out all of those solutions and compare the effect between each other. The profiler will provide you with a metric and based on that you can make a decision about which approach fits best to your particular problem.

There’s more info about the Android Profiler here.

# SYSTEM TRACING

Using the Android Studio CPU Profiler, we can also make a system tracing. We can check when the appropriate function has been called. We can triage all threads and see which function is the costliest which affects the UX. To enable system tracing, click on the CPU section and select System Trace Recording.

Profiler com.pagerviewexample (Motorola Moto X4)

# SESSIONS

# CPU

17:08

pagerviewexample (Motorola Moto X4)

26 sec

16:41

pagerviewexample (Motorola Moto X4)

1 min 57 sec

# System Trace Recording

00:00:06.064

# Callstack Sample Recording

Samples Java/Kotlin and native code using simpleperf.

# System Trace Recording

Traces Java/Kotlin and native code at the Android platform level

# Java/Kotlin Method Trace Recording

Instruments Java/Kotlin code using Android Runtime, tracking every method call (this incurs high overhead making timing information inaccurate).

# Java/Kotlin Method Sample Recording (legacy)

Samples Java/Kotlin code using Android Runtime.

Load saved custom profiling configurations

Edit Configurations Record

Git Profile ETODO Problems Terminal Build Profiler

After some interaction, you should be able to see all the threads with details:

# com.pagerviewexample (Motorola Moto X4)

SSIONS CPU VSync guide Clear thresdievent selection 0C

41 CU Sap Analysis All threads agerviewexample X

# System Trace Recording

Interaction 01.000 Summary Top Down Flame Chart Bottom Up Events

00.00:06.004 Time Range 00:00.000 - 00:06.265

User Duration 6.27s

Lifecyle Data Type Thread

Display 13725

Frames States

- SurfaceFlinger 1000010 Thraed State Duration Occurrences

| Sleeping | 3.5s     | 56.8%  | 702  |
| -------- | -------- | ------ | ---- |
| Running  | 2.50 s   | 41.28% | 1416 |
| Runnable | 125.5 ms | 2%     | 542  |
| Unknown  | 32.42 ms | 0.52%  | 153  |
| Waiting  | 15.88 ms | 0.25%  | 18   |

# Longest running events (top 10)

| Event                | CPU Duration | CPU Seit Time |
| -------------------- | ------------ | ------------- |
| Choreographer#doFr.. | 33.66 ms     | 213 us        |
| input                | 30.1 ms      | 28.91 ms      |
| Choreographer#doFr.. | 29.15 ms     | 137.5 us      |
| Choreographer#doFr.  | 26.18 ms     | 95 us         |
| Choreographer#doFr.. | 25.57 ms     | 99 us         |
| input                | 23.42 ms     | 17.35 ms      |
| input                | 21.65 ms     | 20.63 ms      |
| Choreographer#doFr.. | 20.61 ms     | 141 us        |
| input                | 20.25 ms     | 13.1 ms       |
| input                | 18.47 ms     | 12.6 ms       |

00.000 D1.OO0 02.000 03.000 04.000 06.000

You can also save your data by clicking the Save Button:

| SystemTrace Reco...           | a Lifecycle | 00:00:06.064 |
| ----------------------------- | ----------- | ------------ |
| Export System Trace Recording |             |              |
| Frames                        |             |              |

And use the data in a different tool, e.g. Perfetto:

| Search    | 626.5 ms | 1.3s    | EEeI      | 2.5s      | 3.8s      |           |           |           |           |
| --------- | -------- | ------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
|           | 0s       |         |           | 1.9s      | 3.1s      |           |           |           |           |
| 20353.8 $ | + 0s     | +6.9 ms | +106.9 ms | #206.9 ms | +306.9 ms | +406.9 ms | +506.9 ms | +606.9 ms | +706.9 ms |

X

| Cpu 0         | Cpu 1  | Cpu 2       | Cpu 3  | Cpu 4          | Cpu 5 | Cpu 6 | Cpu 7 |
| ------------- | ------ | ----------- | ------ | -------------- | ----- | ----- | ----- |
| com.pagerv... | com... | com.page... | com.p. | com.pagerviewe |       |       |       |

You’ll also want to check the official Android Profiling guide by the React Native core team. They use different tools, but the outcome will be the same. The guide provides case studies and how to spot an issue on different threads:

- UI thread
- JS thread
- Native module thread
- Render Thread (only Android)

You can find more about threading models in the New Architecture chapter.

# FLIPPER PERFORMANCE PLUGIN FOR ANDROID

We already know Flipper can be quite handy in hunting performance issues. One of the most interesting plugins to help us out on Android is android-performance-profiler. It can be used as a standalone tool or on a CI. It can generate beautiful reports, so this tool can be used to make some sophisticated experiments.

# Here is a picture of an example experiment:

|                                        | Results FABRIC List scrolling | Results FABRIC Showing 100 Tweets | Results NO FABRIC List scrolling | Results NO FABRIC Showing 100 Tweets |
| -------------------------------------- | ----------------------------- | --------------------------------- | -------------------------------- | ------------------------------------ |
| Score                                  | 67                            | 54                                | 83                               | 60                                   |
| Average Test Runtime                   | 11187ms                       | 6307ms                            | 12150ms                          | 5535ms                               |
| Average FPS                            | 47.9                          | 36.5                              | 48.2                             | 40.7                                 |
| Average CPU usage                      | 99.7%                         | 106.7%                            | 95.5%                            | 111.2%                               |
| Average RAM Usage                      | 239.9MB                       | 237.3MB                           | 229.1MB                          | 226.6MB                              |
| Total:                                 | 3.8s                          |                                   |                                  |                                      |
| Processes with high CPU usage detected | fabric_bg for 3.7s            | mqt_js for 1.1s                   | mqt_js for 1s                    |                                      |
|                                        | FrescoDecodeExe for 0.95s     | None                              | FrescoDecodeExe for 0.65s        |                                      |
|                                        | UI Thread for 0.1s            | UI Thread for 0.4s                | mqt_native_modu for 0.25s        |                                      |
|                                        | fabric_bg for 0.05s           |                                   | FrescoloBoundEx for 0.1s         |                                      |
| Framework Detection                    | React Native                  | React Native                      | React Native                     | React Native                         |

Comparison of the new vs old architecture of React Native by Almouro. Source.

You can also automate your experiments with e2e tests and generate reports locally or on a CI. Those reports can be used to compare solutions with each other.

# BENEFITS: REAL-TIME METRICS WILL IMPROVE YOUR APP UNDERSTANDING

As stated above, users will abandon your app if the response time is too long. Using specific tools will help you understand the root cause of the app’s performance issue.

# THANK YOU

We hope that you found the aforementioned best practices for React Native optimization useful and that they will make your work easier. We did our best to make this guide comprehensive and describe both the technical and business aspects of the optimization process.

If you enjoyed it, don’t hesitate to share it with your friends who also use React Native in their projects.

# IF YOU HAVE MORE QUESTIONS OR NEED HELP WITH CROSS- PLATFORM OR REACT NATIVE DEVELOPMENT, WE WILL BE HAPPY TO PROVIDE A FREE CONSULTATION.

JUST CONTACT US!

# AUTHORS

# MICHAŁ PIERZCHAŁA

As Head of Technology at Callstack, he is passionate about building mobile and web experiences, high-quality JS tooling, and Open Source. Core Jest and React Native community contributor. Space exploration enthusiast.

twitter.com/thymikee

github.com/thymikee

# JAKUB BUJKO

With multiple years of delving deep into react.js development in his pocket, Kuba went on to master mobile development. Passionate about edge technologies, clean and minimalistic code, and charting the paths for the future of React and React Native development.

twitter.com/f3ng

github.com/Xiltyn

# MACIEJ JASTRZĘBSKI

React &#x26; React Native developer with multiple years of experience building native iOS and Android apps. Passionate about building robust and delightful apps along with writing well-architected and readable code. Loves learning new things. He likes to travel in his free time, hike in the mountains, and take photographs.

twitter.com/mdj_dev

github.com/mdjastrzebski

# Team Members

# PIOTR TROCKI

Software developer who started his journey from mobile apps. Now Piotr is focused on mastering both Native (Android, iOS) and React Native technologies in brownfield applications. When not coding, he spends his free time on the dance floor.

twitter.com/Tr0zZe

github.com/troZee

# JAKUB BINDA

A dedicated software developer who pays a lot of attention to the details in every task he does. Always committed and eager to learn, Kuba likes to create things and dive into how they work. A father of two and a husband to the woman of his life. Those two roles motivate him the most and give him the strength to move mountains.

github.com/jbinda

# SZYMON RYBCZAK

Szymon is a 17-year-old React Native Developer with three years of experience and currently doing mobile app development at Callstack. In his free time, he likes to discover new and interesting technologies.

github.com/szymonrybczak

twitter.com/SzymonRybczak

# HUR ALI

TypeScript enthusiast mastering the React-Native and Native realm. He feels best in diving deep with mobile tech, making proof-of-concept projects, and experimenting with new technologies. In his free time, he enjoys playing FIFA and contribution to OSS.

twitter.com/hurali97

github.com/hurali97

# Team Members

# OSKAR KWAŚNIEWSKI

React Native Developer at Callstack. Currently, he’s strengthening his knowledge of native development and making some OSS contributions. During his free time, he enjoys riding a bike, going to the gym, and playing video games.

github.com/okwasniewski

twitter.com/o_kwasniewski

# TOMASZ MISIUKIEWICZ

React Native Developer at Callstack with a strong background in web development. Big fan of keeping the code clean and simple. Loves to learn new stuff and enhance his programming skillset every day.

github.com/TMisiukiewicz

# EDUARDO GRACIANO

Senior mobile developer at Callstack. Hacking almost all kinds of mobile tech and always looking forward to making readable and maintainable code without messing up everything.

github.com/gedu

twitter.com/teddydroid07

# ANDREW ANDILEVKO

React Native developer with a background in Android development. He likes complex tasks to constantly expand his expertise and knowledge. He spends his free time with his wife and pug.

github.com/andrewworld

# Team Members

# JAMES IDE

I work on Expo, which I co-founded with Charlie Cheever when we wanted to make it easier to make and use universal mobile apps that run everywhere.

https://github.com/ide

https://twitter.com/JI

# GRZEGORZ KRUK

Senior Frontend Developer with years of experience in building mobile and web solutions in multiple frameworks and libraries. After mastering web development, he’s become passionate about building beautiful and neat mobile solutions in React Native.

https://github.com/grzegorzkruk

# KANSTANTSIN KIYKO

JavaScript expert with experience in mobile and web apps development. Has a can-do attitude, loves to solve complex problems and automate things.

https://twitter.com/xfozzyx

https://github.com/sneakyechidna

# JACEK PACIOREK

React Native Developer at Callstack with full stack development background. Loves to explore boundaries between software and hardware and tinkering with IoT devices. Likes a good challenge and gets stuff done. Besides that, he is obsessed with cars – loves driving them, fixing them up and sharing his passion with others. Also tries to stay active by skiing and sailing.

https://github.com/booua

# ABOUT CALLSTACK

Callstack is the Total Software Engineering consultancy that develops high-performing cross-platform apps set in the React Universe. We work with global enterprise clients such as PwC, Major League Soccer and AutoZone, and fast-growing startups and SMEs like Evernote and Coinmine.

We build apps in the React Universe: an approach that leverages React-based full-stack, cross-platform tech stack to create better, faster apps, smoother running teams, and lower operational costs.

Ever since the company’s beginning, we’ve been an active part of the community the co-creators of React Native. We make free Open Source tools and libraries that help millions of developers globally build better-performing apps quicker and easier. Projects like Reassure, Re.Pack or React Native Testing Library were born from the belief that (code) sharing is caring and proved invaluable in improving developer and user experience alike.

We also help raise industry standards by training developers around the world through business and technology podcasts, articles, and events like React Universe Conf (formerly React Native EU) and React Conf.
