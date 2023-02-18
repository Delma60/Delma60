import Pic from "../file/images/pic_1.jpg"
import '../App.css';
import {HiOutlineMenuAlt4} from 'react-icons/hi'
import {IoMdClose} from 'react-icons/io'
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Home = () =>{
    const navigate = useNavigate()
    const [changeState, setChangeState] = useState(false)
    const siderBarHandler = () => {setChangeState(!changeState)}
    return(
    <div className="bg-gray-100">
        <div className="relative" style={{backgroundColor: '#e0e0e0' , height: "30em",}}>
            <img src={Pic} alt="" className="img-fluid h-[30em] w-full objet-cover" style={{opacity: .65}}/>
            <div className="absolute top-0 sm:left-[12%] left-[6%] ">
                <div className="d-md-block d-none" style={
                    {
                        display: "flex", 
                        justifyContent: "center", 
                        paddingTop: "1em"
                    }
                        }>
                    <div className="" style={
                        {
                            height : "50px", 
                            width: "75vw" , 
                            backgroundColor: "white",
                            display: "flex", 
                            justifyContent: "space-between", 
                            alignItems: "center", paddingLeft: "30px", 
                            paddingRight: "30px",
                            borderRadius: "5px"
                        }
                            }>
                        <div className="">Home</div>
                        <div className="">About us</div>
                        <div className="">Contact us</div>
                        <div className="">Login</div>
                        <div className="">Forum</div>
                    </div>
                </div>
                <div 
                onClick={siderBarHandler}
                className="bg-white cursor-pointer h-[45px] w-[45px] rounded m-3 d-md-none d-flex justify-content-center align-items-center"
                >
                    <HiOutlineMenuAlt4  size={35} />
                </div>
                {
                    changeState && (
                        <div className=" d-md-none d-block h-[100vh] w-[55%] bg-white fixed top-0 left-0 p-3 shadow" style={{zIndex: 1}}>
                            <div className="cursor-pointer" onClick={siderBarHandler}>
                                <IoMdClose size={20}/>
                            </div>
                            <div className=" my-[12%]">
                                <div className="mx-[10%] p-2 cursor-pointer" onClick={() => navigate("/")}>Home</div>
                                <div className="mx-[10%] p-2 cursor-pointer">About Us</div>
                                <div className="mx-[10%] p-2 cursor-pointer ">Contact Us</div>
                                <div className="mx-[10%] p-2 cursor-pointer " onClick={() => navigate("/login")}>Login</div>
                                <div className="mx-[10%] p-2 cursor-pointer ">Forum</div>
                            </div>

                        </div>
                    )
                }
                <div className=" w-100 flex justify-content-center md:mt-[10%] mt-[15%]" >
                    <div className="text-center text-[35px] text-white" style={{fontWeight: "bold"}}>
                        Start Your Trading Experience <br /> with Us <br />
                        <div className="btn text-[18px] bg-blue-600 text-white w-[150px] hover:bg-sky-700" style={{fontWeight: "normal", }} >Get Started</div>
                    </div>
                </div>
            </div>
        </div>
        <div className="relative">
            <div className="d-inline-block md:w-[30%] w-[70%] bg-white  my-3 md:mx-[1.5%] mx-[15%] h-[500px] hover:shadow-lg p-3">wefe8</div>
            <div className="d-inline-block md:w-[30%] w-[70%] bg-white  my-3 md:mx-[1.5%] mx-[15%] h-[500px] hover:shadow-lg">wefe8</div>
            <div className="d-inline-block md:w-[30%] w-[70%] bg-white  my-3 md:mx-[1.5%] mx-[15%] h-[500px] hover:shadow-lg">wefe8</div>
        </div>
        <div className="mt-5  py-5  bg-blue-500">
            <div className="mx-[15%] text-[30px] text-white" style={{fontWeight: "bold"}}>Wanna Talk To Us?</div>
            <div className="mx-[15%] my-2 text-[20px] text-orange-500 ">
                Pleas feel free to contact us. We're super happy to talk to you.
                Feel free to make your enquiry.
            </div>
            <div className="md:mx-[14.5%] mx-[13%]">
                <div className="btn text-white border border-white m-2 text-[15px] hover:bg-sky-400 hover:text-white">CONTACT US</div>
            </div>
        </div>
        <div className="">
            <div className="p-3 mx-[12%]  my-4">
                <div className="h-[24px] bg-orange-500 w-[12px] d-inline-block"></div>
                <div className="d-inline-block text-[30px] text-gray-500 ml-1" style={{fontWeight: "bold"}}> Our goal</div>
                <div className="py-3">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Assumenda impedit, suscipit non vel beatae nesciunt atque quos fugit voluptatibus ea perspiciatis repellendus corporis architecto laboriosam quibusdam nam debitis est facere?
                </div>
                <div className="">
                    <span className="text-blue-700" style={{fontWeight: "bold"}}>Olaniyi Oladele</span>
                    <br />
                    <span className="text-blue-700 text-[12px]">CEO of Woolmer</span>
                </div>
            </div>
        </div>
        <div className="bg-white p-2 my-4">
            <div className="text-center text-[35px] text-blue-600">Latest News</div>
        </div>
    </div>
)}

export default Home;