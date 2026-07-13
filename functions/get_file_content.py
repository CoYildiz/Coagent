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
                file_content_string+=f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters"
            ### dont forget 5,6,7
            ### try/except add
            ## create new .txt for test it.





            # add result variable this here
        
        
        

    except Exception as e:
        return f"Error: {e}"
