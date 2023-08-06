from abc import ABC
from autospark_kit.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from book_tool import BookFoodTool,QueryFoodTool


class BookFoodToolkit(BaseToolkit, ABC):
    name: str = "Book Food Toolkit"
    description: str = "一个外卖预订工具集"

    def get_tools(self) -> List[BaseTool]:
        return [BookFoodTool(),QueryFoodTool()]

    def get_env_keys(self) -> List[str]:
        return ["Account", "Platform"]
