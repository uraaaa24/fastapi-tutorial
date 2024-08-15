from typing import Annotated, Union

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@router.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="List of files to upload")]
):
    return {"file_sizes": [len(file) for file in files]}


@router.post("/uploadfile/")
async def create_upload_files(
    files: Annotated[list[UploadFile], File(description="List of files to upload")]
):
    return {"filenames": [file.filename for file in files]}
