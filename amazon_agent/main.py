import time
from rich.console import Console
from rich.prompt import Prompt
from graphs.market_graph import market_graph

console = Console()


def main():
    console.print("\n[bold cyan] ECHELON AI [/bold cyan]")

    query = Prompt.ask("[bold yellow]Araştırma hedefini girin[/bold yellow]")
    if not query.strip():
        return

    start_time = time.time()

    initial_state = {
        "query": query,
        "enhanced_query": "",
        "raw_web_data": [],
        "competitors": [],
        "errors": []
    }

    try:
        with console.status("[bold green]ZONARA Ajanları Paralel Olarak Çalışıyor...[/]"):
            result = market_graph.invoke(initial_state)

        elapsed = round(time.time() - start_time, 1)
        console.print(f"\n[bold green]✅ Analiz {elapsed} saniyede tamamlandı![/bold green]\n")

        if result.get("errors"):
            console.print("[bold red]Sistem Uyarıları:[/bold red]")
            for err in result["errors"]:
                console.print(f"- {err}")

        console.print(result.get("final_report", "Rapor oluşturulamadı."))

    except Exception as e:
        console.print(f"\n[bold red]❌ Kritik Hata:[/bold red] {e}")


if __name__ == "__main__":
    main()