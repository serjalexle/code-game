"use client";
import MiniMap from "@/components/MiniMap/MiniMap";
import ScriptEditor from "@/components/ScriptEditor/ScriptEditor";
import Terminal from "@/components/Terminal/Terminal";
import { FULL_MAP_MOCK } from "@/mock/map";
import { Box, Container } from "@mui/material";
import { useState } from "react";

const TerminalPage = () => {
  const [history, setHistory] = useState<string[]>([]);
  const [playerPosition, setPlayerPosition] = useState({ x: 3, y: 2 });

  const handleCommand = (input: string) => {
    const trimmed = input.trim().toLowerCase();

    switch (trimmed) {
      case "cleartext":
        setHistory([]);
        break;

      case "up":
        setPlayerPosition((prev) => ({ ...prev, y: prev.y - 1 }));
        setHistory((prev) => [...prev, `$ ${input}`, "🔼 Player moved up."]);
        break;

      case "down":
        setPlayerPosition((prev) => ({ ...prev, y: prev.y + 1 }));
        setHistory((prev) => [...prev, `$ ${input}`, "🔽 Player moved down."]);
        break;

      case "left":
        setPlayerPosition((prev) => ({ ...prev, x: prev.x - 1 }));
        setHistory((prev) => [...prev, `$ ${input}`, "◀️ Player moved left."]);
        break;

      case "right":
        setPlayerPosition((prev) => ({ ...prev, x: prev.x + 1 }));
        setHistory((prev) => [...prev, `$ ${input}`, "▶️ Player moved right."]);
        break;

      case "goal":
        setHistory((prev) => [
          ...prev,
          `$ ${input}`,
          "🚩 Checking destination...",
          "✅ Player reached the GOAL!",
          "🏆 Congratulations, you win!",
        ]);
        break;

      case "script":
        setHistory((prev) => [
          ...prev,
          `$ ${input}`,
          "📜 Script mode activated.",
          "Type multiple lines. Type '}' when done.",
          "----------------------------------------",
        ]);
        break;

      case "exit":
        setHistory((prev) => [
          ...prev,
          `$ ${input}`,
          "🚪 Exiting script mode.",
        ]);
        break;

      case "help":
        setHistory((prev) => [
          ...prev,
          `$ ${input}`,
          "💡 Available commands:",
          " ├─ up / down / left / right – move",
          " ├─ goal – celebrate",
          " ├─ script – multiline input",
          " ├─ clearText – wipe terminal",
          " └─ help – this menu",
        ]);
        break;

      default:
        setHistory((prev) => [
          ...prev,
          `$ ${input}`,
          "❌ Unknown command.",
          "Type 'help' for a list of available commands.",
        ]);
        break;
    }
  };

  return (
    <Box sx={{ backgroundColor: "#000", px: "200px" }}>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          height: "100vh",
          backgroundColor: "#000",
          gap: 2,
        }}
      >
        <Box sx={{ display: "flex", gap: 2, width: "100%" }}>
          <MiniMap
            viewSizeX={10}
            viewSizeY={10}
            playerPosition={playerPosition}
            tiles={FULL_MAP_MOCK}
          />
          <Terminal history={history} onCommandSubmit={handleCommand} />
        </Box>
        <ScriptEditor />
      </Box>
    </Box>
  );
};

export default TerminalPage;
