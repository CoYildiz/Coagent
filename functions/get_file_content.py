import os

def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        # Working directory'nin mutlak yolu
        working_dir_abs = os.path.abspath(working_directory)

        # Kullanıcının istediği dizinin mutlak yolu
        target_file = os.path.normpath(
            os.path.join(working_dir_abs, file_path)
        )

        # Çalışma dizininin dışına çıkılıyor mu?
        valid_target_file = (
            os.path.commonpath([working_dir_abs, target_file])
            == working_dir_abs
        )

        if not valid_target_file:
            return (
                f'Error: Cannot read "{file_path}" '
                "as it is outside the permitted working directory"
            )

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the context of file
        
        MAX_CHARS = 10000


        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string+=f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"

        return file_content_string
        
    except Exception as e:
        return f"Error: {e}"





# json format for llm
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the contents of a file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path of the file to read relative to the working directory"
                }
            },
            "required": ["file_path"]
        }
    }
}
