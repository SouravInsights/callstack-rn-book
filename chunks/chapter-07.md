## CHAPTER 7

REPLACE LOTTIE WITH RIVE

### LEVERAGE STATE MACHINES TO PROVIDE ROBUST INTERACTIVE ANIMATIONS AT 60FPS

#### ISSUE: REAL-TIME ANIMATIONS SUFFERING FROM LOW FPS, FILE SIZE, AND NOT BEING ROBUST

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

#### SOLUTION: LEVERAGE DEVELOPER-FRIENDLY TOOLS WHICH OFFER BETTER FPS WITH LESS FILE SIZE.

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

### BENEFITS: A REDUCED REGRESSION CYCLE WHILE DEVELOPING A FEATURE AND A HAPPY USER BASE

If we opt-in to a world without state machines, the developers will be implementing the logic in their code. And each time there is a change in the interactivity of the animation, devs will be required to re-work their code. This is not a good developer experience.

Rive's state machines give designers the power to think as if they were coding and structure the state machine for an animation.

that will interact after being given a certain input. Now the developer can use that animation and implement the interactivity firing the inputs on the animation and be done with it. If this animation needs to be changed with the same inputs, the dev only needs to replace the animation source and that's it. More info here.

Almost 18.7% of people uninstall the app due to storage issues. This hurts the company's ROI. Developers should always pay attention to reducing the bundle size and the storage utilized by their app. In a tweet by Rive's CEO, the Lottie file was around 24.37 KB and the same Rive file was around 2 KB. At the end of the day, each KB saved adds up to a reduced app size. We always want to choose a library that best fulfills our needs by providing a better developer experience, ease of API, and a smooth experience for the end user.

# PART 1
