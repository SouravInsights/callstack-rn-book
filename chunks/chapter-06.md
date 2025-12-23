## CHAPTER 6

### EXPERIMENT WITH THE NEW ARCHITECTURE OF REACT NATIVE

70

### LEVERAGE THE CAPABILITIES OF THE NEW RENDERING SYSTEM INSIDE YOUR APP.

#### ISSUE: YOUR APP IS USING OLD ARCHITECTURE WITHOUT THE CONCURRENT FEATURES OF REACT 18.

Maybe it's better to say “current” architecture since it's still mostly used by production apps. This term refers to how React Native's two realms (Native and JS) communicate with each other. Both new and old architecture is based on the communication between JavaScript and the native side. Currently, this communication is handled by the bridge. Let's go over its limitations in order to easier understand the problems that the New Architecture is trying to solve.

- It is asynchronous: the JavaScript side submits data to a bridge and waits for the data to be processed by the native side.
- It's single-threaded (that's why it's important to not overload the JS thread and execute animations on the UI thread).
- It adds additional overhead when it comes to the serialization of data from JSON objects.

The bridge is still working fine for most use cases. However, when we start to send a lot of data over the bridge, it may become a bottleneck for our app. This problem can be seen when rendering a lot of components in a long list. In the case when the user scrolls fast, there will be a blank space caused by the communication between the JS and native sides being asynchronous. Essentially what happens is that we are having a “traffic jam” on our bridge with objects waiting to be serialized. The same issue with the bridge being “overloaded” can be seen in native modules sending a lot of data back and forth.

This bottleneck, together with providing a type safe way of communicating between native and JS, are the main things that the new architecture is trying to solve. However, not everything about new architecture is as good as it may seem. We will also get into the drawbacks that it brings.

#### SOLUTION: MIGRATE YOUR APP TO NEW ARCHITECTURE.

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

### HOW TO TURN ON NEW ARCHITECTURE

According to official React Native core team recommendation, in order to turn on the New Architecture in your app, you need to update your app to the latest version of React Native.

To migrate your app to the New Architecture, follow these steps:

1. Upgrade your app to at least React Native version, you can use https://react-native-community.github.io/upgrade-helper/
2. [Android] Set newArchEnabled=true in gradle.properties.
3. [iOS] Run RCT_NEW_ARCH_ENABLED=1 pod install inside the iOS folder.
4. Run the app in debug and release modes. Look for Components that are not yet compatible – they will show as red boxes – Unimplemented component: &#x3C;ComponentName> – and you will likely notice them.
5. In case of unsupported components, use the Interop Layer through react-native.config.js file and the unstable_react-LegacyComponentNames option and try again. Take note that the interop layer is not fully compatible with the old rendering and event system, so inconsistencies may be expected in some cases.

### BENEFITS: YOU ARE ABLE TO LEVERAGE ALL THE LATEST FEATURES INCLUDING REACT 18, FABRIC, TURBOMODULES, AND JSI.

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

### FUTURE READINESS

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

### IF YOU NEED HELP WITH

### PERFORMANCE, STABILITY, USER

### EXPERIENCE, OR OTHER COMPLEX

# ISSUES – CONTACT US!

As React Native Core Contributors and leaders of the com-

munity, we will be happy to help.

# PART 3

### HOW TO SHIP QUICKER WITH A STABLE DEVELOPMENT ENVIRONMENT

React Native is great for shipping fast and with confidence, but are you ready for that?

These days, having a stable and comfortable development setup that encourages shipping new features and doesn't slow you down is a must. You have to ship fast and be ahead of your competitors.

React Native plays really well in such environments. For example, one of its biggest selling points is that it allows you to ship updates to your applications without undergoing the App Store submission. They're called Over-the-Air (OTA) updates.

The question is: is your application ready for that? Does your development pipeline accelerate the development and shipping features with React Native?

Most of the time, you would like the answer to be simply yes. But in reality, it gets complicated.

In this section, we present some of the best practices and recommendations that allow you to ship your apps faster and with more confidence. And it's not just about turning on the Over-the-Air updates, as most articles suggest. It's about building a steady and healthy development environment where React Native shines and accelerates innovation.

And that's what this part of our guide is all about.

# PART 3

# | CHAPTER 1

### RUN TESTS FOR KEY PIECES OF YOUR APP

### FOCUS TESTING ON KEY PIECES OF THE APP TO HAVE A BETTER OVERVIEW OF NEW FEATURES AND TWEAKS.

#### ISSUE: YOU DON'T WRITE TESTS AT ALL OR WRITE LOW-QUALITY TESTS WITH NO REAL COVERAGE, AND YOU ONLY RELY ON MANUAL TESTING.

Building and deploying apps with confidence is a challenging task. However, verifying if everything actually works requires a lot of time and effort – no matter if it is automated or not. Having somebody who manually verifies that the software works as expected is vital for your product.

Unfortunately, this process doesn't scale well as the amount of your app functionalities grow. It also doesn't provide direct feedback to the developers who write the code. Because of that, it increases the time needed to spot and fix a bug.

So what do the developers do to make sure their software is always production-ready and doesn't rely on human testers? They write automated tests. And React Native is no exception. You can write a variety of tests both for your JS code – which contains the business logic and UI – and the native code that is used underneath.

You can do it by utilizing end-to-end testing frameworks, spinning up simulators, emulators, or even real devices. One of the great features of React Native is that it bundles to a native app bundle, so it allows you to employ all the end-to-end testing frameworks that you love and use in your native projects.

But beware, writing a test may be a challenging task on its own, especially if you lack experience. You might end up with a test that doesn't have a good coverage of your features. Or only to test positive behavior, without handling exceptions. It's very common.

to encounter low-quality tests that don't provide too much value and hence, won't boost your confidence in shipping the code.

Whichever kind of test you're going to write, be it unit, integration, or E2E (short for end-to-end), there's a golden rule that will save you from writing the bad ones. And the rule is to “avoid testing implementation details.” Stick to it and your test will start to provide value over time. You can't move as fast as your competition, chances of regressions are high, and apps can be removed from stores when receiving bad reviews. The main goal of testing your code is to deploy it with confidence by minimizing the number of bugs you introduce in your codebase. And not shipping bugs to the users is especially important for mobile apps, which are usually published in app stores.

Because of that, they are a subject of a lengthy review process, which may take from a few hours up to a few days. And the last thing you want is to frustrate your users with an update that makes your app faulty. That could lead to lower ratings and, in extreme cases, even taking the app down from the store.

Such scenarios may seem pretty rare, but they happen. Then, your team may become so afraid of having another regression and crash that it will lose its velocity and confidence.

#### SOLUTION: DON'T AIM AT 100% COVERAGE, FOCUS ON KEY PIECES OF THE APP. TEST MOSTLY INTEGRATION.

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

### JAVASCRIPT TESTING

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

### E2E TESTS

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

### BENEFITS

YOU HAVE A BETTER OVERVIEW OF THE NEW FEATURES AND TWEAKS, CAN SHIP WITH CONFIDENCE, AND WHEN THE TESTS ARE GREEN – YOU SAVE THE TIME OF OTHER PEOPLE (THE QA TEAM).

A high-quality test suite that provides enough coverage for your core features is an investment in your team's velocity. After all, you can move only as fast as your confidence allows you to. And the tests are all about making sure you're heading in the right direction.

The React Native community is working hard to make testing as easy and pleasant as possible – for both your team and the QA teams. Thanks to that, you can spend more time innovating and pleasing users with flashy new functionalities, and not squashing bugs and regressions over and over again.

“By testing key features of an app via integration testing, developers can effectively identify and eliminate potential bugs, ultimately leading to a more confident and efficient development process.”

Christoph Nakazawa – Senior Engineering Manager &#x26; Creator of Jest

# PART 3 | CHAPTER 2

### HAVE A WORKING CONTINUOUS INTEGRATION (CI) IN PLACE

### USE A CI PROVIDER TO IMPROVE THE BUILDING, TESTING, AND DISTRIBUTION OF YOUR APPS.

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

#### SOLUTION: USE A CI PROVIDER SUCH AS CIRCLE CI OR EAS BUILD TO BUILD YOUR APPLICATION.

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
