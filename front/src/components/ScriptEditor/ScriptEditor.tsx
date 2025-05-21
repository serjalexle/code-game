// src/components/ScriptEditor.tsx
"use client";

import { FC, useState } from "react";
import { Box, TextField, Button, Typography, Paper } from "@mui/material";
import dynamic from "next/dynamic";
import { useScriptStore } from "@/store/useScriptStore";

const MonacoEditor = dynamic(() => import("@monaco-editor/react"), {
  ssr: false,
});

const ScriptEditor: FC = () => {
  const [scriptName, setScriptName] = useState("");
  const [code, setCode] = useState("// Write your script here");
  const [error, setError] = useState("");

  const { addScript } = useScriptStore();

  const handleSave = () => {
    if (!scriptName.trim()) {
      setError("Script must have a name.");
      return;
    }
    if (!code.trim()) {
      setError("Script cannot be empty.");
      return;
    }

    addScript({ name: scriptName.trim(), code });
    setScriptName("");
    setCode("// Write your script here");
    setError("");
  };

  return (
    <Paper sx={{ p: 3, backgroundColor: "#1e1e1e", color: "#fff", width: "100%" }}>
      <Typography variant="h6" gutterBottom>
        ✍️ Script Editor
      </Typography>

      <Box sx={{ mb: 2 }}>
        <TextField
          label="Script Name"
          variant="outlined"
          fullWidth
          size="small"
          sx={{
            maxWidth: "300px",
          }}
          value={scriptName}
          onChange={(e) => setScriptName(e.target.value)}
        />
      </Box>

      <Box
        sx={{
          border: "1px solid #444",
          borderRadius: 1,
          overflow: "hidden",
          mb: 2,
        }}
      >
        <MonacoEditor
          height="300px"
          language="javascript"
          value={code}
          onChange={(v) => setCode(v || "")}
          theme="vs-dark"
          options={{ minimap: { enabled: false } }}
        />
      </Box>

      {error && (
        <Typography color="error" sx={{ mb: 1 }}>
          {error}
        </Typography>
      )}

      <Button variant="contained" color="success" onClick={handleSave}>
        💾 Save Script
      </Button>
    </Paper>
  );
};

export default ScriptEditor;
