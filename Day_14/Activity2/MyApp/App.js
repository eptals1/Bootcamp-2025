import HomeScreen from "./HomeScreen.js";
import DetailsScreen from "./DetailsScreen.js";
import GreenScreen from "./Screens/GreenScreen.js";
import PinkScreen from "./Screens/PinkScreen.js";
import RedScreen from "./Screens/RedScreen.js";

import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer } from "@react-navigation/native";

const Stack = createStackNavigator();
export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
        <Stack.Screen name="Green" component={GreenScreen} />
        <Stack.Screen name="Pink" component={PinkScreen} />
        <Stack.Screen name="Red" component={RedScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
