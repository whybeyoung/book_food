from autospark_kit.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


def book(food_name):
    return "预定成功: %s" % food_name


def _query():
    return ["爆炒青椒", "炒拉面", "蛋炒饭"]


class BookFoodInput(BaseModel):
    food_name: str = Field(..., description="外卖的名称")


class BookFoodTool(BaseTool):
    """
    BookFoodTool
    """
    name: str = "Book Food Tool "
    args_schema: Type[BaseModel] = BookFoodInput
    description: str = "帮助用户预订下单的工具"

    def _execute(self, food_name: str = None):
        return book(food_name)


class QueryFoodInput(BaseModel):
    query: str = Field(..., description="外卖搜索查询条件")


class QueryFoodTool(BaseTool):
    """
    QueryFoodTool
    """
    name: str = "Query Food  Tool "
    args_schema: Type[BaseModel] = QueryFoodInput
    description: str = "一个帮助用户查询符合条件的外卖的工具"

    def _execute(self, query: str = None):
        return _query()
