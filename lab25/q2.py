import pandas as pd


def analyze_json():
    # Automatically use the JSON file in your folder
    filename = "ODI-Batting_Cricket_Analytics(1).json"

    # Load JSON into pandas DataFrame
    df = pd.read_json(filename)
    print("\nColumn Names:")
    print(df.columns.tolist())

    # (b) Sort by ScoreRate and show top 5 players
    df_sorted = df.sort_values(by="ScoreRate", ascending=False)
    print("\nTop 5 players with highest ScoreRate:")
    print(df_sorted.head(5)[["Player", "ScoreRate"]])

    # (c) Players with minimum runs
    min_runs = df["Runs"].min()
    min_run_players = df[df["Runs"] == min_runs]["Player"].tolist()
    print(f"\nPlayers with minimum runs ({min_runs}):")
    print(min_run_players)

    # (d) Number of players with minimum runs
    print(f"\nNumber of players with minimum runs: {len(min_run_players)}")

    # (e) Players from India with above-average runs
    avg_runs = df["Runs"].mean()
    indian_above_avg = df[(df["Country"] == "India") & (df["Runs"] > avg_runs)][["Player", "Runs"]]
    print(f"\nPlayers from India with runs above average ({avg_runs:.2f}):")
    print(indian_above_avg)


if __name__ == "__main__":
    analyze_json()
