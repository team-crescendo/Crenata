# pyright: reportUnknownMemberType=false
import asyncio
from datetime import datetime
from io import BytesIO
from typing import Any, Optional, Sequence

import matplotlib  # type: ignore[import]
import numpy as np
import pandas as pd  # type: ignore[import]

matplotlib.use("Agg")
from matplotlib import font_manager
from matplotlib import pyplot as plt
from matplotlib.figure import Figure  # type: ignore[import]

from crenata.utils.datetime import to_datetime, to_weekday

font_path = "./crenata/fonts"
font_files = font_manager.findSystemFonts(font_path)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

plt.rcParams["font.family"] = "NanumBarunGothic"


# 고마워요 스택오버플로우!
# https://stackoverflow.com/a/39358752
def render_mpl_table(
    data: pd.DataFrame,
    date: datetime,
    col_width: float = 3.0,
    row_height: float = 0.625,
    font_size: float = 14,
    header_color: str = "#56af6b",
    row_colors: list[str] = ["#f1f1f2", "w"],
    edge_color: str = "w",
    highlight_color: list[str] = ["#9ADFAA", "#82CF94"],
    bbox: list[int] = [0, 0, 1, 1],
    header_columns: int = 0,
    ax: Optional[plt.Axes] = None,
    **kwargs: Any
) -> tuple[Figure, plt.Axes]:
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array(
            [col_width, row_height]
        )
        fig, ax = plt.subplots(figsize=size)
        ax.axis("off")

    mpl_table = ax.table(
        cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs
    )
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    current_weekday_position: Optional[Sequence[int]] = None

    for k, cell in mpl_table.get_celld().items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight="bold", color="w")
            # if cell text is current weekday
            cell_text = cell.get_text().get_text()
            if cell_text == to_weekday(date):
                current_weekday_position = k
                cell.set_text_props(weight="bold", color="#000000")
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0] % len(row_colors)])

    # 요일에 맞는 시간표가 없을 경우 종료
    if not current_weekday_position:
        return ax.get_figure(), ax
    # 현재 요일에 맞는 시간표 하이라이팅
    for k, cell in mpl_table.get_celld().items():
        # 인덱스 컬럼은 무시한다.
        if k[0] == 0:
            continue
        if current_weekday_position[1] == k[1]:
            cell.set_facecolor(highlight_color[k[0] % len(highlight_color)])

    return ax.get_figure(), ax


async def make_timetable_image(results: list[list[Any]], date: datetime) -> BytesIO:
    """
    시간표를 이미지로 변환합니다.
    """
    r = results[0][0]
    image = BytesIO()

    df = pd.DataFrame()
    for result in results:
        timetable: list[Any] = []
        day = ""
        for r in result:
            timetable.append(r.ITRT_CNTNT)
            day = to_weekday(to_datetime(r.ALL_TI_YMD))

        tmp = pd.DataFrame({day: timetable})
        df = pd.concat([df, tmp], axis=1)

    df.index += 1
    df.fillna("", inplace=True)

    pd.set_option(
        "colheader_justify",
        "center",
    )
    fig, _ = render_mpl_table(df, date, cellLoc="center", font_size=16)
    await asyncio.to_thread(
        fig.savefig, image, format="png", bbox_inches="tight", dpi=350
    )
    image.seek(0)
    return image
