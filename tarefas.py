def adicionar(self, nome, prioridade="normal"):
        self.lista.append({
            "nome": nome,
            "concluida": False,
            "prioridade": prioridade
        })

def listar(self):
        if not self.lista:
            print("Nenhuma tarefa cadastrada.")
            return
        for i, t in enumerate(self.lista, 1):
            s = "✓" if t["concluida"] else "○"
            p = t.get("prioridade", "normal")
            print(f"{i}. [{s}] {t['nome']} ({p})")