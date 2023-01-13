from typing import Optional
from switch.utils.types import JSONDict
from switch.base.switch_object import SwitchObject


class Group(SwitchObject):
    __slots__ = (
        "id",
        "name",
        "community_id",
        "enabled_free",
        "enabled_public",
        "default_group",
        "is_public",
        "created_by",
        "icon",
        "group_logo_url",
        "allowed_content",
        "created_at",
        "updated_at",
    )

    def __init__(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        community_id: Optional[str] = None,
        enabled_free: Optional[bool] = None,
        enabled_public: Optional[bool] = None,
        default_group: Optional[bool] = None,
        is_public: Optional[bool] = None,
        created_by: Optional[str] = None,
        icon: Optional[str] = None,
        group_logo_url: Optional[str] = None,
        allowed_content: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ):
        self.id = id
        self.name = name
        self.community_id = community_id
        self.enabled_free = enabled_free
        self.enabled_public = enabled_public
        self.default_group = default_group
        self.is_public = is_public
        self.created_by = created_by
        self.icon = icon
        self.group_logo_url = group_logo_url
        self.allowed_content = allowed_content
        self.created_at = created_at
        self.updated_at = updated_at

    def to_json(self) -> JSONDict:
        return {
            "groupId": self.id,
            "groupName": self.name,
            "communityId": self.community_id,
            "enabledFree": self.enabled_free,
            "enabledPublic": self.enabled_public,
            "defaultGroup": self.default_group,
            "isPublic": self.is_public,
            "createdBy": self.created_by,
            "icon": self.icon,
            "groupLogoUrl": self.group_logo_url,
            "allowedContent": self.allowed_content,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

    @classmethod
    def from_json(self, data: JSONDict) -> "Group":
        if data is not None:
            self.id = data.get("groupId")
            self.name = data.get("groupName")
            self.community_id = data.get("communityId")
            self.enabled_free = data.get("enabledFree")
            self.enabled_public = data.get("enabledPublic")
            self.default_group = data.get("defaultGroup")
            self.is_public = data.get("isPublic")
            self.created_by = data.get("createdBy")
            self.icon = data.get("icon")
            self.group_logo_url = data.get("groupLogoUrl")
            self.allowed_content = data.get("allowedContent")
            self.created_at = data.get("createdAt")
            self.updated_at = data.get("updatedAt")
        return self
