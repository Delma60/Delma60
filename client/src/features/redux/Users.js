import { createSlice } from "@reduxjs/toolkit";


const initialState = {
    id: null,
    name: 'wale'
}
const userReducer = (state = initialState, action) => {
    switch (action.type) {
        case "set_user":
            return {}
            break;
    
        default:
            return state;
    }

}

export default userReducer;