from typing import Literal, Optional

from discord import app_commands

from crenata.typing import CrenataInteraction


@app_commands.command()  # pyright: ignore [reportGeneralTypeIssues]
async def meal(
    interaction: CrenataInteraction,
    school_name: Optional[str],
    meal_time: Literal["조식", "중식", "석식"] = "중식",
    date: Optional[str] = None,
) -> None:
    if school_name:
        results = await interaction.client.crenata_neispy.search_school(school_name)
    ...
    

