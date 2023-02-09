import React from 'react'


const BookItem = ({ item }) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.author.name}</td>
        </tr>
    )
}

const BookList = ({ items }) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUTHOR</th>
                {/* {items.map((item) => <BookItem item={item} />)}*/}
           </tr>
        </table>

    )
}

export default BookList