## CHAPTER 4

ALWAYS REMEMBER TO USE

LIBRARIES DEDICATED TO

THE MOBILE PLATFORM

### USE LIBRARIES DEDICATED TO MOBILE

AND BUILD FEATURES FASTER ON MANY PLATFORMS AT ONCE, WITHOUT COMPROMISING ON THE PERFORMANCE AND USER EXPERIENCE.

#### ISSUE: YOU USE WEB LIBRARIES THAT ARE NOT OPTIMIZED FOR MOBILE.

As discussed earlier, one of the best things about React Native is that you can write the mobile application with JavaScript, reuse some of your React components, and do business logic with your favorite state management library.

While React Native provides web-like functionality for compatibility with the web, it is important to understand that it is not the same environment. It has its own set of best practices, quick wins, and constraints.

For example, while working on a web application, we don’t have to worry too much about the overall CPU resources needed by our application. After all, most of the websites run on devices that are either plugged into the network or have large batteries.

It is not hard to imagine that mobile is different. There’s a wide range of devices with different architectures and resources available. Most of the time, they run on a battery and the drain caused by the application can be a deciding factor for many developers.

In other words – how you optimize the battery consumption both in the foreground and background can make all the difference.

### NOT OPTIMIZED LIBRARIES CAUSE BATTERY DRAIN AND SLOW DOWN

THE APP. THE OS MAY LIMIT YOUR APPLICATION/S CAPABILITIES.

While React Native makes it possible to run the same JavaScript on mobile as in the browser, that doesn’t mean you should be doing this every time. As with every rule, there are exceptions.

If the library depends heavily on networking, such as real-time messaging or offers the ability to render advanced graphics (3D structures, diagrams), it is very likely that you’re better off going with a dedicated mobile library.

Mobile libraries were developed within the web environment in the first place, assuming the capabilities and constraints of the browser. It is very likely that the result of using a web version of a popular SDK will result in extraneous CPU and memory consumption.

Certain OSs, such as iOS, are known to be constantly analyzing the resources consumed by the application in order to optimize the battery life. If your application is registered to perform background activities and these activities take too much of the resources, the interval for your application may get adjusted, lowering the frequency of the background updates that you initially signed up for.

#### SOLUTION: USE A DEDICATED, PLATFORM-SPECIFIC VERSION OF THE LIBRARY.

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

### BENEFITS: PROVIDE THE FASTEST AND MOST PERFORMANT SUPPORT WITH NO HARM TO THE BATTERY LIFE.

React Native is all about giving you control and freedom to choose
how you want to build your application.

For straightforward aspects and maximum reusability, you can
choose to go with the web version of the library. This will give

you access to the same features as in the browser with relatively low effort.

For advanced use cases, you can easily extend React Native with a native functionality and talk directly to the mobile SDKs. Such an escape hatch is what makes React Native extremely versatile and enterprise-ready. It allows you to build features faster on many platforms at once, without compromising on the performance and user experience – something other hybrid frameworks cannot claim.

# PART 1
