import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, Button } from "react-native";

export default function GreenScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text>GREEN</Text>
      <Button
        title="Go to Home"
        onPress={() => {
          navigation.navigate("Home");
        }}
      />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "green",
    alignItems: "center",
    justifyContent: "center",
  },
});
