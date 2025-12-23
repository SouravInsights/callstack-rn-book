## CHAPTER 9

# OPTIMIZE YOUR APP’S JAVASCRIPT BUNDLE

#### ISSUE: METRO, THE DEFAULT JS BUNDLER FOR REACT NATIVE, PRODUCES A BUNDLE THAT’S TOO LARGE.

React Native application’s logic is mostly located in the JavaScript code which runs in the JavaScript engine (JavaScriptCore or Hermes). But before loading JavaScript code into the app, it should be bundled, usually into a single JS file or sometimes to multiple files. React Native provides a built-in tool for JavaScript code bundling called Metro.

#### SOLUTION: USE EXTERNAL PLUGINS OR SWAP IT WITH THIRD-PARTY BUNDLERS.

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

### BENEFITS: SHIP LESS JAVASCRIPT TO YOUR USERS.

# SAVE DEVELOPERS’ TIME WHEN BUNDLING.

The choice of a bundle tool depends on the specific case. It is impossible to select only one bundler for all the apps.

# Tree-Shaking in React Native

As you can see, tree-shaking in React Native can be achieved through use of Webpack (via Re.Pack) or ESBuild (via rnx-kit or react-native-esbuild). Tree-shaking implementation differs between bundlers, so it might be feasible to check the results of both and determine what’s best for your app. Note that tree-shaking through rnx-kit is still in beta, but the results are optimistic so far. It’s reasonable to expect the bundle size difference between 0% and 20%, and in rare cases, even more than that.

Should you feel a need for customization options provided by the Webpack ecosystem or plan to split your app code, then we would suggest using Re.Pack for its widely customizable configuration, a huge amount of loaders, plugins maintained by the community. If the Webpack ecosystem feels like an overhead, then it is better to stay with the default Metro bundler or try to use other bundler options like react-native-esbuild and rnx-kit which also provides some benefits like decreased build time, using esbuild under the hood, symlinks, and typescript support out-of-the-box. But be careful and always pay attention to the tradeoffs that come with a new bundling system.

# IF YOU NEED HELP WITH PERFORMANCE, STABILITY, USER EXPERIENCE, OR OTHER COMPLEX ISSUES – CONTACT US!

As React Native Core Contributors and leaders of the community, we will be happy to help.

# PART 2

### IMPROVE PERFORMANCE BY USING THE LATEST REACT NATIVE FEATURES.

React Native is growing fast and so is the number of features.

Last year, developers contributed more than 3670 commits to the React Native core. The number may seem impressive, but, in fact, it's even larger, since it doesn't include the smaller contributions made under the React Native Community organization (9678 commits).

All that proves that React Native is developing at a really healthy pace. Contributions made by both the community and Meta enable more and more advanced use cases of the framework. A great example of that is Hermes – an entirely new JavaScript engine built and designed specifically for React Native and Android. Hermes aims to replace the JavaScriptCore, previously used on both Android and iOS. It also brings a lot of enterprise-grade optimizations by improving your Android application's performance, start-up time, and overall size reduction.

In this section, we will show you some of the features you can turn on right now to start your optimization process. We also encourage you to keep track of all the new React Native features to make sure you use the framework to its full potential.

# PART 2

# | CHAPTER 1

ALWAYS RUN THE LATEST REACT NATIVE VERSION TO ACCESS THE NEW FEATURES

### UPGRADE YOUR APP TO THE LATEST VERSION TO GET MORE FEATURES AND BETTER SUPPORT.

ISSUE: YOU ARE RUNNING AN OLD AND UNSUPPORTED VERSION OF REACT NATIVE AND DEPRIVING YOURSELF OF NEW IMPROVEMENTS AND FEATURES

Keeping your application up to speed with the frameworks you use is crucial. That is why you should subscribe to the latest features, performance improvements, and security fixes.

The JavaScript ecosystem is particularly interesting in this aspect, as it moves really quickly. If you don't update your app regularly, chances are your code will end up being so far behind that upgrading it will become painful and risky.

Every day, developers from all around the world introduce new features, critical bug fixes, and security patches. On average, each release includes around 500 commits.

Over the years, React Native has grown significantly, thanks to open-source contributors and Meta's dedication to improving the ecosystem. Here are some highlighted crucial features that have been introduced to React Native over the course of its releases.

### FAST REFRESH

To improve the developer experience and velocity, the React team introduced a feature called Fast Refresh to React Native. This lets you quickly reflect the code on the device, whenever you save the file instead of building or reloading the app. It is smart enough

# to decide when to do a reload after we fix an error or just render otherwise.

A tip here: the local state of functional components and hooks is preserved by default. We can override this by adding a comment to that file: // @refresh reset. Whereas, class components are remounted without preserving the state.

### AUTO-LINKING

Whenever we add native code to our React Native app as a dependency, it needs to be linked. Previously linking was done manually or using react-native link dep-name. React Native CLI introduced auto-linking so the devs didn't need to link a library themselves. After a couple of years, when the re-architecture of React Native was released to the community, a need arose to auto link fabric components and turbo modules, which was handled gracefully by the CLI team. They released an update to the community to help the developer experience and velocity.

### FLIPPER

Important note: Debugging React Native apps with Flipper is deprecated in React Native 0.73. The out-of-the box support will eventually be removed for JS debugging via Flipper in 0.74.

It is one of the ways of debugging React Native apps. It is loaded with awesome tools such as ReactDevtools, Network Inspector, Native Layout Inspector, and plugins for e.g. to measure the performance of the React Native apps. We can also view the Metro and Device logs right in Flipper.

### NEW DEBUGGING EXPERIENCE

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

### EXPO DEV TOOLS PLUGINS

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

### NAVIGATE

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

### LOGBOX

React Native redesigned its error and warning handling system. They had to do a ground-up redesign of its logging system and the developer experience is much better because of it. Developers can easily trace the cause of an error using code frames and component stacks. Syntax error formatting helps to understand the issue more quickly with the aid of syntax highlighting. Log Notifications show warnings and logs at the bottom of the screen instead of covering the whole screen.

### HERMES

A new JS engine created by Meta to improve the performance of React Native apps in terms of CPU usage, memory consumption, app size, and Time To Interactive (TTI). Initial support was launched for Android devices, but after two years, support was extended to iOS as well. After a couple of months, the previously used garbage collector for Hermes GenGC was replaced with a new one called Hades – a concurrent garbage collector. The Meta team saw improvements of CPU-intensive workloads by 20-50%. Later on, the team decided to ship a bundled Hermes.

instead of downloading it from NPM. This was done to avoid con-

fusion between what version of Hermes is compatible with React

Native. Also, both Hermes and React Native use the same JSI

code which makes it hard to maintain. Now whenever a version

of React Native is released, a version of Hermes can be released

as well, making sure that both are fully compatible.

### NEW ARCHITECTURE

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

### RUNNING ON AN OLD VERSION MEANS SHIPPING WITH ISSUES THAT MAY DISCOURAGE YOUR USERS

If you are running on an older version, it is likely that you are lagging behind your competition that uses the latest versions of the framework.

The number of fixes, improvements, and advancements in the React Native framework is really impressive. If you're playing a game of catch up, you are opting out of a lot of updates that would make your life a lot easier. The workload and the cost involved in making regular upgrades are always offset by the immediate DX enhancements.

In this section, we present some of the well-established practices to make upgrading React Native to the newer version easier.

#### SOLUTION: UPGRADE TO THE LATEST VERSION OF REACT NATIVE (WE'LL SHOW YOU HOW).

Upgrading React Native might not be the easiest thing in the world. But there are tools that can simplify the process and take most of the problems away.

The actual amount of work will depend on the number of changes and your base version. However, the steps presented in this section can be applied to every upgrade, regardless of the state of your application.

### PREPARING FOR THE UPGRADE

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

### APPLYING THE JAVASCRIPT CHANGES

The process of upgrading the JavaScript part of React Native is similar to upgrading other JavaScript frameworks. Our recommendation here is to perform upgrades step-by-step – bumping one library at a time. As a rule of thumb, once you have upgraded a library, save your work at that point in a commit and then move on to the next library. In our opinion, this approach is better than upgrading everything at once as it gives you more control and makes catching regressions much easier.

### UPGRADING REACT NATIVE

The first step is to bump the React and React Native dependencies to the desired versions and perform the necessary changes (including breaking changes). To do so, you can look up the suggestions provided by React Native Upgrade Helper and apply them manually. Once it's completed, make sure to reinstall your node_modules.

Note: When performing the upgrade, you may see a lot of changes coming from iOS project files (everything inside .xcodeproj, including .pbxproj). These are files generated by Xcode as you work with your iOS part of React Native application. Instead of modifying the source file, it is better to perform the changes via the Xcode UI. This was the case with upgrading to React Native 0.60 and the appropriate operations were described in this issue.

Finally, you should try running the application. If everything is working – perfect. The upgrade was smooth and you can call it a day! On a more serious note though – now you should check if there are newer versions of other dependencies you use! They may be shipping important performance improvements.

Unfortunately, there's also another more pessimistic scenario. Your app may not build at all or may instantly crash with a red screen. In that case, it is very likely that some of your third-party dependencies are not working properly, as in some cases the dependencies include native code which supports new OS features, so you need to make them compatible with your React Native version.

Note: If you have a problem with your upgrades, you can check the Upgrade Support project. It is a repository where developers share their experience and help each other solve some of the most challenging operations related to upgrading.

### UPGRADING THIRD-PARTY LIBRARIES

In most cases, it's your React Native dependencies that you should look at first. Unlike regular JavaScript/React packages, they often depend on native build systems and more advanced React Native.

APIs. This exposes them to potential errors as the framework matures into a more stable API.

If the error occurs during the build time, bumping the dependency to its latest version usually makes it work. But it may not always be the case. To make sure the version of React Native you're upgrading to is compatible with your dependencies, use the align-deps project by Microsoft developers. It allows you to keep your dependencies on the right version based on the requirements and by leveraging the presets of rules. It also has a CLI, so you can wire it up to your CI and ensure that no one in your repo or monorepo will inadvertently introduce incompatible versions of packages and break the app.

Once your application builds, you are ready to check the changelog and make yourself familiar with the JavaScript changes that happened to the public API. If you overlook this step, it can result in runtime exceptions. Using Flow or TypeScript should help you ensure that the changes were applied properly.

As you can see, there is no magic trick that would fix all the errors and upgrade the dependencies automatically. This is mostly manual work that has to be done with patience and attention. It also requires a lot of testing to ensure that you didn't break any features along the way. Fortunately, there are tools like align-deps that help you avoid at least some of the manual work, improving the upgrading experience significantly.

### BENEFITS: YOU'RE RUNNING THE LATEST VERSIONS WHICH TRANSLATES TO MORE FEATURES AND BETTER SUPPORT.

Upgrading to the latest React Native version shouldn't be different from keeping your other frameworks and libraries up to date. Apart from critical performance and security improvements, new React Native releases also address the latest underlying changes to iOS and Android. That includes the breaking changes that apply to mobile phones, such as when certain APIs get deprecated.

Here is an example: In 2019, Google announced that all Android applications submitted to Google Play after August 1, 2019 had to

be 64-bit. In order to continue developing their applications and shipping new features, developers had to upgrade to React Native 0.59 and perform the necessary adjustments.

Similar situation happened in 2023, when Google announced a new target API level requirement, which required developers to either manually update their targetSdkVersion to 33 or upgrade their React Native apps to v0.71 or higher.

Upgrades like this are really critical to keeping your users satisfied. After all, they would be disappointed if the app started to crash with the newer version of the operating system or disappeared from the App Store. There might be some additional workload associated with every release, but staying up to date will pay back with happier users, more stable apps, and a better development experience.

# PART 2 | CHAPTER 2

### HOW TO DEBUG FASTER AND BETTER WITH FLIPPER

AE4

### ESTABLISH A BETTER FEEDBACK LOOP BY IMPLEMENTING FLIPPER AND HAVE MORE FUN WHILE WORKING ON YOUR APPS.

#### ISSUE: YOU’RE USING CHROME REMOTE DEBUGGER OR SOME OTHER HACKY WAY TO DEBUG AND PROFILE YOUR REACT NATIVE APPLICATION.

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

### SPENDING MORE TIME ON DEBUGGING AND FINDING PERFORMANCE ISSUES MEANS A WORSE DEVELOPER EXPERIENCE AND LESS SATISFACTION

Unlike native developers, the ones working with React Native have access to a wide range of debugging tools and techniques. Each originates from a different ecosystem, such as iOS, Android, or JS. While it may sound great at first, you need to remember that every tool requires a different level of expertise in the native development. That makes the choice challenging for the vast majority of JavaScript developers.

Inconvenient tooling usually decreases the velocity of the team and frustrates its members. As a result, they are not as effective as they could be, affecting the quality of the app and making the releases less frequent.

#### SOLUTION: TURN ON FLIPPER AND START DEBUGGING.

Wouldn’t it be great to have one comprehensive tool to handle all of the above use cases? Of course, it would! And that’s where Flipper comes into play!

Flipper is a debugging platform for mobile apps. It also supports React Native as its first-class citizen. Launched in September

# Flipper (0.176.0)

2019, Flipper has been shipped by default with React Native since version 0.62.

### APP INSPECT

MyForkedApp

React Native

### PLUGINS

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

### BENEFITS: YOU HAVE MORE FUN WORKING WITH REACT NATIVE AND ESTABLISH A BETTER FEEDBACK LOOP.

A better debugging process makes your app development cycle faster and more predictable. As a result, your team is able to produce more reliable code and spot any kind of issues much easier.

Having all the debugging utilities in one interface is definitely ergonomic and does not disrupt any interactions with an emulator or device. The process will be less burdensome for your team and that will positively impact the velocity of the product development and bug fixing.

“Feel like a functionality is missing in Flipper? Good news! Flipper is easily extensible and has a comprehensive guide on how to write custom plugins in React. Why not build your own?”

— Alexandre Moureaux, App performance specialist at BAM

# PART 2

# | CHAPTER 3

### AVOID UNUSED NATIVE DEPENDENCIES

### IMPROVE THE TIME TO INTERACTIVE OF YOUR APP BY REMOVING THE LINKING OF UNUSED DEPENDENCIES.

#### ISSUE: YOU HAVE A LOT OF DEPENDENCIES IN YOUR PROJECT BUT YOU DON’T KNOW IF YOU NEED ALL OF THEM

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

#### SOLUTION: FIND AND REMOVE UNUSED DEPENDENCIES.

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

### BENEFITS: A SMALLER BUNDLE SIZE AND FASTER TIME TO INTERACTIVE.

Removing a few unused native dependencies ended up reducing both the size of the app bundle and TTI by around 17%. Providing only resources needed by the app can improve the Time to Interactive metric, making users less likely to uninstall your app from their devices due to excessive load time.

It’s worth remembering that although autolinking is a great and powerful feature, it can be overzealous when it comes to linking code our app doesn’t really use. Make sure to keep your dependencies up to date and clean up unused ones during refactorings.

“There are so many tricky parts to making a great native app, and to lower the barrier to entry, React Native can abstract away things that you might want to come back and check on later once you’ve got your app up and running – this ebook does a solid job of helping you understand how to really get from good to great.“

Orta Therox – CocoaPods creator, TypeScript core contributor

# PART 2 | CHAPTER 4

### OPTIMIZE YOUR APPLICATION STARTUP TIME WITH HERMES

4 2

### ACHIEVE A BETTER PERFORMANCE OF YOUR APPS WITH HERMES.

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

### LONG STARTUP TIMES AND SLOW UX CAN BE ONE OF THE REASONS YOUR APP GETS A BAD RATING AND ENDS UP BEING ABANDONED.

Creating applications that are fun to play with is extremely important, especially considering how saturated the mobile market already is. Now, all mobile apps have to be not only intuitive, they also should be pleasant to interact with.

# There is a common misconception that React Native applications come with a performance trade-off compared to their native counterparts.

The truth is that with enough attention and configuration tweaks, they can load just as fast and without any considerable difference.

#### SOLUTION: TURN ON HERMES TO BENEFIT FROM A BETTER PERFORMANCE.

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

### BYTECODE PRECOMPILATION

Typically, the traditional JavaScript VM works by parsing the JavaScript source code during the runtime and then producing the bytecode. As a result, the execution of the code is delayed until the parsing completes. It is not the same with Hermes. To reduce the time needed for the engine to execute the business logic, it generates the bytecode during the build time.

It can spend more time optimizing the bundle using various techniques to make it smaller and more efficient. For example, the generated bytecode is designed in a way so that it can be mapped in the memory without eagerly loading the entire file. Optimizing that process brings significant TTI improvements as I/O operations on mobile devices tend to increase the overall latency.

### NO JIT

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

### BENEFITS: A BETTER STARTUP TIME LEADS TO A BETTER PERFORMANCE. IT'S A NEVER-ENDING STORY.

Making your application load fast is an ongoing effort and its final result will depend on many factors. You can control some of them by tweaking both your application's configuration and the tools it uses to compile the source code.

Turning Hermes on is one of the things that you can do today to drastically improve certain performance metrics of your app, mainly the TTI.

Apart from that, you can also look into other significant improvements shipped by the Meta team. To do so, get familiar with their write-up on React Native performance. It is often a game of gradual improvements that make all the difference when applied at once. The React Native core team has created a visual report on benchmarking between stock RN and Hermes-enabled RN: see here.

As we have mentioned in the section on running the latest React Native, Hermes is one of those assets that you can leverage as long as you stay up to date with your React Native version.

Doing so will help your application stay on top of the performance game and let it run at a maximum speed.

### THE FUTURE WITH STATIC HERMES (EXPERIMENTAL)

At the React Native EU 2023 conf, the lead Hermes engineer, Tzvetan Mikov, announced an experimental tool that his team works on codenamed “Static Hermes”. It pushes what Hermes can do today with the ability to statically compile typed JavaScript code (essentially TypeScript or Flow) into native assembler instructions ahead of time. It exercises the idea that your app does not need to use Hermes or any other JavaScript engine to run, because it already has the native code inside it. That’s pretty wild.

Static Hermes is an ongoing experiment, however you can give it a try today. Read more on Hermes GitHub issue tracker: “How to try Static Hermes”

# PART 2

# | CHAPTER 5

# OPTIMIZE YOUR ANDROID APPLICATION’S SIZE WITH THESE GRADLE SETTINGS

### IMPROVE TTI AND REDUCE MEMORY USAGE

### AND THE SIZE OF YOUR APP BY ADJUSTING PROGUARD RULES TO YOUR PROJECTS.

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

### A BIGGER APK SIZE MEANS MORE TIME NEEDED TO DOWNLOAD FROM THE APP STORE AND MORE BYTECODE TO LOAD INTO MEMORY

It’s great that you and your team operate on the latest devices and have fast and stable access to the internet. But you need to remember that not everyone has the same luxury. There are still parts of the world where network accessibility and reliability are far from perfect. Projects such as Starlink already improve that situation, but that will take time to cover the most remote areas out there.

Right now, there are still markets where every megabyte of traffic has its price. In those regions, the application’s size directly impacts the conversion, and the installation/cancellation ratio increases along with the app size.

Source: https://segment.com/blog/mobile-app-size-effect-on-downloads/

It is also a common belief that every well crafted and carefully designed application not only provides a beautiful interface but is also optimized for the end device. Well, that is not always the case. And because the Android market is so competitive, there is a big chance that a smaller alternative to those beautiful yet large apps is already gaining more traction from the community.

Another important factor is device fragmentation. The Android market is very diverse in that respect. There are more than 20 popular manufacturers, each releasing an array of devices every year. Contributing to a relatively significant share of mid to low-end devices, which account for over 60% of all smartphone sales annually. And those devices may face issues when dealing with bigger APKs.

As we have stressed already, the startup time of your application is essential. The more code the device has to execute while opening up your code, the longer it takes to launch the app and make it ready for the first interaction.

Now, let’s move to the last factor worth mentioning in this context – device storage.

Apps usually end up taking up more space after the installation. Sometimes they may even not fit into the device’s memory. In such a situation, users may decide to skip installing your product if that would mean removing other resources such as applications or images.

#### SOLUTION: FLIP THE BOOLEAN FLAG

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

### APP STUOTOS

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

### BENEFITS: A SMALLER APK, SLIGHTLY FASTER TTI, AND SLIGHTLY LESS MEMORY USED.

All the mentioned steps are worth taking when you’re struggling with a growing application size. You will achieve the most significant size reduction by building the app for different architectures. But the list of possible optimizations doesn’t stop there.

By striving for a smaller APK size, you will do your best to reduce the download cancellation rate. Also, your customers will benefit from a shorter Time To Interactive and be more inclined to use the app more often.

Finally, you will demonstrate that you care about every user, not only those with top-notch devices and fast internet connections. The bigger your platform gets, the more important it is to support those minor groups, as every percent of users translates into hundreds of thousands of actual users. If you’d like to learn more about optimizing Android, check the Android Profiling chapter.

# PART 2
