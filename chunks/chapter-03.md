## CHAPTER 3

# DON’T BE AFRAID TO SHIP

### FAST WITH CONTINUOUS DEPLOYMENT

### ESTABLISH A CONTINUOUS DEPLOYMENT SETUP TO SHIP NEW FEATURES AND VERIFY CRITICAL BUGS FASTER.

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

#### SOLUTION: ESTABLISH A CONTINUOUS DEPLOYMENT SETUP THAT MAKES THE BUILD AND GENERATES THE CHANGELOG. SHIP TO YOUR USERS INSTANTLY.

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

### DEPLOYING THE BINARIES

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

### SHIP OTA (OVER-THE-AIR)

### WHEN IN AN EMERGENCY

### SUBMIT CRITICAL UPDATES AND FIXES INSTANTLY THROUGH OTA.

ISSUE: TRADITIONAL WAYS OF UPDATING APPS ARE TOO SLOW AND YOU LOSE YOUR PRECIOUS TIME ON THEM.

The traditional model of sending updates on mobile is fundamentally different from the one we know from writing JavaScript applications for other platforms. Unlike the web, mobile deployment is much more complex and comes with better security out-of-the-box. We have talked about that in detail in the previous section focused on the CI/CD.

# What does it mean for your business?

Every update, no matter how quickly shipped by your developers, is usually going to wait some time while the App Store and Play Store teams review your product against their policies and best practices.

This process is particularly challenging in all Apple platforms, where apps are often taken down or rejected, because of not following certain policies or meeting the required standard for the user interface. Thankfully, the risk of your app being rejected with React Native is reduced to a minimum, as you're working on the JavaScript part of the application. The React Native Core Team ensures that all the changes done to the framework have no impact on the success of your application's submission.

As a result, the submission process takes a while. And if you're about to ship a critical update, every minute counts.

Fortunately, with React Native, it is possible to dynamically ship your JavaScript changes directly to your users, skipping the App Store review process. This technique is often referred to as an over-the-air update. It lets you change the appearance of your

application immediately, for all the users, following the technique that you have selected.

### WHEN CRITICAL BUGS HAPPEN – MINUTES AND HOURS CAN BE CRITICAL. DON'T WAIT TO FIX YOUR END USERS' EXPERIENCE.

If your application is not OTA-ready, you risk it being left with a critical bug on many devices, for as long as Apple/Google reviews your product and allows it to be distributed.

Even though the review times have gotten much better over the years, it is still a good escape hatch to be able to immediately recover from an error that slipped through the testing pipeline and into production.

#### SOLUTION: IMPLEMENT OTA UPDATES WITH APP CENTER/ CODEPUSH OR EAS UPDATE

As mentioned earlier, React Native is OTA-ready. It means that its architecture and design choices make such updates possible. However, it doesn't ship with the infrastructure to perform such operations. To do so, you will need to integrate a 3rd-party service that carries its own infrastructure for doing so.

These are the popular ways to implement OTA into your app:

- CodePush: A service that is part of Microsoft's App Center suite.
- EAS Update: A service that is created by Expo and is part of EAS suite.

# APP CENTER/CODEPUSH

# Configuring the native side

To integrate CodePush into your application, please follow the required steps for iOS and Android, respectively. We decided to link to the official guides instead of including the steps here as they include additional native code to apply and that is very likely to change in the coming months.

### CONFIGURING THE JAVASCRIPT SIDE

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

### SHIPPING UPDATES TO THE APPLICATION

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

### BENEFITS: SHIP CRITICAL FIXES AND SOME CONTENT INSTANTLY TO THE USERS.

With OTA updates integrated into your application, you can send your JavaScript updates to all your users in a matter of minutes. This possibility may be crucial for fixing significant bugs or sending instant patches.

For example, it may happen that your backend will stop working and it causes a crash at startup. It may be a mishandled error – you

never had a backend failure during the development and forgot to handle such edge cases.

You can fix the problem by displaying a fallback message and informing users about the problem. While the development will take you around one hour, the actual update and review process can take hours if not days. With OTA updates set up, you can react to this in minutes without risking the bad UX that will affect the majority of users.

# PART 3

# | CHAPTER 5

### MAKE YOUR APP CONSISTENTLY FAST

### USE THE DMAIC PROCESS TO HELP YOU PREVENT REGRESSING ON APP PERFORMANCE

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

### TESTING REGRESSIONS AS A PART OF THE DEVELOPMENT PROCESS

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

### KNOW HOW TO PROFILE IOS

30

### IMPROVE YOUR APP WITH REAL-TIME METRICS

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

### IOS INSTRUMENTS

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

#### SOLUTION: COMBINING WITH A TOOL SPECIFIC FOR JS CONTEXT TRACKING.

Let’s use Flipper, the same one that we used in Pay Attention to UI re-renders, but we are going to use another monitor called Hermes Debugger (RN). With the app open and running, we go to Flipper, select the running app if not selected already, and go to Hermes Debugger (RN) –> Profiler

### APP INSPECT

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

### BENEFITS: HAVING A FASTER AND MORE RESPONSIVE APP.

70% of the users will leave the app if the response to a given action takes too long. Profiling our apps has become one of the main steps in our development life cycle. Using specific tools like Time Profiler will help us understand if our app is responding fast or where we could find areas of improvement. Remember, users are becoming more sensitive to speed and delays, even a 0.1 sec of improvement can increase a conversion rate by 10.1%.

# PART 3

# | CHAPTER 7

### KNOW HOW TO

### PROFILE ANDROID

### GET REAL-TIME METRICS TO BETTER YOUR APP UNDERSTANDING

#### ISSUE: YOU ENCOUNTER A PERFORMANCE ISSUE THAT COMES DIRECTLY FROM ANDROID RUNTIME.

In the event of any performance issues, we mostly use React Profiler to troubleshoot and resolve our problems. Since most of the performance problems originate from the JS realm, we don’t usually need to do anything beyond that. But sometimes we’ll encounter a bug or performance issue that comes directly from the Android runtime. In such a case, we’ll need a fine tool to help us gather the following metrics from the device:

- CPU
- memory
- network
- battery usage

Based on that data, we can check whether our app consumes more energy than usual or in some cases, uses more CPU power than it should. It is useful especially to check the executed code on lower-end (LE) Android devices. Some algorithms can run faster on some devices and the end user will not spot any glitches, but we have to remember, some customers can use LE devices and the algorithm or function can be too heavy for their phones. High-end devices will handle it because their hardware is powerful.

#### SOLUTION: PROFILE YOUR APP WITH ANDROID PROFILER IN ANDROID STUDIO

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

### USE ANDROID PROFILER IN ACTION

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

### SYSTEM TRACING

Using the Android Studio CPU Profiler, we can also make a system tracing. We can check when the appropriate function has been called. We can triage all threads and see which function is the costliest which affects the UX. To enable system tracing, click on the CPU section and select System Trace Recording.

Profiler com.pagerviewexample (Motorola Moto X4)

### SESSIONS

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

### FLIPPER PERFORMANCE PLUGIN FOR ANDROID

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

### BENEFITS: REAL-TIME METRICS WILL IMPROVE YOUR APP UNDERSTANDING

As stated above, users will abandon your app if the response time is too long. Using specific tools will help you understand the root cause of the app’s performance issue.

### THANK YOU

We hope that you found the aforementioned best practices for React Native optimization useful and that they will make your work easier. We did our best to make this guide comprehensive and describe both the technical and business aspects of the optimization process.

If you enjoyed it, don’t hesitate to share it with your friends who also use React Native in their projects.

### IF YOU HAVE MORE QUESTIONS OR NEED HELP WITH CROSS- PLATFORM OR REACT NATIVE DEVELOPMENT, WE WILL BE HAPPY TO PROVIDE A FREE CONSULTATION.

JUST CONTACT US!

### AUTHORS

# MICHAŁ PIERZCHAŁA

As Head of Technology at Callstack, he is passionate about building mobile and web experiences, high-quality JS tooling, and Open Source. Core Jest and React Native community contributor. Space exploration enthusiast.

twitter.com/thymikee

github.com/thymikee

### JAKUB BUJKO

With multiple years of delving deep into react.js development in his pocket, Kuba went on to master mobile development. Passionate about edge technologies, clean and minimalistic code, and charting the paths for the future of React and React Native development.

twitter.com/f3ng

github.com/Xiltyn

# MACIEJ JASTRZĘBSKI

React &#x26; React Native developer with multiple years of experience building native iOS and Android apps. Passionate about building robust and delightful apps along with writing well-architected and readable code. Loves learning new things. He likes to travel in his free time, hike in the mountains, and take photographs.

twitter.com/mdj_dev

github.com/mdjastrzebski

# Team Members

### PIOTR TROCKI

Software developer who started his journey from mobile apps. Now Piotr is focused on mastering both Native (Android, iOS) and React Native technologies in brownfield applications. When not coding, he spends his free time on the dance floor.

twitter.com/Tr0zZe

github.com/troZee

### JAKUB BINDA

A dedicated software developer who pays a lot of attention to the details in every task he does. Always committed and eager to learn, Kuba likes to create things and dive into how they work. A father of two and a husband to the woman of his life. Those two roles motivate him the most and give him the strength to move mountains.

github.com/jbinda

### SZYMON RYBCZAK

Szymon is a 17-year-old React Native Developer with three years of experience and currently doing mobile app development at Callstack. In his free time, he likes to discover new and interesting technologies.

github.com/szymonrybczak

twitter.com/SzymonRybczak

### HUR ALI

TypeScript enthusiast mastering the React-Native and Native realm. He feels best in diving deep with mobile tech, making proof-of-concept projects, and experimenting with new technologies. In his free time, he enjoys playing FIFA and contribution to OSS.

twitter.com/hurali97

github.com/hurali97

# Team Members

# OSKAR KWAŚNIEWSKI

React Native Developer at Callstack. Currently, he’s strengthening his knowledge of native development and making some OSS contributions. During his free time, he enjoys riding a bike, going to the gym, and playing video games.

github.com/okwasniewski

twitter.com/o_kwasniewski

### TOMASZ MISIUKIEWICZ

React Native Developer at Callstack with a strong background in web development. Big fan of keeping the code clean and simple. Loves to learn new stuff and enhance his programming skillset every day.

github.com/TMisiukiewicz

### EDUARDO GRACIANO

Senior mobile developer at Callstack. Hacking almost all kinds of mobile tech and always looking forward to making readable and maintainable code without messing up everything.

github.com/gedu

twitter.com/teddydroid07

### ANDREW ANDILEVKO

React Native developer with a background in Android development. He likes complex tasks to constantly expand his expertise and knowledge. He spends his free time with his wife and pug.

github.com/andrewworld

# Team Members

### JAMES IDE

I work on Expo, which I co-founded with Charlie Cheever when we wanted to make it easier to make and use universal mobile apps that run everywhere.

https://github.com/ide

https://twitter.com/JI

### GRZEGORZ KRUK

Senior Frontend Developer with years of experience in building mobile and web solutions in multiple frameworks and libraries. After mastering web development, he’s become passionate about building beautiful and neat mobile solutions in React Native.

https://github.com/grzegorzkruk

### KANSTANTSIN KIYKO

JavaScript expert with experience in mobile and web apps development. Has a can-do attitude, loves to solve complex problems and automate things.

https://twitter.com/xfozzyx

https://github.com/sneakyechidna

### JACEK PACIOREK

React Native Developer at Callstack with full stack development background. Loves to explore boundaries between software and hardware and tinkering with IoT devices. Likes a good challenge and gets stuff done. Besides that, he is obsessed with cars – loves driving them, fixing them up and sharing his passion with others. Also tries to stay active by skiing and sailing.

https://github.com/booua

### ABOUT CALLSTACK

Callstack is the Total Software Engineering consultancy that develops high-performing cross-platform apps set in the React Universe. We work with global enterprise clients such as PwC, Major League Soccer and AutoZone, and fast-growing startups and SMEs like Evernote and Coinmine.

We build apps in the React Universe: an approach that leverages React-based full-stack, cross-platform tech stack to create better, faster apps, smoother running teams, and lower operational costs.

Ever since the company’s beginning, we’ve been an active part of the community the co-creators of React Native. We make free Open Source tools and libraries that help millions of developers globally build better-performing apps quicker and easier. Projects like Reassure, Re.Pack or React Native Testing Library were born from the belief that (code) sharing is caring and proved invaluable in improving developer and user experience alike.

We also help raise industry standards by training developers around the world through business and technology podcasts, articles, and events like React Universe Conf (formerly React Native EU) and React Conf.
