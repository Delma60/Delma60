import  { useState } from 'react'

export const Api = (addon, type) => {
    const [first, setfirst] = useState({})
    switch (type) {
        case "Post":
            fetch("http://127.0.0.1:5000"+ addon, {
        method: "POST" , 
        headers:{ 'Content-Type': 'application/json'}, 
        body: JSON.stringify({'name': Name.value, 'email': Email.value, 'password': Password.value})
    }).then(
        res => res.json()
    ).then(
        data => setfirst(data)
    )
            return first
        case "Post":
                fetch("http://127.0.0.1:5000"+ addon, {
            method: "POST" , 
            headers:{ 'Content-Type': 'application/json'}, 
            body: JSON.stringify({'name': Name.value, 'email': Email.value, 'password': Password.value})
        }).then(
            res => res.json()
        ).then(
            data => setfirst(data)
        )
            return first
        
        default:
            break;
    }
    
    return first

}
