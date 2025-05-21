// src/components/MiniMap.tsx
import { FC } from 'react';
import { Box, Tooltip } from '@mui/material';

export type TileType = 'empty' | 'wall' | 'goal' | 'unknown' | 'player';

export type IProps = {
  viewSizeX: number;
  viewSizeY: number;
  playerPosition: { x: number; y: number };
  tiles: TileType[][];
  tileSize?: number;
};

const tileColors: Record<TileType, string> = {
  empty: '#2a2a2a',
  wall: '#c62828',
  goal: '#fbc02d',
  unknown: '#111',
  player: '#00e676', // лишається тільки для підсвітки
};

const MiniMap: FC<IProps> = ({
  viewSizeX = 10,
  viewSizeY = 10,
  playerPosition,
  tiles,
  tileSize = 28,
}) => {
  const getTile = (x: number, y: number): TileType => {
    const globalX = playerPosition.x + x;
    const globalY = playerPosition.y + y;

    if (globalX === playerPosition.x && globalY === playerPosition.y) {
      return 'player';
    }

    if (
      globalY < 0 ||
      globalY >= tiles.length ||
      globalX < 0 ||
      globalX >= tiles[0].length
    ) {
      return 'unknown';
    }

    return tiles[globalY][globalX];
  };

  return (
    <Box
      sx={{
        display: 'grid',
        gridTemplateColumns: `repeat(${viewSizeX}, ${tileSize}px)`,
        gridTemplateRows: `repeat(${viewSizeY}, ${tileSize}px)`,
        gap: '2px',
        backgroundColor: '#1a1a1a',
        padding: 1,
        borderRadius: 2,
        boxShadow: '0 0 4px #000',
      }}
    >
      {Array.from({ length: viewSizeY }, (_, y) =>
        Array.from({ length: viewSizeX }, (_, x) => {
          const localX = x - Math.floor(viewSizeX / 2);
          const localY = y - Math.floor(viewSizeY / 2);
          const type = getTile(localX, localY);

          const isPlayer = type === 'player';

          return (
            <Tooltip
              key={`${x}-${y}`}
              title={`[${playerPosition.x + localX}, ${playerPosition.y + localY}] - ${type}`}
            >
              <Box
                sx={{
                  width: tileSize,
                  height: tileSize,
                  backgroundColor: isPlayer ? tileColors['player'] : tileColors[type],
                  border: '1px solid #333',
                  borderRadius: isPlayer ? '50%' : '4px',
                  transition: 'background-color 0.2s ease',
                  animation: isPlayer ? 'pulse 1.2s infinite' : undefined,
                  '@keyframes pulse': {
                    '0%': { boxShadow: '0 0 0 0 rgba(0, 230, 118, 0.5)' },
                    '70%': { boxShadow: '0 0 0 10px rgba(0, 230, 118, 0)' },
                    '100%': { boxShadow: '0 0 0 0 rgba(0, 230, 118, 0)' },
                  },
                }}
              />
            </Tooltip>
          );
        })
      )}
    </Box>
  );
};

export default MiniMap;
