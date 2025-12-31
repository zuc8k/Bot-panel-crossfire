# ui/help_view.py

import discord
from services.help_service import get_available_categories

class HelpSelect(discord.ui.Select):
    def __init__(self, rank: str):
        self.rank = rank
        categories = get_available_categories(rank)

        options = [
            discord.SelectOption(
                label=data["label"],
                value=key
            )
            for key, data in categories.items()
        ]

        super().__init__(
            placeholder="اختر قسم الأوامر 📂",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        rank = self.view.rank
        categories = get_available_categories(rank)
        category = categories[self.values[0]]

        embed = discord.Embed(
            title=category["label"],
            description="\n".join(f"/{cmd}" for cmd in category["commands"]),
            color=0x2F3136
        )

        await interaction.response.edit_message(embed=embed, view=self.view)


class HelpView(discord.ui.View):
    def __init__(self, rank: str):
        super().__init__(timeout=120)
        self.rank = rank
        self.add_item(HelpSelect(rank))