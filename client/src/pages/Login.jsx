import React, { useRef } from 'react'
import {FaUserCircle} from "react-icons/fa"
import { useDispatch, useSelector } from 'react-redux'
import { Api } from '../features/api/Api'


export const Login = () => {
    dispatch = useDispatch()
    const user = useSelector(state => state.user)
    const formRef = useRef()
    const formHandler = (e) => {
        e.preventDefault()
        const {Name, Email, Password} = formRef.current
    }
  return (
    <div className='bg-[lightgray] p-2 h-[100vh]'>
        <div className="p-3 bg-white shadow md:mx-[30%]  mx-[15%] mt-4 h-[85vh]">
            <div className="flex flex-col align-items-center justify-content-center p-3">
                <FaUserCircle size={40} className="text-blue-400" />
                <div className="text-[30px]" style={{fontWeight: "bold"}}>Create account!</div>

                <div className=" ">
                    <form action=""   className='flex flex-col align-items-center'  method="post" onSubmit={formHandler} ref={formRef}>
                        <div className=" md:w-[400px] w-[300px] my-2 py-2">
                            <input type="text" name="Name" placeholder="Name" className="border-b w-[100%] p-2 outline-none " />
                        </div>
                        <div className="  md:w-[400px] w-[300px] my-2 py-2">
                            <input type="text" name="Email" placeholder="Email" className="border-b w-full p-2 outline-none " />
                        </div>
                        <div className="  md:w-[400px] w-[300px] my-2 py-2">
                            <input type="text" name="Password" placeholder="Password" className="border-b w-full p-2 outline-none " />
                        </div>
                        <div className="md:w-[400px] w-[300px] my-3 py-2">
                            <input type="submit" value="Create" className="btn btn-primary hover:text-white text-primary w-[40%] " />
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
  )
}
