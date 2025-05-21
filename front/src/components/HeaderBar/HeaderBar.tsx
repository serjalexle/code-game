// src/components/HeaderBar.tsx
import { FC } from "react";
import { Box, Typography } from "@mui/material";

type HeaderBarProps = {
  balance: number;
  level: number;
  energy: number;
  iq: number;
};

const HeaderBar: FC<HeaderBarProps> = ({ balance, level, energy, iq }) => {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        p: 1,
        backgroundColor: "#111",
        color: "#0f0",
        fontFamily: "monospace",
        fontSize: "0.9rem",
        borderBottom: "1px solid #333",
      }}
    >
      <Box sx={{ display: "flex", gap: 3 }}>
        <Typography>💰 Balance: {balance}</Typography>
        <Typography>📈 Level: {level}</Typography>
        <Typography>🔋 Energy: {energy}</Typography>
        <Typography>🧠 IQ: {iq}</Typography>
      </Box>
    </Box>
  );
};

export default HeaderBar;
