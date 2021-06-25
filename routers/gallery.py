import cloudinary.api
from fastapi import status

from . import router
from helpers import cloudinary_init


@router.get("/gallery/haldi", status_code=status.HTTP_200_OK)
async def get_haldi_images():
    cloudinary_init.initalize_cloudinary()

    return cloudinary.api.resources(
        prefix="gallery/haldi_prod",
        type="upload",
        context=True,
        max_results=100,
    )


@router.get("/gallery/wedding", status_code=status.HTTP_200_OK)
async def get_wedding_images():
    cloudinary_init.initalize_cloudinary()

    return cloudinary.api.resources(
        prefix="gallery/wedding_prod",
        type="upload",
        context=True,
        max_results=100,
    )


@router.get("/gallery/reception", status_code=status.HTTP_200_OK)
async def get_reception_images():
    cloudinary_init.initalize_cloudinary()

    return cloudinary.api.resources(
        prefix="gallery/reception_prod",
        type="upload",
        context=True,
        max_results=100,
    )
