## CHAPTER 1

### PAY ATTENTION TO

### UI RE-RENDERS

### OPTIMIZE THE NUMBER OF STATE OPERATIONS AND REMEMBER ABOUT MEMOIZED COMPONENTS TO MAKE YOUR APP WORK FASTER WITH FEWER RESOURCES.

#### ISSUE: INCORRECT STATE UPDATES CAUSE EXTRANEOUS RENDERING CYCLES OR THE DEVICE IS JUST TOO SLOW.

As discussed briefly, React Native takes care of rendering the application for you. You have to define all the components you need and compose the final interface out of these smaller building blocks. In that approach, you don’t control the application rendering lifecycle.

In other words, when and how to repaint things on screen is purely React Native’s responsibility. React looks out for the changes you have done to your components, compares them, and, by design, only performs the required and smallest number of actual updates.

By default, a component can re-render if its parent is re-rendering or the props are different. This means that your component’s render method can sometimes run, even if their props didn’t change. This is an acceptable tradeoff in most scenarios, as comparing the two objects (the previous and current props) would take longer.

### NEGATIVE IMPACT ON PERFORMANCE, UI FLICKER, AND FPS DECREASE

While the above heuristics are correct most of the time, performing too many operations can cause performance problems, especially on low-end mobile devices.

As a result, you may observe your UI flickering (when the updates are performed) or frames dropping (while there’s an animation happening and an update is coming along).

Note: Performing premature optimizations may have the opposite of the intended effect. Try looking at performance issues as soon as you spot dropped frames or undesired performance within your app.

As soon as you see any of these symptoms, it is the right time to look a bit deeper into your application lifecycle and look for extraneous operations that you would not expect to happen.

# HOW DO WE KNOW WHAT TO OPTIMIZE?

When it comes to performance optimization, we want to make decisions based on data. The data comes from measuring performance using specialized tools. The process is often referred to as profiling. There are many tools available that can help us with profiling our React Native apps: react-devtools, why-did-you-render, Profiler, and others.

For this exercise, we’ll use Flipper, a platform for debugging iOS, Android, and React Native apps. It has React DevTools Profiler integrated as a plugin that can produce a flame graph of the React rendering pipeline as a result of profiling. We can leverage this

# Flipper (0.176.0)

### APP INSPECT

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

#### SOLUTION: OPTIMIZE THE NUMBER OF STATE OPERATIONS AND REMEMBER TO USE MEMOIZED COMPONENTS WHEN NEEDED.

There’re a lot of ways your application can turn into unnecessary rendering cycles and that point itself is worth a separate article. Here, we will focus on two common scenarios – using a controlled component, such as TextInput and global state.

### CONTROLLED VS UNCONTROLLED COMPONENTS

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

### STATE NORMALIZATION (REDUX TOOLKIT):

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

### ATOMIC STATE

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

### FUTURE WITH REACT FORGET

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

### BENEFITS: FEWER RESOURCES NEEDED AND A FASTER APPLICATION.

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
