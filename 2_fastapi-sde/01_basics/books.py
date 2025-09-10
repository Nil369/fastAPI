import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI(
    title="Books API",
    description="A simple CRUD API for managing books",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Books",
            "description": "Operations with books."
        }
    ]
)

class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    title: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="The title of the book"
    )
    author: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="The author of the book"
    )
    description: Optional[str] = Field(
        None,
        max_length=1000,
        description="Description of the book"
    )
    rating: Optional[int] = Field(
        None,
        ge=0,
        le=5,
        description="Rating of the book (0 to 5)"
    )

class BookUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=3,
        max_length=200,
        description="The title of the book"
    )
    author: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="The author of the book"
    )
    description: Optional[str] = Field(
        None,
        max_length=1000,
        description="Description of the book"
    )
    rating: Optional[int] = Field(
        None,
        ge=0,
        le=5,
        description="Rating of the book (0 to 5)"
    )



# FakeDB: In-memory database
BOOKS_DB = []

@app.get("/", name="Home")
def home():
    return {
        "success": True,
        "message": "Welcome to the Books API store"
    }



## CRUD Endpoints

### Create
@app.post("/books", status_code=status.HTTP_201_CREATED, tags=["Books"])
def create_book(book: Book):
    """Adds a new book to the database."""
    BOOKS_DB.append(book)
    return {"message": "Book added successfully!"}


### Read
@app.get("/books", response_model=List[Book], tags=["Books"])
def get_all_books():
    """Returns a list of all books in the database."""
    return BOOKS_DB


@app.get("/books/{book_id}", response_model=Book, tags=["Books"])
def get_book_by_id(book_id: UUID):
    """Retrieves a single book by its UUID."""
    for book in BOOKS_DB:
        if book.id == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found."
    )


### Update
@app.put("/books/{book_id}", response_model=Book, tags=["Books"])
def update_book(book_id: UUID, updated_book: BookUpdate):
    """
    Updates an existing book by its UUID.
    
    You can update any field except the ID.
    """
    for index, book in enumerate(BOOKS_DB):
        if book.id == book_id:
            # Update only the fields provided in the request body
            update_data = updated_book.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(BOOKS_DB[index], key, value)
            return BOOKS_DB[index]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found."
    )


### Delete
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Books"])
def delete_book(book_id: UUID):
    """Deletes a book from the database by its UUID."""
    initial_len = len(BOOKS_DB)
    BOOKS_DB[:] = [book for book in BOOKS_DB if book.id != book_id]
    if len(BOOKS_DB) == initial_len:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found."
        )
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=f"Book of ID: {book_id} deleted successfully!")



# Run the application
if __name__ == "__main__":
    uvicorn.run(
        "books:app",  # This assumes your file is named books.py
        host="localhost",
        port=8000,
        reload=True  # Enables hot-reloading
    )