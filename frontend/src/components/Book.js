

import React from 'react'
import { Link } from 'react-router-dom'

const BookItem = ({ item, deleteBook }) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.author.last_name}</td>
            <td><button onClick={() => deleteBook(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const BookList = ({ items, deleteBook }) => {
    return (
        <div>
            <table>
                <tbody>
                    <tr>
                        <th>ID</th>
                        <th>NAME</th>
                        <th>AUTHOR</th>
                        <th></th>
                    </tr>
                    {items.map((item) => <BookItem item={item} deleteBook={deleteBook} />)}
                </tbody>
            </table>
            <Link to='/books/create'>Create</Link>
        </div>
    )
}

export default BookList