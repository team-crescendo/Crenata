from crenata.utils.discord import CrenataEmbed


def major_info_embed_builder() -> CrenataEmbed:
    embed = CrenataEmbed()
    embed.title = "특성화고 또는 특목고인것으로 추정됩니다."
    embed.description = "아래에서 귀하의 학교학과를 선택해주세요."
    return embed