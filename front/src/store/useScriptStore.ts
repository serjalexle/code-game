import { create } from "zustand";
import { persist } from "zustand/middleware";

export type Script = {
  name: string;
  code: string;
};

type ScriptStore = {
  scripts: Script[];
  addScript: (script: Script) => void;
  removeScript: (name: string) => void;
  getScriptByName: (name: string) => Script | undefined;
};

export const useScriptStore = create<ScriptStore>()(
  persist(
    (set, get) => ({
      scripts: [],

      addScript: (newScript) =>
        set((state) => {
          const withoutDuplicates = state.scripts.filter(
            (s) => s.name !== newScript.name
          );
          return { scripts: [...withoutDuplicates, newScript] };
        }),

      removeScript: (name) =>
        set((state) => ({
          scripts: state.scripts.filter((s) => s.name !== name),
        })),

      getScriptByName: (name) =>
        get().scripts.find((script) => script.name === name),
    }),
    {
      name: "script-storage", // ключ у localStorage
    }
  )
);
