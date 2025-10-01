from mcp.server.fastmcp import FastMCP

mcp = FastMCP("chess.com")

from chess.chess_api import get_player_profile, get_player_stats, get_recent_games

@mcp.tool()
def get_chess_player_profile(username: str):
    """Fetches the profile of a chess player by username."""
    return get_player_profile(username)

@mcp.tool()
def get_chess_player_stats(username: str):
    """Fetches the statistics of a chess player by username."""
    return get_player_stats(username)   

@mcp.tool()
def get_chess_recent_games(username: str):
    """Fetches the recent games of a chess player by username."""
    return get_recent_games(username)   

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()