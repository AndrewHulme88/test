import dataclasses
import uuid
from typing import List, Optional

@dataclasses.dataclass
class ShoppingList:
    id: Optional[str] = None
    name: Optional[str] = None
    items: Optional[List['ShoppingListItem']] = None

@dataclasses.dataclass
class ShoppingListItem:
    id: Optional[str] = None
    name: Optional[str] = None
    quantity: Optional[int] = None
    unit: Optional[str] = None
    purchased: Optional[bool] = None
    category: Optional[str] = None
    notes: Optional[str] = None
    priority: Optional[str] = None

# Mock database
lists_db = {}

def generate_id() -> str:
    return str(uuid.uuid4())

def createList(id: Optional[str] = None, name: Optional[str] = None, items: Optional[List[ShoppingListItem]] = None) -> ShoppingList:
    if id is None:
        id = generate_id()
    if id in lists_db:
        raise ValueError("List ID already exists.")
    shopping_list = ShoppingList(id=id, name=name, items=items or [])
    lists_db[id] = shopping_list
    return shopping_list

def getAllLists() -> List[ShoppingList]:
    return list(lists_db.values())

def updateListItems(
    list_id: str,
    item_ids: str,
    name: Optional[str] = None,
    quantity: Optional[int] = None,
    unit: Optional[str] = None,
    purchased: Optional[bool] = None,
    category: Optional[str] = None,
    notes: Optional[str] = None,
    priority: Optional[str] = None,
) -> ShoppingList:
    if list_id not in lists_db:
        raise ValueError("Shopping list ID not found.")

    shopping_list = lists_db[list_id]
    item_ids = item_ids.split(',')

    for item in shopping_list.items:
        if item.id in item_ids:
            if name is not None:
                item.name = name
            if quantity is not None:
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                item.quantity = quantity
            if unit is not None:
                item.unit = unit
            if purchased is not None:
                item.purchased = purchased
            if category is not None:
                item.category = category
            if notes is not None:
                item.notes = notes
            if priority is not None:
                if priority not in {"high", "medium", "low"}:
                    raise ValueError("Invalid priority level.")
                item.priority = priority

    return shopping_list

shopWellList.createList(
    id="f866d78a-4ff0-4a60-a443-530eb2f53a7c",
    name="Grocery, Shopping",
    items=[
        ShoppingListItem(
            id="1",
            name="Milk",
            quantity=1,
            unit="gallon",
            purchased=False,
            category="dairy",
            notes="Get, the lactose-free, kind",
            priority="high",
        ),
        ShoppingListItem(
            id="2",
            name="Eggs",
            quantity=1,
            unit="dozen",
            purchased=False,
            category="dairy",
            notes=None,
            priority="medium",
        ),
    ],
)
