# systems/gp_utils.py

def gp_rank(gp: int):
    if gp < 1_000:
        return "🟤 Beginner"
    elif gp < 10_000:
        return "🟢 Normal"
    elif gp < 50_000:
        return "🔵 Advanced"
    elif gp < 100_000:
        return "🟣 Pro"
    elif gp < 500_000:
        return "🟠 Expert"
    else:
        return "🟡 Legendary"