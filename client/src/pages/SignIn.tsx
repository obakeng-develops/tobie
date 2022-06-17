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
        <hr className='my-5'></hr>
        <div className='flex flex-col space-y-3'>
            <input type="text" placeholder="Email" className="font-overpass bg-slate-100 p-2"/>
            <input type="password" placeholder="Password" className="font-overpass bg-slate-100 p-2"/>
        </div>
    </div>
  )
}

export default SignIn