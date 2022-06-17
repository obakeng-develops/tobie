import React from 'react'

function SignIn() {
  return (
    <div className='flex flex-col justify-center items-center'>
        <img src='/images/tobie-logo.png' className='w-24 h-24'/>
        <label className='font-overpass font-bold text-2xl'>Sign In</label>
        <div className='flex flex-col space-y-2'>
            <button className='bg-blue-700 p-2 font-overpass text-white'>Login with Facebook</button>
            <button className='bg-rose-600 p-2 font-overpass text-white'>Login with Google</button>
        </div>
        <hr></hr>
        <div>
            <input type="text" placeholder="Email" className="font-overpass"/>
            <input type="password" placeholder="Password" className="font-overpass"/>
        </div>
    </div>
  )
}

export default SignIn