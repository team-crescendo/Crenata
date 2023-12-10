from crenata.application.embeds import CrenataEmbed


def exit_embed_builder() -> CrenataEmbed:
    embed = CrenataEmbed(title="🔒 탈퇴", description="정말 탈퇴하시겠습니까?")

    return embed
