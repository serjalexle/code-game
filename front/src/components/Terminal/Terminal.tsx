import { FC, useState, KeyboardEvent } from "react";
import { Box, Typography, InputBase, Paper } from "@mui/material";

type TerminalProps = {
  onCommandSubmit: (input: string) => void;
  history: string[];
  prompt?: string;
};

const Terminal: FC<TerminalProps> = ({
  onCommandSubmit,
  history,
  prompt = "$",
}) => {
  const [input, setInput] = useState("");
  const [commandHistory, setCommandHistory] = useState<string[]>([]);
  const [historyIndex, setHistoryIndex] = useState<number | null>(null);

  const [isScriptMode, setIsScriptMode] = useState(false);
  const [scriptLines, setScriptLines] = useState<string[]>([]);

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      if (isScriptMode) {
        if (input.trim() === "}") {
          // Закінчення скрипта
          const fullScript = scriptLines.join("\n");
          onCommandSubmit(fullScript);
          setScriptLines([]);
          setIsScriptMode(false);
        } else {
          setScriptLines((prev) => [...prev, input]);
        }
        setInput("");
        return;
      }

      if (input.trim().toLowerCase() === "clear") {
        onCommandSubmit("__CLEAR__");
        setInput("");
        return;
      }

      if (input.trim() === "script {") {
        setIsScriptMode(true);
        setScriptLines([]);
        setInput("");
        return;
      }

      onCommandSubmit(input);
      setCommandHistory((prev) => [...prev, input]);
      setHistoryIndex(null);
      setInput("");
    }

    if (e.key === "ArrowUp") {
      e.preventDefault();
      if (commandHistory.length === 0) return;
      const nextIndex =
        historyIndex === null
          ? commandHistory.length - 1
          : Math.max(0, historyIndex - 1);
      setInput(commandHistory[nextIndex]);
      setHistoryIndex(nextIndex);
    }

    if (e.key === "ArrowDown") {
      e.preventDefault();
      if (commandHistory.length === 0) return;
      if (historyIndex === null) return;
      const nextIndex = historyIndex + 1;
      if (nextIndex >= commandHistory.length) {
        setInput("");
        setHistoryIndex(null);
      } else {
        setInput(commandHistory[nextIndex]);
        setHistoryIndex(nextIndex);
      }
    }
  };

  return (
    <Paper
      onClick={() => document.querySelector("input")?.focus()}
      sx={{
        bgcolor: "#121212",
        color: "#00ff00",
        p: 2,
        minHeight: 300,
        width: "100%",
        display: "flex",
        flexDirection: "column",
        overflow: "hidden",
        fontFamily: "monospace",
        borderRadius: 2,
        minWidth: 800,
        maxHeight: 300,
      }}
      elevation={4}
    >
      <Box sx={{ flexGrow: 1, overflowY: "auto", mb: 1 }}>
        {history.map((line, index) => (
          <Typography key={index} sx={{ whiteSpace: "pre-wrap" }}>
            {line}
          </Typography>
        ))}
      </Box>
      <Box sx={{ display: "flex", alignItems: "center" }}>
        <Typography sx={{ mr: 1 }}>{isScriptMode ? ">" : prompt}</Typography>
        <InputBase
          fullWidth
          autoFocus
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          sx={{
            color: "#00ff00",
            fontFamily: "monospace",
          }}
        />
      </Box>
    </Paper>
  );
};

export default Terminal;
