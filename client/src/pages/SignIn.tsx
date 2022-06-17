import React from 'react'

function SignIn() {
  return (
    <div className='flex flex-col justify-center items-center'>
        <img src='/images/tobie-logo.png' className='w-24 h-24'/>
        <label className='font-overpass font-bold text-2xl'>Sign In</label>
        <button>Login with Facebook</button>
    </div>
  )
}

export default SignIn