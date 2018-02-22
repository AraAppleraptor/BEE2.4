from collections import namedtuple
from tkinter.font import Font

from tkinter import (
    ttk, PhotoImage, Toplevel, Event, Misc, PanedWindow, Canvas,
    Menu,
    IntVar,
)

from enum import Enum

from richTextBox import tkRichText
from sound import SamplePlayer
from srctools import Vec, FileSystemChain
from typing import (
    NamedTuple, Optional, Union, Tuple, List, Dict, Any,
    Callable, Iterable,
)

from tkMarkdown import MarkdownData
from tk_tools import HidingScroll


class NAV_KEYS(Enum):
    """Enum representing keys used for shifting through items.

    The value is the TK key-sym value.
    """
    UP: str = ...
    DOWN: str = ...
    LEFT: str = ...
    RIGHT: str = ...
    DN: str = ...
    LF: str = ...
    RT: str = ...
    PG_UP: str = ...
    PG_DOWN: str = ...
    HOME: str = ...
    END: str = ...
    ENTER: str = ...
    PLAY_SOUND: str = ...

class AttrTypes(Enum):
    """The type of labels used for selectoritem attributes."""
    STR: str = ...
    STRING: str = ...
    LIST: str = ...
    BOOL: str = ...
    COLOR: str = ...
    COLOUR: str = ...

_Attr_Values = Union[str, list, bool, Vec]

class AttrDef(tuple):
    """The definition for attributes."""
    id: str
    type: AttrTypes
    desc: str
    default: _Attr_Values

    def __new__(
            cls,
            id: str,
            desc='',
            default: Optional[Union[str, list, bool, Vec]]=None,
            type=AttrTypes.STRING,
        ) -> 'AttrDef': ...

    def __init__(self,
        id: str,
        desc='',
        default: Optional[Union[str, list, bool, Vec]]=None,
        type=AttrTypes.STRING,
    ): super().__init__()

    # Generated from AttrTypes, so we need stubs...
    @classmethod
    def string(cls, id: str, desc='', default: str=None) -> 'AttrDef':
        """An alternative constructor to create string-type attrs."""

    @classmethod
    def list(cls, id: str, desc='', default: list=None) -> 'AttrDef':
        """An alternative constructor to create list-type attrs."""

    @classmethod
    def bool(cls, id: str, desc='', default: bool=None) -> 'AttrDef':
        """An alternative constructor to create bool-type attrs."""

    @classmethod
    def color(cls, id: str, desc='', default: Vec=None) -> 'AttrDef':
        """An alternative constructor to create color-type attrs."""

SelitemData = namedtuple('SelitemData', 'name, short_name, auth, icon, large_icon, desc, group, sort_key')

class GroupHeader(ttk.Frame):
    parent: selWin = ...
    sep_left: ttk.Separator = ...
    title: ttk.Label = ...
    sep_right: ttk.Separator = ...
    arrow: ttk.Label = ...
    _visible: bool = ...

    def __init__(self, win: selWin, title: str) -> None: ...

    @property
    def visible(self) -> bool: ...
    @visible.setter
    def visible(self, value: bool): ...

    def toggle(self, e: Optional[Event] = ...): ...
    def hover_start(self, e: Optional[Event] = ...): ...
    def hover_end(self, e: Optional[Event] = ...): ...

def get_icon(
    icon: Optional[str],
    size: Union[float,
    Tuple[float, float]],
    err_icon: PhotoImage,
) -> PhotoImage: ...

class Item:
    name: str = ...
    shortName: str = ...
    group: Optional[str] = ...
    longName: str = ...
    sort_key: Optional[str] = ...
    context_lbl: str = ...
    icon: PhotoImage = ...
    large_icon: PhotoImage = ...
    desc: MarkdownData = ...
    snd_sample: Optional[str] = ...
    authors: List[str] = ...
    attrs: Dict[str, _Attr_Values] = ...
    button: ttk.Button = ...
    win: Toplevel = ...
    win_x: int = ...
    win_y: int = ...

    def __init__(
        self,
        name: str,
        short_name: str,
        long_name: str=None,
        icon: str=None,
        large_icon: str=None,
        authors: List[str]=None,
        desc: Union[MarkdownData, str]='',
        group: str=None,
        sort_key: str=None,
        attributes: Dict[str, _Attr_Values]=None,
        snd_sample: str=None,
    ) -> None: ...

    @classmethod
    def from_data(cls: Any, obj_id: Any, data: SelitemData, attrs: Any=...) -> Any: ...
    def set_pos(self, x: Optional[Any] = ..., y: Optional[Any] = ...): ...
    def copy(self) -> 'Item': ...

class selWin:
    noneItem: Optional[Item] = ...
    display: Any = ...
    disp_label: Any = ...
    disp_btn: Any = ...
    chosen_id: Any = ...
    callback: Optional[Callable[..., None]] = ...
    callback_params: List[Any] = ...
    suggested: Optional[Item] = ...
    has_def: bool = ...
    description: Optional[str] = ...
    readonly_description: Optional[str] = ...
    item_list: List[Item] = ...
    selected: Item = ...
    orig_selected: Item = ...
    parent: Toplevel = ...
    modal: bool = ...
    win: Toplevel = ...
    group_widgets: Dict[str, GroupHeader] = ...
    group_names: Dict[str, str] = ...
    grouped_items: Dict[str, List[Item]] = ...
    group_order: List[str] = ...
    item_width: int = ...
    desc_label: ttk.Label = ...
    pane_win: PanedWindow = ...
    wid_canvas: Canvas = ...
    pal_frame: ttk.Frame = ...
    wid_scroll: HidingScroll = ...
    sugg_lbl: Union[ttk.Label, ttk.LabelFrame] = ...
    prop_frm: ttk.Frame = ...
    prop_icon_frm: ttk.Frame = ...
    prop_icon: ttk.Label = ...
    prop_name: ttk.Label = ...
    samp_button: ttk.Button = ...
    sampler: SamplePlayer = ...
    prop_author: ttk.Label = ...
    prop_desc_frm: ttk.Frame = ...
    prop_desc: tkRichText = ...
    prop_scroll: HidingScroll = ...
    prop_reset: ttk.Button = ...
    context_menu: Menu = ...
    norm_font: Font = ...
    sugg_font: Font = ...
    mouseover_font: Font = ...
    context_var: IntVar = ...
    context_menus: Dict[str, Menu] = ...
    attr: Optional[Dict[str, ttk.Label]] = ...

    def __init__(
        self,
        tk: Toplevel,
        lst: List[Item],
        *,
        has_none: bool=...,
        has_def: bool=...,
        sound_sys: FileSystemChain=...,
        modal: bool=...,
        none_desc: Union[str, MarkdownData]=...,
        none_attrs: Dict[str, _Attr_Values]=...,
        title: Any=...,
        desc: Optional[str]=...,
        readonly_desc: Optional[str]=...,
        callback: Callable[..., None]=...,
        callback_params: List[Any]=...,
        attributes: Iterable[AttrDef]=...,
    ) -> None: ...

    def widget(self, frame: Misc) -> ttk.Entry: ...

    @property
    def readonly(self) -> bool: ...
    @readonly.setter
    def readonly(self, value: bool): ...
    _readonly: bool = ...

    def exit(self, event: Event = ...): ...
    def save(self, event: Event = ...): ...
    def set_disp(self, event: Event = ...): ...
    def rollover_suggest(self): ...
    def open_win(self, e: Event = ..., force_open: bool = ...): ...
    def open_context(self, e: Event): ...
    def sel_suggested(self): ...
    def do_callback(self): ...
    def sel_item_id(self, it_id: str): ...
    def sel_item(self, item: Item, event: Event=...) -> None: ...
    def key_navigate(self, event: Event): ...

    def _offset_select(
        self,
        group_list: List[str],
        group_ind: int,
        item_ind: int,
        is_vert: bool=False,
    ) -> None: ...

    def flow_items(self, e: Event = None): ...
    def scroll_to(self, item: Item) -> None: ...
    def __contains__(self, obj: Union[str, Item]): ...
    def is_suggested(self) -> bool: ...
    def set_context_font(self, item: Item, font: Font) -> None: ...
    def set_suggested(self, suggested: Optional[str] = None) -> None: ...
