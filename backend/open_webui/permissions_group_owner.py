"""
Default permission profile for the `group_owner` role.
Adjust the values in this module to fine-tune what capabilities
`group_owner` users have without granting full admin access.
"""

GROUP_OWNER_PERMISSIONS = {
    "workspace": {
        "models": True,
        "knowledge": True,
        "prompts": True,
        "tools": True,
    },
    "sharing": {
        "public_models": True,
        "public_knowledge": True,
        "public_prompts": True,
        "public_tools": True,
        "public_notes": True,
    },
    "chat": {
        "controls": True,
        "valves": True,
        "system_prompt": True,
        "params": True,
        "file_upload": True,
        "delete": True,
        "delete_message": True,
        "continue_response": True,
        "regenerate_response": True,
        "rate_response": True,
        "edit": True,
        "share": True,
        "export": True,
        "stt": True,
        "tts": True,
        "call": True,
        "multiple_models": True,
        "temporary": True,
        "temporary_enforced": False,
    },
    "features": {
        "direct_tool_servers": False,
        "web_search": True,
        "image_generation": True,
        "code_interpreter": True,
        "notes": True,
    },
}
