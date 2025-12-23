## CHAPTER 2

### USE DEDICATED COMPONENTS FOR CERTAIN LAYOUTS

9

### FIND OUT HOW TO USE DEDICATED HIGHER-ORDERED REACT NATIVE COMPONENTS TO IMPROVE THE USER EXPERIENCE AND THE PERFORMANCE OF YOUR APPS

ISSUE: YOU ARE UNAWARE OF THE HIGHER-ORDER COMPONENTS THAT ARE PROVIDED WITH REACT NATIVE.

In a React Native application, everything is a component. At the end of the component hierarchy, there are so-called primitive components, such as Text, View, or TextInput. These components are implemented by React Native and provided by the platform you are targeting to support the most basic user interactions.

When we're building our application, we compose it out of smaller building blocks. To do so, we use primitive components. For example, in order to create a login screen, we would use a series of TextInput components to register user details and a Touchable component to handle user interaction. This approach is true from the very first component that we create within our application and holds true through the final stage of its development.

On top of primitive components, React Native ships with a set of higher-order components that are designed and optimized to serve a certain purpose. Being unaware of them or not using them can potentially affect your application performance, especially as you populate your state with real production data. A bad performance of your app may seriously harm the user experience. In consequence, it can make your clients unsatisfied with your product and turn them towards your competitors.

### NOT USING SPECIALIZED COMPONENTS WILL AFFECT YOUR PERFORMANCE AND UX AS YOUR DATA GROWS.

If you're not using specialized components, you are opting out of performance improvements and risking a degraded user experience when your application enters production. It is worth noting that certain issues remain unnoticed while the application is developed, as mocked data is usually small and doesn't reflect the size of a production database. Specialized components are more comprehensive and have a broader API to cover than the vast majority of mobile scenarios.

#### SOLUTION: ALWAYS USE A SPECIALIZED COMPONENT, E.G. FLATLIST FOR LISTS.

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

### FLASHLIST AS A SUCCESSOR TO FLATLIST

to render the next batch of data, it will have to wait for all the new items to render to measure their height.

However, you can implement getItemHeight() to define the element height up-front without the need for measurement. It is not straightforward for items without a constant height. You can calculate the value based on the number of lines of text and other layout constraints.

We recommend using the react-native-text-size library to calculate the height of the displayed text for all list items at once. In our case, it significantly improved the responsiveness for scroll events of FlatList on Android.

### FLASHLIST AS A SUCCESSOR TO FLATLIST

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

### THINK TWICE BEFORE YOU PICK AN EXTERNAL LIBRARY

### HOW WORKING WITH THE RIGHT JAVASCRIPT LIBRARIES CAN HELP YOU BOOST THE SPEED AND PERFORMANCE OF YOUR APPS.

#### ISSUE: YOU ARE CHOOSING LIBRARIES WITHOUT CHECKING WHAT IS INSIDE

JavaScript development is like assembling applications out of smaller blocks. To a certain degree, it is very similar to building React Native apps. Instead of creating React components from scratch, you are on the hunt for the JavaScript libraries that will help you achieve what you had in mind. The JavaScript ecosystem promotes such an approach to development and encourages structuring applications around small and reusable modules.

This type of ecosystem has many advantages, but also some serious drawbacks. One of them is that developers can find it hard to choose from multiple libraries supporting the same use case.

When picking the one to use in the next project, they often research the indicators that tell them if the library is healthy and well maintained, such as GitHub stars, the number of issues, contributors, and PRs.

What they tend to overlook is the library's size, number of supported features, and external dependencies. They assume that since React Native is all about JavaScript and embracing the existing toolchain, they will work with the same constraints and best practices they know from making web applications.

Truth is, they won't, as mobile development is fundamentally different and has its own set of rules. For example, while the size of the assets is crucial in the case of web applications, it is not

### COMPLEX LIBRARIES HAMPER THE SPEED OF YOUR APPS

as equally important in React Native, where assets are located in the filesystem.

The key difference lies in the performance of the mobile devices and the tooling used for bundling and compiling the application.

Although you will not be able to do much about the device limitations, you can control your JavaScript code. In general, less code means faster opening time. And one of the most important factors affecting the overall size of your code is libraries.

Unlike a fully native application, a React Native app contains a JavaScript bundle that needs to be loaded into memory. Then it is parsed and executed by the JavaScript VM. The overall size of the JavaScript code is an important factor.

While that happens, the application remains in the loading state. We often describe this process as TTI – Time to Interactive. It is a time expressed in (well, hopefully) the milliseconds between when the icon gets selected from the application drawer and when it becomes fully interactive.

Unfortunately, Metro – the default React Native bundler – currently doesn't support tree shaking. If you're not familiar with this notion, read this article.

This means that all the code that you pull from NPM and import to your project will be present in your production JS bundle, loaded into memory, and parsed. That can have a negative impact on the total startup time of your application.

What's worth pointing out is that it's not the case with Hermes engine, which automatically pages only necessary bytecode into memory. Read more in the Hermes chapter.

### HOW DO WE ANALYZE BUNDLE SIZE

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

#### SOLUTION: BE MORE SELECTIVE AND USE SMALLER SPECIALIZED LIBRARIES.

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

### BENEFITS: YOUR APP HAS A SMALLER FOOTPRINT AND LOADS FASTER.

Mobile is an extremely competitive environment, with lots of applications designed to serve similar purposes and fight over the same customers. Faster startup time, smoother interactions, and the overall look and feel might be your only way to stand out from the crowd.

You shouldn't downplay the importance of choosing the right set of libraries. Being more selective with third-party dependencies may seem irrelevant at first. But all the saved milliseconds will add up to significant gains over time.

# PART 1
