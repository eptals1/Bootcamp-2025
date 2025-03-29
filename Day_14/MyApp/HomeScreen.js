import React, { useState } from "react";
import { Text, View, Button, StyleSheet } from "react-native";

const HomeScreen = ({ navigation }) => {
  const [count, setCount] = useState(0);
  return (
    <View style={styles.container}>
      <Button
        title="Green"
        onPress={() => {
          navigation.navigate("Green");
        }}
        color="green"
      />
      <Button
        title="Pink"
        onPress={() => {
          navigation.navigate("Pink");
        }}
        color="pink"
      />
      <Button
        title="Red"
        onPress={() => {
          navigation.navigate("Red");
        }}
        color="red"
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#255",
    alignItems: "center",
    justifyContent: "center",
  },
});

export default HomeScreen;
